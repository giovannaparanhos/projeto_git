'''
Assertions

assert - checa se expressão é válida ou não.


def soma_positivos(a,b):
    assert a > 0 and b > 0
    return  a + b

ret = soma_positivos(4, 6)
#ret2 = soma_positivos(-2, 3)
print(ret)

def fast_food(comida):
    assert comida in[
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'dogão'
    ], 'A comida precisa ser fast food'
    return  f'Estou comendo {comida}'

comida = input('Informe a comida: ')
print(fast_food(comida))

#ALERTA! Cuidado ao utilizar assert. se o programa for executado com o parametro -O, nenhum assertion será validado.
-----------------------------
Doctests:
testes que colocamos nas docsyrings das funções/metodos python.
para rodar umtest do doctest:
python -m doctest -v nome_do_modulo.py


'''
import doctest
def soma(a, b):
    """soma a e b
    >>>soma(1,2)
    3
    """
    return a+b
