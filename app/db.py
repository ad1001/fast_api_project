import sqlite3 

class UOWManager(object):
    def __init__(self):
        self.db = sqlite3.connect('User')
        self.cursor = self.db.cursor()
    
    def get_cursor(self):
        return self.cursor

class CreateDataBase(object):
    def __init__(self,cursor):
        sql_query = """
        Create table user(
            email_id text primary key,
            twitter_id text,
            twitter_password password
            todo text
            
        )
        """
        cursor.execute(sql_query)
        print('db created')
    
    def insert_user(self,curr,user):
        sql_query = """
            Insert into user values(
                ?,?,?,?,?
            );
        
        """
        curr.execute(sql_query,())
    
    def get_user_creds(self,curr,email_provided):
        sql_query = """
        select * from user where email_id in ? ;
    """
        curr.execute(sql_query,(email_provided))



