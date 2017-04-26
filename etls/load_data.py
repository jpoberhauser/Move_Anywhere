from database import *
from indead import indead
from eventbrite import events
from greatschools import great_schools


def load_data(conn, package):

    data = package.get_data()
    columns = ", ".join(data[1].keys())
    tablename = data[0]

    for row in data[1:]:
        row_item = ", ".join(["'%s'" % val.replace("'", "''") for val in row.values()])

        try:
            insert_into_table(cursor, tablename, columns, row_item)
        except:
            print row

        conn.commit()


if __name__=="__main__":
    packages = [indead, events, great_schools]
    conn = connectdb(db_name="numinous", user_name="stanley",
                     hostname="appdev.cuq8d0oymhgs.us-west-2.rds.amazonaws.com",
                     pswd="Msan4ever!")

    cursor = db_cursor(db_conn=conn)

    #for package in packages:
    #    load_data(conn, package)

    load_data(conn, indead)
    # load the data for list of packages
    # close communication with database.
    cursor.close()
    conn.close()