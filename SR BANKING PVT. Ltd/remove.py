import os
import time
no = raw_input("Enter you PIN no.: ")
print "Do you really want to DELETE YOUR ACCOUNT (y/n)"
ch = str.lower(raw_input("Enter Your Choice: "))
if ch == 'y':
    pp = "\\" + str(no) + ".txt"
    if os.path.exists("C:\Python27\Lib\importlib" + pp + ""):
        try:
            os.remove("C:\Python27\Lib\importlib" + pp + "")
            time.sleep(1)
            print "DELETING YOUR ACCOUNT......."
            time.sleep(3)
            print "ACCOUNT REMOVED..."
            a = raw_input("Press ENTER to continue-")
            import Menu
        except OSError, e:
            print ("Error: %s - %s." % (e.no, e.strerror))
    else:
        print("Sorry, No Account found of your given PIN ." % no)
        import Menu


else:
    import Menu
