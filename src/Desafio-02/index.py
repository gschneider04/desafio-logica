

def getRankedLevel(Level):
    if RankedLevel < 10:
        ResultLevel = 'Ferro'
    elif RankedLevel > 10 and RankedLevel <= 20:
        ResultLevel = 'Bronze'
    elif RankedLevel > 20 and RankedLevel <= 50:
        ResultLevel = 'Prata'
    elif RankedLevel > 50 and RankedLevel <= 80:
        ResultLevel = 'Ouro'
    elif RankedLevel > 80 and RankedLevel <= 90:
        ResultLevel = 'Diamante'
    elif RankedLevel > 90 and RankedLevel <= 100:
        ResultLevel = 'Lendário'
    elif RankedLevel >= 101:
        ResultLevel = 'Imortal'
    else:
        ResultLevel = 'Error'
    return ResultLevel


def showRankedLevel(LevelResult):
    print(f'O Herói tem de saldo {Wins} vitórias e {Losses} derrotas, e está no nivel {getRankedLevel(RankedLevel)}')


Wins = int(input('Digite o número de vitórias: '))
Losses = int(input('Digite o número de derrotas: '))
RankedLevel = Wins - Losses

# getRankedLevel(RankedLevel)
showRankedLevel(RankedLevel)