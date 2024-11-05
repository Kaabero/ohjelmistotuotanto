# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") # muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"Summa: {x} + {y} = {summa(x, y)}") # merge
print(f"Summa:{x} - {y} = {erotus(x, y)}") # merge

logger("lopetetaan")
print("goodbye!") # lisäys bugikorjaus-branchissa