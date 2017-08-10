Fbase = open("indexbase.txt", "r")
Textbase = Fbase.read()
Fbase.close()

Fsplitted = Textbase.split("!!!")
print len(Fsplitted)
