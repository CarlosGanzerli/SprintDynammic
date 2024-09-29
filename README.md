RM: 98809 - Gustavo Melo<br>
RM: 550433 - Guilherme Alves<br>
RM: 98840 - Carlos Ganzerli<br>
RM: 551137 - Paulo Lopes<br>
# Comparação de Dados de Treino Médicos

Este projeto é uma aplicação Python que permite comparar os dados de treino de médicos com base em métricas específicas. A aplicação utiliza um DataFrame do Pandas para armazenar os dados e calcular as diferenças entre os valores de treino de um médico de referência e outros médicos.

## Funcionalidades

- **Adicionar Dados**: Insere os dados de treino de médicos, incluindo a métrica, valor do médico de referência e valor do médico comparado.
- **Comparar Médicos**: Compara os dados de um médico de referência com outro médico, calculando a diferença entre os valores de treino.
- **Calcular Diferenças**: Calcula as diferenças entre todos os médicos comparados e o médico de referência para todas as métricas.
- **Gerar Relatório**: Gera um relatório consolidado com todas as comparações e as diferenças entre os valores de treino.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Pandas**: Biblioteca utilizada para manipulação de dados.

## Como Usar

1. **Instale as dependências**:
   Certifique-se de que o Pandas está instalado no seu ambiente:
   ```bash
   pip install pandas
   ```

2. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

3. **Execute o código**:
   O arquivo principal inclui exemplos de como adicionar dados e gerar o relatório.
   ```bash
   python main.py
   ```

### Exemplo de Uso

```python
# Adicionando dados de treino de médicos
adicionar_dados_medico('Medico_A', 'Medico_B', 'tempo_procedimento', 30, 35)
adicionar_dados_medico('Medico_A', 'Medico_C', 'precisao', 90, 85)
adicionar_dados_medico('Medico_A', 'Medico_D', 'tempo_recuperacao', 7, 6)

# Comparando médicos
resultado_comparacao = comparar_medicos('Medico_A', 'Medico_B')

# Calculando as diferenças para todos os médicos comparados com Medico_A
resultado_diferencas = calcular_diferencas('Medico_A')

# Gerando o relatório consolidado
relatorio_final = gerar_relatorio()
print(relatorio_final)
```

## Metodologia

A aplicação utiliza um conjunto de funções que seguem os seguintes passos:

1. **Coleta de Dados**: Os dados de treino de cada médico são adicionados ao sistema utilizando a função `adicionar_dados_medico`, que armazena informações como tempo de procedimento, precisão e tempo de recuperação.
   
2. **Comparação**: A função `comparar_medicos` realiza a comparação direta entre o médico de referência e outros médicos, calculando a diferença entre os valores de treino.
   
3. **Análise das Diferenças**: Com a função `calcular_diferencas`, o sistema gera as diferenças de todas as métricas para os médicos comparados com o médico de referência.
   
4. **Geração de Relatório**: A função `gerar_relatorio` consolida os dados em um formato tabular para análise posterior.

## Resultados

O sistema consegue gerar, com precisão, as diferenças entre os dados de treino de diferentes médicos, proporcionando uma visão clara das áreas onde cada médico pode ter um desempenho superior ou inferior ao médico de referência. O uso de tabelas facilita a visualização e interpretação dos resultados.

### Exemplo de Resultados:
```text
  medico_referencia | medico_comparado | metrica            | valor_referencia | valor_comparado | diferenca
  -----------------------------------------------------------------------------------------------
  Medico_A          | Medico_B         | tempo_procedimento | 30               | 35              | 5
  Medico_A          | Medico_C         | precisao           | 90               | 85              | -5
  Medico_A          | Medico_D         | tempo_recuperacao  | 7                | 6               | -1
```

## Conclusão

Este projeto oferece uma solução eficiente para comparar os dados de treino de médicos, ajudando a identificar oportunidades de melhoria e áreas de destaque entre os profissionais. A utilização de `pandas` para manipulação de dados torna o sistema flexível, escalável e fácil de utilizar. O relatório gerado proporciona uma visão consolidada que pode ser útil em contextos de treinamento e avaliação de desempenho clínico.
