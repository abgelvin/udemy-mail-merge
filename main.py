#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def write_letter(names):
    with open('./Input/Letters/starting_letter.txt') as file:
        letter = file.read()
        
        for name in names:
            print(name)
            new_letter = letter.replace('[name]', name)
            print(new_letter)
            with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as new_file:
                new_file.write(new_letter)


def get_names():
    with open('./Input/Names/invited_names.txt') as names:
        name_list = names.read().splitlines()
        print(name_list)
        return name_list
    

write_letter(get_names())