nums=[12,42,5,32,42,4,21]

#wow indexing is work also in list type and str  type 

print(nums[0])

# i can add differnt type of data in list

name=["navin",80,90.90]

mil=nums + name
print(mil)


# list is mutable it means we can change list value

type(nums.append(100))
print(nums)
#remove form the list
nums.insert(0,90) # .insert(index number,value)
print(nums)

print(nums.remove(100))#remove value



