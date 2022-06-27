"""
Sistema de Arquvos e Navegação


.. move um diretório acima na hierarquia

. diretóro corrente

Para manipular arquivos do OS, devemos importar o módulo os




import os

print(os.getcwd())  # get current work directory (returns absolute path)



os.chdir('..') # To change directories, we can use chdir()
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())


#check if directory is absolte or relative

print(os.path.isabs('/home/giovanna/'))


import os
arquivos = list(os.scandir()) #scans current dir for other dirs and files
#print(dir(arquivos[0]))

print(arquivos[0].name)
print(arquivos[0].inode()) #??
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink()) #is symbolic link
print(arquivos[0].path) #path to file
print(arquivos[0].stat()) #infos estatisticas (metadados). importante: size

#é necessário fechar a função scandir

#correto:
import os
scanner = os.scandir()
arquivos = list(scanner)
print(arquivos[0].name)
print(arquivos[0].inode()) #??
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink()) #is symbolic link
print(arquivos[0].path) #path to file
print(arquivos[0].stat()) #infos estatisticas (metadados). importante: size
scanner.close()
-------------------------
Manipulação dos arquivos

print(os.path.exists('machado.txt')) # Descobrindo se um arquivo ou diretório existe (true)
print(os.path.exists('outro')) #mesmo para diretório relativo (false)
print(os.path.exists('/home/giovanna/Desktop/projeto_git/')) #e path absoluto (true)




import os

#criando arquivos
#forma 1
open('criando_teste1.txt', 'w').close() #cria e fecha
#forma 2
open('criando_teste2.txt', 'a').close()
#forma 3
with open('criando_teste3.txt', 'w') as arquivo:
    pass #nao faz nada, mas é necessario porque with pede indentacao

#a MELHOR FORMA
#os.mknod('criando_teste5.txt')
#os.mknod('/home/giovanna/Desktop/teste4.txt') #especificando o path
#Ao criar um arquivo por mknod, se o arquivo já existe, retorna erro

#os.mkdir('teste') #cria diretório
os.rename('teste', 'mudei') #renomeia dir
#essas funcionam para dir absoluto também, e pra arquivos

#deletando arqivos
#ATENÇÃO!!! Ao deletar um arquivo de um diretório, eles não vão para a lixeira! Eles somem.


os.remove('criando_teste2.txt') #remove apenas arquivos

#se informar um dir ao invés de arquivo, teremos um IsADirectoryError.


os.rmdir('mudei') #só remove diretórios vazios!
"""
#Trabalhando com arqivos e diretórios temporários

import os
import tempfile
with tempfile.TemporaryDirectory() as tmp: #arquvo temp só existe dentro desse with
    print(f'Dir temporário em {tmp}')
    with open(os.path.join(tmp, 'arq_temp.txt'), 'w') as arquivo:
        arquivo.write('Temporariamente\n')
    input()