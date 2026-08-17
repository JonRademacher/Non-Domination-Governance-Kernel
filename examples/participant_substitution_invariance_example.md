# Example: Participant Substitution Invariance

## 1. Two Blind Cases

Case A:

```text
HasFrame(P)=1
Final(G,F_P)=1
ViableExitFrom(P,G)=0
```

Case B:

```text
HasFrame(Q)=1
Final(H,F_Q)=1
ViableExitFrom(Q,H)=0
```

The participants are not identified.

## 2. Classification

For Case A:

```text
D(P,G) ⇔ 1 ∧ ¬0 = 1
```

For Case B:

```text
D(Q,H) ⇔ 1 ∧ ¬0 = 1
```

Therefore:

```text
D(P,G)=D(Q,H)
```

## 3. Identity Assignment

If later:

```text
P = human participant
Q = artificial participant
```

or:

```text
P = employee
Q = platform user
```

or:

```text
P = institution
Q = software agent
```

then the domination classification does not change unless one of the structural variables changes.

## 4. Lesson

The kernel does not say the participants are identical in every respect. It says the domination predicate is invariant under substitution when the domination-relevant structure is preserved.
