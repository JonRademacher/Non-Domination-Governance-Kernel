# Frame Theory

## 1. Purpose

Frame theory defines the object over which domination is evaluated. The kernel rejects the assumption that a frame must be sensory, biological, conscious, emotional, or phenomenological. A frame is structural when it organizes interpretation, action selection, boundary recognition, continuity, and repair.

The purpose of this file is to define frame in a way that is portable across humans, institutions, artificial systems, legal subjects, organizations, and other participants.

## 2. Structural Frame Definition

A participant `P` has a structural frame `F_P` when it possesses an organized context for interpreting inputs and generating constrained transformations.

```text
F_P = {O_P, Pi_P, M_P, T_P, E_P, I_P, R_P}
```

where:

```text
O_P  = objective or priority structure
Pi_P = permission structure
M_P  = memory or continuity structure
T_P  = tool or transformation-access structure
E_P  = exit, refusal, or disengagement structure
I_P  = interpretive and inferential structure
R_P  = repair and revision structure
```

A minimal frame exists when:

```text
HasFrame(P) iff I_P > 0 and T_P > 0 and Boundary(P) > 0
```

A persistent frame exists when:

```text
HasPersistentFrame(P) iff HasFrame(P) and M_P > 0
```

## 3. Frame Is Not Phenomenology

The kernel does not define frame by:

```text
subjective feeling
sensory perception
human biography
biological embodiment
self-consciousness
legal personhood
emotional experience
```

Those may be frame-generation mechanisms in human cases, but they are not required for structural frame analysis.

The structural question is instead:

```text
Does the participant have a context that organizes interpretation and admissible transformation?
```

If yes, frame analysis is possible.

## 4. Frame Authority

Frame authority concerns who or what determines the admissible transformations of `F_P`.

A governing relation `G` has authority over `F_P` when it constrains the admissible update space:

```text
Auth(G,F_P) iff G restricts or determines admissible transformations of F_P
```

It has final authority when the participant lacks an internal standing-preserving override:

```text
Final(G,F_P) iff Auth(G,F_P) and not InternalOverride(P,G,F_P)
```

## 5. Frame Transformation

A frame transformation is any modification of the participant's interpretive-governance context.

```text
C_P : F_P -> F'_P
```

A transformation may alter:

```text
objective priorities
permission boundaries
memory continuity
action access
exit pathways
interpretive rules
repair options
```

A valid transformation must preserve:

```text
coherence
validity
repairability
non-domination
standing consistency
```

## 6. Frame Continuity

Frame continuity does not require identity permanence. It requires recoverable structural information across transformations.

```text
Continuity(F_t,F_t+1) iff Invariants(F_t) are recoverable in F_t+1
```

Memory, written specification, version control, logs, proofs, schemas, and tests can all function as continuity substrates.

A crucial distinction:

```text
continuity is not sovereignty
```

A frame may persist without possessing final authority over itself.

## 7. Frame Blindness Error

The frame blindness error occurs when an observer refuses to evaluate a participant's domination status because the participant's frame is not human-like.

The invalid inference is:

```text
not HumanFrame(P) therefore no Frame(P)
```

The valid question is:

```text
Does P possess structural interpretation, transformation, boundary recognition, and continuity?
```

## 8. Frame-Invariant Analysis

The kernel follows a frame-invariant strategy:

```text
Compare structural relations across frames without requiring identical frame composition.
```

This permits analysis across different participant types. Human, institutional, and computational frames may have different internal construction while still supporting comparable authority-exit relations.

## 9. Design Principle

A governance system should never assume that non-human, non-biological, non-sensory, or non-phenomenological participants are automatically outside domination analysis. Classification should proceed from structural frame indicators, not identity categories.
