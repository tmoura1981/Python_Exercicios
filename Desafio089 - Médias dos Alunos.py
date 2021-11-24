principal, secundaria = [], []
while True:
    num = 0
    secundaria.append(num)  # 0
    secundaria.append(input('Nome: '))  # 1
    nota1 = int(input('Nota 1 = '))
    nota2 = int(input('Nota 2 = '))
    media = (nota1+nota2)/2
    secundaria.append(nota1)  # 2
    secundaria.append(nota2)  # 3
    secundaria.append(media)  # 4
    resp = input('Continuar? S/N ').upper()
    principal.append(secundaria[:])
    secundaria.clear()
    print('=' * 55)
    if 'S' not in resp:
        break
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')  # Fazer mais exemplos desta estrutura
print('='*55)
for pos, alunos in enumerate(principal):
    print(f'{pos:<4}{alunos[1]:<10}{alunos[4]:>8.1f}')
print('=' * 55)
while True:
    num = int(input('Qual aluno quer ver as notas? - (99 p/ interromper): '))
    if num == 99:
        break
    else:
        if num <= len(principal)-1:
            print(f'Notas de {principal[num][1]}: {principal[num][2], principal[num][3]}')  # Fazer mais exemplos desta estrutura
    print('=' * 55)
