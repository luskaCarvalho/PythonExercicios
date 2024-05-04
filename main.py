class Cadastro:
    def __init__(self, nome, endereco, telefone, data_nascimento, login, senha):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.login = login
        self.senha = senha

class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque

class SistemaVendaLivros:
    def __init__(self):
        self.usuarios_cadastrados = {}
        self.livros_disponiveis =

    def cadastrar_usuario(self, usuario):
        self.usuarios_cadastrados[usuario.login] = usuario

    def adicionar_livro(self, livro, quantidades):
        if livro in self.livros_disponiveis:
            self.livros_disponiveis[livro] += quantidade
        else:
            self.livros_disponiveis[livro] = quantidade

    def cadastrar_usuario(self, usuario):
        self.usuarios_cadastrados[usuario.login] = usuario

    def adicionar_livro(self, livro, quantidade):
        if livro in self.livros_disponiveis:
            self.livros_disponiveis[livro] += quantidade
        else:
            self.livros_disponiveis[livro] = quantidade

    def validar_login(self, login, senha):
        if livro in self.usuarios_cadastrados:
            return self.usuarios_cadastrados(login).senha = =senha
        else:
            return False

    def verificar_disponibilidade_livro(self, livro, quantidade):
        if livro in self.livros_disponiveis and self.livros_disponiveis[livro] >= quantidade:
            return true
        else:
            return else