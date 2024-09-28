'''1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1
e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa
na linguagem que desejar onde, informado um número, ele calcule a
sequência de Fibonacci e retorne uma mensagem avisando se o número
informado pertence ou não a sequência.'''


num = input("Digite um numero: ")

n = int(num)
a, b = 0, 1

while (True):
    if (n == a or n == b):
        print(f"O numero {n} pertence a sequencia de Fibonacci.")
        break
    elif (n < b):
        print(f"O numero {n} nao pertence a sequencia de Fibonacci.")
        break
    else:
        a, b = b, a + b
