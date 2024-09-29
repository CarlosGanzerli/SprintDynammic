RM: 98809 - Gustavo Melo
RM: 550433 - Guilherme Alves
RM: 98840 - Carlos Ganzerço
RM: 551137 - Paulo Lopes
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

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
"# SprintDynammic" 
