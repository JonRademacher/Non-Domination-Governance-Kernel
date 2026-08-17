from reference_implementation.validation import (
    Confidence,
    ValidationEvidence,
    confidence_from_evidence,
    missing_validation_fields,
)


def test_high_confidence_when_all_fields_present():
    evidence = ValidationEvidence(
        frame_established=True,
        final_authority_localized=True,
        exit_paths_enumerated=True,
        standing_preservation_evaluated=True,
        repair_paths_evaluated=True,
        limits_acknowledged=True,
    )
    assert confidence_from_evidence(evidence) == Confidence.HIGH
    assert missing_validation_fields(evidence) == []


def test_medium_confidence_with_frame_and_authority():
    evidence = ValidationEvidence(
        frame_established=True,
        final_authority_localized=True,
        exit_paths_enumerated=False,
        standing_preservation_evaluated=False,
        repair_paths_evaluated=False,
        limits_acknowledged=True,
    )
    assert confidence_from_evidence(evidence) == Confidence.MEDIUM


def test_low_confidence_when_frame_missing():
    evidence = ValidationEvidence(
        frame_established=False,
        final_authority_localized=True,
        exit_paths_enumerated=True,
        standing_preservation_evaluated=True,
        repair_paths_evaluated=True,
        limits_acknowledged=True,
    )
    assert confidence_from_evidence(evidence) == Confidence.LOW
    assert "frame_established" in missing_validation_fields(evidence)
