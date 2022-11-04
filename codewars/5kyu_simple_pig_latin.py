"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

Date: 8/4/2022

--- PROMPT ---
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

--- LESSONS ---

"""


# --- MY SOLUTION ---
import string

def pig_it(text):
    new_text_list = []
    word_list = text.split()
    for word in word_list:
        if word not in string.punctuation: # if word is just a word, than pigify it!
            pigied_word = word[1:] + word[0] + 'ay'
            new_text_list.append(pigied_word) # append to solution list
        else:
            new_text_list.append(word)    # append punctuation to solutions list 
    final_string = ' '.join(new_text_list) # convert list to string
    return final_string

# --- PSUEDOCODE ---
    """
take each word and put it in a list
    .split?

    text.split()

take each item and move the first letter to the end, and add ay at the end of the string
    slicing??

need to merge list back into a string
    .join?

challenge is retaining punctuation marks...

in my for loop, I need to somehow identify if something is a punctuation mark, and DO Not make adjustment's if it is punctuation
import string

    """
# --- TEST ---

print(pig_it('Pig latin is cool ?')) #,'igPay atinlay siay oolcay'
print(pig_it('This is my string !')) #,'hisTay siay ymay tringsay'



# --- ALT SOLN by others ---

def pig_it_list_comprehension(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
