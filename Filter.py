import sys
import time

#Dear , once you are done optimize this script , incrment the counter ,
# total counter 1
# Feel Free to put ur name i don't care <3 peace
#if you need more domains add them in domains simply -_- before asking me ! i'm not fucking google !
s = """
Welcome : join t-shop.to Coded By Mister Spy
 """
for c in s:
    sys.stdout.write(c)
    time.sleep(0.005)
domains = ["@cloud", "@gmail", "@hotmail", "@yahoo", "@orange", "@aol", "@outlook", "@comcast"]


def filter(email):
    for check in domains:
        if check in str(email):
            print "[+]" + check + " => " + email
            open(check + '.txt', 'a').write(email)
            break


email = raw_input("\nEnter Ur Email  : ")
a = open(email, 'r').readlines()
for email in a:
    filter(email)
