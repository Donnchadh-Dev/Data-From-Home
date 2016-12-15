# simple python script to get time in Ireland

from time import gmtime, strftime 

# print out date and time
print "In Ireland it is currently: " + strftime("%a, %d %b %Y %H:%M:%S", gmtime())

#TODO

# add weather information for local area

