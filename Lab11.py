# -*- coding: utf-8 -*-
##First Part
def main():
    ##- 	Open the file students.txt for reading
    readfile = open ('students.txt',"r")
    ##-	Read a line
    line = readfile.readline()
    ##-	Create an empty list
    progs = []
    ##-	Loop to process a line
    while line != "":
        ##o	Get the 4 fields
        p, l, f, g = line.split(",")
        ##o	Clean the program field
        p = p.strip('"')
        ##o	Set a boolean to False
        pthere = False
        ##o	For each program in the list
        for prog in progs:
            ##	If the new program name matches the list value
            if p.upper() == prog.upper():
                ##•	Set the boolean to True (It is alread in the list)
                pthere = True
                break
        ##o	If the program isn’t yet in the list (if the Boolean is still False)
        if not pthere: 
            ##	Add the new program to the list
            progs.append(p.upper())
        ##o	Read the next line
        line = readfile.readline()
    ##-	Close the file
    readfile.close()

    ##
    ##Start of Fifth Part
    ##Set a string to “Y”  (Ans = “Y”)
    Ans = "Y"
    ##While the string is not “N”
    while Ans[0].upper() != "N":
    ##Second and Third Part
        ##-	Set a Boolean variable to False
        goodvalue = False

        ##-	While the Boolean is False
        while goodvalue == False:
            ##o	Print a heading for the program list
            print "List of Programs"
            print "================"
        
            ##o	For each program in the list
            ## l is a single line in a list.
            for l in progs:
                ##	Print the name
                print l

            ##o	Ask the user to enter a program name
            prog1 = raw_input("Please enter a program name :")

            ##o	For each prgram in the list
            for l in progs:

                ##	If the value entered matches the list value
                
                if prog1.upper() == l:
                    
                    ##•	Set the Boolean to True
                    goodvalue = True
                    ##•	Break out of the loop (No need to search further)
                    break
            ##	If the Boolean is still False (ie. Name wasn’t found)
                ##•	Tell the user to enter a program shown.
            if goodvalue == False:
                
                print "Please enter a valid program name"
        ##
        ##Fourth Part
        ##-	Open the file students.txt for reading
        readfile = open('students.txt',"r")
        ##-	Read a line of the file
        line = readfile.readline()
        ##-	Print a heading for the list of students and grades
        
        print "\nResults For: %10s" %prog1.upper()
        print "========================="
        ##-	Initialize the grade total and student count for the program to 0
        gtotal = 0
        scount = 0
            
        ##-	Loop to process a line
        while line != "":
        ##o	Get the 4 fields from the line
            
            p, l, f, g = line.split(",")
            ##o	Clean the program field
            p = p.strip('"')
            
            ##o	If the program field matches the selected program
            if p.upper() == prog1.upper():

                ##	Clean the name fields
                l = l.strip('"')
                f = f.strip('"')
                ##	Convert the grade to an integer
                g = int(g)
                ##	Add the grade to the grade total
                gtotal = gtotal + g
                ##	Increment the count by 1
                scount = scount + 1
                ##	Print the student name and grade
                print "%10s %-10s %2d" % (l, f, g)
            ##o	Read the next line
            line = readfile.readline()
        ##-	Close the file
        readfile.close()
        ##-	Calculate the average (grade total / program count)
        average = float(gtotal)/scount
        ##-	Print the average

        print "\n      Average %5.2f\n" %average
        Ans = raw_input("Do you want to continue? :")
        #Ans = Ans[0].upper()
        ##-	If there is no response
        if len(Ans) == 0:
        
            ##o	Set the response to “Y”
            Ans = "Y"
    ##
    ##The Rest of the Fifth Part
    ##-	Ask the user if they want another list.
        #Ans = raw_input("Do you want to continue? :"

main()

##
##Ans="Y"
##while Ans == "Y":
##    main()
##
##
##    ##
##    ##When the response is “NO” the program will end.
##if Ans[0].upper() == "N":
print "Goodbye"
