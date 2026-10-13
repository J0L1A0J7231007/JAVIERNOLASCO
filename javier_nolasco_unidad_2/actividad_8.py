# Act 5. Create a class Book with attributes title and num_pages. Override:
# __str__() to print "Book: X, Pages: Y".
# __len__() so that len(book) returns the number of pages.

class Libro:
    # Clase para representar un libro y sus características
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas

    def __str__(self):
        # Sobrescribe la representación en formato texto
        return f'Libro: {self.titulo}, Páginas: {self.total_paginas}'

    def __len__(self):
        # Define el comportamiento al usar la función integrada len()
        return self.total_paginas


ejemplar = Libro("Fundamentos de Programación", 340)

print(ejemplar)  # Invoca automáticamente __str__()
print(f'Extensión del libro: {len(ejemplar)} páginas')  # Invoca __len__()