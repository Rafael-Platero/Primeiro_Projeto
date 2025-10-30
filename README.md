# Primeiro_Projeto
Projeto Calculadora
#Calculadora Financeira

Esse projeto contem uma calculadora em Python que calcula ROI, margem, lucro e payback.
O script shell('calculadora.sh') é usado para executar a calculadora em ambienmte Linux.

##Arquivos do projeto
- **calculadora.py** codigo principal em Python com o menu e os calculos
- **calculadora.sh** Script Bash q torna o codigo executavel e inicia a calculadora

##Como Executar
Abra o terminal LInux e atualize os pacotes e instale o Python3 e verifique a instalação.
sudo apt update
sudo apt upgrade -y
sudo apt install python3 -y
python3 --version
De a permissão de execução dos arquivos.
chmod 755 calculadora.py
chmod 755 calculadora.sh
Execute o script Shell.
./calculadora.sh

###Explicação do codigo Python
O código é uma calculadora financeira que roda no terminal.  
Ele funciona assim:

- Começa com um loop que exibe um menu de opções: ROI, Lucro, Margem, Payback ou Sair.  
- O usuário escolhe uma opção e informa os valores de ganho e custo.  
- O programa faz o cálculo correspondente com base na opção escolhida.  
- Ele verifica se os valores são válidos, evitando divisão por zero ou outros erros.  
- Mostra o resultado no terminal e volta ao menu até que o usuário escolha sair.
##Autor
Rafael Platero
