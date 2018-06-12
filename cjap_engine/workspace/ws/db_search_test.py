import sqlite3

class db_test_get():

    def __init__(self):
        self.job_type_db = "/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/job_type.db"
        self.conn = sqlite3.connect(self.job_type_db)
        self.c = self.conn.cursor()
        self.job_list = []

    def fetch_data(self):
        self.c.execute("SELECT * from job_type_data")
        for row in self.c:
            self.job_list.append(str("(r'" + row[1] + "','" + row[0] + "')"))
        return self.job_list

#
# db_get = db_test_get()
# print db_get.fetch_data()
