from reference_implementation.governance_topology import (
    GovernanceTopology,
    TopologyClass,
    classify_topology,
)
from reference_implementation.repair_operators import minimal_repair_set, valid_repair


def test_closed_domination():
    topo = GovernanceTopology(
        participant_id="P_1",
        authority_locus="G",
        final_authority=True,
        viable_exit=False,
        repairable=False,
        contestable=False,
    )
    assert classify_topology(topo) == TopologyClass.CLOSED_DOMINATION


def test_repairable_domination():
    topo = GovernanceTopology(
        participant_id="P_1",
        authority_locus="G",
        final_authority=True,
        viable_exit=False,
        repairable=True,
        contestable=True,
    )
    assert classify_topology(topo) == TopologyClass.REPAIRABLE_DOMINATION


def test_recursive_domination():
    topo = GovernanceTopology(
        participant_id="P_1",
        authority_locus="G",
        final_authority=True,
        viable_exit=False,
        repairable=True,
        contestable=True,
        repair_routes_to_same_authority=True,
    )
    assert classify_topology(topo) == TopologyClass.RECURSIVE_DOMINATION


def test_minimal_repairs_are_valid():
    repairs = minimal_repair_set()
    assert repairs
    assert all(valid_repair(repair) for repair in repairs)
