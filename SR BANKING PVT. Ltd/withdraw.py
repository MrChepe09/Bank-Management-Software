import os
import time
os.system('cls')
print "----WITHDRAW CASH----"
no = raw_input("Enter you PIN no.: ")
pp = "\\" + str(no) + ".txt"
f = open("C:\Python27\Lib\importlib" + pp + "", "r")
time.sleep(1)
cash = int(raw_input("Enter cash to be withdrawn: "))
h = open("C:\Python27\Lib\importlib\\tempp.txt""", "w")
g = f.readlines()
if cash > int(g[3]):
    print "Not enough cash in your Account...."
    print " Your balance is ",str(g[3])
    f.close()
    h.close()
    os.remove("C:\Python27\Lib\importlib\\tempp.txt""")
    time.sleep(1)
    import usermenu
else:
    a = str(g[0])
    b = str(g[1])
    c = str(g[2])
    d = str(int(g[3]) - int(cash))
    e = str(g[4])   
    h.write(a)
    h.write(b)
    h.write(c)
    h.write(d + "\n")
    h.write(e + "\n")
    f.close()
    h.close()
    os.remove("C:\Python27\Lib\importlib" + pp + "")
    os.rename("C:\Python27\Lib\importlib\\tempp.txt", "C:\Python27\Lib\importlib" + pp + "")
    print "Amount Withdraw Succesfull......."
    print "Your Balance is ", d
    time.sleep(2)
    import usermenu
