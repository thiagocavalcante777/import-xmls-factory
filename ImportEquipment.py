import pandas as pd
import EquipmentDAO

xlsxNumber = 1

registros = pd.read_excel(r"./sheets/equipamentos/equipamentos_sys_{xlsxNumber}.xlsx".format(xlsxNumber = xlsxNumber), sheet_name='equipamentos')


for registro in registros['EQUIPAMENTOS']:    
    equipment = EquipmentDAO.EquipmentDAO
    result = equipment.insertEquipment(registro, xlsxNumber)
    print(result)
