import MySQLdb
import sys

HOST = "10.1.6.72"
USER = "root"
PASSWORD = "admin123"
DATABASE = "cokdb1"
DB = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
CURSOR = DB.cursor()


def execute(sql):
    try:
        CURSOR.execute(sql)
        data = CURSOR.fetchall()
        if not len(data) == 0:
            print data
        DB.commit()
    except:
        DB.rollback()
    finally:
        DB.close()

if __name__ == "__main__":
    sql = sys.argv[1]
    execute(sql)
