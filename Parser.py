import os
import numpy as np
import matplotlib.pyplot as plt

import statistics
from fractions import Fraction as F
vetor = []
desviozao = []
def faz_algo(arquivo, nome_pasta):
  # filtra as linhas desejadas
  command = 'cat ' + nome_pasta + '/' + arquivo + ' | grep "RSSIRecv" >' + nome_pasta + '/' + 'temp.txt'
  command2 =  'cat ' + nome_pasta + '/' + arquivo + ' | grep "RSSISend:" >' + nome_pasta + '/' + 'temp2.txt'
 
  os.system(command)
  os.system(command2)


  arq = open(nome_pasta + '/' + 'temp.txt', 'r')
  arq2 = open(nome_pasta + '/' + 'temp2.txt', 'r')

  lst = []
  lst2 = []

  
  
  cont1=0
  for linha in arq:
    if((linha) and (cont1 <= 99)):
      aux = linha.split(',')[3]
      aux = aux.split(' ')[2]
      lst.append(int(aux[0:-2]))
  
  
  cont2=0
  for linha2 in arq2:
    if((linha2) and (cont2 <= 99)):
      aux2 = linha2.split(',')[2] 
      aux2 = aux2.split(' ')[2]
      cont2 = cont2+1
      lst2.append(int(aux2))  
      
   
  print("RSSIRecv")
  media = sum(lst)/len(lst)
  desvio = statistics.pstdev(lst)
  
  vetor.append(media*(-1))
  desviozao.append(desvio)
  print("Media do Arquivo:", arquivo, "=",media)
  print("Desvio Padrao:", arquivo, "= ", desvio)
  
  media = 0
  desvio = 0
  
  print("----------------------------------------------------------")
  print("----------------------------------------------------------")
  print()
  print("RSSISend")
  print("Media do Arquivo:", arquivo, "=",sum(lst2)/len(lst2))
  print("Desvio Padrao:", arquivo, "= ", statistics.pstdev(lst2))
  
  print("----------------------------------------------------------")
  print("----------------------------------------------------------")
  print()
  
nome_pasta = 'arqs'

arquivos = os.listdir(nome_pasta)
arquivos.sort()

for arquivo in arquivos:
  faz_algo(arquivo, nome_pasta)
  os.system('rm ' + nome_pasta + '/' + 'temp.txt')
  os.system('rm ' + nome_pasta + '/' + 'temp2.txt')
  
vetor.sort()

x = desviozao.pop() #tirando o desvio do primeiro arquivo que ficou no final do vetor
desviozao.insert(0,x) #colocando no inicio, pois ele é o primeiro
#print("valormorto", x)

print(desviozao)

plt.xlim(0,40) #eixo x com as distancias
plt.ylim(0,70) #eixo y com os rssi
plt.ylabel("RSSI")
plt.xlabel("Distância(m)")

plt.title("RSSIRecv")
data1= [5,10,15,20,25,30] #valores da distencias para fazer a ligacao dos pontos
plt.errorbar(data1, vetor, desviozao)

plt.grid()
plt.show()
