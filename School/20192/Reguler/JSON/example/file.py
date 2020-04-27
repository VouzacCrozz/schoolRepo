from json import load, dump

fileJson = 'data.json'

data = {}

#mode 'r' -> read
with open(fileJson) as f:
	data = load(f)

nama = input("Enter your name : ")
alamat = input("Enter your Addr : ")
phone = input("Enter your number phone : ")

data[nama] = {
	'alamat' : alamat,
	'phone' : phone
}

#mode 'w' -> write
with open(fileJson, 'w') as f:
	dump(data, f)

print("Saving Done!")