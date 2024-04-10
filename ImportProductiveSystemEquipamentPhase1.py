import pandas as pd

import sys
sys.path.append('./DAO')

import ProductiveSystemEquipamentPhase1DAO

xlsPath = "./sheets/sistemas_produtivos_equipamentos_fase_1.xlsx"

registros = pd.read_excel(xlsPath, sheet_name='sheet')

registros = pd.MultiIndex.from_frame(registros, names=('sistemas_produtivo', 'equipamento', 'numero'))

for registro in registros:    
    print(registro)
    productiveSystemEquipment = ProductiveSystemEquipamentPhase1DAO.ProductiveSystemEquipamentPhase1DAO
    result = productiveSystemEquipment.insertRegister(registro[0], registro[1], registro[2])
    print(result)
