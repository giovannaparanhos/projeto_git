"""
Aula 13 - Manipulação de Arquivos


Parte 1 - Leitura de arquivos

Para ler um arquivo, utilizamos a função open

open() - em sua forma mais simples, passamos apenas um parâmetro de entrada, neste caso o caminho do arquivo a ser lido.
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos.

https://docs.python.org/3/library/functions.html#open

A função abre um arquivo EXISTENTE Para leitura.
"""
#exemplo
arquivo = open('machado.txt')

print(type(arquivo))