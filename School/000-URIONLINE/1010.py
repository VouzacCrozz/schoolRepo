#input Program

codeP1, numberP1, priceP1 = input().split() #tipedata masih string
codeP1, numberP1, priceP1 = int(codeP1), int(numberP1), float(priceP1)

codeP2, numberP2, priceP2 = input().split() #tipedata masih string
codeP2, numberP2, priceP2 = int(codeP2), int(numberP2), float(priceP2)

#proses Program

result = (numberP1*priceP1)+(numberP2*priceP2)

#output Program

print("VALOR A PAGAR: R$ %.2f" % (result))