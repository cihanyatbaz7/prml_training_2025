import pandas as pd
import pytest

from pandas.testing import assert_series_equal

from animal_shelter import features


def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features.check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)


@pytest.fixture()
def sex_upon_outcome_data():
    """Fixture providing sample sex_upon_outcome data for testing."""
    return pd.Series([
        "Neutered Male",
        "Spayed Female",
        "Intact Male",
        "Intact Female",
        "Unknown"
    ])

def test_check_sex(sex_upon_outcome_data):
    """Test that get_sex correctly extracts sex from sex_upon_outcome."""
    result = features.get_sex(sex_upon_outcome_data)
    expected = pd.Series(["male", "female", "male", "female", "unknown"])
    assert_series_equal(result, expected)


def test_get_neutered(sex_upon_outcome_data):
    """Test that get_neutered correctly identifies fixed/intact status."""
    result = features.get_neutered(sex_upon_outcome_data)
    expected = pd.Series(["fixed", "fixed", "intact", "intact", "unknown"])
    assert_series_equal(result, expected)


def test_get_sex_raises_error_for_non_series():
    """Test that get_sex raises TypeError when input is not a Series."""
    with pytest.raises(TypeError, match="Input must be a pandas Series"):
        features.get_sex("not a series")