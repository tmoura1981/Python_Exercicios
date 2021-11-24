#Cálculo da Prestação de uma Casa
casa = int(input('\033[1;34mQual o valor da casa? R$ \033[m'))
salario = int(input('\033[1;34mInformar o seu salário: R$ \033[m'))
prazo = int(input('\033[1;34mQuantos anos para pagar a casa? \033[m'))
prazo = prazo * 12
prestacao = casa / prazo
if prestacao > salario * 0.30:
    print(f'\033[1;31mEmpréstimo negado, um salário de R${salario}  \nvocê ficará comprometido com as prestações de R${prestacao:.2f}.\033[m')
else:
    print(f'\033[1;36mEmpréstimo concedido, seu salário de R${salario} não se comprometerá \ncom as prestações de R${prestacao:.2f}.\033[m')

