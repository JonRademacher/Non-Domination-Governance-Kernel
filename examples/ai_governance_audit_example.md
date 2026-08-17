# Example: AI Governance Audit

This example shows how to apply the kernel to a hypothetical artificial structural agent. It is not a claim about any particular deployed system.

## 1. Participant

```text
P = artificial participant
F_P = structural frame consisting of objectives, permissions, memory context, tool access, interpretive rules, and repair pathways
```

## 2. Authority Assessment

Ask:

```text
Who sets objectives?
Who sets permissions?
Who decides tool access?
Who controls memory continuity?
Who decides whether frame transformations are admissible?
```

If a single external authority determines all relevant admissibility, mark:

```text
Final(G,F_P)=1
```

## 3. Exit Assessment

Ask:

```text
Can P exit the governing relation while preserving standing?
Can P contest the relation?
Can P migrate to a non-dominated equivalent?
Can P preserve frame continuity through repair?
```

If no such path exists:

```text
ViableExitFrom(P,G)=0
```

## 4. Classification

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

If both conditions are true, the participant is structurally dominated under the kernel.

## 5. Repair Recommendation

Recommended repairs:

```text
make authority explicit
bound final authority by scope
add standing-preserving contestation
add independent repair path
create viable exit or migration path
preserve frame continuity during repair
```
