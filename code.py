import sys

# Name: Boyd Belshof
# Student: S3012158
# Date: 25-03-2018
# Description: This program checks in which place in the Netherlands the most political parties
# are mentioned. The program consists out of 4 files, the code.py, the clean_man_names.txt, 
# clean_woman_names.txt and parties.txt
# clean_man_names and clean_woman_names contain files with names of women and men and de parties.txt
# contain names of political parties

def get_political_parties():
    """Opens the parties.txt file and places this in a string. Then returns
    it so it can be used later on."""
    party_words = []
    f = open("parties.txt", "r")
    for line in f:
        stripped_line = line.strip()
        party_words.append(stripped_line)
    return party_words

def get_man_names():
    """Reads all the mens names from a file """ 
    man_names = {}
    f = open("clean_man_names.txt", "r")
    for line in f:
        new_line = line.strip()
        new_line_lower = new_line.lower()
        man_names[new_line_lower] = 0
    return man_names

def get_woman_names():
    """Reads all the womens names from a file """ 
    woman_names = {}
    f = open("clean_woman_names.txt", "r")
    for line in f:
        new_line = line.strip()
        new_line_lower = new_line.lower()
        woman_names[new_line_lower] = 0
    return woman_names


def is_number(s):
    """check if s is a digit"""
    return any(i.isdigit() for i in s)

def main():
    total_tweets = 0
    """The main function, this is where all the help functions are runned and the checks for
    partys and there location. """
    #Gets the party words
    party_words = get_political_parties()
    #The counter for all the tweets that the program has checked
    #Gets the men names
    man_names = get_man_names()
    # Gets the women names
    woman_names = get_woman_names()
    #The counter for all the tweets send by men
    man_names_counter = 0
    #The counter for all the tweets send by women
    woman_names_counter = 0
    #The counter for all the tweets send by men that contain parties
    man_names_party_counter = 0
    #The counter for all the tweets send by women that contain parties
    woman_names_party_counter = 0
    #The Dictionary to check which party words are used the most
    woman_party_words = {}
    #The Dictionary to check which party words are used the most.
    man_party_words = {}
    for line in sys.stdin:
        if total_tweets == 5000:
            print(total_tweets)
            break;
        #Splits the input
        two_parts = line.split("\t")
        if (len(two_parts) == 3):
            if is_number(two_parts[2]):
                continue
            else:
                #Seperates the text part
                text = two_parts[1]
                #Seperates the names part
                name = two_parts[0]
        else:
            #Seperates the text part
            text = two_parts[1]
            #Seperates the names part
            name = two_parts[0]
        #Remove characters that are not allowed
        non_allowed_chars = ",.!-?/#@"
        for ch in non_allowed_chars:
            if ch in name:
                name = name.replace(ch, "")
            if ch in text:
                text = text.replace(ch, "")
        stripped_name = name.lower()
        stripped_text = text.lower()
        #Creates a word and name list for iteration.
        splitted_words = stripped_text.split(" ")
        splitted_name = stripped_name.split(" ")
        #Check if the name is in the name list
        for name in splitted_name:
            if name in man_names:
                man_names_counter += 1
                total_tweets += 1
            elif name in woman_names:
                woman_names_counter += 1
                total_tweets += 1


        #Check for parties in the text
        for word in splitted_words:
            if word in party_words:
                for name in splitted_name:
                    if name in man_names:
                        if word in man_party_words:
                            man_party_words[word] += 1
                        else:
                            man_party_words[word] = 1
                        man_names[name] += 1
                        man_names_party_counter += 1
                    elif name in woman_names:
                        if word in woman_party_words:
                            woman_party_words[word] += 1
                        else:
                            woman_party_words[word] = 1
                        woman_names[name] += 1
                        woman_names_party_counter += 1



    #write the output to a file
    file = open("output.txt", "w") 
    file.write("Woman party count: ")
    woman_sorted = sorted(woman_party_words.items(), key=lambda x: x[1])
    file.write(str(woman_sorted) + "\n") 
    file.write("Man party count: ")
    man_sorted = sorted(man_party_words.items(), key=lambda x: x[1])
    file.write(str(man_sorted) + "\n")
    file.write("Total Tweets:\t" + str(total_tweets) + "\n")
    file.write("Tweets by Women:\t" + str(woman_names_counter) + "\t" + str(woman_names_party_counter) + "\n")
    file.write("Tweets by Men:\t" + str(man_names_counter) + "\t" + str(man_names_party_counter) + "\n")
    file.close()


main()





