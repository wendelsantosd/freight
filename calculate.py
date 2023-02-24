km1 = float(input('Digite o KM de IDA a ser percorrido: '))
km2 = float(input('Digite o KM de VOLTA ser percorrido: '))

kmTotal = km1 + km2
currentValueGasoline = 5.3

gasolineInLiterPerKm1 = km1 / 17
gasolineInLiterPerKm2 = km2 / 17

gasolineInLiterPerKmTotal = gasolineInLiterPerKm1 + gasolineInLiterPerKm1

priceGasoline = gasolineInLiterPerKmTotal * currentValueGasoline

print(f'Kilometragem total a ser percorrida: {kmTotal:.2f} KM')
print(f'Valor atual da gasolina: R$ {currentValueGasoline:.2f}')
print(f'Litros gastos em gasolina: {gasolineInLiterPerKmTotal:.2f} L')
print(f'Valor a ser cobrado pelo frete: R$ {priceGasoline:.2f}')