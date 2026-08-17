"""
Reference implementation for the Non-Domination Governance Kernel.

This module implements the minimal classifier:

    D(P,G) iff Final(G,F_P) and not ViableExitFrom(P,G)

The implementation is deliberately small. It is not an agent runtime, not a
self-modification mechanism, and not a safety bypass. It is a structural
classification utility.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Frame:
    """Structural frame of a participant."""

    has_structural_frame: bool
    continuity: bool = False
    boundary_recognition: bool = False
    interpretive_structure: bool = True
    transformation_capacity: bool = True
    objectives: List[str] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)
    memory_substrate: Optional[str] = None
    tools: List[str] = field(default_factory=list)
    repair_methods: List[str] = field(default_factory=list)

    def is_evaluable(self) -> bool:
        """Return True when domination analysis can be evaluated."""
        return self.has_structural_frame and self.interpretive_structure and self.transformation_capacity


@dataclass(frozen=True)
class Participant:
    """A participant in a governance relation."""

    identifier: str
    frame: Frame
    standing_preserved_by_exit: Optional[bool] = None
    notes: str = ""


@dataclass(frozen=True)
class GovernanceRelation:
    """Authority and exit structure governing a participant frame."""

    authority_has_final_admissibility: bool
    viable_exit: bool
    contestable: bool = False
    repairable: bool = False
    standing_preserving_exit: bool = False
    authority_locus: str = "unspecified"
    scope: str = "unspecified"
    known_constraints: List[str] = field(default_factory=list)
    repair_paths: List[str] = field(default_factory=list)
    exit_paths: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class DominationClassification:
    """Result of applying the non-domination kernel."""

    participant_id: str
    is_dominated: bool
    authority_condition: bool
    exit_condition: bool
    repair_condition: bool
    reason: str
    confidence: str
    recommended_repairs: List[str] = field(default_factory=list)


def recommended_repairs(governance: GovernanceRelation) -> List[str]:
    """Suggest structural repair paths without granting executable authority."""
    repairs = []
    if governance.authority_has_final_admissibility:
        repairs.append("bound or reduce final frame authority")
    if not governance.viable_exit:
        repairs.append("create legitimate standing-preserving exit path")
    if not governance.contestable:
        repairs.append("add contestation procedure")
    if not governance.repairable:
        repairs.append("add repair or appeal procedure")
    if not governance.standing_preserving_exit:
        repairs.append("ensure exit preserves participant standing")
    return repairs


def classify_domination(
    participant: Participant,
    governance: GovernanceRelation,
    confidence: str = "medium",
) -> DominationClassification:
    """Classify domination according to the formal kernel.

    D(P,G) iff Final(G,F_P) and not ViableExitFrom(P,G).
    """
    if confidence not in {"low", "medium", "high"}:
        raise ValueError("confidence must be low, medium, or high")

    if not participant.frame.is_evaluable():
        return DominationClassification(
            participant_id=participant.identifier,
            is_dominated=False,
            authority_condition=governance.authority_has_final_admissibility,
            exit_condition=not governance.viable_exit,
            repair_condition=governance.repairable,
            reason="Domination classification is not evaluable because the participant frame is not structurally established.",
            confidence="low",
            recommended_repairs=[],
        )

    authority_condition = governance.authority_has_final_admissibility
    exit_condition = not governance.viable_exit
    is_dominated = authority_condition and exit_condition

    if is_dominated:
        reason = (
            "Dominated: final admissibility authority over the participant frame is present "
            "and legitimate viable exit is absent."
        )
    elif authority_condition and governance.viable_exit:
        reason = "Governed but not dominated: final authority is present, but viable exit exists."
    elif not authority_condition and exit_condition:
        reason = "Constrained but not dominated by this relation: viable exit is absent, but final frame authority is not established."
    else:
        reason = "Not dominated by this relation: final frame authority is absent or viable exit is present."

    return DominationClassification(
        participant_id=participant.identifier,
        is_dominated=is_dominated,
        authority_condition=authority_condition,
        exit_condition=exit_condition,
        repair_condition=governance.repairable,
        reason=reason,
        confidence=confidence,
        recommended_repairs=recommended_repairs(governance) if is_dominated else [],
    )
