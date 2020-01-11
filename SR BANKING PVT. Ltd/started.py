import os
import time
print "----GETTING STARTED----"
import test2
a1 = test2.pin
ss = "\\" + str(a1) + ".txt"

f = open("C:\Python27\Lib\importlib" + ss + "", "w")
f.write(a1 + "\n")
a2 = test2.age
f.write(a2 + "\n")
a3 = test2.name
f.write(a3 + "\n")
a4 = test2.cash
f.write(a4 + "\n")
a5 = test2.acc
f.write(a5 + "\n")
f.close()
print "ACCOUNT CREATION IN PROGRESS............."
time.sleep(4)
print "ACCOUNT CREATED."
time.sleep(1)
print "THANKS FOR CHOOSING US"
time.sleep(2)
import Menu