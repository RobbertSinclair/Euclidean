def euclidean(n1, n2):
     if (n2 > n1):
         return euclidean(n2, n1)
     else:
        initial_result = n1 // n2
        remainder = n1 % n2
        print("{n1} = {result} x {n2} + {remainder}".format(n1=n1, result=initial_result, n2=n2, remainder=remainder))
        if remainder == 0:
            return n2
        else:
            return euclidean(n2, remainder)

n1 = int(input("Please enter your first number: "))
n2 = int(input("Please enter your second number: "))
result = euclidean(n1, n2)
print("The value of hcf({n1}, {n2}) is {result}".format(n1=n1, n2=n2, result=result))

         
