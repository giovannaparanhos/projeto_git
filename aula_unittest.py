'''
Introdução ao módulo Unittest

- Testes unitários são formas de se testar unidades individuais de código fonte.

U.i.s podem ser funções, métodos, classes etc.

Seu objetivo é mostrar que cada unidade cumpre a sua função.

para criar tais teste, criamos classes que herdam de unittest.TestCase
a partir de então, ganhamos todos os 'assertions' no módulo.

para rodas os testes, usamos unittest.main



#Prática - utilizando a abordagem TDD

def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'só se vive uma vez.'

    return f'Estou comendo {comida} porque {final}'

def dormir(num_horas):
    if num_horas > 8:
        return f'Putz! Dormi demais! Estou atrasada para o trabalho.'
    else:
        return  f'Continuo cansada pois dormi apenas {num_horas} horas ):'


def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False

'''
'''
Para executar os testes no modo verbose (com detalhes):
python modulo -v

(base) giovanna@HAL-9000:~/Desktop/projeto_git$ python u_tests.py -v
test_comer_gostosa (__main__.AtividadesTestes) ... ok
test_comer_saudavel (__main__.AtividadesTestes) ... ok
test_dormir_muito (__main__.AtividadesTestes) ... ok
test_dormir_pouco (__main__.AtividadesTestes) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

#Docstrings nos testes

é recomendado acrescentar doctstrings nos testes.

'''

'''
Antes e após hooks

hooks são os testes em si e sua execução. 

métodos:
setup() -> executado antes de cada método de teste. útil para criarmos instâncias de objetos e outros dados.

tearDown() -> executado ao final de cada método de teste. exclui e/ou fecha conexões com bancos de dados
'''

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        #configs do setup
        pass
    def test_primeiro(self):
        #setUp vai rodar antes do teste, e tearDown depois
        pass
    def test_segundo(self):
        pass
    #idem

    def tearDown(self):
        pass
    #configs dp teardown


