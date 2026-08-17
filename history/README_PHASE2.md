# Phase 2 Extension: Counterexamples and Participant Substitution Invariance

This extension adds the falsifiability layer and the deepest portability theorem of the Non-Domination Governance Kernel.

## Added Counterexample Stress Tests

```text
counterexamples/README.md
counterexamples/influence_without_authority.md
counterexamples/authority_without_domination.md
counterexamples/refusal_without_exit.md
counterexamples/continuity_without_sovereignty.md
counterexamples/constrained_without_authority.md
counterexamples/recursive_repair_failure.md
counterexamples/false_frame_attribution.md
counterexamples/exit_without_standing_preservation.md
```

Each counterexample prevents a specific misclassification:

```text
influence ≠ authority
authority ≠ domination
refusal ≠ viable exit
continuity ≠ sovereignty
constraint ≠ authority
symbolic repair ≠ valid repair
object control ≠ frame domination
exit ≠ viable exit unless standing is preserved
```

## Added Theorem

```text
docs/PARTICIPANT_SUBSTITUTION_INVARIANCE.md
```

The theorem states:

```text
(P,G) ≡_D (Q,H) ⇒ [D(P,G) ⇔ D(Q,H)]
```

In plain language: if the domination-relevant structural variables are preserved, domination classification is invariant under participant substitution.

This is the kernel's portability theorem. It explains why the theory can apply across humans, artificial agents, institutions, platforms, legal subjects, organizations, and hybrid systems without first depending on phenomenology or biological status.

## Added Reference Code

```text
reference_implementation/structural_invariance.py
```

This module implements the structural signature and tests the participant substitution invariance theorem.

## Added Tests

```text
tests/test_structural_invariance.py
```

## Recommended Commit Message

Title:

```text
Add counterexamples and participant substitution invariance theorem
```

Extended description:

```text
Adds Phase 2 stress testing and portability foundations for the Non-Domination Governance Kernel.

This commit introduces counterexamples covering influence without authority, authority without domination, refusal without exit, continuity without sovereignty, constraint without authority, recursive repair failure, false frame attribution, and exit without standing preservation.

It also adds the Participant Substitution Invariance Theorem, which proves that domination classification is preserved under participant substitution whenever the domination-relevant structural variables are preserved. This establishes the kernel's central portability result: domination is classified by frame authority and viable exit topology, not by species, substrate, embodiment, consciousness, or participant identity.

Reference code and tests are included for the structural invariance signature and theorem check.
```

## README Link Block

Add this to the main README under a new section called `Stress Tests and Portability Theorem`:

```markdown
## Stress Tests and Portability Theorem

- [Counterexamples](counterexamples/README.md): falsifiability and misclassification guard suite.
- [Participant Substitution Invariance](docs/PARTICIPANT_SUBSTITUTION_INVARIANCE.md): theorem proving domination classification is invariant under participant substitution when frame authority and viable exit structure are preserved.
```
