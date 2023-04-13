clientesisentos = int(input("Informe o número de clientes isentos de parecelas:"))
clientesemdia = int(input("Informe o número de clientes com as parcelas em dia:"))
clienteatraso = int(input("Informe o número de clientes com parcelas em atraso:"))
totalclientes = clienteatraso + clientesemdia + clientesisentos
print(f"O número total de clientes é de: {totalclientes:.0f}")
totalisentos = (clientesisentos / totalclientes) * 100
print(f"A porcentagem de clientes isentos é de {totalisentos:.0f}%")
totalemdia = (clientesemdia / totalclientes) * 100
print(f"A porcentagem de clientes com as parcelas em dia é de {totalemdia:.0f}%")
totalatraso = (clienteatraso / totalclientes) * 100
print(f"A porcentagem de clientes com as parcelas em atraso é de {totalatraso:.0f}%")