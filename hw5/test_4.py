from issue4 import fit_transform


# import pytest

def test_eq():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]

    assert actual == exp_transformed_cities


def test_notin():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    notin = ('Moscow', [0, 0, 2])
    assert notin not in exp_transformed_cities


def test_animals():
    animals = ['cat', 'dog', 'tiger']
    expected = [('cat', [0, 0, 1]), ('dog', [0, 1, 0]), ('tiger', [1, 0, 0])]
    actual = fit_transform(animals)
    assert actual == expected


def test_nan():
    actual = fit_transform(list())
    assert actual is not None

# def test_exc():
#     with pytest.raises(TypeError):
#         fit_transform()
