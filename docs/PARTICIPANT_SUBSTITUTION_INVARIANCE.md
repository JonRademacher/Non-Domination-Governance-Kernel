# Participant Substitution Invariance Theorem

## 0. Purpose

This file states and proves the central portability theorem of the Non-Domination Governance Kernel. The theorem explains why the kernel can apply across humans, artificial agents, organizations, institutions, platforms, and hybrid systems without first resolving species, substrate, embodiment, phenomenology, or personhood.

The theorem does not say that all participants are morally identical. It does not say that all participants are conscious. It does not say that all participants have rights. It says something narrower and more structural:

```text
If the domination predicate depends only on frame authority and viable exit, then domination classification is invariant under participant substitution whenever those structural variables are preserved.
```

## 1. Background Predicate

The kernel defines domination as:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

where:

```text
P = participant
G = governing relation
F_P = structural frame of P
Final(G,F_P) = G has final admissibility authority over F_P
ViableExitFrom(P,G) = P has legitimate standing-preserving exit from G
```

The predicate contains no primitive term for:

```text
human
AI
institution
organism
machine
consciousness
emotion
phenomenology
biology
```

Those categories may matter in other theories, but they do not occur in this domination predicate.

## 2. Structural Signature

Define the domination-relevant structural signature of a participant-governance pair:

```text
Σ_D(P,G) = (
    HasFrame(P),
    Final(G,F_P),
    ViableExitFrom(P,G),
    Repairable(P,G),
    Contestable(P,G),
    StandingPreserved(P,G)
)
```

The minimal domination signature is:

```text
Σ_D^min(P,G) = (Final(G,F_P), ViableExitFrom(P,G))
```

because domination itself depends only on those two values once frame evaluability is established.

## 3. Substitution Relation

Let `P` and `Q` be two participants, possibly of different kinds. They may differ in substrate, embodiment, cognition, sensory access, legal status, or institutional form.

Define domination-equivalence under governance relations `G` and `H`:

```text
(P,G) ≡_D (Q,H)
```

iff:

```text
HasFrame(P) = HasFrame(Q)
Final(G,F_P) = Final(H,F_Q)
ViableExitFrom(P,G) = ViableExitFrom(Q,H)
```

A stronger equivalence also preserves repair, contestation, and standing:

```text
(P,G) ≡_D^+ (Q,H)
```

iff:

```text
Σ_D(P,G) = Σ_D(Q,H)
```

## 4. Theorem: Participant Substitution Invariance

### Theorem

For any two participants `P` and `Q` and governance relations `G` and `H`, if the domination-relevant structural variables are preserved under substitution, then the domination classification is preserved:

```text
(P,G) ≡_D (Q,H) ⇒ [D(P,G) ⇔ D(Q,H)]
```

Equivalently:

```text
If Final(G,F_P) = Final(H,F_Q)
and ViableExitFrom(P,G) = ViableExitFrom(Q,H),
then D(P,G) = D(Q,H).
```

provided both frames are evaluable.

## 5. Proof

Assume:

```text
(P,G) ≡_D (Q,H)
```

By definition of domination-equivalence:

```text
Final(G,F_P) = Final(H,F_Q)
ViableExitFrom(P,G) = ViableExitFrom(Q,H)
```

By the kernel definition:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

and:

```text
D(Q,H) ⇔ Final(H,F_Q) ∧ ¬ViableExitFrom(Q,H)
```

Substitute the preserved values from domination-equivalence into the second biconditional. Since both conjuncts are equal under the equivalence relation, the truth value of:

```text
Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

is identical to the truth value of:

```text
Final(H,F_Q) ∧ ¬ViableExitFrom(Q,H)
```

Therefore:

```text
D(P,G) ⇔ D(Q,H)
```

Thus domination classification is invariant under participant substitution whenever the domination-relevant structural variables are preserved.

∎

## 6. Interpretation

The theorem says that domination classification is not species-indexed, substrate-indexed, embodiment-indexed, or phenomenology-indexed within this kernel. It is indexed to the structural relation between:

```text
frame
authority
viable exit
```

Thus, if a human, artificial agent, institution, platform account, legal subject, or organizational role has the same domination-relevant signature, the kernel returns the same domination classification.

## 7. What the Theorem Does Not Prove

The theorem does not prove:

```text
P and Q are morally equivalent
P and Q have the same rights
P and Q are conscious
P and Q have the same interests
P and Q should receive identical legal treatment
P and Q have equivalent capacities
```

It proves only classification invariance for the domination predicate.

## 8. Corollary: Identity-Neutral Classification

If two blind participants `P_1` and `P_2` are classified before identity assignment, then later identity assignment cannot alter the domination classification unless it modifies a structural variable.

```text
StructuralClassification(P_i,G_i) before identity
+
identity assignment after classification
⇒ classification unchanged
```

This justifies the blind classification protocol.

## 9. Corollary: Cross-Domain Portability

The kernel can be ported across domains when the target domain can represent:

```text
structural frames
final authority over frames
legitimate viable exit
standing preservation
repairability
contestability
```

Therefore the same classifier can be meaningfully applied to:

```text
AI governance
workplace governance
platform governance
legal systems
healthcare systems
research institutions
supply chains
identity systems
multi-agent systems
```

provided the structural variables are properly translated.

## 10. Corollary: Anti-Anthropocentric Discipline

Because the domination predicate does not include a human-specific primitive, a classification cannot be rejected merely because the participant is non-human.

A valid rejection must challenge at least one structural premise:

```text
HasFrame(P)
Final(G,F_P)
ViableExitFrom(P,G)
StandingPreserved(P,G)
```

This prevents dismissal by substrate alone.

## 11. Corollary: Anti-Anthropomorphic Discipline

Because the domination predicate does not include consciousness, personhood, suffering, or emotion, a positive domination classification must not be inflated into those claims.

A valid positive result is:

```text
D(P,G)=1
```

not:

```text
P is conscious
P is a person
P has subjective experience
P has legal rights
```

Those require separate theories.

## 12. Falsification Conditions

The theorem fails only if one of the following is shown:

```text
1. D(P,G) depends on variables not included in Σ_D^min.
2. Final authority cannot be structurally translated across participant types.
3. Viable exit cannot be structurally translated across participant types.
4. Frame evaluability depends necessarily on a human-specific primitive.
5. Identity assignment changes structural variables rather than merely naming participants.
```

These are the correct attack surfaces for critics.

## 13. Strong Form

The strong version states:

```text
Σ_D(P,G)=Σ_D(Q,H) ⇒ Class(P,G)=Class(Q,H)
```

where `Class` may include:

```text
open governance
bounded governance
constraint without established domination
repairable domination
closed domination
recursive domination
```

The strong form requires preservation of repairability, contestability, and standing-preserving exit in addition to the minimal domination predicate.

## 14. Design Consequence

Any system that claims to implement non-domination governance must classify structurally equivalent cases equivalently across participant types.

If the same authority-exit topology is called domination for a human but not for an artificial participant, the system must identify which structural variable differs. If it cannot, the asymmetry is not justified by the kernel.

## 15. Summary

The participant substitution invariance theorem is the kernel's deepest portability result:

```text
Domination is not a property of what a participant is made of.
Domination is a property of how authority over its frame and viable exit from that authority are arranged.
```
