import connection
def PrintDataBaseValues():
    cursor = connection.conn.cursor()
    query = 'SELECT * FROM "user";'
    cursor.execute(query)
    for row in cursor:
        print(row)
    cursor.close()
def InsertValuesToDataBase(name,caste,email,password):
    try:
        '''query = 'INSERT INTO "user" (user_fname, user_lname, user_email, user_pwd) VALUES(?,?,?,?);'
        cursor = connection.conn.cursor()
        cursor.execute(query,(name,caste,email,password))'''
        cursor = connection.conn.cursor()
        params = (name,caste,email,password)
        cursor.execute("{CALL AddUser (?,?,?,?)}",params)
        connection.conn.commit()
        print("Values Exerted Successfully")
        cursor.close()
    except :
        print("Error Exist")
        connection.conn.rollback()
def DeleteValueFromDataBase(id):
    try:
        query = 'DELETE FROM "user" WHERE user_id=?;'
        cursor = connection.conn.cursor()
        cursor.execute(query,(id))
        connection.conn.commit()
        print("Value Deleted ")
        cursor.close()
    except :
        print("Value does not deleted")
        connection.conn.rollback()

InsertValuesToDataBase("Hafeez","Awan","hafeez@gmail.com","12345")
# PrintDataBaseValues()
# DeleteValueFromDataBase(5)
PrintDataBaseValues()
connection.conn.close()