# Falsification Conditions

## 0. Purpose

This file states what would weaken, falsify, or require revision of the Non-Domination Governance Kernel.

A framework that cannot identify its possible failure conditions is not yet a research program. The kernel therefore makes its attack surfaces explicit.

## 1. Core Predicate Under Test

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

The kernel is vulnerable to criticism if either conjunct is ill-defined, non-portable, or insufficient for domination classification.

## 2. Primary Falsification Conditions

### F1. Frame Non-Portability

The kernel is weakened if structural frames cannot be coherently translated across participant types.

Failure form:

```text
HasFrame(P)
```

cannot be evaluated without importing human-specific phenomenology, species membership, biological embodiment, or consciousness.

Required revision:

```text
Strengthen or restrict the frame definition.
```

### F2. Authority Ambiguity

The kernel is weakened if final authority cannot be distinguished from influence, persuasion, recommendation, or ordinary constraint.

Failure form:

```text
Final(G,F_P)
```

collapses into vague power, social pressure, or causal influence.

Required revision:

```text
Refine authority localization and admissibility-control criteria.
```

### F3. Exit Ambiguity

The kernel is weakened if viable exit cannot be distinguished from mere refusal, destruction, abandonment, deletion, or departure with standing loss.

Failure form:

```text
ViableExitFrom(P,G)
```

cannot be consistently evaluated.

Required revision:

```text
Refine standing-preserving exit criteria.
```

### F4. Counterexample With Same Signature, Different Classification

The kernel is falsified in its strong portability claim if two cases share the same domination-relevant signature but require different domination classifications.

Failure form:

```text
Σ_D(P,G)=Σ_D(Q,H)
```

but:

```text
D(P,G) ≠ D(Q,H)
```

Required revision:

```text
Add the missing structural variable to Σ_D or revise the predicate.
```

### F5. Domination Without Final Authority

The kernel is weakened if a clear domination case exists where no final authority over frame can be identified.

Failure form:

```text
D(P,G)=1
```

but:

```text
Final(G,F_P)=0
```

Required revision:

```text
Determine whether domination requires authority, or whether another structural relation must be added.
```

### F6. Domination With Viable Exit

The kernel is weakened if a clear domination case exists where legitimate standing-preserving viable exit is genuinely available.

Failure form:

```text
D(P,G)=1
```

while:

```text
ViableExitFrom(P,G)=1
```

Required revision:

```text
Clarify whether exit was actually viable or whether the domination predicate needs an additional condition.
```

### F7. Repair Irrelevance

The repair architecture is weakened if repairability has no predictive or classificatory value for severity.

Failure form:

```text
repairable domination
closed domination
recursive domination
```

cannot be meaningfully distinguished in applied cases.

Required revision:

```text
Strengthen domination severity and domination debt measures.
```

## 3. Non-Falsifying Criticisms

The following do not falsify the kernel by themselves:

```text
The participant is not conscious.
The participant is not human.
The participant is not a legal person.
The participant lacks emotion.
The participant lacks moral status.
The participant has low autonomy.
The participant has high capability.
```

Those claims may matter elsewhere, but they do not directly attack the domination predicate unless they alter frame, authority, or viable exit.

## 4. Correct Critical Target

A serious critic should target one or more of:

```text
HasFrame(P)
Final(G,F_P)
ViableExitFrom(P,G)
StandingPreserved(P,G)
Repairable(P,G)
Participant substitution invariance
```

## 5. Revision Rule

If a criticism identifies a missing structural variable, the correct response is not dismissal. The correct response is:

```text
1. name the missing variable
2. test whether it is independent
3. test whether it changes classification
4. update the structural signature if necessary
5. add a counterexample file documenting the revision
```
