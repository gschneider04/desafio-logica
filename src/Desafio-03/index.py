class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")

# Testando a classe com exemplos
heroi1 = Heroi("Arthas", 30, "guerreiro")
heroi2 = Heroi("Jaina", 28, "mago")
heroi3 = Heroi("Shen", 25, "ninja")
heroi4 = Heroi("Iroh", 60, "monge")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
