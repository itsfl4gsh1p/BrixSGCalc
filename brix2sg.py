# Justin A
# @itsFL4GSH1P

print "==============================================================="
print "|  This a simple script to convert the brix reading from a    |"
print "| refractometer into a more brewer friendly specific gravity. |"
print "|  This calculation is a bit more accurate than the 4 rule.   |"
print "==============================================================="

brix = int(raw_input("Please enter your brix reading: ")) #simple - enter your reader - forces integer
sg = (brix/(258.6-((brix/258.2)*227.1)))+1 #formula from http://www.brewersfriend.com/brix-converter/
print "The specific gravity of your wort is: ", round(sg, 3) # round function rounds our floating point number to 3 digits

# variable explanation to define above.
# brix = brix reading from your refractometer
# sg = specific gravity expressed as such: 1.xxx
