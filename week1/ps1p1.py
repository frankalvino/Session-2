item = input("Enter item (A or B)")
qty = float(input("Enter quantity"))

if item == "A":
  unitprice = 10.00
else:
  unitprice = 20.00

extprice = qty * unitprice

print("Item:   ", item)
print ("Quantity:", qty)
print ("Unit Price", unitprice)
print ("Extended Price: ", extprice)

