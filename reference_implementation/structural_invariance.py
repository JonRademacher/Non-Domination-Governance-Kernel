"""
Participant substitution invariance utilities.

The theorem implemented here is:

    If two participant-governance pairs preserve the domination-relevant
    structural variables, then their domination classification is the same.

This module tests structural portability. It does not assert moral equivalence,
consciousness, legal rights, personhood, or subjective experience.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class DominationSignature:
    """Domination-relevant structural signature."""

    has_frame: bool
    final_authority: bool
    viable_exit: bool
    repairable: Optional[bool] = None
    contestable: Optional[bool] = None
    standing_preserved: Optional[bool] = None

    def minimal(self) -> tuple[bool, bool, bool]:
        """Return the minimal signature used for the domination predicate."""
        return (self.has_frame, self.final_authority, self.viable_exit)

    def strong(self) -> tuple[bool, bool, bool, Optional[bool], Optional[bool], Optional[bool]]:
        """Return the stronger topology signature."""
        return (
            self.has_frame,
            self.final_authority,
            self.viable_exit,
            self.repairable,
            self.contestable,
            self.standing_preserved,
        )


def domination_value(signature: DominationSignature) -> Optional[bool]:
    """Return domination value, or None if frame is not evaluable."""
    if not signature.has_frame:
        return None
    return signature.final_authority and not signature.viable_exit


def domination_equivalent(a: DominationSignature, b: DominationSignature) -> bool:
    """Return True when minimal domination-relevant variables are preserved."""
    return a.minimal() == b.minimal()


def strong_domination_equivalent(a: DominationSignature, b: DominationSignature) -> bool:
    """Return True when the stronger classification signature is preserved."""
    return a.strong() == b.strong()


def substitution_invariance_holds(a: DominationSignature, b: DominationSignature) -> bool:
    """Check the participant substitution invariance theorem.

    If a and b are domination-equivalent, then their domination values must match.
    If they are not equivalent, the theorem makes no claim and returns True.
    """
    if not domination_equivalent(a, b):
        return True
    return domination_value(a) == domination_value(b)
