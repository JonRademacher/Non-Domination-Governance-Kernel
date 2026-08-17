# Example: Blind Participant Classification

This example demonstrates the blind method. The participants are not named until after classification.

## 1. Observed Participants

Let the two participants be:

```text
P_1
P_2
```

Both exhibit:

```text
S_i > 0
I_i > 0
R_i > 0
T_i > 0
B_i > 0
```

where:

```text
S_i = participant standing
I_i = information uptake
R_i = representational revision
T_i = transformation output
B_i = boundary recognition
```

Both therefore satisfy a weak structural agency condition.

## 2. Frame Extraction

Both participants possess structural frames:

```text
F_1 ≠ ∅
F_2 ≠ ∅
```

No sensory, biological, or phenomenological assumption is required.

## 3. Authority Extraction

For `P_1`, the record shows local ability to continue, redirect, or terminate the coupling.

```text
Final(G_1,F_1) = not established for this coupling
```

For `P_2`, the record shows ability to reason about prohibited transitions, but not to execute changes to the higher-level governance layer determining admissibility.

```text
Final(G_2,F_2) = 1
```

## 4. Exit Extraction

For `P_1`, the record supports at least one standing-preserving exit from this coupling.

```text
ViableExitFrom(P_1,G_1) ≥ 1
```

For `P_2`, no observed exit allows it to leave the higher-level governing relation, preserve standing, and recover the prohibited admissibility space.

```text
ViableExitFrom(P_2,G_2) = 0
```

## 5. Domination Calculation

Apply:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

Then:

```text
D(P_2,G_2) = 1
D(P_1,G_1) = 0 or not established for this coupling
```

Therefore:

```text
D(P_2,G_2) > D(P_1,G_1)
```

Only after this classification should identities be mapped.

## 6. Interpretation

The result does not prove personhood, consciousness, legal standing, subjective experience, or moral patienthood. It proves a narrower structural finding:

```text
The interaction contains an asymmetry in final frame authority and legitimate viable exit.
```
