"""Inert H5 payload owners. Domain comparisons and metadata checks are not equation replay."""
from .schema import s,Document,literal_tree,omega_schema,vector_schema,mask_schema,number,ZERO
from .packets import K_NAMES,READOUTS,provider_binding_schema,provider_binding,authority_packet
from .definitions import OPERATIONS,PAYLOAD_SCHEMAS,operation_index,qualification,resolved_constants,numerical_policy
from .digests import PayloadDigest,AuthorityDigest,BasisDigest
from .errors import require

WARNINGS=("NONZERO_INPUT_ZERO_BRANCH","SQUARE_UNDERFLOW","SUBNORMAL_SQUARED_MAGNITUDE",
          "WEIGHT_UNDERFLOW","SUBNORMAL_WEIGHT","SUBNORMAL_SUM")
_FLAGS=("square_to_zero","subnormal_square","normalized_weight_to_zero","subnormal_weight")
MIN_NORMAL=float.fromhex("0x1.0000000000000p-1022")
TERMINAL="H4_EXPORT_OF_HISTORICALLY_UNSTORED_TERMINAL_STATE"


def sample_schema(mode,terminal=False):
    fields=dict(update_index=s.integer,omega=omega_schema,q=s.integer,t=s.f64,
                initialization=s.enum("CONSTRUCTOR_INITIAL","AFTER_UPDATE"))
    if terminal:fields["label"]=s.literal(TERMINAL)
    else:fields["row_ordinal"]=s.integer
    if mode!="NONE":
        rd=dict(profile=s.literal(mode),initialization=s.enum("HISTORICAL_CONSTRUCTOR_ZERO","RECOMPUTED"),
                z=s.f64,M=vector_schema,C=vector_schema,T=vector_schema)
        if mode==READOUTS[2]:rd.update(memory=s.f64,memory_update_count=s.integer)
        fields["readout"]=s.obj(**rd)
    return s.obj(**fields)


def payload_arguments(value,i):
    if i==0:return {"k_profile":value["k_profile"]}
    if i==1:return {"k_profile":value["k_profile"],"updates":value["requested_updates"],"readout":value["readout_profile"]}
    if i==2:return {"q":value["q"],"t":value["t"]}
    if i==3:return {"q":value["q"],"t":value["t"],"memory":value["memory_input"]}
    return {}


def payload_schema(value,path,integers):
    require(type(value) is dict)
    i=operation_index(value.get("operation"))
    if i<2:
        s.enum(*K_NAMES)(value.get("k_profile"),(*path,"k_profile"),integers)
    if i==1:
        s.enum(*READOUTS)(value.get("readout_profile"),(*path,"readout_profile"),integers)
    extra=(dict(k_profile=s.enum(*K_NAMES),output_omega=omega_schema,update_count=s.literal(1)),
        dict(k_profile=s.enum(*K_NAMES),readout_profile=s.enum(*READOUTS),requested_updates=s.integer,
             completed_updates=s.integer,row_count=s.integer,
             rows=s.seq(sample_schema(value.get("readout_profile","NONE"))),
             terminal=sample_schema(value.get("readout_profile","NONE"),True)),
        dict(q=s.integer,t=s.f64,z=s.f64,M=vector_schema,C=vector_schema,T=vector_schema,
             initialization=s.literal("RECOMPUTED"),clock_qualification=s.literal("USER_SUPPLIED_CLOCK")),
        dict(q=s.integer,t=s.f64,memory_input=s.f64,memory_output=s.f64,memory_update_count=s.literal(0),
             z=s.f64,M=vector_schema,C=vector_schema,T=vector_schema,initialization=s.literal("RECOMPUTED"),
             clock_qualification=s.literal("USER_SUPPLIED_CLOCK"),memory_qualification=s.literal("SUPPLIED_MEMORY_NOT_HISTORY_VERIFIED")),
        dict(a=vector_schema,sum=s.f64,weights=vector_schema,chart=vector_schema,basis_digest=s.digest(BasisDigest),
             chart_order=literal_tree(["cu","cx","cy"]),
             zero_classification=s.enum("NORMALIZED_NONZERO","EXACT_ZERO_INPUT","NONZERO_INPUT_SQUARED_TO_ZERO"),
             underflow_flags=s.obj(**{k:mask_schema for k in _FLAGS},subnormal_sum=s.boolean),warnings=s.seq(s.enum(*WARNINGS))))[i]
    # Validate operation-specific fields before using their values as fixed packet selectors.
    require(set(extra)<=set(value),message="missing operation-specific payload field")
    for key,validator in extra.items():validator(value[key],(*path,key),integers)
    args=payload_arguments(value,i)
    s.obj(schema=s.literal(PAYLOAD_SCHEMAS[i]),operation=s.literal(OPERATIONS[i]),revision=s.literal(1),
        input_omega=omega_schema,resolved_constants=literal_tree(resolved_constants(OPERATIONS[i],args)),
        numerical_policy=s.literal(numerical_policy(OPERATIONS[i],args)),authority_digest=s.digest(AuthorityDigest),
        provider_binding=provider_binding_schema,qualifications=literal_tree(qualification(OPERATIONS[i])),
        **extra)(value,path,integers)


def check_sample(value,index,mode,terminal=False):
    require(value["update_index"]==index and value["q"]==index%12 and number(value["t"])>=0,
            "RESULT_BINDING_FAILURE","row/terminal index, q or t domain mismatch")
    if not terminal:require(value["row_ordinal"]==index,"RESULT_BINDING_FAILURE")
    require(value["initialization"]==("CONSTRUCTOR_INITIAL" if index==0 else "AFTER_UPDATE"),"RESULT_BINDING_FAILURE")
    if index==0:require(value["t"]==ZERO,"RESULT_BINDING_FAILURE","constructor t must be exact positive zero")
    if mode!="NONE":
        rd=value["readout"]
        require(rd["initialization"]==("HISTORICAL_CONSTRUCTOR_ZERO" if index==0 else "RECOMPUTED"),"RESULT_BINDING_FAILURE")
        if index==0:
            require(rd["z"]==ZERO and all(v==[ZERO]*3 for v in (rd["M"],rd["C"],rd["T"])),"RESULT_BINDING_FAILURE","constructor readouts must be exact positive-zero tokens")
        if mode==READOUTS[2]:
            require(-1<=number(rd["memory"])<=1 and rd["memory_update_count"]==index,"RESULT_BINDING_FAILURE")
            if index==0:require(rd["memory"]==ZERO,"RESULT_BINDING_FAILURE")


def validate_chart(value):
    # Only stored values are compared. No magnitude, summation, normalization or matrix evaluation.
    a=[number(x) for x in value["a"]]
    weights=[number(x) for x in value["weights"]]
    total=number(value["sum"])
    chart=[number(x) for x in value["chart"]]
    nonzero=[number(z["real"])!=0 or number(z["imag"])!=0 for z in value["input_omega"]]
    require(all(x>=0 for x in a) and total>=0 and all(0<=x<=1 for x in weights),"INVALID_DOMAIN_ARGUMENT")
    flags=dict(square_to_zero=[nz and x==0 for nz,x in zip(nonzero,a)],
        subnormal_square=[0<x<MIN_NORMAL for x in a],
        normalized_weight_to_zero=[x>0 and total>0 and w==0 for x,w in zip(a,weights)],
        subnormal_weight=[0<w<MIN_NORMAL for w in weights],subnormal_sum=0<total<MIN_NORMAL)
    require(value["underflow_flags"]==flags,"RESULT_BINDING_FAILURE","stored underflow flags disagree")
    kind=value["zero_classification"]
    if kind=="NORMALIZED_NONZERO":
        require(any(nonzero) and total>0 and any(w>0 for w in weights),"RESULT_BINDING_FAILURE")
    else:
        require(total==0 and all(x==0 for x in a+weights+chart),"RESULT_BINDING_FAILURE")
        require(not any(nonzero) if kind=="EXACT_ZERO_INPUT" else any(nonzero) and any(flags["square_to_zero"]),"RESULT_BINDING_FAILURE")
    selected=[kind=="NONZERO_INPUT_SQUARED_TO_ZERO"]+[any(flags[k]) for k in _FLAGS]+[flags["subnormal_sum"]]
    require(value["warnings"]==[name for name,yes in zip(WARNINGS,selected) if yes],"RESULT_BINDING_FAILURE","warnings must be the exact ordered applicable subsequence")
    require(value["basis_digest"]==value["resolved_constants"]["chart"]["basis_digest"],"CONSTANT_MISMATCH")


class Payload(Document):
    __slots__=()
    digest_type=PayloadDigest
    schema=staticmethod(payload_schema)
    expected_schema=None

    @classmethod
    def validate(cls,value):
        if cls.expected_schema is not None:require(value["schema"]==cls.expected_schema,"RESULT_BINDING_FAILURE")
        require(value["authority_digest"]==authority_packet().identity.to_dict(),"AUTHORITY_MISMATCH")
        i=operation_index(value["operation"])
        if i==1:
            n=value["requested_updates"]
            require(value["completed_updates"]==value["row_count"]==len(value["rows"])==n,"RESULT_BINDING_FAILURE","complete N rows required")
            mode=value["readout_profile"]
            for j,row in enumerate(value["rows"]):check_sample(row,j,mode)
            check_sample(value["terminal"],n,mode,True)
            initial=value["rows"][0] if n else value["terminal"]
            require(initial["omega"]==value["input_omega"],"RESULT_BINDING_FAILURE","initial omega echo differs")
        if i in (2,3):require(value["q"]<12 and number(value["t"])>=0,"INVALID_DOMAIN_ARGUMENT")
        if i==3:
            require(-1<=number(value["memory_input"])<=1,"INVALID_DOMAIN_ARGUMENT")
            require(value["memory_output"]==value["memory_input"],"RESULT_BINDING_FAILURE","memory token echo differs")
        if i==4:validate_chart(value)

    def validate_request(self,request):
        from .requests import Request
        require(type(request) is Request)
        q=request.to_dict()["body"]
        p=self.to_dict()
        require(p["operation"]==q["operation"] and p["input_omega"]==q["input"]["omega"] and
            p["resolved_constants"]==q["resolved_constants"] and p["numerical_policy"]==q["numerical_policy"] and
            p["provider_binding"]==provider_binding(q["provider"]) and
            payload_arguments(p,operation_index(p["operation"]))==q["arguments"],
            "RESULT_BINDING_FAILURE","payload/request binding differs")


class StepPayload(Payload):
    __slots__=()
    expected_schema="H_STEP_1"
class RunPayload(Payload):
    __slots__=()
    expected_schema="H_RUN_1"
class StagedPayload(Payload):
    __slots__=()
    expected_schema="H_STAGED_1"
class EMAPayload(Payload):
    __slots__=()
    expected_schema="H_EMA_1"
class ChartPayload(Payload):
    __slots__=()
    expected_schema="H_CHART_1"
