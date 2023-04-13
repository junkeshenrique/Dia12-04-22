valordaconta = float(input("Informe o valor da conta de compra:"))
valorpaga = float(input("Informe o valor fornecido pelo cliente para pagar a conta:"))
troco = valorpaga - valordaconta
if troco > 0:
    print(f"O valor do troco é de R${troco:.2f}")
else:
    trocofinal = troco * -1
    print(f"Falta pagar R${trocofinal:.2f}")
print(f"O valor total da compra é de R${valordaconta:.2f}")
print(f"O valor total pago pelo cliente é de R${valorpaga:.2f}")

numcelulas100 = int(troco/100)
print(f"O número de celulas de 100 reais é de: {numcelulas100:.0f} notas.")
resto = troco - numcelulas100*100
numcelulas10 = int(resto/10)
print(f"O número de celulas de 10 reais é de: {numcelulas10:.0f} notas.")
resto1 = resto - numcelulas10*10
numcelulasum = int(resto1/1)
print(f"O número de celulas de 1 real é de: {numcelulasum:.0f} notas.")