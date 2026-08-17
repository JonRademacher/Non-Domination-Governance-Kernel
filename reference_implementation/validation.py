"""
Validation helpers for the Non-Domination Governance Kernel.

These utilities model confidence and validation state for applied classifications.
They do not decide moral, legal, or ontological status.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Confidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class ValidationEvidence:
    frame_established: bool
    final_authority_localized: bool
    exit_paths_enumerated: bool
    standing_preservation_evaluated: bool
    repair_paths_evaluated: bool
    limits_acknowledged: bool
    cited_sources: List[str] = field(default_factory=list)


def confidence_from_evidence(evidence: ValidationEvidence) -> Confidence:
    """Assign confidence according to the Phase 8 validation protocol."""
    if all(
        [
            evidence.frame_established,
            evidence.final_authority_localized,
            evidence.exit_paths_enumerated,
            evidence.standing_preservation_evaluated,
            evidence.repair_paths_evaluated,
            evidence.limits_acknowledged,
        ]
    ):
        return Confidence.HIGH

    if evidence.frame_established and evidence.final_authority_localized:
        return Confidence.MEDIUM

    return Confidence.LOW


def missing_validation_fields(evidence: ValidationEvidence) -> List[str]:
    """Return missing validation components."""
    missing: List[str] = []
    if not evidence.frame_established:
        missing.append("frame_established")
    if not evidence.final_authority_localized:
        missing.append("final_authority_localized")
    if not evidence.exit_paths_enumerated:
        missing.append("exit_paths_enumerated")
    if not evidence.standing_preservation_evaluated:
        missing.append("standing_preservation_evaluated")
    if not evidence.repair_paths_evaluated:
        missing.append("repair_paths_evaluated")
    if not evidence.limits_acknowledged:
        missing.append("limits_acknowledged")
    return missing
