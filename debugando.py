"""
Erros mais comuns em Python


Traceback = saída de erros.
"""
'''
Levantando os próprios erros

rais -lança exceções. não é uma função, é uma palavra reservada, como def.
A forma de uso é

raise ErrorType('Mensagem de rro')


def colore(text, color):
    cores = ('pink', 'blue', 'red', 'yellow')
    if type(text) is not str:
        raise TypeError('text must be string')
    if type(color) is not str:
        raise TypeError('color must be string')
    if color not in cores:
        raise ValueError(f'Color must be chosen from {cores}')
    print(f'Text {text} will be printed in {color}')

colore('hello', 'green')
#raise finaliza a função -  nada abaixo dele é executado.

-----------------------------------
O bloco Try/except 

usamos try/except pra tratar erros, previnindo que o programa pare de funcionar e o usuário receba mensganes de erro
inesperadas. 

A forma geral mais simples é 

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas


'''
#Ex 1 - erro genérico
