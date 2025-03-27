# Desafio 1 - Nível do Herói

exp = int(input("Digite o valor de exp: "))
name = input("Digite o nome: ")
print(f'Olá {name}, o valor de exp é {exp}')

if exp < 1001:
    nivel = 'Ferro'
elif exp > 1001 and exp < 2000:
    nivel = 'Bronze'
elif exp > 2001 and exp < 5000:
    nivel = 'Prata'
elif exp > 5001 and exp < 7000:
    nivel = 'Ouro'
elif exp > 7001 and exp < 8000:
    nivel = 'Platina'
elif exp > 8001 and exp < 9000:
    nivel = 'Ascendente'
elif exp > 9001 and exp < 10000:
    nivel = 'Imortal'
elif exp > 10001:
    nivel = 'Radiante'

print(f'O Herói de nome {name} está no nível de {nivel}')
