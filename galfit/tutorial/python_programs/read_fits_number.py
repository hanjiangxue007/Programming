
with open("galfit.365") as file:
     lines = file.readlines() # all your lines are here

     # should print "#  Input menu file: 10f160w39.feedme"
     # since it is the first line in the file
     print (lines[0])

     index_of_w = lines[0].index('w')

     # this should give you 39
     number_after_w = lines[0][index_of_w+1] + lines[0][index_of_w+2]
     print (number_after_w)
