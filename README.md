# Calculadora GUI em Python

Este projeto é uma calculadora gráfica desenvolvida utilizando a linguagem Python, a biblioteca Tkinter para a interface gráfica e conceitos de Programação Orientada a Objetos (POO). A calculadora realiza operações aritméticas básicas e possui funcionalidades adicionais como o uso do histórico de operações e um botão de reset.

## Funcionalidades

- **Operações básicas**: Adição, subtração, multiplicação e divisão.
- **Histórico de operações**: Permite que o resultado da última operação seja reutilizado como operando.
- **Botão de reset (C)**: Limpa o display e reseta a calculadora.
- **Tratamento de erros**: Mensagens de erro são exibidas em casos como divisão por zero.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **Tkinter**: Biblioteca para criar interfaces gráficas.
- **Programação Orientada a Objetos**: Implementação baseada em classes para componentes da calculadora


### Arquivos:
1. **`main.py`**: Arquivo principal que inicializa a calculadora.
2. **`calculadora.py`**: Contém a lógica da calculadora, como armazenamento de histórico, cálculo das operações e tratamento de erros.
3. **`display.py`**: Classe que gerencia o display da calculadora, exibindo os números e resultados.
4. **`botao.py`**: Classe que representa os botões da calculadora e suas funcionalidades.

## Instalação

### Requisitos:
- **Python 3.x**: Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).
- **Tkinter**: Tkinter já vem com a instalação padrão do Python, então não é necessário instalar separadamente.

### Passos de Instalação:

1. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/usuario/calculadora
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd calculadora
    ```

3. Execute o arquivo principal:
    ```bash
    python main.py
    ```

## Como Usar

- **Números e Operações**: Clique nos botões numerados para inserir números no display e use os botões de operação para realizar cálculos.
- **Igual (=)**: Após inserir a operação, clique no botão `=` para calcular o resultado.
- **Reset (C)**: O botão `C` limpa o display e reseta a calculadora.
- **Histórico de Operações**: O resultado da última operação será armazenado no display e pode ser utilizado em novas operações.

## Tratamento de Erros

A calculadora trata erros comuns, como:
- **Divisão por zero**: Exibe uma mensagem de erro quando uma operação inválida, como divisão por zero, é realizada.
- **Entrada inválida**: Qualquer outra entrada inválida será exibida no display como "Erro".

## Decisões de Design

1. **Interface Gráfica (Tkinter)**: A interface foi desenvolvida para ser simples e intuitiva, com botões grandes e um display claro.
2. **Programação Orientada a Objetos**: O projeto foi dividido em classes para tornar o código mais modular e organizado.
3. **Avaliação das Operações**: Foi utilizado o `eval()` para avaliar a expressão matemática digitada no display, simplificando o processo de cálculo.

## Contribuição

Se desejar contribuir com melhorias no projeto, sinta-se à vontade para fazer um fork do repositório e enviar um pull request com as suas alterações.
