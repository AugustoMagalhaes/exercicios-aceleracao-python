from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro("titulo", "autor", 100)
    titulo, autor, paginas = livro.titulo, livro.autor, livro.paginas
    assert titulo == "titulo"
    assert autor == "autor"
    assert paginas == 100
