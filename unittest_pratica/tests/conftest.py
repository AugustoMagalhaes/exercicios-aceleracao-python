import pytest


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return "Trybe"
