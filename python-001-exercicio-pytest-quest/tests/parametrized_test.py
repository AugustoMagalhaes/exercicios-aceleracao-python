import pytest

from src.hex_converter import hexadecimal_to_decimal  # noqa: F401

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


@pytest.mark.parametrize(
        "hex, hex_equivalent",
        [
            ("8", 8),
            ("9", 9),
            ("a", 10),
            ("b", 11),
            ("c", 12),
            ("e", 14),
            ("f", 15)
        ]
)
@pytest.mark.dependecy
def test_converter(hex, hex_equivalent):
    assert hexadecimal_to_decimal(hex) == hex_equivalent
