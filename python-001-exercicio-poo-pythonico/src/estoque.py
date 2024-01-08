from typing import Dict


class Estoque:
    def __init__(self, produtos: Dict[str, int]) -> None:
        self.produtos = produtos

    def adicionar_produto_no_estoque(self, nome: str, quantidade: int) -> None:
        if nome in self.produtos:
            qtd = self.produtos.get(nome, 0)
            self.produtos.update({nome: qtd + quantidade})
        else:
            self.produtos.setdefault(nome, quantidade)

    def remover_produto_do_estoque(self, nome: str, quantidade: int) -> None:
        if quantidade > self.produtos.get(nome, 0):
            raise ValueError
        if nome in self.produtos:
            qtd = self.produtos.get(nome, 0)
            self.produtos.update({nome: qtd - quantidade})
        else:
            self.produtos.pop(nome, None)

    def atualizar_produto_no_estoque(
        self, nome: str, nova_quantidade: int
    ) -> None:
        if nome not in self.produtos:
            raise ValueError
        self.produtos.update({nome: nova_quantidade})

    def visualizar_estoque(self) -> None:
        lista_produtos_msg = [f"{k}: {v}" for k, v in self.produtos.items()]
        msg = "\n".join(lista_produtos_msg)
        print(msg)
