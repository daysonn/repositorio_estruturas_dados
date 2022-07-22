
class Livro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn

    def setEditora(self, editora):
        self.editora = editora

    def getTitulo(self):
        return self.titulo

class Ebook(Livro):
    def __init__(self, titulo, isbn, link):
        Livro.__init__(self, titulo, isbn)
        self.link = link

nome_livro = input("Nome do livro: ")
isbn = input()
link = input()

primeiro_ebook = Ebook(nome_livro, isbn, link) 
primeiro_ebook.setEditora("Editora Resilia")
segundo_ebook = Ebook("Python para data science", '978-3-16-148410-0', 'http://www...') 

print(f"Nome do livro {primeiro_ebook.titulo} com ISBN: {primeiro_ebook.isbn}")