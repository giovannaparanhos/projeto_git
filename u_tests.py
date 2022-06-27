import unittest
from aula_unittest import  comer, dormir, eh_engracada

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )
    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque só se vive uma vez.'
        )
    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansada pois dormi apenas 4 horas ):'
        )
    def test_dormir_muito(self):
        """Testando o retorno dormindo muito."""
        self.assertEqual(
            dormir(10),
            'Putz! Dormi demais! Estou atrasada para o trabalho.'
        )

    def test_eh_engracada(self):
        #self.assertEqual(eh_engracada('Sérgio Malandro'), False) #executar enquanto a função não estiver implementada
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado.')

if __name__ == '__main__':
    unittest.main()

#por convenção, todos os testes começam com test_<nome>
"""
(base) giovanna@HAL-9000:~/Desktop/projeto_git$ python u_tests.py -v
test_comer_gostosa (__main__.AtividadesTestes)
Testando o retorno com comida gostosa. ... ok
test_comer_saudavel (__main__.AtividadesTestes)
Testando o retorno com comida saudável. ... ok
test_dormir_muito (__main__.AtividadesTestes)
Testando o retorno dormindo muito. ... ok
test_dormir_pouco (__main__.AtividadesTestes)
Testando o retorno dormindo pouco. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
"""