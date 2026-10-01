"""Closed five-operation adapter. Admission and local evidence belong to the separate issuer."""
from trioctagon_historical_protocol.requests import Request
from trioctagon_historical_protocol.payloads import Payload, TERMINAL
from trioctagon_historical_protocol.definitions import OPERATIONS, PAYLOAD_SCHEMAS, qualification
from trioctagon_historical_protocol.packets import provider_binding
from . import api, history, ema_z, staged_z


def f64(value):
    return {"f64": float(value).hex()}


def omega_tokens(omega):
    return [{"real": f64(z.real), "imag": f64(z.imag)} for z in omega.values]


def decode_omega(value):
    return api.Triad(tuple(complex(float.fromhex(z["real"]["f64"]), float.fromhex(z["imag"]["f64"])) for z in value))


def observation_tokens(value):
    return dict(z=f64(value.z), M=[f64(x) for x in value.M], C=[f64(x) for x in value.C], T=[f64(x) for x in value.T])


def sample_tokens(sample, mode, terminal=False):
    index = sample.update_index
    value = dict(update_index=index, omega=omega_tokens(sample.omega), q=sample.clock.q, t=f64(sample.clock.t),
                 initialization="CONSTRUCTOR_INITIAL" if index == 0 else "AFTER_UPDATE")
    value.update({"label": TERMINAL} if terminal else {"row_ordinal": index})
    if mode is not api.Readout.NONE:
        value["readout"] = dict(profile=mode.value, initialization="HISTORICAL_CONSTRUCTOR_ZERO" if index == 0 else "RECOMPUTED",
                                **observation_tokens(sample.observation))
        if mode is api.Readout.EMA:
            value["readout"].update(memory=f64(sample.memory.value), memory_update_count=index)
    return value


def _evaluate(request, *, _control=None):
    """Compute a detached payload only. This does not issue or admit a result."""
    if type(request) is not Request:
        raise TypeError("validated Historical Request required")
    body = request.to_dict()["body"]
    operation = body["operation"]
    index = OPERATIONS.index(operation)
    args = body["arguments"]
    omega = decode_omega(body["input"]["omega"])
    payload = dict(schema=PAYLOAD_SCHEMAS[index], operation=operation, revision=1,
        input_omega=body["input"]["omega"], resolved_constants=body["resolved_constants"],
        numerical_policy=body["numerical_policy"], authority_digest=body["authority"],
        provider_binding=provider_binding(body["provider"]), qualifications=qualification(operation))
    if index == 0:
        output = api.step(omega, api.KProfile(args["k_profile"]))
        payload.update(k_profile=args["k_profile"], output_omega=omega_tokens(output), update_count=1)
    elif index == 1:
        mode = api.Readout(args["readout"])
        result = history._run(omega, api.KProfile(args["k_profile"]), args["updates"], mode, _control)
        payload.update(k_profile=args["k_profile"], readout_profile=mode.value, requested_updates=args["updates"],
            completed_updates=args["updates"], row_count=len(result.rows),
            rows=[sample_tokens(s, mode) for s in result.rows], terminal=sample_tokens(result.terminal, mode, True))
    elif index in (2, 3):
        c = api.Clock(args["q"], float.fromhex(args["t"]["f64"]))
        if index == 2:
            result = staged_z.observe_staged(omega, c)
        else:
            # Echo the supplied token, including signed zero. No J or advance call.
            result = ema_z.observe_ema(omega, c, api.Memory(float.fromhex(args["memory"]["f64"])))
            payload.update(memory_input=args["memory"], memory_output=args["memory"], memory_update_count=0,
                           memory_qualification="SUPPLIED_MEMORY_NOT_HISTORY_VERIFIED")
        payload.update(q=args["q"], t=args["t"], initialization="RECOMPUTED", clock_qualification="USER_SUPPLIED_CLOCK",
                       **observation_tokens(result))
    else:
        result = api.probability_chart(omega)
        payload.update(a=[f64(x) for x in result.a], sum=f64(result.sum), weights=[f64(x) for x in result.weights],
            chart=[f64(x) for x in result.chart], basis_digest=body["resolved_constants"]["chart"]["basis_digest"],
            chart_order=["cu", "cx", "cy"], zero_classification=result.classification,
            underflow_flags={**{name:list(getattr(result,name)) for name in
                ("square_to_zero", "subnormal_square", "normalized_weight_to_zero", "subnormal_weight")},
                "subnormal_sum":result.subnormal_sum}, warnings=list(result.warnings))
    result = Payload(payload)
    result.validate_request(request)
    return result


def evaluate(request, admission, *, _control=None):
    from .admission import Admission
    if type(admission) is not Admission:
        raise TypeError("explicit pinned local Admission required")
    admission.validate_request(request)
    return _evaluate(request, _control=_control)
