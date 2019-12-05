import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


def test_fours(inyector):
    # Es necesario un objeto ya creado
    valorEsperado = 4
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()


def test_yatzy_uno():
    assert 50 == Yatzy.yatzy([4, 4, 4, 4, 4])
    assert 50 == Yatzy.yatzy([2, 2, 2, 2, 2])


def test_yatzy_dos():
    assert 0 == Yatzy.yatzy([1, 5, 6, 3, 2])


def test_ones():
    assert 2 == Yatzy.ones(1, 2, 3, 1, 4)


def test_twos():
    assert 4 == Yatzy.twos(1, 2, 2, 4, 3)


def test_pair_uno():
    assert 12 == Yatzy.score_pair(1, 1, 6, 2, 6)


def test_pair_dos():
    assert 8 == Yatzy.score_pair(3, 3, 3, 4, 4)


def test_pair():
    assert 2 == Yatzy.checkRepeatedNumber(1, (1, 1, 2, 3, 4))
