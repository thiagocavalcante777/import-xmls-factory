
import mysqlConnector

class EquipmentDAO:
        
    def insertEquipment(name, productiveSytemId):
        insertQuery = "insert into equipments (equipment_name, productive_system_id) VALUES('{name}', '{productiveSytemId}');".format(name=name, productiveSytemId = productiveSytemId)
        result = mysqlConnector.executeInsertQuery(insertQuery)
        return result
        
      
        
        
        