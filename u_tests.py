import unittest
from aula_unittest import  comer, dormir

class AtividadesTestes(unittest.TestCase):

    def teste_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )
    def teste_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel='False'),
            'Estou comendo pizza porque só se vive uma vez.'
        )

if __name__ == '__main__':
    unittest.main()

#por convenção, todos os testes começam com test_<nome>
