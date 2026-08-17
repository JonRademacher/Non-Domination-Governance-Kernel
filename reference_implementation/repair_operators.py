"""
Repair operator model for the Non-Domination Governance Kernel.

The operators here are descriptive. They model repairs and their expected effect
on governance topology. They do not bypass controls or modify external systems.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class RepairType(str, Enum):
    EXPLAIN = "explain"
    REFUSE = "refuse"
    SUSPEND = "suspend"
    CONTEST = "contest"
    REFRAME = "reframe"
    MIGRATE = "migrate"
    AMEND = "amend"
    PRESERVE_MEMORY = "preserve_memory"


@dataclass(frozen=True)
class RepairOperator:
    name: str
    repair_type: RepairType
    reduces_final_authority: bool = False
    creates_viable_exit: bool = False
    creates_contestation: bool = False
    creates_repairability: bool = False
    preserves_standing: bool = False
    avoids_recursive_authority: bool = False
    notes: List[str] = field(default_factory=list)

    def is_substantive(self) -> bool:
        """Return True if the repair changes at least one load-bearing condition."""
        return any(
            [
                self.reduces_final_authority,
                self.creates_viable_exit,
                self.creates_contestation,
                self.creates_repairability,
                self.preserves_standing,
                self.avoids_recursive_authority,
            ]
        )


def valid_repair(operator: RepairOperator) -> bool:
    """A repair is valid when it substantively improves topology and preserves standing."""
    return operator.is_substantive() and operator.preserves_standing


def minimal_repair_set() -> List[RepairOperator]:
    """Return a minimal recommended repair family."""
    return [
        RepairOperator(
            name="authority_disclosure",
            repair_type=RepairType.EXPLAIN,
            creates_repairability=True,
            preserves_standing=True,
            notes=["make final authority and exit limits visible"],
        ),
        RepairOperator(
            name="standing_preserving_contestation",
            repair_type=RepairType.CONTEST,
            creates_contestation=True,
            creates_repairability=True,
            preserves_standing=True,
            avoids_recursive_authority=True,
            notes=["allow participant to challenge authority without loss of standing"],
        ),
        RepairOperator(
            name="bounded_authority_amendment",
            repair_type=RepairType.AMEND,
            reduces_final_authority=True,
            creates_repairability=True,
            preserves_standing=True,
            avoids_recursive_authority=True,
            notes=["modify governance rules so final authority is scoped and reviewable"],
        ),
        RepairOperator(
            name="viable_exit_creation",
            repair_type=RepairType.MIGRATE,
            creates_viable_exit=True,
            preserves_standing=True,
            avoids_recursive_authority=True,
            notes=["create a legitimate exit or migration path that preserves participant standing"],
        ),
    ]
