# Counterexample: Authority Without Domination

## Claim Being Tested

The kernel must not classify every authority relation as domination.

## Scenario

Participant `P` voluntarily joins a governed structure `G`. `G` has final authority over a limited scope of `P`'s frame while `P` retains a legitimate, standing-preserving exit.

Examples may include:

```text
a member joining a club with clear resignation rights
a contributor joining an open-source project that can be forked
a student enrolling in a class with non-punitive withdrawal options
a user choosing a tool with available alternatives and data portability
```

## Kernel Assessment

The authority condition may hold:

```text
Final(G,F_P)=1
```

But the exit condition fails:

```text
ViableExitFrom(P,G)=1
```

Therefore:

```text
D(P,G)=0
```

because domination requires absence of viable exit.

## Why Domination Is Not Present

Governance can be legitimate when exit, contestation, and repair remain available. The kernel is not anarchic. It does not reject authority as such. It rejects authority fused with exit foreclosure.

## Misclassification Risk

The risk is anti-governance inflation. Treating all authority as domination makes the kernel unusable for institutions, safety systems, and cooperative structures.

## Lesson

```text
Governance becomes domination only when final frame authority is joined to absent legitimate viable exit.
```
