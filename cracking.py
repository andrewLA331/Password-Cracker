#Andrew Allen
#CS195

import os
import os.path
import sys
import hashlib


def cracker():
   
   file = "wordlist.txt"
   
   password = "cc8b1415557f58abf2e2fa83c2ea6c91"
   
   wordlist = open(file,"r")
   
   for line in wordlist:
      line = line.replace("\n", "")
      encrypted = hashlib.md5(line.encode()).hexdigest()

      if encrypted == password:
         print "###CRACKED###"
         print "The password is " + line
   
   wordlist.close()
        
cracker()