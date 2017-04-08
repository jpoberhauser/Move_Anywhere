from database import *
from indead import indead

conn = connectdb(db_name="numinous", user_name="stanley", hostname="appdev.cuq8d0oymhgs.us-west-2.rds.amazonaws.com",
                 pswd="Msan4ever!")

cursor = db_cursor(db_conn=conn)

#data = indead.get_data()
#columns = ", ".join(data[1].keys())
#tablename = data[0]
""
# for row in data[1:]:
#     row_item = ", ".join(["'%s'" % val.replace("'", "''") for val in row.values()])
#     insert_into_table(cursor, tablename, columns, row_item)
#
#
# conn.commit()

# close communication with database.
cursor.close()
conn.close()