username = str (input("Nombre de ususario\n")) 
password = str (input("Contraseña\n"))
val=False
res=False

if 3<=len(username)<10: 
  val=True

if password=="Tokio" or password=="Python":
  res=True

print ("Username:",val)
print ("Password:", res)