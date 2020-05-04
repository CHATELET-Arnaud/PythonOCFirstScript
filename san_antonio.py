# -*- coding: utf8 -*-
print("L'écrivain et humoriste Frédéric Dard est né à Bourgoin-Jallieu.")
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_item_in(my_list):
    # TODO: get a random item
    item = my_list[0] # get an item from a list
    # TODO: show the quote
    return "program is over"

user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

# Show random quote

if user_answer == "B": 
	pass
elif user_answer == "C":
	print("C pas la bonne réponse !")
else:
	print(get_random_item_in(quotes))

