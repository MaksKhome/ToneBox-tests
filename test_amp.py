import pytest
from amp import Amp

@pytest.fixture
def amp():
    yield Amp("ToneBox")

@pytest.mark.smoke
def test_default_gain_is_5(amp):
    assert amp.gain == 5

def test_set_gain_changes_gain(amp):
    amp.set_gain(9)
    assert amp.gain == 9

@pytest.mark.parametrize("value", [0, 5, 10, 7])
def test_set_gain_accepts_value(amp, value):
    amp.set_gain(value)
    assert amp.gain == value

@pytest.mark.skip(reason="feature not built yet")
def test_preset_rename():
    ...

@pytest.mark.xfail(reason="Amp does not limit gain to 10 yet")
def test_gain_above_10_is_clamped(amp):
    amp.set_gain(15)
    assert amp.gain <= 10