# /////////// INSTRUCTIONS /////////////////
# 🎨 Now it's up to you to create your own Mad Libs! 

# 💻 It's up to you to finish this story! 
#    - fill in the lists 
#    - use `choice()`to pick a random item from the list 
#    - add 5 lines to the story, using the different lists 

# 🤔 Be sure to think about the following things:
#    - What words in a story would be good candidates for MadLib words
#        example: locations, names, phrases, etc. 
# ////////////////////////////////////////////

from random import choice


print("-"*25)
print("        Mad Libs        ")
print("-"*25)
print()

# 💻 your code goes below here 💻

adjective_list = []
noun_list = [] 
number_list = []
location_list = []
verb_ing_list = []

print(f"A {choice(adjective_list)} hero set out to slay the {choice(noun_list)}.")