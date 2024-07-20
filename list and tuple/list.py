f=['apple', 'mango', 7, False]
print(f[0])
print(f[2])
s="shubham"
print(s[0])
s[3]="y"  # cant add value give error
print(s) # string imutable cant change value
f[1]="banana"  #list is mutable mango will replace with bannana
print(f)
print(f[1:4])
print(f[2:5])
f[0]="cherry"
print(f)