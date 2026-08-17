# Counterexamples and Stress Tests

This folder exists to make the Non-Domination Governance Kernel falsifiable, criticizable, and harder to misuse. A governance theory becomes stronger when it states not only where it applies, but where it does not apply.

The kernel's domination predicate is:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

The counterexamples test each component separately:

```text
influence without authority
authority without domination
refusal without exit
continuity without sovereignty
constraint without authority
recursive repair failure
false frame attribution
exit without standing preservation
```

Each file follows the same structure:

```text
claim being tested
scenario
kernel assessment
why domination is or is not present
misclassification risk
lesson
```

The purpose is not to weaken the kernel. The purpose is to prevent it from becoming a slogan. A serious structural theory must distinguish domination from nearby but non-identical relations.
