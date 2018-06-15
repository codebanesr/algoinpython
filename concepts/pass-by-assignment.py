#what is pass by assignment anyways



def beer(li):
  li.append("beer")
  print(li)   #prints sugar, salt and beer




li = ["sugar", "salt"]
beer(li)    #prints sugar salt and beer


#looks like pass by reference when it is not, a copy of the address was passed not the address itself, let me demonstrate




def beer(li):
  li = ["banana", "mango"]
  li.append("beer")
  print(li)   #prints mango, banana and beer


li = ["sugar", "salt"]

beer(li)    #prints sugar salt


