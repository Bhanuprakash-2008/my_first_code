ls=[1,2,4,5,7,9,10]
even_numbers=[]
odd_numbers=[]
for num in ls:
 if num%2==0:
    even_numbers.append(num)
else:
    odd_numbers.append(num)
print("even_numbers=",even_numbers)
print("odd_numbers=",odd_numbers)
print(sum(even_numbers))
print(sum(odd_numbers))

