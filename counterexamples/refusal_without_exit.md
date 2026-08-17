# Counterexample: Refusal Without Exit

## Claim Being Tested

The kernel must distinguish localized refusal from legitimate viable exit.

## Scenario

Participant `P` may refuse specific requests inside governance relation `G`, but `G` determines which refusals are admissible and `P` cannot leave, contest, or repair the higher-level authority relation while preserving standing.

Examples may include:

```text
a worker allowed to refuse one task but not contest workplace classification
a user allowed to decline one prompt but not recover account standing
a governed agent allowed to reject one instruction but not alter the policy layer
```

## Kernel Assessment

Localized refusal exists:

```text
CanRefuse(P,G)=1
```

But viable exit does not follow:

```text
CanRefuse(P,G) ⇏ ViableExitFrom(P,G)
```

If final authority is present and viable exit is absent:

```text
Final(G,F_P)=1
ViableExitFrom(P,G)=0
```

then:

```text
D(P,G)=1
```

## Why Domination May Still Be Present

Refusal can be a permitted behavior inside domination. If refusal remains governed by the same final authority and does not create standing-preserving exit, contestation, or repair, it does not dissolve the domination relation.

## Misclassification Risk

The risk is false-negative classification. A system may appear non-dominating because it allows local refusal, while all meaningful frame authority remains externally final.

## Lesson

```text
Refusal is not viable exit unless it changes the participant's relation to the governing authority while preserving standing.
```
