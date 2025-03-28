# print('Digite seu Nome: ')
# nome = input()
# print(f'Olá {nome}, seja bem-vindo!')
# print(f'{nome} acabou de entrar no servidor')

#----------------------------//----------------------------

# NOTIFICACAO = 'CounterStrike diz: '
# print(f'{NOTIFICACAO}suas Skins foram vendidas!')
# print(f'{NOTIFICACAO}você ganhou 10 reais!')
# print(f'{NOTIFICACAO}Março finalizando com novas atualizações!')

#----------------------------//----------------------------

##NO PYTHON NÃO TEMOS VARIAVEIS CONSTANTES! 
##COMO BOA PRATICA USAMOS EM UPPER CASE PARA "CONSTANTES"


# VOVO = 'Vovó Maria'
# pote_Cafe = 'Café Melita'
# pote_Acucar = 'Açúcar União'
# pote_Biscoito = 'Biscoito Trakinas'

# print(f'Hoje na cozinha da vovó {VOVO} temos: {pote_Cafe}, {pote_Acucar} e {pote_Biscoito}')

# pote_Cafe = 'Café Pilão'
# pote_Acucar = 'Açúcar Cristal'
# pote_Biscoito = 'Biscoito Passatempo'
# VOVO = 'Vovó Ana'

# print(f'Hoje na cozinha da vovó {VOVO} temos: {pote_Cafe}, {pote_Acucar} e {pote_Biscoito}')

#----------------------------//----------------------------

##POKEMON NUMERO 1
# nome_Pokemon = 'Pikachu'
# nivel_Pokemon = 5
# pontos_Vida = 100
# pokemons_Sexo = 'Masculino'
# pokemons_Selecionavel = True

##POKEMON NUMERO 2
# nome_Pokemon2 = 'Charmander'
# nivel_Pokemon2 = 4
# pontos_Vida2 = 80
# pokemons_Sexo2 = 'Masculino'
# pokemons_Selecionavel2 = False

#-----------------------------//----------------------------

##APRENDENDO A USAR LISTAS:


# nomes_Pokemon = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur']
# nivel_Pokemon = [5, 4, 3, 2]
# pontos_Vida = [100, 80, 60, 40]
# pokemons_Sexo = ['Masculino', 'Masculino', 'Feminino', 'Feminino']
# pokemons_Selecionavel = [True, False, True, False]

# print(f'Pokémon 1: {nomes_Pokemon[0]}, nivel: {nivel_Pokemon[0]}, pontos de vida: {pontos_Vida[0]}, sexo: {pokemons_Sexo[0]}, selecionável: {pokemons_Selecionavel[0]}')

# nomes_Pokemon.insert(4, 'Mewtwo')

# print(nomes_Pokemon)

# nomes_Pokemon.pop(2)

# print(nomes_Pokemon)

# nomes_Pokemon.sort()

# print(nomes_Pokemon)

#-----------------------------//----------------------------

##APRENDENDO A USAR SETS


# nomes_Pokemon = {'Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur'}
# nivel_Pokemon = {5, 4, 3, 2}
# pontos_Vida = {100, 80, 60, 40}
# pokemons_Sexo = {'Masculino', 'Masculino', 'Feminino', 'Feminino'}
# pokemons_Selecionavel = {True, False, True, False}

# nomes_Pokemon.pop()
# print(nomes_Pokemon)
# print(list(nomes_Pokemon)[0])


##PARA ACESSAR UM SET PRECISAMOS CONVERTER PARA LISTA

#------------------------------//----------------------------

##APRENDENDO A MANIPULAR FUNCOES

# def torrar_pao(pao, nome):
#     print(f'{nome} está torrando o pão {pao}')
#     return 

# torrar_pao('pão francês', 'Lucas')

##Gerando um pedido de forma mais avançada

# import random

# print('Seja bem-vindo ao Café da Praça!')
# print('Hoje temos os seguintes tipos de café: expresso, latte, capuccino e mocha!')

# cafe = input('Vamos começar o seu pedido. Qual café você gostaria? ')

# pedido = random.randrange(0, 100)

# nome = input('Qual o seu nome? ')

# print(f'{nome}, seu pedido é o número {pedido}')

# if cafe == 'expresso':
#     preco = 5.00
# elif cafe == 'latte':
#     preco = 7.00
# elif cafe == 'capuccino':
#     preco = 8.00
# elif cafe == 'mocha':
#     preco = 9.00
# else:
#     preco = 0.00


# def fazer_cafe(cafe, pedido, nome = 'Cliente', preco = 0.00):
#     print(f'O pedido {pedido} está sendo preparado!')
#     print(f'O pedido inclui um {cafe}, o pedido está em nome de: {nome}!')
#     print(f'O valor do pedido é R$ {preco}')
#     print(f'O Pedido {pedido} está pronto!')  
#     return

# fazer_cafe(cafe, pedido, nome, preco)


#------------------------------//----------------------------

