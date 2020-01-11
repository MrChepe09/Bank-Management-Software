import time
no = raw_input("Enter you PIN no.: ")
pp = "\\" + str(no) + ".txt"
f = open("C:\Python27\Lib\importlib" + pp + "", "r")
try:
    g = f.readlines()
    print ("Your ACCOUNT balance is : "+g[3]+ "RUPEES")
    time.sleep(0.5)
    b = raw_input("Press ENTER to continue: ")
    f.close()
    time.sleep(2)
    import usermenu
except:
    print "ERROR 42.0, NO ACCOUNT FOUND"
    import usermenu




