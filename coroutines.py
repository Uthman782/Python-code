def search():
    print("I am started.")
    book = "This is my Book. I read this book at 9 pm."
    import time
    time.sleep(3)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")

s1 = search()
next(s1)
s1.send('Book')
print("I am searching again okay.")
s1.send('Usman')
