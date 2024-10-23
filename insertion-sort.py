n = int(input("Enter number of elements : "))
my_list = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n+1]
print(my_list)
for i in range(1,len(my_list)):
    key_value=my_list[i]
    j=i-1
    while j >= 0 and my_list[j] > key_value :
        my_list[j+1]=my_list[j]
        j=j-1
    my_list[j+1]=key_value

print(my_list)