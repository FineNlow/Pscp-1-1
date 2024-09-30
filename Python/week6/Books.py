"""Books"""
from math import ceil
def books(num_book,pages,x,y):
    """Books"""
    day = 0
    left_book = num_book
    for _ in range(num_book):
        page_read=0
        while page_read<pages:
            read=ceil(((x+day)/(y+day))*pages)
            if read>=pages:
                day+=left_book
                left_book=0
                break
            page_read+=read
            day+=1
        if not left_book:
            break
        left_book-=1
    print(day)
books(int(input()),int(input()),int(input()),int(input()))
