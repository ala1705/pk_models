import pytest
import pkmodel as pk


@pytest.mark.parametrize(
    "test",
    [
        (0.1, 0.1, 1, 0, 0.1, 1, [0.1], [0.2], 1.0, 1.0),
        (1, 0.1, 2, 2, 0.1, 1, [0.1], [0.2], 2.0, 1),
        (0.1, 1, 2, 4, 0.1, 1, [0.1], [0.2], 3.0, 2),
        (0.1, 0.1, 0, 0, 1, 1, [0.1], [0.2], 2, 60),
        (0.1, 0.1, 1, 1, 0.1, 2, [1, 2], [0.2, 0.2], 2, 2),
        (0.1, 0.1, 1, 1, 0.1, 1, [0.1], [2], 1, 1),
    ]
)
def test_accept_input(test):
    """Test if the Model.__init__ function accepts different kinds of acceptable input
    """
    pk.Model(*test)


@pytest.mark.parametrize(
    "test",
    [
        ("1", 0.1, 1, 1, 0.1, 1, [0.1], [0.2], 1, 1),
        (0.1, "0.1", 1, 1, 0.1, 1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, "1", 1, 1, 1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 0.1, 1.0, 1, 1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 1, 1, ["0.1"], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 1, 1, [0.1], ["0.2"], 1, 1),
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
        (-0.1, 0.1, 1, 1, 0.1, 1, [0.1], [0.2], 1, 1),
        (-1, 0.1, 1, 1, 0.1, 1, [0.1], [0.2], 1, 1),
        (0.1, -0.1, 1, 1, 0.1, 1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0, 1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, -0.1, 1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0.1, 1, [-0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0.1, 1, [0], [-0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0.1, -1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0.1, 3, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0.1, 3, [0.1, 0.1, 0.1], [0.2, 0.2, 0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0.1, 1, [0.1, 0.1], [0.2], 1, 1),
        (0.1, 0.1, 1.0, 0, 0.1, 1, [0.1], [0.2], 1.0, 1.0),
        (0.1, 0.1, 1, -1, 0.1, 1, [0.1], [0.2], 1.0, 1.0),
        (0.1, 0.1, 1, 0, 0.1, 1, [0.1], [0.2], 1.0, 61),
        (0.1, 0.1, 1, 0, 0.1, 1, [0.1], [0.2], 1.0, -1),
        (0.1, 0.1, 1, 0, 0.1, 1, [0.1], [0.2], -1, 1.0)
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
        (1, 1, 1, 1, 1, 1, [0.1], [0.2], 1, 1),
        (0.1, 0.1, 1, 1, 0.1, 2, [0.1, 1], [2, 0.2], 1, 1),
    ]
)
def test_ints_get_changed_to_floats(test):
    """Test if the integer values specified by the user are converted into floats
    """
    mod = pk.Model(*test)
    assert all(isinstance(val, float) for val in [mod.CL, mod.X, mod.dose_on, mod.dose_off,
                                                  mod.V_c, *mod.V_p_list, *mod.Q_p_list,
                                                  mod.run_time, mod.time_step_length])


@pytest.mark.parametrize(
    "test",
    [
        (),
        ([1]),
        (1, 1),
        (1, 1, 1, 0),
        (1, 1, 1, 2),
        (1, 1, 1, 2, [1, 1])
    ]
)
def test_default_values(test):
    """Test if the default values are properly processed
    """
    pk.Model(*test)


def test_default_values_with_named_arguments():
    """Test if the default values work well with named arguments
    """
    pk.Model(num_peripheries=2)
    pk.Model(time_step_length=40)


def test_default_values_raise_errors():
    """Test if an error is raised if some provided values are incompatible with the defaults.
    The default number of compartments is 0 so an empty list of parameters is going to be incompatible
    """
    with pytest.raises(ValueError):
        pk.Model(V_p_list=[])
