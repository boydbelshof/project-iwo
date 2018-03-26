def remove_duplicates(l):
    #functions for remove duplicate items from a list
    return list(set(l))

def main():
    #the files
    fname = "man_names.txt"
    f2name = "woman_names.txt"

    #open the files
    with open(fname) as f:
        man_names = f.readlines()
        
    with open(f2name) as f:
        woman_names = f.readlines()

    #Read the names and insert into a list
    man_names = [x.strip() for x in man_names]
    woman_names = [x.strip() for x in woman_names]
    
    #Remove duplicate names
    man_names = remove_duplicates(man_names)
    woman_names = remove_duplicates(woman_names)
    
    #Remove names that are used for man and women
    man_names = list(set(man_names) - set(woman_names))
    woman_names = list(set(woman_names) - set(man_names))
    
    #Writes the names back to a file
    man_file = open('clean_man_names.txt', 'w')
    for item in man_names:
        man_file.write("%s\n" % item)
    
    
    woman_file = open('clean_woman_names.txt', 'w')
    for item in woman_names:
        woman_file.write("%s\n" % item)
    
    
main()