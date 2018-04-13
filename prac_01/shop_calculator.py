p = 0
i = int(input("Number of items:"))
for x in range(0, i):
	n = float(input("Price of item:"))
	p = n + p
if p > 100:
	p = p * 0.9
print("Total price is $ {:.2f}".format(p))
