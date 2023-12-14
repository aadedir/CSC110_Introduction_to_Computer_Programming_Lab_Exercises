name=input("Enter your name: ")
date=input("Enter the date: ")

home_am=input("CO2 reading home (AM)? ")
comment_1=input("Comment for reading: ")

transport_am=input("CO2 reading transportation (AM)? ")
comment_2=input("Comment for reading: ")

work_am=input("CO2 reading work (AM)? ")
comment_3=input("Comment for reading: ")

work_pm=input("CO2 reading work (PM)? ")
comment_4=input("Comment for reading: ")

transport_pm=input("CO2 reading transportation (PM)? ")
comment_5=input("Comment for reading: ")

home_pm=input("CO2 reading home (PM)? ")
comment_6=input("Comment for reading: ")

print("\n")
print(f"Student Name:	{name}")
print(f"Date:		    {date}")
print("\n")
print("--> C A R B O N  D I O X I D E   R E A D I N G S <--")
print("\n")
print("Location		Time	Level	Description")
print("--------		----	-----	-----------")
print(f"Home		    AM	    {home_am}	    {comment_1}")
print(f"Transport       AM	    {transport_am}	    {comment_2}")
print(f"Work		    AM	    {work_am}	    {comment_3}")
print("\n")
print(f"Work		    PM	    {work_pm}	    {comment_4}")
print(f"Transport       PM	    {transport_pm}	    {comment_5}")
print(f"Home		    PM	    {home_pm}	    {comment_6}")