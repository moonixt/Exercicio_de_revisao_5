def calcular_salario (a):
    if a > 2000 : 
        aumento = a*1.07
    else:
         aumento = a*1.15
    return aumento
S =float(input('insira o salario:'))
print(calcular_salario(S))