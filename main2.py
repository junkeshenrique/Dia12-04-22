totalprestacoes = int(input("Informe a quantidade total de prestações:"))
prestacoespagas = int(input("Informe a quantidade de prestações pagas:"))
valorprestacao = float(input("Informe o valor de cada prestação:"))
valortotal = totalprestacoes * valorprestacao
print(f"O valor total a ser pago é de R${valortotal:.2f}")
valorpago = prestacoespagas * valorprestacao
print(f"O valor já pago é de R${valorpago:.2f}")
faltapagar = valortotal - valorpago
print(f"O valor que falta pagar é de R${faltapagar:.2f}")