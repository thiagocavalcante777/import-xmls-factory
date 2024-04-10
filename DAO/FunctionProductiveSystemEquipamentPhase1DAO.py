import sys
sys.path.append('../')
import mysqlConnector

class FunctionProductiveSystemEquipamentPhase1DAO:
    
    def insertRegister(function, productiveSystem, equipment, number):
        insertQuery = "insert into equipment_function_productive_system_equipment_phase_1(equipment_function, productive_system, equipment_name, equipment_number) VALUES('{function}', '{productiveSystem}', '{equipment}', '{number}');".format(function=function, productiveSystem=productiveSystem, equipment=equipment, number=number)
        result = mysqlConnector.executeInsertQuery(insertQuery)
        return result