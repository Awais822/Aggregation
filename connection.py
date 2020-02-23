import pyodbc
try:
   conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=DESKTOP-ECF3RH7;'
                         'Database=Project;'
                         'Trusted_Connection=yes;')
except pyodbc.Error as ex:
    sqlState = ex.args[1]
    print(sqlState)
'''for driver in pyodbc.drivers():
        print(driver)'''
def News(heading,description,link,img,newspaper):
    try:
        '''query = 'INSERT INTO "user" (user_fname, user_lname, user_email, user_pwd) VALUES(?,?,?,?);'
        cursor = connection.conn.cursor()
        cursor.execute(query,(name,caste,email,password))'''
        cursor = conn.cursor()
        params = (heading,description,link,img,newspaper)
        cursor.execute("{CALL AddNews (?,?,?,?,?)}",params)
        conn.commit()
        print("Values Exerted Successfully")
        cursor.close()
    except :
        print("Error Exist")
        conn.rollback()
def GetValuesFromDatabase():
    try:
        corpus = []
        query = "select heading,newspaper,description from Project.dbo.News"
        cursor = conn.cursor()
        rows = cursor.execute(query)
        for x in rows:
            text = x.description
            newText = str.replace(text,"\\xad",'')
            corpus.append([newText,x.newspaper])
        cursor.close()
    except:
        print("Error Exists in this module")
        conn.rollback()
    return corpus