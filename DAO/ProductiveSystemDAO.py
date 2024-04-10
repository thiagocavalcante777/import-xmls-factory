
import mysqlConnector

class ProductiveSystemDAO:
    
    def insertProductiveSystem(name):
        insertQuery = "insert into productive_systems(name) VALUES('{name}');".format(name=name)
        result = mysqlConnector.executeInsertQuery(insertQuery)
        return result