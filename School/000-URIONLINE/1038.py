#input Program
X, Y = input().split()
X, Y = int(X), int(Y)

#proses Program
snack = {
	1 : 4.00,
	2 : 4.50,
	3 : 5.00,
	4 : 2.00,
	5 : 1.50
}
result = snack[X]*Y

#output Program
print("Total: R$ %.2f" % (result))