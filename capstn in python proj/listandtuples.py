#list are mutable which can changed
student = ["Asmagulzar", 95.4, 21, "berlin"]
print(student[0])
student[0] = "khamar"
print(student)
#append
student.append("kha")
print(student)
#aapend which joins

#sort which are 2 types ascending(0..)descending(1..) 
list = [10,5,9,8,4,27]
print(list.sort(reverse=True))
print(list)
#insert
list = [1,2,3]
#list.insert(2,5)
list.insert(7,4)
print(list)

#tuple are immutable they can't be changed,has no attribute 'insert'
tup =  (2,1,3,5,"asma")
print(tup[0])
print(tup[1])
print(tup[1:5])#slicing
#tup.insert(6)
#print(tup[6])
#methods
print(tup.count(2))
print(tup.index(5))#return index of typed no. 
#pop remove the element at index
list = [2, 1,3,7]
list.pop(2)
print(list)
list.remove(1) # removes the typed no. which occurred first
print(list)

movie = ['asma','gulzar','shaik']
print(movie[0])
movie.append(input("enter 1st movie:"))
movie.append(input("enter 2nd movie:"))
print(movie)

DNA = [1,2,1]
RNA = [5,6,7,8]
print(DNA.copy)
print(DNA)
copy_DNA = DNA.copy()
copy_DNA.reverse()
if(copy_DNA == DNA):
    print("palindrome")
else:
    print("Not")

#list = ["'being asma,'Sk.Sheixs.sK','Sheixs Asma gulzar,'being asma'"]
list = [4,8,0,7,9,20]
print(list.sort(reverse=True))
print(list)

         














