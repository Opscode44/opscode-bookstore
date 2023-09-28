import sqlite3


def query(sql_query, **query_var):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    rows = []
    if query_var.get("query") == "insert":
        cur.execute(sql_query, (query_var.get("title"), query_var.get("author"), query_var.get("year"), query_var.get("isbn")))
    elif query_var.get("query") == "view":
        cur.execute(sql_query)
        rows = cur.fetchall()
    elif query_var.get("query") == "search":
        cur.execute(sql_query, (query_var.get("title"), query_var.get("author"), query_var.get("year"), query_var.get("isbn")))
        rows = cur.fetchall()
    elif query_var.get("query") == "delete":
        cur.execute(sql_query, (query_var.get("id"),))
    elif query_var.get("query") == "update":
        cur.execute(sql_query, (query_var.get("title"), query_var.get("author"), query_var.get("year"), query_var.get("isbn"), query_var.get("id")))
    else:
        cur.execute(sql_query)

    conn.commit()
    conn.close()
    return rows


def create_table():
    query("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")


def insert(title, author, year, isbn):
    query("INSERT INTO book VALUES (NULL,?,?,?,?)", query="insert", title=title, author=author, year=year, isbn=isbn)


def view_all():
    rows = query("SELECT * FROM book", query="view")
    return rows


def search(title="", author="", year="", isbn=""):
    rows = query("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", query="search", title=title, author=author, year=year, isbn=isbn)
    return rows


def delete(id):
    query("DELETE FROM book WHERE id=?", query="delete", id=id)


def update(id, title, author, year, isbn):
    query("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", query="update", title=title, author=author, year=year, isbn=isbn, id=id)

#create_table()
#insert("The Ocean", "Alan Smith", 1950, 67557873927)
#print(search(author="Alan Smith"))
#delete(2)
#update(3, 'The Wind', 'Alan Smiths', 1951, 66767765657)
#print(view_all())
