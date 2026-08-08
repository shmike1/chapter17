# %%
import sqlite3

connection = sqlite3.connect("books.db")
# %%
import pandas as pd
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])
# %%
pd.read_sql("SELECT * FROM titles", connection)
# %%
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
df.head()
# %%
#retrieving only specific columns requires different than SELECT *
pd.read_sql('SELECT first, last FROM authors', connection)
# %%
# where clause finds predicates to satisfy certain selection criteria
pd.read_sql("""SELECT title, edition, copyright
FROM titles
WHERE copyright > '2016'""", connection)
# %%
#LIKE clause is for pattern matching
pd.read_sql("""SELECT id, first, last
FROM authors
WHERE last LIKE 'D%'""", connection, index_col=['id'])
# %%
#and underscore indicates a wildcard. % is account fill for rest
pd.read_sql("""SELECT id, first, last
FROM authors
WHERE first LIKE '_b%'""", connection, index_col=['id'])
# %%
# order by is for ascending/descinding orders
pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
# %%
#and do multiple columns by adding comma-separated value check
pd.read_sql("""SELECT id, first, last
FROM authors
ORDER BY last, first""",
            connection, index_col='id')
# %%
#can mix and match these orders by column
pd.read_sql("""SELECT id, first, last
FROM authors
ORDER BY last DESC, first ASC""",
            connection, index_col=['id'])
# %%
#where and order by can be combined
pd.read_sql("""SELECT isbn, title, edition, copyright
FROM titles
WHERE title LIKE '%How to Program'
ORDER BY title""", connection)
# %%
#merge data output with INNER_JOIN to include info from different sql places
pd.read_sql("""SELECT first, last, isbn
FROM authors
INNER JOIN author_ISBN
ON authors.id = author_ISBN.id
ORDER BY last, first""",connection).head()

#qualified name syntax is sometimes needed to distinguish that have the same name potentially
# %%
# modifying time with cursor statement
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
VALUES ('Sue', 'Red')""")
# values provided must match the column names specified both in order and type
# is also auto assigned a unique id
# %%
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
# %%
#update statement
cursor = cursor.execute("""UPDATE authors
SET last='Black'
WHERE last='Red' AND first='Sue'""")
#gets applied to every row w/i the where
# %%
cursor.rowcount
# %%
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
# %%
#delete from statement to remove rows
cursor = cursor.execute('DELETE FROM authors WHERE id=6')
# %%
cursor.rowcount
# %%
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
# %%
#close when no longer in use
connection.close()