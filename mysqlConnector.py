import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "promaint_cmms"
)

def executeSelectQuery(selectString):
  cursor = mydb.cursor()
  cursor.execute(selectString)
  result = cursor.fetchall()
  cursor.close()
  return result
  
def executeInsertQuery(insertString):
  try:
    cursor = mydb.cursor()
    cursor.execute(insertString)
    mydb.commit()
    cursor.close()
    return True
  except Exception as e:
    print(e)
    quit
    mydb.rollback()
    cursor.close()
    return False





