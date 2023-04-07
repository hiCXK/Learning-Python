from ast import ListComp


i='Hello'   #strings are immutable
j='World'
k=i+' '+j+'!'
print(k)

print("%s to %s!" %(i,j))

a="3"
b="5"
d=a+b+"c"
print(d)

vari1="Good"
vari2="Boy"
vari3=" "
k=vari3.join([vari1,vari2])
print(k)


l=("{} {}".format(vari1,vari2))
print(l)