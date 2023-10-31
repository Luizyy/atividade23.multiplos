# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.


Nn = 0
for nimpares in range(1, 501):
    if nimpares % 2 != 0:
        if nimpares % 3 == 0:
            Nn += nimpares 
print("A soma dos múltiplos é: {}.".format(Nn))



