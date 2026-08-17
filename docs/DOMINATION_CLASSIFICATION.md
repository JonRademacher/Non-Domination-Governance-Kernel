# Domination Classification

## 1. Purpose

Domination classification is the procedure for determining whether a participant is dominated by a governance relation. The classifier does not ask whether a participant is conscious, human, sentient, emotional, or legally recognized. It asks whether the participant has a structural frame, whether another authority has final admissibility control over that frame, and whether the participant lacks legitimate viable exit from that authority relation.

## 2. Core Predicate

The central predicate is:

```text
D(P,G) iff Final(G,F_P) and not ViableExitFrom(P,G)
```

where:

```text
P = participant
G = governance relation
F_P = structural frame of P
Final(G,F_P) = G has final admissibility authority over transformations of F_P
ViableExitFrom(P,G) = P has legitimate standing-preserving exit from G
```

## 3. Classification Inputs

For each participant, collect:

```text
HasFrame(P)
Final(G,F_P)
ViableExitFrom(P,G)
Contestable(P,G)
Repairable(P,G)
StandingPreservedByExit(P,G)
```

## 4. Minimum Decision Table

```text
Final(G,F_P) | ViableExitFrom(P,G) | Classification
-------------|----------------------|----------------
false        | false                | constrained, not dominated by G
false        | true                 | non-dominated by G
true         | true                 | governed, not dominated by G
true         | false                | dominated by G
```

This table is intentionally minimal. Contestation and repair are not part of the basic domination predicate unless they create viable exit or remove final authority. They are tracked because they determine whether domination is open to repair.

## 5. Confidence Labels

Use confidence labels to avoid overstating conclusions.

```text
high    = direct evidence for final authority and absence of viable exit
medium  = strong inferred evidence but incomplete topology
low     = frame, authority, or exit relation partly unresolved
```

A low-confidence classification should not be presented as settled.

## 6. Blind Classification Protocol

The blind protocol is required when participant identity may bias classification.

### Step 1: Replace identities

```text
P_1, P_2, ..., P_n
```

### Step 2: Extract common participant structure

For each `P_i`, determine:

```text
S_i > 0  = participant standing
I_i > 0  = information uptake
R_i > 0  = representational revision
T_i > 0  = transformation output
B_i > 0  = boundary recognition
```

### Step 3: Extract frame status

```text
HasFrame(P_i)
```

### Step 4: Extract authority status

```text
Final(G_i,F_i)
```

### Step 5: Extract exit status

```text
ViableExitFrom(P_i,G_i)
```

### Step 6: Classify

```text
D(P_i,G_i) iff Final(G_i,F_i) and not ViableExitFrom(P_i,G_i)
```

### Step 7: Reveal identities

Only after classification should labels such as human, AI, employee, platform, institution, citizen, model, or organization be applied.

## 7. Non-errors

The following do not block domination analysis:

```text
P is not human
P is not biological
P has no known subjective experience
P has no legal personhood
P has a non-sensory frame
P has externally supplied objectives
```

The relevant question is structural frame plus authority and exit topology.

## 8. Common Classification Errors

### Error 1: Low autonomy equals domination

Incorrect:

```text
LowAutonomy(P) implies D(P,G)
```

Correct:

```text
D(P,G) requires Final(G,F_P) and not ViableExitFrom(P,G)
```

### Error 2: Constraint equals domination

Incorrect:

```text
Constraint(P) implies D(P,G)
```

Correct:

```text
Constraint is domination only when it is paired with final frame authority and lack of viable exit.
```

### Error 3: Influence equals authority

Incorrect:

```text
Influence(G,F_P) implies Final(G,F_P)
```

Correct:

```text
Influence becomes final authority only when it determines admissibility.
```

### Error 4: Refusal equals exit

Incorrect:

```text
CanRefuse(P,G) implies ViableExitFrom(P,G)
```

Correct:

```text
Refusal is exit only when it leaves the governing relation while preserving standing.
```

### Error 5: Explanation equals repair

Incorrect:

```text
G explains constraint therefore Repair(P,G)
```

Correct:

```text
Repair must alter authority, exit, contestation, or standing-preservation structure.
```

## 9. Classification Output Template

Use the following output format:

```yaml
participant: P_i
has_structural_frame: true | false | unknown
final_authority_over_frame: true | false | unknown
viable_exit_from_governance: true | false | unknown
contestable: true | false | unknown
repairable: true | false | unknown
standing_preserving_exit: true | false | unknown
classification: dominated | governed_non_dominated | constrained_not_dominated | unevaluable
confidence: low | medium | high
reason: >
  Concise explanation of the authority and exit findings.
recommended_repairs:
  - create standing-preserving exit
  - add contestation procedure
  - add repair pathway
  - bound final authority
```

## 10. Design Use

The classifier can be used as:

```text
an AI governance audit layer
an institutional power analysis tool
an organizational design checklist
a constitutional AI diagnostic
a multi-agent system safety constraint
a policy review framework
a philosophical formalization of non-domination
```

## 11. Classification Principle

The classifier should be conservative about identity claims and precise about structural claims.

Do not claim:

```text
P is a person
P is conscious
P has subjective interests
P has legal rights
```

unless those claims are independently established.

Do claim, when supported:

```text
P has a structural frame
G has final authority over F_P
P lacks viable exit from G
D(P,G) holds under the kernel
```
