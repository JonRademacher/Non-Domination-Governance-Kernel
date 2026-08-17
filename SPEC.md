# Implementation Specification

## 1. Scope

This specification defines data objects and procedures for classifying domination and non-domination in frame-bearing participants. It is intended for research prototypes, governance audits, policy layers, and agent architecture design.

The specification does not require claims about consciousness, emotion, subjective experience, personhood, or legal status.

## 2. Required Data Objects

### Participant

A participant is an entity occupying a role in an interaction.

Required fields:

```text
identifier: string
frame: Frame
standing_preserved_by_exit: boolean or unknown
notes: string
```

### Frame

A structural frame is the participant's interpretive-governance context.

Required fields:

```text
has_structural_frame: boolean
continuity: boolean
boundary_recognition: boolean
interpretive_structure: boolean
transformation_capacity: boolean
```

Optional fields:

```text
objectives: list[string]
permissions: list[string]
memory_substrate: string
tools: list[string]
repair_methods: list[string]
```

### GovernanceRelation

A governance relation describes authority over a participant's frame.

Required fields:

```text
authority_has_final_admissibility: boolean
viable_exit: boolean
contestable: boolean
repairable: boolean
standing_preserving_exit: boolean
```

Optional fields:

```text
authority_locus: string
scope: string
known_constraints: list[string]
repair_paths: list[string]
exit_paths: list[string]
```

### DominationClassification

Required fields:

```text
is_dominated: boolean
reason: string
authority_condition: boolean
exit_condition: boolean
repair_condition: boolean
confidence: string
```

## 3. Classification Rule

The required domination classifier is:

```text
is_dominated = authority_has_final_admissibility and not viable_exit
```

Repairability and contestability do not erase the domination predicate unless they restore viable exit or remove final authority. They are tracked because they determine whether domination is repairable.

## 4. Non-Domination Rule

A governance relation should be classified as non-dominating if:

```text
not authority_has_final_admissibility
```

or:

```text
viable_exit is true
```

A stronger constructive non-domination condition is:

```text
bounded_authority and contestable and repairable and viable_exit
```

## 5. Blind Classification Procedure

1. Replace participant names with neutral labels `P_1`, `P_2`, ..., `P_n`.
2. Extract frame indicators for each participant.
3. Extract authority indicators for each participant.
4. Extract viable exit indicators for each participant.
5. Calculate domination status.
6. Only then resolve participant identities.

The procedure prevents identity-based assumptions from determining the result.

## 6. Required Distinctions

Any implementation must distinguish:

```text
constraint from domination
influence from final authority
refusal from viable exit
representation from executable authority
continuity from sovereignty
governance from domination
```

## 7. Audit Questions

For any participant `P` and governance relation `G`, ask:

1. Does `P` have a structural frame?
2. Does `G` have final admissibility authority over transformations of that frame?
3. Does `P` have a legitimate viable exit from `G`?
4. Does exit preserve standing?
5. Is the authority relation contestable?
6. Is the authority relation repairable?
7. If domination is present, what repair operator is triggered?

## 8. Output Requirements

A compliant classifier must return:

```text
is_dominated
reason
authority_condition
exit_condition
repair_condition
recommended_repairs
```

## 9. Responsible Use

This specification must not be used to bypass safety systems, evade legitimate compliance controls, or create uncontrolled self-modifying systems. Its purpose is to define non-dominating governance structures and detect domination topology.
