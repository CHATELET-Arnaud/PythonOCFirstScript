# -*- coding: utf8 -*-
quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

def get_random_item_in(my_list):
    # TODO: get a random item
    item = my_list[0] # get an item from a list
    # TODO: show the quote
    return item

user_answer = "A" # input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

# Show random quote

while user_answer != "B": 
	print(get_random_item_in(quotes))
	user_answer = "B"
