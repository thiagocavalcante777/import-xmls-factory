import pandas as pd

import sys
sys.path.append('./DAO')

import EquipamentFunctionProductiveSystemPhase1DAO

xlsPath = "./sheets/funcoes_sistemas_produtivos_fase_1.xlsx"

registros = pd.read_excel(xlsPath, sheet_name='sheet')

registros = pd.MultiIndex.from_frame(registros, names=('funcao', 'sistema_produtivo'))

for registro in registros:    
    print(registro)
    equipmentFunctionSystemEquipment = EquipamentFunctionProductiveSystemPhase1DAO.EquipamentFunctionProductiveSystemPhase1DAO
    result = equipmentFunctionSystemEquipment.insertRegister(registro[0], registro[1])
    print(result)
