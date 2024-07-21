#immutable_var = 1,2,3,"TOST",5
#print(immutable_var)
#immutable_var[3] = 9 Кортеж хранит ссылку на список, а не сам список
#print(immutable_var)
mutable_list = [1,7,"list",3,10]
mutable_list[2] = "F"
mutable_list.extend(["Lion"])
print(mutable_list)