import pandas as pd

dados_medicos = pd.DataFrame(columns=['medico_referencia', 'medico_comparado', 'metrica', 'valor_referencia', 'valor_comparado'])

def adicionar_dados_medico(medico_referencia, medico_comparado, metrica, valor_referencia, valor_comparado):
    global dados_medicos
    novo_dado = pd.DataFrame({
        'medico_referencia': [medico_referencia],
        'medico_comparado': [medico_comparado],
        'metrica': [metrica],
        'valor_referencia': [valor_referencia],
        'valor_comparado': [valor_comparado]
    })
    dados_medicos = pd.concat([dados_medicos, novo_dado], ignore_index=True)

def comparar_medicos(medico_referencia, medico_comparado):
    global dados_medicos
    filtro = (dados_medicos['medico_referencia'] == medico_referencia) & (dados_medicos['medico_comparado'] == medico_comparado)
    dados_filtrados = dados_medicos[filtro]
    
    dados_filtrados['diferenca'] = dados_filtrados['valor_comparado'] - dados_filtrados['valor_referencia']
    
    return dados_filtrados

def calcular_diferencas(medico_referencia):
    global dados_medicos
    filtro = (dados_medicos['medico_referencia'] == medico_referencia)
    dados_filtrados = dados_medicos[filtro]
    
    dados_filtrados['diferenca'] = dados_filtrados['valor_comparado'] - dados_filtrados['valor_referencia']
    
    return dados_filtrados

def gerar_relatorio():
    global dados_medicos
    dados_medicos['diferenca'] = dados_medicos['valor_comparado'] - dados_medicos['valor_referencia']
    
    return dados_medicos

adicionar_dados_medico('Medico_A', 'Medico_B', 'tempo_procedimento', 30, 35)
adicionar_dados_medico('Medico_A', 'Medico_C', 'precisao', 90, 85)
adicionar_dados_medico('Medico_A', 'Medico_D', 'tempo_recuperacao', 7, 6)

resultado_comparacao = comparar_medicos('Medico_A', 'Medico_B')
print("Comparação de Medico_A com Medico_B:")
print(resultado_comparacao)

resultado_diferencas = calcular_diferencas('Medico_A')
print("\nDiferenças para todos os médicos comparados com Medico_A:")
print(resultado_diferencas)

relatorio_final = gerar_relatorio()
print("\nRelatório consolidado:")
print(relatorio_final)
