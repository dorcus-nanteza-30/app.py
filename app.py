#exercise on lists
list=[60,80,90,98]
print(list)

#change 80 to 89
list=[60,80,90,98]
list[1]=89
print(list)


#append list
list=[60,80,90,98]
list.append("55")
print(list)

#finding size of the list
print(len(list))


#python program to sum all items.
a=[60,80,90,98]
sum(a)
print(sum(a))


#lists
list_html= [80,90,78,89]
list_python= [70,89,77,94]
def common_member(list_html,list_python):
    result = True
    for value in list_html:
        for number in list_python:
            value == number
            return result
print(common_member(list_html,list_python))
            
