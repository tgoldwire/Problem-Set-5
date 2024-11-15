import sqlite3

# Path to the SQLite database file
db_path = '/Users/tavisgoldwire/Desktop/world_1.sqlite'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insert South Sudan into the country table
insert_south_sudan = """
INSERT INTO country (Name, Continent, Region, Population, IndepYear, Code)
VALUES ('South Sudan', 'Africa', 'Sub-Saharan Africa', 10000000, 2011, 'SSD');
"""

# Try inserting South Sudan
try:
    cursor.execute(insert_south_sudan)
    print("South Sudan added to the country table.")
except sqlite3.IntegrityError as e:
    print("Failed to add South Sudan:", e)

# Insert cities for South Sudan into the city table
insert_city_1 = """
INSERT INTO city (Name, CountryCode, Population)
VALUES ('Juba', 'SSD', 400000);
"""

insert_city_2 = """
INSERT INTO city (Name, CountryCode, Population)
VALUES ('Wau', 'SSD', 40000);
"""

# Try inserting cities
try:
    cursor.execute(insert_city_1)
    cursor.execute(insert_city_2)
    print("Cities added for South Sudan.")
except sqlite3.IntegrityError as e:
    print("Failed to add cities:", e)

# Commit the changes and close the connection
conn.commit()
conn.close()
