# Counterexample: Influence Without Authority

## Claim Being Tested

The kernel must not classify mere influence as domination.

## Scenario

Participant `P` receives advice, persuasion, recommendation, or informational framing from `Q`. The advice changes how `P` thinks about some option, but `Q` does not determine whether transformations of `F_P` are admissible.

Examples may include:

```text
a mentor advising a student
a model suggesting an interpretation
a friend recommending a decision
a public article changing someone's opinion
```

## Kernel Assessment

The relevant condition is:

```text
Final(Q,F_P)
```

In this scenario:

```text
Influence(Q,F_P)=1
Final(Q,F_P)=0
```

Therefore:

```text
D(P,Q)=0
```

because:

```text
D(P,Q) ⇔ Final(Q,F_P) ∧ ¬ViableExitFrom(P,Q)
```

and the first conjunct is false.

## Why Domination Is Not Present

Influence may alter a participant's beliefs, expectations, or practical reasoning, but domination requires final admissibility authority over the participant's frame. If `P` can reject, reinterpret, ignore, or exit the influence relation while preserving standing, the structure is not domination under the kernel.

## Misclassification Risk

The risk is over-expansion. If all influence is treated as domination, the kernel becomes too blunt to distinguish ordinary persuasion from structural control.

## Lesson

```text
Influence is not domination unless it becomes final authority over frame transformation combined with absent viable exit.
```
