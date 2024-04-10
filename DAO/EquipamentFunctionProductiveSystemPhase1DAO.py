import sys
sys.path.append('../')
import mysqlConnector

class EquipamentFunctionProductiveSystemPhase1DAO:
    
    def insertRegister(equipmentFunction, productiveSystem):
        insertQuery = "insert into equipment_function_productive_system_phase_1(equipment_function, productive_system) VALUES('{equipmentFunction}', '{productiveSystem}');".format(equipmentFunction=equipmentFunction, productiveSystem=productiveSystem)
        result = mysqlConnector.executeInsertQuery(insertQuery)
        return result