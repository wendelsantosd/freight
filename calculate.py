km = float(input('Digite o KM a ser percorrido: '))

currentValueGasoline = 5

gasolineInLiterPerKm = km / 16

priceGasoline = gasolineInLiterPerKm * currentValueGasoline * 2

print(f'Kilometragem total a ser percorrida: {km:.2f} KM')
print(f'Valor atual da gasolina: R$ {currentValueGasoline:.2f}')
print(f'Litros gastos em gasolina: {gasolineInLiterPerKm:.2f} L')
print(f'Valor a ser cobrado pelo frete: R$ {priceGasoline:.2f}')