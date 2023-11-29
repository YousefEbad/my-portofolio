import sqlite3
con = sqlite3.connect("movies.db")
curser = con.cursor()
curser.execute("CREATE TABLE movie(title TEXT, generTEXT, year INTEGER)")
con.commit()

con.close()

