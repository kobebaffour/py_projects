                        #### Exercise 2 - Try and Except Structure

x =  input("Enter Hours: ")
y = input("Enter Rate: ")
try:
    z = int(x)
    d = int(y)
    pay = z * d
    print("Pay:", pay)
except:
    z = -1
    d = -1
    print("Error, Only Numeric values can be added.")