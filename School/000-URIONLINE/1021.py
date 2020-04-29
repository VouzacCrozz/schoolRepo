#input Program
money = float(input())

money = int(money*100)

#proses Program
NOTAS = [100, 50, 20, 10, 5, 2] #uang Kertas
MOEDAS = [1, 0.5, 0.25, 0.10, 0.05, 0.01] #uang Koin

resNotas = []
resMOEDAS = []

for uang in NOTAS:
	reminder = money//(uang*100)
	money -= (reminder*(uang*100))
	resNotas.append(reminder)

for uang in MOEDAS:
	reminder = money//(uang*100)
	money -= (reminder*(uang*100))
	resMOEDAS.append(reminder)

#output Program
print("NOTAS:")

for i in range(len(NOTAS)):
	print("%i nota(s) de R$ %.2f" % (resNotas[i], NOTAS[i]))

print("MOEDAS:")

for i in range(len(MOEDAS)):
	print("%i moeda(s) de R$ %.2f" % (resMOEDAS[i], MOEDAS[i]))