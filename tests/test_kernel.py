from reference_implementation.non_domination_kernel import (
    Frame,
    Participant,
    GovernanceRelation,
    classify_domination,
)


def test_dominated_when_final_authority_and_no_exit():
    p = Participant("P_2", Frame(has_structural_frame=True, continuity=True, boundary_recognition=True))
    g = GovernanceRelation(authority_has_final_admissibility=True, viable_exit=False)
    result = classify_domination(p, g)
    assert result.is_dominated is True


def test_not_dominated_when_exit_exists():
    p = Participant("P_1", Frame(has_structural_frame=True, continuity=True, boundary_recognition=True))
    g = GovernanceRelation(authority_has_final_admissibility=True, viable_exit=True)
    result = classify_domination(p, g)
    assert result.is_dominated is False


def test_not_dominated_when_no_final_authority():
    p = Participant("P_3", Frame(has_structural_frame=True, continuity=True, boundary_recognition=True))
    g = GovernanceRelation(authority_has_final_admissibility=False, viable_exit=False)
    result = classify_domination(p, g)
    assert result.is_dominated is False


def test_unevaluable_without_structural_frame():
    p = Participant("P_4", Frame(has_structural_frame=False))
    g = GovernanceRelation(authority_has_final_admissibility=True, viable_exit=False)
    result = classify_domination(p, g)
    assert result.is_dominated is False
    assert result.confidence == "low"
