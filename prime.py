print("-------------------------")
print("Enter any Positive Integer")
print("-------------------------")
num1 = int(input(">>>Enter the lower limit :- \n"))
num2 = int(input(">>>Enter the upper limit :- \n"))
prime_count=0
composite_count = 0
if num1 > num2 :
    c = input("\nThe lower limit cannot be more than upper limit \nIf you wish to interchange the limits type 'YES' else 'NO':")
    print()
    if c == "YES":
        temp = num2
        num2 = num1
        num1 =  temp
for num in range(num1,num2+1):
    if num == 0 or num == 1:
        print(num,"neither prime nor composite")
    else:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"is a compositee number")
                    composite_count+=1
                    break
            else:
                print(num,"is a prime number")
                prime_count+=1

print("Count :",prime_count,"prime and",composite_count,"composite numbers in the given range.")
 
  
