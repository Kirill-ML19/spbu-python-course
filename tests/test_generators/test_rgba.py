import pytest
from itertools import islice
from project.Generators.rgba_generator import rgba_generator, get_rgba_element


@pytest.fixture
def sample_rgba():
    """
    Fixture to provide a sample of generated RGBA values.
    """
    return list(islice(rgba_generator(), 10))


def test_rgba_generator_structure(sample_rgba):
    """
    Test that each element in the RGBA generator has the correct structure.
    """
    for rgba in sample_rgba:
        assert isinstance(rgba, tuple)
        assert len(rgba) == 4
        assert all(isinstance(value, int) for value in rgba)
        assert 0 <= rgba[0] <= 255
        assert 0 <= rgba[1] <= 255
        assert 0 <= rgba[2] <= 255
        assert 0 <= rgba[3] <= 100 and rgba[3] % 2 == 0


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, (0, 0, 0, 0)),
        (1, (0, 0, 0, 2)),
        (2, (0, 0, 0, 4)),
        (3, (0, 0, 0, 6)),
        (4, (0, 0, 0, 8)),
    ],
)
def test_get_rgba_element(index, expected):
    """
    Test retrieval of specific indexed elements from the RGBA generator.
    """
    assert get_rgba_element(index) == expected


def test_rgba_elements_out_of_range():
    """
    Test that accessing an out-of-range index raises an IndexError.
    """
    with pytest.raises(IndexError):
        get_rgba_element(10**10)
