num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))

print("Opretor\n+ for Add \n - for subtract \n * for multiply\n / for divide")
opretor=input("Enter opretor :" )
if opretor=="add":
    result=str(num1+num2)
    print("your answer is "+ result)

elif opretor == "-":
   result = str(num1-num2)
   Print("your answer is "+ result)

elif opretor == "*":
    result = str(num1*num2)
Print("your answer is "+ result)

 elif opretor == "/":
  result = str(num1/num2)
Print("your answer is "+result)

else:
Print("UNKNOWN input ")
