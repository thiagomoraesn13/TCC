import os
import numpy as np
import matplotlib.pyplot as plt

import statistics
from fractions import Fraction as F
vetor = []
desviozao = []
def faz_algo(arquivo, nome_pasta):
  # filtra as linhas desejadas
  string = ""
  string2 = ""
  string3 = ""

  command = 'cat ' + nome_pasta + '/' + arquivo + ' | grep "nodeId: 4" >' + nome_pasta + '/' + 'temp.txt'
  command2 = 'cat ' + nome_pasta + '/' + arquivo + ' | grep "nodeId: 3" >' + nome_pasta + '/' + 'temp2.txt'
  command3 = 'cat ' + nome_pasta + '/' + arquivo + ' | grep "nodeId: 2" >' + nome_pasta + '/' + 'temp3.txt'
  os.system(command)
  os.system(command2)
  os.system(command3)

  #abre os arquivos para leitura
  arq = open(nome_pasta + '/' + 'temp.txt', 'r')
  arq2 = open(nome_pasta + '/' + 'temp2.txt', 'r')
  arq3 = open(nome_pasta + '/' + 'temp3.txt', 'r')

  #Um vator pra cada campo/Nó
  lst = [] 
  lst2 = []
  lst3 = []

  cont1 = 0
  cont2 = 0
  cont3 = 0 

  #formatando primeiro No, pegando os 100 pacotes
  for linha in arq:
    if((linha) and (cont1 <= 99)):
      aux = linha.split(',')[3]
      aux = aux.split(' ')[2]
      cont1 = cont1 + 1
      lst.append(int(aux[0:-2]))
  

  string = "Nó 4" + "\n"
  w1 = open(nome_pasta + '/' +arquivo+"_log.out", "w")
  w1.write(string)
  
  #gravando nó 4 no arquivo
  #string = ""
  string = ""
  for x in lst:
    string += str(x) + "\n"
  w1 = open(nome_pasta + '/' +arquivo+"_log.out", "a+")
  w1.write(string)

  
  string2="No3" + "\n"
  w1 = open(nome_pasta + '/' +arquivo+"_log.out", "a+")
  w1.write(string2)

  
  for linha2 in arq2:
    if((linha2) and (cont2 <= 99)):
      aux = linha2.split(',')[3]
      aux = aux.split(' ')[2]
      cont2 = cont2 + 1
      lst2.append(int(aux[0:-2]))

 
  #gravando nó 3 no arquivo
  string2=""
  
  for x2 in lst2:
    string2 += str(x2) + "\n"
  w1 = open(nome_pasta + '/' +arquivo+"_log.out", "a+")
  w1.write(string2)

  string3="No2" + "\n"
  w1 = open(nome_pasta + '/' +arquivo+"_log.out", "a+")
  w1.write(string3)

  string3 = ""
  for linha3 in arq3:
    if((linha3) and (cont3 <= 99)):
      aux = linha3.split(',')[3]
      aux = aux.split(' ')[2]
      cont3 = cont3 + 1
      lst3.append(int(aux[0:-2]))
 
  #gravando nó 2 no arquivo

  for x3 in lst3:
    string3 += str(x3) + "\n"
  w1 = open(nome_pasta + '/' +arquivo+"_log.out", "a+")
  w1.write(string3)


nome_pasta = 'sabado/30'

arquivos = os.listdir(nome_pasta)
#arquivos.sort()

for arquivo in arquivos:
  faz_algo(arquivo, nome_pasta)
  os.system('rm ' + nome_pasta + '/' + 'temp.txt')
  os.system('rm ' + nome_pasta + '/' + 'temp2.txt')
  os.system('rm ' + nome_pasta + '/' + 'temp3.txt')
 