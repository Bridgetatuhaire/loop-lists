#working with lists
#A program that prints all elements in list below that are less than 5

a = [1,1,2,3,5,8,13,21,34,55,89]
for element in a:
    if element < 5:
     print(element)

#creating a list and storing new items in it
a = [1,1,2,3,5,8,13,21,34,55,89]
new_list = []
for i in a:
   if i < 5:
      new_list.append(i) #used to add new elements in the new list
      new_list.sort()
print(new_list)

 #consider two consider a,b; a = [1,1,2,3,5,8,13,21,34,55,89] , b = [1,1,2,3,4,5,6,7,8,9,10,11,12,13]
 #write a program that contains only elements that are common in both lists and are not duplicated.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_items = []
for x in a:
   for y in b:
      if y in common_items:
         continue #ends the current iteration
      else:
           common_items.append(y)
print(common_items)


