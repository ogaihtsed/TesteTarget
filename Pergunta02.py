'''2) Escreva um programa que verifique, em uma string,
a existência da letra ‘a’, seja maiúscula ou minúscula,
além de informar a quantidade de vezes em que ela ocorre.'''

st = input("Informe a string: ")

cont = 0
i = 0

while(i < len(st)):
    if st[i] == 'a' or st[i] == 'A':
        cont += 1
    i+=1

if cont == 0:
    print("A letra 'a' nao aparece na String informada.")
else:
    print(f"A letra 'a' aparece {cont} vezes na String informada.")
