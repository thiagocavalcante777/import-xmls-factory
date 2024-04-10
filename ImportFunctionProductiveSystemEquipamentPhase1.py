import pandas as pd

import sys
sys.path.append('./DAO')

import FunctionProductiveSystemEquipamentPhase1DAO

xlsPath = "./sheets/funcoes_sistemas_produtivos_equipamentos_fase_1.xlsx"

registros = pd.read_excel(xlsPath, sheet_name='sheet')

registros = pd.MultiIndex.from_frame(registros, names=('funcao','sistemas_produtivo', 'equipamento', 'numero'))

for registro in registros:    
    print(registro)
    functionProductiveSystemEquipment = FunctionProductiveSystemEquipamentPhase1DAO.FunctionProductiveSystemEquipamentPhase1DAO
    result = functionProductiveSystemEquipment.insertRegister(registro[0], registro[1], registro[2], registro[3])
    print(result)
