#input Program
money = int(input())
print(money)

#proses Program
pecahanUang = [100, 50, 20, 10, 5, 2, 1]
result = []

for uang in pecahanUang:
	reminder = money//uang
	money -= (reminder*uang)
	result.append(reminder)

#output Program
for i in range(7):
	print("%i nota(s) de R$ %i,00" % (result[i], pecahanUang[i]))