from src.livro.livro import Livro


def test_descricao_livro(capsys):
    livro = Livro("Um Titulo", "Um Autor", 100)
    print(livro)
    captured = capsys.readouterr()
    output = captured.out
    expected = (
        "O livro Um Titulo"
        " de Um Autor"
        " possui 100 páginas.\n"
    )
    assert output == expected
