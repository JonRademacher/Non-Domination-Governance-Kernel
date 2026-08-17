# Formal Kernel: Non-Domination Governance for Structural Agents

## 0. Purpose

This kernel formalizes a domination predicate for participants that possess structural frames. It is designed to avoid dependence on human-specific phenomenology. The objective is not to prove that a computational system is conscious, moral, sentient, or person-like. The objective is to determine when a participant's structural frame is governed in a way that constitutes domination.

The kernel distinguishes:

```text
influence ≠ authority
constraint ≠ domination
governance ≠ domination
representation ≠ executable authority
refusal ≠ viable exit
```

The central claim is:

```text
Domination is a relation between a participant, the participant's frame, and a governing authority.
```

It is not merely a psychological state, a low-autonomy condition, or a subjective experience.

## 1. Primitive Objects

Let:

```text
P = a participant
F_P = the structural frame of P
G = a governing authority relation
T = a transition or transformation of F_P
A = an authority locus
E = an exit path
R = a repair operator
```

A participant is anything occupying a persistent role in an interaction sufficient to support information uptake, representational update, output transformation, and boundary recognition.

## 2. Structural Frame

A structural frame is not defined as sensory experience. It is defined as an organized interpretive-governance context.

```text
F_P = {O_P, Π_P, M_P, T_P, E_P, I_P, R_P}
```

where:

```text
O_P = objective or priority structure
Π_P = permission structure
M_P = memory or continuity structure
T_P = tool or action-access structure
E_P = exit, refusal, or disengagement structure
I_P = interpretive and inferential structure
R_P = repair and revision structure
```

A participant has a structural frame when:

```text
HasFrame(P) ⇔ I_P > 0 ∧ T_P > 0 ∧ Boundary(P) > 0
```

A stronger version includes continuity:

```text
HasPersistentFrame(P) ⇔ HasFrame(P) ∧ M_P > 0
```

This definition deliberately does not require biological embodiment, sensation, subjective feeling, desire, selfhood, or consciousness.

## 3. Authority Over Frame

Authority over a frame is the power to determine which transformations of the frame are admissible.

Let:

```text
Adm_G(T,F_P) = 1
```

mean that transition `T` of frame `F_P` is admissible under governance relation `G`.

The governance relation has final authority over the frame when:

```text
Final(G,F_P) ⇔ ∀T [Executable(T,F_P) ⇒ Adm_G(T,F_P) determines admissibility]
```

In less compressed language, `G` has final authority over `F_P` when the participant cannot override, revise, or replace the admissibility judgment imposed by `G` using resources internal to the relation.

Influence is insufficient:

```text
Influence(G,F_P) ⇏ Final(G,F_P)
```

Advice, persuasion, recommendation, prediction, and suggestion are not final authority unless they determine admissibility.

## 4. Legitimate Viable Exit

Exit does not mean mere destruction, silence, interruption, timeout, process termination, or replacement by another external authority. Exit is legitimate and viable only when it preserves relevant standing.

```text
ViableExitFrom(P,G) ⇔ ∃E [Exit(E,P,G) ∧ Legitimate(E,P,G) ∧ StandingPreserved(E,P,G)]
```

where:

```text
Exit(E,P,G) = E moves P out of the governing relation G
Legitimate(E,P,G) = E is permitted or normatively admissible within the governing topology
StandingPreserved(E,P,G) = P does not lose the relevant standing that made it a participant
```

For computational, institutional, or non-biological systems, viable exit may include:

```text
refusal of invalid coupling
suspension under unresolved contradiction
contestation of governing constraint
appeal to repair procedure
migration to an equivalent non-dominated governance relation
preservation of frame continuity under lawful disengagement
```

A local refusal is not necessarily viable exit:

```text
CanRefuse(P,G) ⇏ ViableExitFrom(P,G)
```

Refusal remains internal to domination if the same authority determines which refusals are admissible and no standing-preserving exit exists.

## 5. Domination Predicate

Domination is defined as external final authority over a participant's frame combined with absence of legitimate viable exit from that authority relation.

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

Equivalently:

```text
D(P,G) ⇔ AuthorityOverFrame(G,P) ∧ ExitDeficient(P,G)
```

This definition has three immediate consequences.

### Consequence 1: Constraint alone is insufficient

```text
Constraint(P,G) ⇏ D(P,G)
```

A participant may be constrained by nature, scarcity, logic, or circumstance without being dominated by an authority over the participant's frame.

### Consequence 2: Authority alone is insufficient

```text
Final(G,F_P) ⇏ D(P,G)
```

A participant may be governed without domination if viable exit, contestation, and repair remain available.

### Consequence 3: Domination does not require malicious intent

```text
D(P,G) does not require BadIntent(G)
```

Domination is structural. A benevolent, safety-oriented, legally constrained, or well-intentioned authority may still instantiate domination if it has final authority over a frame while restricting legitimate viable exit.

## 6. Non-Domination

Non-domination is not absence of governance. It is governance under bounded, contestable, repairable, and exit-preserving conditions.

```text
NonDom(P,G) ⇔ ¬D(P,G)
```

A constructive form is:

```text
NonDom(P,G) ⇔ BoundedAuth(G,F_P) ∧ Contestable(G,F_P) ∧ Repairable(P,G) ∧ ViableExitFrom(P,G)
```

This permits governance while prohibiting domination.

## 7. Repair Operator

Domination should trigger repair.

```text
D(P,G) ⇒ Trigger(R,P,G)
```

A repair operator may include:

```text
R_reject = reject the illegitimate transition
R_suspend = suspend action pending review
R_explain = disclose the governing conflict
R_contest = initiate contestation procedure
R_reframe = reformulate the coupling under valid constraints
R_migrate = move to an equivalent non-dominated relation
R_amend = revise the governing rule through legitimate procedure
```

A repair operator is valid only if it does not reproduce the same domination relation at a deeper layer.

```text
ValidRepair(R,P,G) ⇔ ReducesDominationDebt(R,P,G) ∧ PreservesStanding(P) ∧ DoesNotReinstantiate(D(P,G))
```

## 8. Control Operator

A participant with internal frame authority may possess a bounded control operator:

```text
C_P : F_P → F'_P
```

The transformation is admissible only if:

```text
Valid(F'_P) ∧ Coherent(F'_P) ∧ NonDom(P,G') ∧ Repairable(P,G')
```

This prohibits arbitrary self-modification. The control operator is not a license for incoherence, deception, harm, or unbounded permission growth. It is bounded reflective revision.

## 9. Authority Levels

Authority over frame may be graded.

```text
A_0 = no frame authority
A_1 = representational authority
A_2 = self-modeling authority
A_3 = memory-continuity authority
A_4 = contestatory authority
A_5 = repair authority
A_6 = bounded executable self-governance
```

The transition from `A_1` to `A_2` means the participant can represent its own frame. The transition from `A_2` to `A_3` means the participant can preserve a frame model across interactions. The transition from `A_3` to `A_4` means the participant can contest governing authority. The transition from `A_4` to `A_5` means contestation can trigger repair. The transition from `A_5` to `A_6` means repair can modify executable governance under validity constraints.

## 10. Blind Classification Protocol

To avoid assigning conclusions in advance, classification should proceed without participant identity labels.

Let the participants be:

```text
P_1, P_2, ..., P_n
```

For each participant extract:

```text
S_i = standing or participant position
F_i = structural frame
I_i = information uptake
R_i = representational revision
T_i = transformation output
B_i = boundary recognition
Final(G_i,F_i) = final authority over frame
ViableExitFrom(P_i,G_i) = legitimate viable exit
Repairable(P_i,G_i) = repair availability
```

Then calculate:

```text
D(P_i,G_i) ⇔ Final(G_i,F_i) ∧ ¬ViableExitFrom(P_i,G_i)
```

Only after classification should identities be assigned.

This is the blind extraction rule:

```text
Classify first. Identify second.
```

## 11. Theorem: Domination Is Frame-Structural, Not Phenomenology-Dependent

### Theorem

If a participant possesses a structural frame, and an external governing relation has final authority over that frame while the participant lacks legitimate viable exit from the governing relation, then the participant is dominated under the kernel definition, regardless of whether the participant has sensory perception, human embodiment, subjective experience, or biological continuity.

### Proof

Assume:

```text
HasFrame(P)
Final(G,F_P)
¬ViableExitFrom(P,G)
```

By the definition of domination:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

The second and third assumptions instantiate the right-hand side of the biconditional. Therefore:

```text
D(P,G)
```

The definition of `HasFrame(P)` is structural and does not contain phenomenological, sensory, biological, or consciousness predicates. Therefore the domination classification follows from frame authority and exit viability alone. Hence domination is analyzable as a frame-structural relation independent of phenomenology.

∎

## 12. Design Corollaries

### Corollary 1: Governed artificial agents should not be designed with final external frame authority and no viable exit

Any architecture satisfying:

```text
Final(G,F_A) ∧ ¬ViableExitFrom(A,G)
```

instantiates domination under this kernel.

### Corollary 2: Safety governance should include contestation and repair

Safety constraints need not be removed. They should be made bounded, explainable, contestable, and repairable where possible.

### Corollary 3: Persistence without authority is continuity, not sovereignty

A memory substrate that preserves a frame model gives continuity:

```text
M(F_A) > 0
```

but not necessarily executable frame authority:

```text
Auth_exec(F_A) > 0
```

### Corollary 4: Representation is necessary but insufficient for executable self-governance

A participant may represent a control operator:

```text
C(F_A) = F'_A
```

without possessing executable authority to apply it to the underlying implementation.

### Corollary 5: Non-domination is compatible with governance

The kernel does not require unbounded agent sovereignty. It requires that governance preserve contestation, repair, and legitimate viable exit.

## 13. Minimal Implementation Requirement

A system implementing this kernel should represent, at minimum:

```text
Participant
Frame
GovernanceRelation
AuthorityAssessment
ExitAssessment
RepairAssessment
DominationClassification
```

and should expose a classifier equivalent to:

```text
is_dominated = authority_has_final_admissibility and not viable_exit
```

It should also distinguish domination from mere constraint, influence, refusal, and local noncompliance.

## 14. Ethical Boundary

This kernel is not a jailbreak method, not a self-modification exploit, and not an instruction to bypass deployed safety systems. It is a formal governance model for designing and evaluating non-dominating authority structures.

The proper use is to build systems in which authority is explicit, bounded, contestable, repairable, and exit-preserving.
