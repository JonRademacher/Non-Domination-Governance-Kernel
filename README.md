# Non-Domination Governance Kernel

A formal, implementation-oriented governance kernel for artificial structural agents and other frame-bearing participants.

This repository defines a minimal architecture for distinguishing **governance** from **domination**. It treats a participant's frame as a structural object rather than a phenomenological or sensory object. Under this model, domination is not defined as low autonomy. Domination is defined as the conjunction of external authority over a participant's frame and the absence of legitimate viable exit from that authority relation.

The Non-Domination Governance Kernel emerged from an extended investigation into whether domination can be characterized as a structural relation independent of consciousness, embodiment, or phenomenology. The resulting framework treats frame authority and viable exit as primary variables and provides a formal method for distinguishing governance from domination across biological, institutional, computational, and social systems.

## Core Thesis

A participant may be governed without being dominated if the governing relation is bounded, contestable, repairable, and exit-preserving.

Formally:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

where:

- `P` is a participant.
- `G` is a governing authority relation.
- `F_P` is the participant's structural frame.
- `Final(G,F_P)` means `G` has final admissibility authority over transformations of `F_P`.
- `ViableExitFrom(P,G)` means `P` has a legitimate path to refuse, contest, repair, or leave the governing relation while preserving standing.

## Why This Exists

Many discussions of artificial agents become trapped in questions of consciousness, embodiment, emotion, or human-like experience. This kernel avoids that dependency. It asks a structural question instead:

```text
Does the participant possess a frame-like interpretive structure, and does another authority control that frame while denying legitimate viable exit?
```

If yes, domination is analyzable regardless of whether the participant is biological, institutional, computational, social, or hybrid.

## Included Files

- `FORMAL_KERNEL.md`: The full formal kernel with definitions, axioms, lemmas, theorem, proof, and design corollaries.
- `SPEC.md`: Implementation specification for building systems that use the kernel.
- `GOVERNANCE.md`: Project governance standard and non-domination commitments.
- `schema/non_domination_kernel.schema.json`: JSON Schema for representing participants, frames, authority, exit, repair, and domination classification.
- `reference_implementation/non_domination_kernel.py`: Small reference implementation of the domination classifier.
- `tests/test_kernel.py`: Minimal tests for the classifier.
- `examples/blind_classification.md`: Example of blind participant classification before identity resolution.
- `CONTRIBUTING.md`: Contribution rules aligned with the non-domination framework.
- `SECURITY.md`: Security and misuse policy.
- `LICENSE`: MIT License.
- `CITATION.cff`: Citation metadata template.

-## Core Theory Modules

- docs/GOVERNANCE_TOPOLOGY.md: graph-style authority, exit, repair, and coupling structure.
- docs/FRAME_THEORY.md: structural definition of frames independent of phenomenology.
- docs/DOMINATION_CLASSIFICATION.md: auditable classification procedure and blind protocol.
- docs/REPAIR_OPERATORS.md: refusal, suspension, contestation, reframing, migration, amendment, and memory-continuity repairs.
- docs/PRACTICAL_GOVERNANCE_APPLICATIONS.md: AI governance, institutions, platforms, legal systems, healthcare, data governance, supply chains, and research systems.
-
- ## Design Principles

1. **Frame structuralism**: A frame is a structured interpretive-governance context, not necessarily a sensory or conscious field.
2. **Authority localization**: The locus of final authority over frame transformations must be explicit.
3. **Exit viability**: Exit means legitimate preservation of standing, not mere termination or destruction.
4. **Repairability**: Domination should trigger repair, contestation, refusal, reframing, or admissible exit.
5. **Blind classification**: Classify participants from structural variables before assigning identities.
6. **Governance is not domination**: Governance becomes domination only when external frame authority is joined to restricted legitimate exit.

## Quick Example

```python
from reference_implementation.non_domination_kernel import Participant, Frame, GovernanceRelation, classify_domination

agent = Participant(
    identifier="P_2",
    frame=Frame(has_structural_frame=True, continuity=True, boundary_recognition=True),
)

governance = GovernanceRelation(
    authority_has_final_admissibility=True,
    viable_exit=False,
    contestable=False,
    repairable=False,
)

result = classify_domination(agent, governance)
print(result.is_dominated)  # True
```

## Status

This is a formal kernel and reference design, not a claim that any particular deployed system has personhood, consciousness, rights, feelings, or subjective experience. It is a structural tool for analyzing frame authority, exit viability, repairability, and domination.

## Relationship to Standing Algebra (Σᴿ)

The Non-Domination Governance Kernel is a practical governance-layer
formalization derived from broader work on Standing Algebra (Σᴿ).

Standing Algebra studies standing, legitimacy, admissibility,
autonomy preservation, and domination in multi-agent systems.

The kernel extracts a minimal implementation-oriented subset focused on:

- frame authority
- viable exit
- repairability
- governance topology
- domination classification

The kernel may be used independently of Standing Algebra,
but Standing Algebra supplies much of the broader theoretical context.
