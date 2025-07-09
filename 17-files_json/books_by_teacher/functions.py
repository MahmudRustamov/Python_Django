from file_manager import write_to_json, read_from_json


def add_book():
    book_id = input("Enter book id: ")
    title = input("Enter book title: ")
    price = int(input("Enter book price: "))
    author = input("Enter book author: ")

    data = {
        "id": book_id,
        "title": title,
        "price": price,
        "author": author
    }

    books = read_from_json(file="books.json")
    books.append(data)
    write_to_json(file="books.json", data=books)
    print("New books is added")


def show_books():
    books = read_from_json(file="books.json")
    for book in books:
        print(f"ID: {book['id']}\t{book['title']}\t{book['price']}\t{book['author']}")


def delete_book():
    book_id = input("Enter book id: ")
    books = read_from_json(file="books.json")
    for index, book in enumerate(books):
        if book['id'] == book_id:
            books.pop(index)
            write_to_json(file="books.json", data=books)
            return
    print("Book not found")


def update_book():
    book_id = input("Enter book id: ")
    books = read_from_json(file="books.json")
    for index, book in enumerate(books):
        if book['id'] == book_id:
            title = input("Enter new title: ")
            books[index]["title"] = title
            write_to_json(file="books.json", data=books)
            return
    print("Book not found")
