import pandas as pd
import ProductiveSystemDAO

registros = pd.read_excel(r'./sheets/sistemas_produtivos_filtered.xlsx', sheet_name='sistemas_produtivos')


for registro in registros['SISTEMAS_PRODUTIVOS']:    
    productiveSystem = ProductiveSystemDAO.ProductiveSystemDAO
    result = productiveSystem.insertProductiveSystem(registro)
    print(result)
