import pytest

@pytest.mark.great
def test_greater():
   num = 100
   assert num > 90
@pytest.mark.great1
def test_greater_equal():
   num = 100
   assert num >= 100
@pytest.mark.less
def test_less():
   num = 100
   assert num < 200
