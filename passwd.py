#David Moreno Lumbreras - dlumbrer
fich=open("/etc/passwd","r");
data = fich.readlines();
diccionario = {};
for user in data:
    diccionario[user.split(":")[0]] = user.split(":")[-1][:-1]
print "Total users: " + str(len(diccionario))

print diccionario['root']

try:
    print diccionario['imaginario']
except KeyError as err:
    print "The user: " + str(err) + " does not exist"   
