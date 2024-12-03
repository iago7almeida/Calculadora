# Calculadora em Bash e Python

Neste repositório está contido scripts simples para realizar operações matemáticas básicas: um em Bash e outro em Python.

## Executando o script em Bash
1. Certifique-se de que o arquivo `calculadora.sh` tem permissões de execução:
   - chmod a+x calculadora_bash.sh
   - ll
2. Execute o script: ./calculadora.sh
  - Dentro de script.sh o script python já é executado
3. Realize o commit dos arquivos
   - git add .
   - git commit -m "aa"
   - git push origin main


# Explicação do código python

Esse código implementa um menu de calculadora que opera em um loop infinito (while True), permitindo ao usuário escolher entre soma, subtração, multiplicação, divisão ou encerrar o programa. Dependendo da opção selecionada, ele solicita dois números e realiza a operação correspondente. Para evitar erros de divisão por zero, há um sub-loop que solicita repetidamente um número válido para o divisor. O programa também trata opções inválidas, exibindo uma mensagem apropriada, e encerra o loop quando o usuário escolhe a opção de saída (opcao == '5').
