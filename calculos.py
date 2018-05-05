#import functions_for_classes
#from functions import *
from functions_for_classes import promedio as fun_promedio

notas = [16,14,11,10]
#promedio = functions_for_classes.promedio(*notas)

promedio = fun_promedio(*notas)
print ( "mi promedio es : {}".format (promedio))
print (PI)