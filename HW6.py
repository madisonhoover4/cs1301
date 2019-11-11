#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW6 - File I/O - due March 02, 2017
"""
import csv
import urllib.request
import urllib.parse
from datetime import datetime

__author__ = "MADISON HOOVER"
__collaboration__ = """ I WORKED ON THIS ASSIGNMENT ALONE USING ONLY THIS SEMESTER'S COURSE MATERIALS """

#######################
#       PART 1        #
#   File Manipulation #
#######################

"""
You have been provided with a text file. You can download it here: http://cs1301.com/downloads/RamblinWreck.txt Read the file and replace all instances of ‘engineer’ with title<str>. If title<str> begins with a consonant, then the ‘an’ before the title<str> should be replaced with ‘a’. Also, indent all lines that do not contain the word ‘engineer’ (in the original file). The improved fight song is written to a new file. Name this file: ImprovedFightSong.txt
"""
def improve_fight_song(title):
    with open("RamblinWreck.txt","r+") as myfiler:
        string = myfiler.read()
        if title == "":
            newstring = string
        elif title[0] in "aeiou":
            prefix = "an"
            newstring = string.replace("engineer",title)
        elif title[0] not in "aeiou":
            prefix = "a"
            newstring = string.replace("an engineer","a " + title)
        
        with open("ImprovedFightSong.txt", "w") as newfile:
            finalstring = ''
            newlist = newstring.split('\n')
            for line in newlist:
                if title == "":
                    if "engineer" not in line:
                        line = "\t" + line + "\n"
                        finalstring = finalstring + line
                    else:
                        line = line + "\n"
                        finalstring = finalstring + line
                elif title not in line:
                    line =  "\t" + line + "\n"
                    finalstring = finalstring + line
                else:
                    line = line + "\n"
                    finalstring = finalstring + line
            newfile.write(finalstring)

# DONE
    

"""
Maintain an active log of a chat history by writing the information to a text file. Name your file: log.txt. You should write information about the message. Include the time, determined by the value passed in via the time<datetime.datetime> parameter. Also include the sender<str>, the
receiver<str>, and finally the message, msg<str>. Check the test cases for exact format.
"""
def my_chat(sender, receiver, msg, time = datetime.now()):
    with open("log.txt","r+") as mylog:
        mylog.read()
        mylog.write(str(time.strftime("%m/%d/%y %I:%M%p ")))
        mylog.write("-- From: ")
        mylog.write(sender)
        mylog.write(" To: ")
        mylog.write(receiver)
        mylog.write("\n")
        mylog.write("Message: ")
        mylog.write(msg)
        mylog.write("\n")
        mylog.write("\n")

# DONE

"""
Writes a file containing the information in the list sorted by artist_name<str>. The songs by an artist should be written to the file in a numbered list. The function can handle any number of tuples. The name of the file being created is songInfo.txt.
"""
def song_by_artist(songs):
    with open("songInfo.txt","w") as file:
        songs.sort(key=lambda tup:(tup[1],tup[0],tup[2]))
        counter = 1
        artist = songs[0][1]
        print(songs)
        file.write(artist+"\n")
        for tup in songs:
            if artist != tup[1]:
                artist = tup[1]
                file.write("\n" +artist+" \n")
                counter = 1
                
            file.write(str(counter)+". "+tup[0]+", "+str(tup[2])+"\n")
            counter += 1
            

# DONE


#########################
#         PART 2        #
# CSV and Data Analysis #
#########################

"""
Returns a list of the top N<int> company_names<str> in a given year<int>.
If N > length of list for given year, return all company_names ranked that year.
"""
def top_companies(year, N):
    with open('fortune500.csv') as csvfile:
        if N <= 0 or year < 1955 or year > 2009:
            return []
        readCSV = csv.reader(csvfile)
        eligiblecompanies = []
        for line in readCSV:
            if str(year) in line[0]:
                eligiblecompanies.append(line)
        finallist = []
        count = 0
        while count < N:
            finallist.append(eligiblecompanies[count][2])
            count += 1
    return finallist

        
# DONE
    
"""
Returns a tuple (rank<int>, revenue(millions)<float>, profit (millions)<float>) of the company_name for the given year. Return None if the company was not ranked that year
"""
def company_ranking(company_name, year):
    with open('fortune500.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        tup = ()
        companyranked = False
        for row in reader:
            if company_name == row[2]:
                
                if str(year) == row[0]:
                    companyranked = True
                    row[1] = row[1].replace(",","")
                    tup += int(row[1]),
                    row[3] = row[3].replace(",","")
                    tup += float(row[3]),
                    row[4] = row[4].replace(",","")
                    tup += float(row[4]),
        if companyranked == False:
            return None
        else:
            return tup
    
# DONE

"""
Returns a tuple (average<float(2 decimals)>, count<int>) of the company_name. Where average<float> is the average ranking a given company over all the years. Where count<int> is the number of times the company has been in the ranking. Return None if the company has not been
"""
import decimal
def company_average(company_name):
    with open('fortune500.csv') as csvfile1:
        readme = csv.reader(csvfile1)
        next(readme)
        count = 0
        total = 0
        for row in readme:
            if row[2] == company_name:
                count += 1
                total += int(row[1])
        if count == 0:
            return None
        else:
            avg = total / count

            avg = round(avg,2)
            return (avg, count)

# DONE

#######################
#       PART 3        #
#       urllib        #
#######################

def format_url(url, msg):
    """ Returns a safe url for opening using urllib """
    return url+"?str={}".format(urllib.parse.quote(msg))

main_url = "http://cs1301.com/"

def encrypt_message(msg):
    """ Returns an encrypted message. """
    with urllib.request.urlopen(format_url(main_url+"encrypt.php",msg)) as f:
        encryptedmessage = f.read().decode('utf-8',"strict")
        return encryptedmessage

# DONE
    

def decrypt_message(msg):
    """ Returns the decrypted message. """
    with urllib.request.urlopen(format_url(main_url+"decrypt.php",msg)) as f:
        decryptedmessage = f.read().decode('utf-8',"strict")
        return decryptedmessage

# DONE

########################
#        PART 4        #
#     Extra Credit     #
# Concurrent Functions #
########################

"""
Write a function that, on an infinite cycle, opens the file given as an argument, checks for new lines, and prints anything that has not been printed yet.
"""
def my_chat_listen(filename):
    with open(filename,"r") as x:
        print(x.read())
        while True:
            if x.read() != "":
                print(x.read())
            
# DONE

"""
Write a function that, on an infinite cycle, asks the user for input and writes the input to
"""
def my_chat_send(filename):
    with open(filename,"r+") as x:
        while True:
            x.read()
            x.write(input("what would you like to say?")+'\n')

# DONE, but I want to test these in 2 shells

            
            

















        
