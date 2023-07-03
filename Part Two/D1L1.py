mottofile = open("motto.txt","a")
mottofile.write("Fiat Lux!")
mottofile.close()

mottofile = open("motto.txt","r")
print(mottofile.read(), end='')
mottofile.close()

mottofile = open("motto.txt","a")
mottofile.write("\nLet there be monospace!")
mottofile.close()
