from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM ticket")
    rows = cursor.fetchall()

for row in rows:
    print(row)
