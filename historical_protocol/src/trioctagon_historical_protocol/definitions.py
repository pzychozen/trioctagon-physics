"""Five closed, inert H5 descriptor templates; these never invoke operations."""
import copy
from .schema import s, CONTRACT, PROFILE, IMPLEMENTATION
from .packets import READOUTS, NUMERICAL_POLICIES, K_NAMES, frozen
from .errors import require

OPERATIONS = ("historical.triad.step.inspect", "historical.triad.run.inspect",
    "historical.readout.staged_z.inspect", "historical.readout.ema_z.inspect",
    "historical.probability_chart.inspect")
PAYLOAD_SCHEMAS = ("H_STEP_1","H_RUN_1","H_STAGED_1","H_EMA_1","H_CHART_1")
ARGUMENT_SCHEMAS = ("H_STEP_ARGS_1","H_RUN_ARGS_1","H_STAGED_ARGS_1","H_EMA_ARGS_1","H_CHART_ARGS_1")
ISSUANCE = "UNATTESTED_HISTORICAL_RECONSTRUCTION"
TEXT = ("Mathematical reconstruction from the identified historical source profile. "
    "Independent modern implementation and declared numerical conventions are recorded separately. "
    "This result does not reproduce the complete production TORMENT system, establish original execution, "
    "attach state to physical geometry, or provide physical validation.")
_STATUS=("RECONSTRUCTED_HISTORICAL","RECONSTRUCTED_HISTORICAL_SUBSET","RECONSTRUCTED_HISTORICAL_K",
         "RECONSTRUCTED_HISTORICAL_H","RECONSTRUCTED_HISTORICAL_CHART")
_FORMULA=("H2_D0_UNFORCED_COMMON_DOMAIN","H2_D0_PLUS_H4_HISTORY_AND_SELECTED_READOUT",
    "STAGED_AND_CHIRALITY_FORMULAS_COMMON_DOMAIN","H_CURRENT_MEMORY_READOUT_COMMON_DOMAIN",
    "HISTORICAL_FORMULA_NO_CURRENT_RUNTIME_COUNTERPART")
_PRODUCTION=("RECURRENCE_SOURCE_BINDING_ONLY_NOT_PRODUCTION_REPLAY","STANDALONE_SUBSET_NOT_PRODUCTION_RUN",
    "STAGED_FORMULA_IN_PRODUCTION_CORE_NOT_EVENT_AUTHENTICATION",
    "COGNITIVE_SCALAR_FAMILY_ONLY_H_VECTORS_NOT_PRODUCTION_CORE_VECTORS",
    "CHART_SOURCE_CONSUMED_BY_PRODUCTION_MONITOR_MONITOR_EXCLUDED")
_DIFFERENCES=(
    ("CANONICAL_ZERO_PHASE","FINITE_DOMAIN_RESTRICTION","PLATFORM_ROUNDING"),
    ("CANONICAL_ZERO_PHASE","CONSTRUCTOR_ZERO_CACHE","H4_SELECTED_READOUT_GUARDS","REPEATED_DT","PLATFORM_ROUNDING"),
    ("STABLE_NORM","GUARDED_PRODUCTS_SUMS_ENVELOPE","CLOCK_ANGLE_ORDER","PLATFORM_ROUNDING"),
    ("STABLE_NORM","GUARDED_PRODUCTS_SUMS","CLOCK_ANGLE_ORDER","SUPPLIED_MEMORY_NOT_HISTORY_VERIFIED","PLATFORM_ROUNDING"),
    ("LEGACY_UNDERFLOW_RETAINED_AND_FLAGGED","FINITE_DOMAIN_RESTRICTION","PLATFORM_ROUNDING"))


def operation_index(operation):
    require(type(operation) is str and operation in OPERATIONS,"UNKNOWN_OPERATION","exact Historical operation required")
    return OPERATIONS.index(operation)


def qualification(operation):
    i=operation_index(operation)
    return dict(historical_status=_STATUS[i],formula_survival_scope=_FORMULA[i],current_reuse="NONE_INDEPENDENT_IMPLEMENTATION",
        operational_production_scope=_PRODUCTION[i],mathematical_reconstruction="YES",numerical_differences=list(_DIFFERENCES[i]),
        physical_validation="NONE",harmonic_qualification="HISTORICAL_DESIGN_CHOICE_NOT_MATHEMATICALLY_REQUIRED" if i<2
        else "RECURRENCE_HARMONIC_QUALIFICATION_NOT_APPLICABLE",text=TEXT)


qualification_schema=s.obj(historical_status=s.text,formula_survival_scope=s.text,current_reuse=s.literal("NONE_INDEPENDENT_IMPLEMENTATION"),
    operational_production_scope=s.text,mathematical_reconstruction=s.literal("YES"),numerical_differences=s.seq(s.text),
    physical_validation=s.literal("NONE"),harmonic_qualification=s.text,text=s.literal(TEXT))


def descriptor_template(operation):
    i=operation_index(operation)
    base=["K_MODEL","K_PHASE","K_CONSTANTS"]
    roles=(base,{READOUTS[0]:base,READOUTS[1]:base,READOUTS[2]:base+["H_MODEL"]},["K_MODEL"],["H_MODEL"],["K_PROBABILITY"])[i]
    effects=( ["IMMUTABLE_INPUT","ONE_DETACHED_OMEGA_UPDATE"],
        ["IMMUTABLE_INPUT","FRESH_FINITE_HISTORY","SEPARATE_TERMINAL"],
        ["IMMUTABLE_INPUT","PURE_READOUT"],["IMMUTABLE_INPUT","PURE_CURRENT_MEMORY_READOUT"],
        ["IMMUTABLE_INPUT","PURE_CHART"] )[i]+["RETURN_DETACHED_HISTORICAL_RESULT"]
    policies=([NUMERICAL_POLICIES[0]],list(NUMERICAL_POLICIES[1:4]),[NUMERICAL_POLICIES[4]],
              [NUMERICAL_POLICIES[5]],[NUMERICAL_POLICIES[6]])[i]
    return copy.deepcopy(dict(operation=operation,revision=1,argument_schema=ARGUMENT_SCHEMAS[i],payload_schema=PAYLOAD_SCHEMAS[i],
        numerical_policy_ids=policies,source_roles=roles,effects=effects,qualification=qualification(operation),
        provider_id="historical.reference",implementation_strategy="CLEAN_INDEPENDENT_REIMPLEMENTATION",issuance_class=ISSUANCE))


def resolved_constants(operation, arguments):
    """Select frozen token packets, never run a historical k selector or equation."""
    i=operation_index(operation)
    c=frozen("constants")
    if i<2:
        require(arguments.get("k_profile") in K_NAMES,"WRONG_K_PROFILE","fixed k profile required")
        result={"dynamics":c["profiles"][arguments["k_profile"]]}
        if i==1:
            mode=arguments["readout"]
            require(mode in READOUTS,"UNSUPPORTED_READOUT")
            rd={"profile":mode}
            if mode!="NONE":rd["constants"]=c["staged" if mode==READOUTS[1] else "ema"]
            result.update(clock=c["clock"],readout=rd)
        return result
    if i<4:return {"clock":c["clock"],"readout":c["staged" if i==2 else "ema"]}
    return {"chart":c["chart"]}


def numerical_policy(operation, arguments):
    i=operation_index(operation)
    if i==1:return NUMERICAL_POLICIES[1+READOUTS.index(arguments["readout"])]
    return NUMERICAL_POLICIES[(0,1,4,5,6)[i]]
