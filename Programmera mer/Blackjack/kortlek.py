import random as rnd

# behöver en lista för att hålla våra kort


def skapaKortlek():
    kortNummer = [i for i in range(2, 11)]
    klädkort = ["J", "Q", "K", "A"]
    kortNummer += klädkort
    lek = 4*kortNummer
    blandaKort(lek)

    return lek

# blanda korten


def blandaKort(lek):
    return rnd.shuffle(lek)
