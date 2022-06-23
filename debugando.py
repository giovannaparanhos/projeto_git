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



#Ex 1 - erro genérico
try:
    geek()
except:
    print('Problema!')
#trata o erro, mas não sabemos o que está errado.

#ex 2
try:
    len(5)
except NameError:
    print('Função inexistente')
#se o erro nao é Nameerror, não cai no except


try:
    len(5)
except TypeError as err:
    print(f'AConteceu o seguinte erro: {err}')
#assim mostramos detalhes do erro



#ex 3

try:
    #len(5)
    #geek()
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
    
    


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Giovanna'}

print(pega_valor(dic, 8))

------------
Try/Except/Else/finally

TODA ENTRADA DEVE SER TRATADA!!!!!!!



#EXEMPLO 


try:
    num = int(input('informe um número:'))
except ValueError:
    print('Valor incorreto! Insira apenas números')
else: #é executado somente se o erro não ocorre
    print(f'Você digitou {num}')


#finally

try:
    num = int(input('informe um número:'))
except ValueError:
    print('Valor incorreto! Insira apenas números')
else:
    print(f'Você digitou {num}')
finally:
    print('O bloco finally é sempre executado, havendo exceção ou não. Ele é usado para fechar ou desalocar recursos.')

#exemplo mais complexo - ERRADO
def divisao(a, b):
    return a / b

num1 = int(input('Primeiro numero:'))

try:
    num2 = int(input('Segundo numero:'))
except ValueError:
    print('O valor precisa ser numérico.')

try:
    print(divisao(num1, num2))
except NameError:
    print('Valor incorreto')

#correto: as entradas devem ser tratadas dentro da função. Você é responsável por elas! Trate-as!
def divisao(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto.'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero.'


#ou
def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o seguinte erro: {err}'

num1 =input('Primeiro numero:')
num2 = input('Segundo numero:')
#tratamento semi-generico acima

print(divisao(num1, num2))
--------------------------------
Debugando com pdb - pYTHON dEBUGGER



#errado
def divisao(a, b):
    print(f'a={a}, b={b}') #a utilização do print para debugar código é uma prática ruim.
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o seguinte erro: {err}'
print(divisao(4, 7))

#Forma mais profissional: utilizando o debugger. Podemos fazer isso em diferentes
#IDEs, como o pycharm ou o PDB.

def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o seguinte erro: {err}'
print(divisao(4, 0))

'''
#Exemplo com o pDb. para utilizá-lo, precisamos importar a biblioteca pdb e usar a função set_trace()


nome = 'Gigi'
sobrenome = 'Hadid'
#import pdb;pdb.set_trace() #Importmaos o pdb assim para apagar assim que finalizarmos o uso
#a partir do python 3.7 pdb é built in, usamos a função breakpoint
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Python Básico ao Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

#comandos básicos PDB:
#l: lista onde estamos no códico
#n: próxima linha
#p: imprime variável
#c: continua a execução - finaliza o debugging

#Cuidado com conflitos ente nomes de variáveis e os comandos do pdb.

