name: str = "ahmed"
city: str = "tripoli"

#print(f"my name is  {name} , and i live in  {city}")

sentence = "appale,banana,orange,mango"

x =sentence.split(",")
#print(x[-1])
#my_list = ["ahmed" , "ali"]

my_list = [1,2,3,4,5,6,7,8,9,10]
even_num = []
odd_num = []
for i in range (len(my_list)):
    if my_list[i] % 2 == 0:
        even_num.append(my_list[i])
    else:
        odd_num.append(my_list[i])
print(even_num)
print(odd_num)


        
