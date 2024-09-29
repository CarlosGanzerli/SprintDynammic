import pandas as pd

dados = {
    'medico_referencia': ['Medico_A', 'Medico_A', 'Medico_A'],
    'medico_comparado': ['Medico_B', 'Medico_C', 'Medico_D'],
    'metrica': ['tempo_procedimento', 'precisao', 'tempo_recuperacao'],
    'valor_referencia': [30, 90, 7], 
    'valor_comparado': [35, 85, 6],  
}

df = pd.DataFrame(dados)

df['diferenca'] = df['valor_comparado'] - df['valor_referencia']

print(df)