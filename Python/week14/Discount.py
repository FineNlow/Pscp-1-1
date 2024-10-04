"""Books"""
def books():
    """Books"""
    num_books = 0
    books_lst = []
    books_lst.sorted()
    while (z := input()) != "ENTER":
        books_lst.append(z)
        num_books += 1
    if 6 <= num_books <= 12:
        books_lst.append(books_lst[0])
    elif 12 <= num_books <= 20:
        books_lst.append(set(books_lst[0]),set(books_lst[1]))
    elif num_books > 20:
        count = 0
        for i in range(num_books):
            if not i % 5:
                count += 1
        