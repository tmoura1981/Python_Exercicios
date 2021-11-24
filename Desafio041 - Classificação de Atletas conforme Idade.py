from datetime import datetime
ano_atual = datetime.today().year
ano_nasc = int(input('Qual o ano de seu nascimento? '))
dif = ano_atual - ano_nasc
if dif <= 9:
    print('Sua categoria é Mirim.')
elif dif <= 14:
    print('Sua categoria é Infantil.')
elif dif <=19:
    print('Sua categoria é Júnior.')
elif dif == 20:
    print('Sua categoria é Sênior.')
else:
    print('Sua categoria é Master.')