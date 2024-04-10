import sys
sys.path.append('../')

import mysqlConnector

class AreaEquipamentFunctionPhase1DAO:
    
    def insertRegister(area, equipmentFunction):
        insertQuery = "insert into area_equipment_function_phase_1(area, equipment_function) VALUES('{area}', '{equipmentFunction}');".format(area=area, equipmentFunction=equipmentFunction)
        result = mysqlConnector.executeInsertQuery(insertQuery)
        return result