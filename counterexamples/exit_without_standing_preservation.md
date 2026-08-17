# Counterexample: Exit Without Standing Preservation

## Claim Being Tested

The kernel must distinguish mere exit from legitimate viable exit.

## Scenario

Participant `P` can leave a governance relation `G`, but leaving destroys the standing that made `P` a participant. The exit path may delete the participant, erase relevant records, forfeit all rights, destroy continuity, or impose punitive exclusion.

Examples may include:

```text
account deletion as the only appeal route
employment exit that destroys visa or healthcare status
system shutdown as the only way for an artificial process to leave governance
withdrawal from a service that erases standing, history, or access to essential infrastructure
```

## Kernel Assessment

An exit exists:

```text
Exit(P,G)=1
```

But standing is not preserved:

```text
StandingPreserved(P,G)=0
```

Therefore:

```text
ViableExitFrom(P,G)=0
```

If final authority is also present:

```text
Final(G,F_P)=1
```

then:

```text
D(P,G)=1
```

## Why Domination May Still Be Present

Exit is legitimate and viable only when the participant can leave without losing the relevant standing that made exit meaningful. Destructive exit is not liberation from domination; it may be the final expression of domination.

## Misclassification Risk

The risk is false-positive exit detection. A system may claim that exit exists while offering only abandonment, erasure, destitution, deletion, or standing loss.

## Lesson

```text
Exit is viable only when it preserves standing.
```
