print("Electric Bill Calculator\n\n")

customer_IDnum = input("Enter Customer IDNO.: ")
customer_name = input("Enter Customer Name: ")
unit_consumed = int(input("Enter unit Consumed: "))

surcharge_1 = 240.00
surcharge_2 = 0.00

print("\n\nCustomer IDNO.: " + customer_IDnum)
print("Customer Name: " + customer_name)
print("unit Consumed: " + str(unit_consumed))
if unit_consumed >= 600:
    amount_charges_perunit_1 = unit_consumed * 2.00
    print("Amount Charges @Rs. 2.00 per unit: ",amount_charges_perunit_1)
    print("Surcharge Amount: ", str(surcharge_1))
    print("Net Amount Paid by the Customer: ", amount_charges_perunit_1 + float(surcharge_1))
elif unit_consumed >= 400 and  600:
    amount_charges_perunit_2 = unit_consumed * 1.80
    print("Amount Charges @Rs. 1.80 per unit: " , amount_charges_perunit_2)
    print("Surcharge Amount: ", str(surcharge_2))
    print("Net Amount Paid by the Customer: ", amount_charges_perunit_2 + float(surcharge_1))
elif unit_consumed >= 200 and  399:
    amount_charges_perunit_3 = unit_consumed * 1.50
    print("Amount Charges @Rs. 1.50 per unit: " , amount_charges_perunit_3)
    print("Surcharge Amount: ", float(surcharge_2))
    print("Net Amount Paid by the Customer: ", amount_charges_perunit_3 + float(surcharge_2))
else:
    amount_charges_perunit_4 = unit_consumed * 1.20
    print("Amount Charges @Rs. 1.20 per unit: " , amount_charges_perunit_4)
    print("Surcharge Amount: ", float(surcharge_2))
    print("Net Amount Paid by the Customer: ", amount_charges_perunit_4 + float(surcharge_2))
