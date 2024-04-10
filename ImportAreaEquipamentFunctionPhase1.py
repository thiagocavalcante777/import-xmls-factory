import pandas as pd

import sys
sys.path.append('./DAO')

import AreaEquipamentFunctionPhase1DAO

xlsPath = "./sheets/areas_funcoes_fase_1.xlsx"

registros = pd.read_excel(xlsPath, sheet_name='sheet')

registros = pd.MultiIndex.from_frame(registros, names=('area', 'funcao'))

for registro in registros:    
    print(registro)
    areaEquipmentFunction = AreaEquipamentFunctionPhase1DAO.AreaEquipamentFunctionPhase1DAO
    result = areaEquipmentFunction.insertRegister(registro[0], registro[1])
    print(result)
