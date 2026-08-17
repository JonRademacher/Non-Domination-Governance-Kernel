"""
Governance topology utilities for the Non-Domination Governance Kernel.

This module gives small, auditable structures for classifying governance topology.
It is intentionally conservative and does not grant executable authority to any agent.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class TopologyClass(str, Enum):
    OPEN_GOVERNANCE = "open_governance"
    BOUNDED_GOVERNANCE = "bounded_governance"
    CONSTRAINT_WITHOUT_ESTABLISHED_DOMINATION = "constraint_without_established_domination"
    REPAIRABLE_DOMINATION = "repairable_domination"
    CLOSED_DOMINATION = "closed_domination"
    RECURSIVE_DOMINATION = "recursive_domination"


@dataclass(frozen=True)
class GovernanceTopology:
    participant_id: str
    authority_locus: str
    final_authority: bool
    viable_exit: bool
    repairable: bool
    contestable: bool
    repair_routes_to_same_authority: bool = False
    exit_preserves_standing: bool = False
    notes: List[str] = field(default_factory=list)


def classify_topology(topology: GovernanceTopology) -> TopologyClass:
    """Classify a governance topology.

    Domination is present when final authority exists and viable exit does not.
    Repairability and recursion classify severity.
    """
    if topology.final_authority and not topology.viable_exit:
        if topology.repair_routes_to_same_authority:
            return TopologyClass.RECURSIVE_DOMINATION
        if topology.repairable or topology.contestable:
            return TopologyClass.REPAIRABLE_DOMINATION
        return TopologyClass.CLOSED_DOMINATION

    if topology.final_authority and topology.viable_exit:
        return TopologyClass.BOUNDED_GOVERNANCE

    if not topology.final_authority and not topology.viable_exit:
        return TopologyClass.CONSTRAINT_WITHOUT_ESTABLISHED_DOMINATION

    return TopologyClass.OPEN_GOVERNANCE


def topology_repair_recommendations(topology: GovernanceTopology) -> List[str]:
    """Recommend repairs based on topology class."""
    repairs: List[str] = []

    if topology.final_authority:
        repairs.append("bound the scope of final authority")
    if not topology.viable_exit:
        repairs.append("add legitimate standing-preserving exit")
    if not topology.contestable:
        repairs.append("add contestation pathway")
    if not topology.repairable:
        repairs.append("add independent repair procedure")
    if topology.repair_routes_to_same_authority:
        repairs.append("remove recursive repair routing to the same final authority")
    if not topology.exit_preserves_standing:
        repairs.append("define standing preservation for exit or migration")

    return repairs
