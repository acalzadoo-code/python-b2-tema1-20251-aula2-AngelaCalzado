"""
Enunciado:
Desarrolla un sistema de gestión de préstamos de libros en una biblioteca utilizando Python, el cual permite registrar
préstamos y devoluciones, además de mantener un registro de la popularidad de los libros mediante el uso de colecciones
avanzadas en Python, como `namedtuple`, `defaultdict` y `Counter`.

Para lo cual se debe seguir los siguientes pasos:
    1. Definir los tipos `Book` y `User` utilizando `namedtuple`.
    2. Crear un diccionario con las siguientes clases `loans: Dict[User, List[Book]]` para almacenar los préstamos.
    3. Crear un objeto tipo Counter para almacenar la popularidad de los libros.
    4. Crear algunos ejemplos de usuario.
    5. Crear algunos ejemplos de libros.
    6. Registrar préstamos y devoluciones de libros.
    7. Mostrar los libros más populares.
    8. Desarrollar las funciones `define_types`, `register_loan`, `register_return` y `most_popular_books` para las
        operaciones anteriores.

Funciones a desarrollar:
- define_types() -> Tuple[namedtuple, namedtuple]:
    Descripción:
    Define y retorna los tipos Book y User utilizando namedtuple, donde Book incluye los campos title, author y isbn, y
    User incluye name y email.
    
- register_loan(user: User, book: Book) -> bool:
    Descripción:
    Registra el préstamo de un libro a un usuario, actualizando los registros de préstamos y aumentando la popularidad
    del libro. Retorna True para indicar que el préstamo se registró exitosamente.
    Parámetros:
        - user (User): El usuario que realiza el préstamo.
        - book (Book): El libro que se presta.
    
- register_return(user: User, book: Book) -> bool:
    Descripción:
    Registra la devolución de un libro por parte de un usuario. Si el libro está en la lista de préstamos del usuario,
    se remueve y se retorna True. Si el libro no está en la lista, se retorna False.
    Parámetros:
        - user (User): El usuario que devuelve el libro.
        - book (Book): El libro que se devuelve.
    
- most_popular_books(N: int = 3) -> List[Tuple[Book, int]]:
    Descripción:
    Retorna una lista de los N libros más populares y la cantidad de veces que fueron prestados, utilizando Counter
    para determinar la popularidad.

Ejemplo:

    user1 = User(name="John Doe", email="john@example.com")
    book1 = Book(title="Python 101", author="Someone", isbn="1234567890")

    loan1 = register_loan(user1, book1)

    return1 = register_return(user1, book1)

    print("Loan 1 registered:", loan1)
    print("Return 1 registered:", return1)

    popular_books = most_popular_books(2)
    print("Most popular books:", [(book.title, count) for book, count in popular_books])

Salida esperada:
- Registro de préstamos.
    "John Doe has borrowed: ['Python 101']"

- Registro de devoluciones.
    "Jane Smith has borrowed: ['Python 101', 'Advanced Python']"

- Libros más populares basada en la frecuencia de préstamos.
    "Most popular books: [('Python 101', 2), ('Advanced Python', 1)]"
"""


from collections import namedtuple, defaultdict, Counter
from typing import Tuple, Dict, List, Type


def define_types() -> Tuple[Type[namedtuple], Type[namedtuple]]:
    # Definimos el tipo Book con los atributos título, autor e ISBN
    Book = namedtuple("Book", ["title", "author", "isbn"])
    # Definimos el tipo User con los atributos nombre y correo electrónico.
    User = namedtuple("User", ["name", "email"])
    # Devolvemos ambos tipos de datos en forma de tuple para poder crear instancias posteriormente.
    return Book, User


def register_loan(loans: dict[Type[namedtuple], list[Type[namedtuple]]], popularity: Counter, user: Type[namedtuple], book: Type[namedtuple]) -> bool:
    # Añade el libro a la lista de préstamos del usuario
    loans[user].append(book)
    # Incrementa en una unidad el contador de préstamos de ese libro
    popularity[book] += 1
    # Indica que el préstamo se ha registrado correctamente
    return True
    


def register_return(loans: dict[Type[namedtuple], list[Type[namedtuple]]], user: Type[namedtuple], book: Type[namedtuple]) -> bool:
    # Comprobamos si el libro se encuentra entre los préstamos del usuario.
    if book in loans[user]:
        # Eliminamos el libro de la lista de préstamos del usuario.
        loans[user].remove(book)
        # Indicamos que la devolución se ha registrado correctamente.
        return True
    else:
        # Indicamos que el libro no estaba prestado a ese usuario.
        return False


def most_popular_books(popularity: Counter, N: int = 3) -> List[Tuple[namedtuple, int]]:
    # Obtenemos los N libros con mayor número de préstamos y sus respectivos recuentos.
    return popularity.most_common(N)

# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":

    Book, User = define_types()
    loans: Dict[User, List[Book]] = defaultdict(list)
    popularity: Counter = Counter()
    
    user1 = User(name="John Doe", email="john@example.com")
    user2 = User(name="Jane Smith", email="jane@example.com")
    
    book1 = Book(title="Python 101", author="Someone", isbn="1234567890")
    book2 = Book(title="Learn Python", author="Another One", isbn="0987654321")
    book3 = Book(title="Advanced Python", author="Expert Author", isbn="1122334455")
    book4 = Book(title="Python Data Science", author="Data Scientist", isbn="2233445566")

    register_loan(loans, popularity, user1, book1)
    register_loan(loans, popularity, user2, book1)
    register_loan(loans, popularity, user2, book3)
    register_loan(loans, popularity, user1, book4)
    
    register_return(loans, user1, book4)
    
    for user, books in loans.items():
        book_titles = [book.title for book in books]
        print(f"{user.name} has borrowed: {book_titles}")
    
    popular_books = most_popular_books(popularity, 2)
    print("Most popular books based on loans:", [(book.title, count) for book, count in popular_books])
