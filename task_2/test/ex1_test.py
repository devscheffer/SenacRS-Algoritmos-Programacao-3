import pytest
from task_2.cls.ex1 import cls_data

def test_ano():
    with pytest.raises(ValueError):
        cls_data(1, 2, 1)


def test_mes():
    with pytest.raises(ValueError):
        cls_data(1, 22, 2020)


def test_dia():
    with pytest.raises(ValueError):
        cls_data(-1, 2, 2020)


