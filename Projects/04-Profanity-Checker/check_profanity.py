# Program to check automatically for curse words
# Steps
# 0 - Import a Database of Curse Words
# 1 - Check each word and compare with curse words
# 2 - Show Result

# Read Text from a document
# Check this text for Curse Words

# http://www.wdylike.appspot.com/?q=shot
# Checking word after the query, in this case: shot
# Google What Do You Love for checking curs word
import urllib

def read_text():
    quotes = open("profanitext.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    # print(output)
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document is politicaly correct")
    else:
        print("Could not scan the document properly.")
        
    connection.close()

read_text()