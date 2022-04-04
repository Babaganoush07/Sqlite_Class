import sqlite3

class Database:
    ''' constructor: Needs Database Name and Table Name
        querry: Uses self
        get_tables staticmethod: Pre-set database
        drop_table staticmethod: Needs Table name
        alter_table staticmethod: Rename a table, Need old Table name, New Table name
        copy_table staticmethod: Needs Table name
        insert: Needs Completion and Task
        update: Needs Completion, Task and the rowid
        search: Needs the search_word
        delete: Needs the rowid,
        destructor: closes connection'''
    def __init__(self, database, table_name):
        
        self.database = database
        self.table_name = table_name

        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS """ + self.table_name + """ (
                    completion text,
                    task text
                    )""")
        self.conn.commit()

    def querry(self):
        self.cursor.execute("SELECT rowid, * FROM " + self.table_name + " ORDER BY task ASC")
        database = self.cursor.fetchall()
        return database

    @staticmethod
    def get_tables(database):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name ASC")
        table_list = cursor.fetchall()
        return table_list

    @staticmethod
    def drop_table(table_name, database):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE " + table_name)

    @staticmethod
    def alter_table(old_table_name, new_table_name, database):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE " + old_table_name + " RENAME TO " + new_table_name)

    @staticmethod
    def copy_table(table_name, database):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE " + table_name + "_COPY AS SELECT * FROM "+ table_name)
        
    def insert(self, completion, task):
        self.cursor.execute("INSERT INTO " + self.table_name + " VALUES (?,?)",
                (completion, task))
        self.conn.commit()

    def update(self, rowid, completion, task):
        self.cursor.execute("UPDATE "+ self.table_name + " SET completion=?, task=? WHERE rowid = ?",
                                (completion, task, rowid))
        self.conn.commit()

    def delete(self, rowid):
        self.cursor.execute("DELETE FROM "+ self.table_name + " WHERE rowid=?",
                            (rowid,))
        self.conn.commit()

    def search(self, search_word):
        self.cursor.execute("SELECT rowid, * FROM " + self.table_name + " WHERE task LIKE ? ORDER BY task ASC", ("%"+search_word+"%",))
        database = self.cursor.fetchall()
        return database

    def delete_all(self, table_name):
        self.cursor.execute("DELETE FROM "+ self.table_name)
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()


if __name__=='__main__':
    
    # What database are you working with
    database = 'Test.db'
    print(database)

    # List all the tables with a staticmethod
    tables = Database.get_tables(database)
    for each in tables:
        print(each[0])

    # Connect to a table
    table_name = tables[0][0]
    connect = Database(database, table_name)

    # Querry the table rows
    data = connect.querry()
    for each in data:
        print(each)

