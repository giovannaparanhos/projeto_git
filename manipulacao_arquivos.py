"""
Aula 13 - Manipulação de Arquivos


Parte 1 - Leitura de arquivos

Para ler um arquivo, utilizamos a função open

open() - em sua forma mais simples, passamos apenas um parâmetro de entrada, neste caso o caminho do arquivo a ser lido.
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos.

https://docs.python.org/3/library/functions.html#open

A função abre um arquivo EXISTENTE Para leitura.

#exemplo
arquivo = open('machado.txt')

#print(type(arquivo))

#Para ler o conteúdo de um arquivo após sua abertura, devemos utar a função read()

#print(arquivo.read())
#o python utiliza um recurso chamado cursor quando trabalha com arquivos.

ret = arquivo.read()
print(type(ret))
print(ret)

----------
2 - Seek e cursores

seek() movimenta o cursor pelo arquivo




arquivo = open('machado.txt')
print(arquivo.read())


arquivo.seek(0) #a função seek recebe um parâmetro que indica onde queremos colocar o cursor.

#forma correta de se manipular arquivos:
with open('machado.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)
print(arquivo.closed)


from csv import reader
with open('cadastro_estabelecimentos_cnes.csv') as arquivo:
   leitor_csv = reader(arquivo, delimiter = ';')
   for linha in leitor_csv:
       print(linha)

#reader = listas
#dictreader -> dicionários
---------
escrevendo em arquivos


from csv import writer
with open('filmes.csv', 'w') as file:
    csv_writer = writer(file)
    filme = None
    csv_writer.writerow(['Title', 'Genre', 'Length']) #writes a single row
    while filme != 'quit':
        filme = input('Write film name:')
        if filme != 'quit':
            genero = input('Inform genre: ')
            duracao = input('Inform length in minutes: ')
            csv_writer.writerow([filme, genero, duracao])


from csv import DictWriter
with open('filmes_dict.csv', 'w') as file:
    header = ['Title', 'Genre', 'Length']
    csv_writer = DictWriter(file, fieldnames=header)
    csv_writer.writeheader()
    filme = None
    while filme != 'quit':
        filme = input('Write film name:')
        if filme != 'quit':
            genero = input('Inform genre: ')
            duracao = input('Inform length in minutes: ')
            csv_writer.writerow({'Title':filme, 'Genre': genero, 'Length': duracao})

-------------
Pickle
- salvando dados de forma  serializada
Objeto Python -> Binarizaçãp
Binarização -> Obj Python

! O módulo Pickle não é seguro contra dados maliciosos. Não é seguro usar com arquivos de estranhos.



#Escrevendo em arquivos pickle
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.__Animal__nome} está latindo')

felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo: #wb = write binary
    pickle.dump((felix, pluto), arquivo) #cria um arquivo hexadecimal com os dados

#Lendo arquivos pickle


with open('animais.pickle', 'rb') as arquivo: #rb = read binary
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato se chama {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

---------------------------
Usando JSON e Pickle



import json

ret = json.dumps(['produto', {'pS4': ('2TB', 'Novo', '220V', 2340)}]) #retorno
#a função .dumps formata o input para o formato json
print(type(ret))
print(ret)


#Criando uma classe:
import  json

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'siames')

ret = json.dumps(felix.__dict__)

print(ret)

#INtegrando Json e  PIckle
precisamos dar pip install jsonpickle


import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'siames')


with open('felix.json', 'w') as arquivo:
    ret =  jsonpickle.encode(felix)
    arquivo.write(ret)

"""