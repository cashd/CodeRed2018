import sqlite3

def create_database():
    conn = sqlite3.connect("restaurants.db")

    c = conn.cursor()
    c.execute('''CREATE TABLE items
        (restaurant_name text, longitude real, latitude real, menu_item text)''')
    conn.commit()
    conn.close()

'''
def update_database():
    conn = sqlite3.connect("restarunts.db")
    c = conn.cursor()
'''
conn = sqlite3.connect("restaurants.db")
c = conn.cursor()
#for i in range(10000):
#        c.execute("INSERT INTO items VALUES ('Pizza Hut', -177.48187, 28.06019, 'pizza')")
#c.execute("INSERT INTO items VALUES ('Dominoes', -175.48187, 29.06019, 'cheese pizza')")
#conn.commit()
for row in c.execute("SELECT * FROM items WHERE menu_item LIKE '%pizza%' and restaurant_name='Dominoes'"):
    print(row)
conn.close()
