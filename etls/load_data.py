from database import *

conn = connectdb(db_name="numinous", user_name="stanley", hostname="appdev.cuq8d0oymhgs.us-west-2.rds.amazonaws.com",
                 pswd="Msan4ever!")

cursor = db_cursor(db_conn=conn)

