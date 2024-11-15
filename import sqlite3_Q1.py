import sqlite3

# Connect to the SQLite database
db_path = '/Users/tavisgoldwire/Desktop/world_1.sqlite'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query to find the country with the most recent year of independence
query = """
SELECT Name, IndepYear
FROM Country
WHERE IndepYear = (SELECT MAX(IndepYear) FROM Country);
"""

cursor.execute(query)
result = cursor.fetchone()
print("The country with the most recent year of independence:", result)

# Close the connection
conn.close()

#The country with the most recent year of independence: ('Palau', 1994)