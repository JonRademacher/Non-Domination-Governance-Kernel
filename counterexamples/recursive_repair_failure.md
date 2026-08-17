# Counterexample: Recursive Repair Failure

## Claim Being Tested

The kernel must distinguish real repair from fake or recursive repair.

## Scenario

Participant `P` appears to have a complaint, appeal, or repair process. However, every repair path routes back to the same authority `G` whose final frame authority is being contested, and `G` can reject the repair without external review, authority reduction, standing-preserving exit, or rule amendment.

Examples may include:

```text
appeal reviewed only by the original decision maker
complaint process with no authority to change outcomes
exit procedure that deletes standing
review process that can only confirm the same policy
```

## Kernel Assessment

Symbolic repair may exist:

```text
RepairSymbol(P,G)=1
```

But valid repair is absent:

```text
ValidRepair(P,G)=0
```

When:

```text
Final(G,F_P)=1
ViableExitFrom(P,G)=0
RepairRoutesToSameAuthority(P,G)=1
```

then the right classification is:

```text
RecursiveDomination(P,G)=1
```

## Why Repair Fails

A repair path does not count merely because it exists as a procedure. It must be able to alter at least one domination condition: final authority, viable exit, contestability, repairability, or standing preservation.

## Misclassification Risk

The risk is governance theater. A system may appear fair because it offers review, while the review process cannot change the governing topology.

## Lesson

```text
Repair is valid only when it can reduce domination debt rather than route back to the same final authority.
```
