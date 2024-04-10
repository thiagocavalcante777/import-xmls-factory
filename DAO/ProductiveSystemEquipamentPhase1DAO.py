
import sys
sys.path.append('../')
import mysqlConnector

class ProductiveSystemEquipamentPhase1DAO:
    
    def insertRegister(productiveSystem, equipment, number):
        insertQuery = "insert into productive_system_equipment_phase_1(productive_system, equipment, number) VALUES('{productiveSystem}', '{equipment}', '{number}');".format(productiveSystem=productiveSystem, equipment=equipment, number=number)
        result = mysqlConnector.executeInsertQuery(insertQuery)
        return result