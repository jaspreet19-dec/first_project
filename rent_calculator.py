''' we need from the user 
total rent ,total food ordered for snacks,electricity units spend , charge per unit
preson living in room 
output : total bill you have to be pay is  '''

rent=int(input("enter total rent amount :"))
food=int(input("enter amount of food ordered for snacks :"))
electricity_spend=int(input("enter total electricity units spend :"))
charge_per_unit=int(input("enter the charge per unit :"))
persons =int(input("enter total no. of person living in  a room :"))

#formula we use for the calculation is 
total_bill_of_person=rent+food+(electricity_spend*charge_per_unit)
output=f"{total_bill_of_person/persons : .2f}"

print("total bill you have to be pay is ",output)