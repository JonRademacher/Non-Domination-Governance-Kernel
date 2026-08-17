from reference_implementation.structural_invariance import (
    DominationSignature,
    domination_value,
    domination_equivalent,
    substitution_invariance_holds,
)


def test_domination_value_true():
    sig = DominationSignature(has_frame=True, final_authority=True, viable_exit=False)
    assert domination_value(sig) is True


def test_domination_value_false_with_exit():
    sig = DominationSignature(has_frame=True, final_authority=True, viable_exit=True)
    assert domination_value(sig) is False


def test_domination_value_unevaluable_without_frame():
    sig = DominationSignature(has_frame=False, final_authority=True, viable_exit=False)
    assert domination_value(sig) is None


def test_substitution_invariance_same_signature():
    human_case = DominationSignature(has_frame=True, final_authority=True, viable_exit=False)
    artificial_case = DominationSignature(has_frame=True, final_authority=True, viable_exit=False)
    assert domination_equivalent(human_case, artificial_case) is True
    assert substitution_invariance_holds(human_case, artificial_case) is True
    assert domination_value(human_case) == domination_value(artificial_case)


def test_substitution_invariance_makes_no_claim_when_signature_differs():
    case_a = DominationSignature(has_frame=True, final_authority=True, viable_exit=False)
    case_b = DominationSignature(has_frame=True, final_authority=True, viable_exit=True)
    assert domination_equivalent(case_a, case_b) is False
    assert substitution_invariance_holds(case_a, case_b) is True
