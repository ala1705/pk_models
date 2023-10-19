import pytest
import pkmodel as pk


@pytest.mark.parametrize(
    "test",
    [
        (0.1, 0.1, 0.1, 1, [0.1], [0.2]),
        (1, 0.1, 0.1, 1, [0.1], [0.2]),
        (0.1, 1, 0.1, 1, [0.1], [0.2]),
        (0.1, 0.1, 1, 1, [0.1], [0.2]),
        (0.1, 0.1, 0.1, 1, [1], [0.2]),
        (0.1, 0.1, 0.1, 1, [0.1], [2]),
    ]
)
def test_accept_input(test):
    """Test if the Model.__init__ function accepts different kinds of acceptable input
    """
    pk.Model(*test)


@pytest.mark.parametrize(
    "test",
    [
        ("1", 0.1, 0.1, 1, [0.1], [0.2]),
        (0.1, "0.1", 0.1, 1, [0.1], [0.2]),
        (0.1, 0.1, "0.1", 1, [0.1], [0.2]),
        (0.1, 0.1, 0.1, 1.0, [0.1], [0.2]),
        (0.1, 0.1, 0.1, 1, ["0.1"], [0.2]),
        (0.1, 0.1, 0.1, 1, [0.1], ["0.2"]),
    ]
)
def test_reject_input_with_type_error(test):
    """Test if the Model.__init__ function rejects incorrect input and raises the appropiate error
    """
    with pytest.raises(TypeError):
        pk.Model(*test)


@pytest.mark.parametrize(
    "test",
    [
        (-0.1, 0.1, 0.1, 1, [0.1], [0.2]),
        (-1, 0.1, 0.1, 1, [0.1], [0.2]),
        (0.1, -0.1, 0.1, 1, [0.1], [0.2]),
        (0.1, 0.1, 0, 1, [0.1], [0.2]),
        (0.1, 0.1, -0.1, 1, [0.1], [0.2]),
        (0.1, 0.1, 0.1, 1, [-0.1], [0.2]),
        (0.1, 0.1, 0.1, 1, [0], [-0.2]),
        (0.1, 0.1, 0.1, -1, [0.1], [0.2]),
        (0.1, 0.1, 0.1, 3, [0.1], [0.2]),
        (0.1, 0.1, 0.1, 3, [0.1, 0.1, 0.1], [0.2, 0.2, 0.2]),
        (0.1, 0.1, 0.1, 1, [0.1, 0.1], [0.2]),
    ]
)
def test_reject_input_with_value_error(test):
    """Test if the Model.__init__ function rejects incorrect input and raises the appropiate error
    """
    with pytest.raises(ValueError):
        pk.Model(*test)


@pytest.mark.parametrize(
    "test",
    [
        (1, 1, 1, 1, [0.1], [0.2]),
        (0.1, 0.1, 0.1, 2, [0.1, 1], [2, 0.2]),
    ]
)
def test_ints_get_changed_to_floats(test):
    """Test if the integer values specified by the user are converted into floats
    """
    mod = pk.Model(*test)
    assert all(isinstance(val, float) for val in [mod.CL, mod.dose_rate, mod.V_c, *mod.V_p_list, *mod.Q_p_list])
