# %%

# %% [markdown]
# # Exercise 17.1 by Michael Gergen
# ## (Books Database) In an IPython session, perform each of the following tasks on the books database from Section 17.2:
# ### a) Select all authors’ last names from the authors table in descending order.
# %%
import sqlite3
import pandas as pd

connection = sqlite3.connect("books.db")
# %%
pd.read_sql("""SELECT *
FROM authors
ORDER BY last DESC, first DESC
""", connection, index_col=['id'])
# %% [markdown]
# ### b) Select all book titles from the titles table in ascending order.
# %%
pd.read_sql("""SELECT title FROM titles
ORDER BY title ASC""", connection)
# %% [markdown]
# ### c) Use an INNER JOIN to select all the books for a specific author. Include the title, copyright year and ISBN. Order the information alphabetically by title.
# %%
# we do not need the ID stuff because they do not share any similar names.
# use the WHERE for a specific author
pd.read_sql("""SELECT first, last, title, copyright, isbn
FROM authors
INNER JOIN titles
WHERE last = 'Quirk'""", connection)

#ORDER BY last, first, title""",connection)
# %% [markdown]
# ### d) Insert a new author into the authors table.
# %%
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
VALUES ('Walter', 'White')""")
# %%
# check insertion
pd.read_sql("SELECT * FROM authors ORDER BY last DESC, first DESC", connection)
# %% [markdown]
# ### e) Insert a new title for an author. Remember that the book must have an entry in the author_ISBN table and an entry in the titles table.
# %%
#in order to link these to the author in the structure of the table, we have to make sure that the IDs and ISBNs match each other in their respective fields.

cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn)
VALUES ('6','0123456789')""")
cursor = cursor.execute("""
INSERT INTO titles (isbn, title, edition, copyright)
VALUES ('0123456789', 'Test Title', 'Test Edition', 'Test Copyright')""")
# %%
pd.read_sql("""SELECT first, last, title, copyright, isbn
FROM authors
INNER JOIN titles
WHERE last = 'White'""", connection)
# %%
connection.close()