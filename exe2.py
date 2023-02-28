'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
anteriores(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence
 ou não a sequência.
'''

#Função para criar a sequência até o número digitado
def fibonacci(num):
    fib = []
    a, b = 0, 1
    while b <= num:
        fib.append(b)
        a, b = b, a + b
    return fib


numero = int(input("Digite um número: "))
fibonacci = fibonacci(numero)

if numero in fibonacci:
    print("esse número pertence a sequência de Fibonacci")
else:
    print("esse número não pertence a sequência de Fibonacci")
