import json
import random as rand

from game import write_json

def add_disquette(author, message):
    default_disquette = {
        "id": 0,
        "author": "author",
        "disquette": "oui"
    }
    
    with open('disquettes.json') as disquettes_json:
        data = json.load(disquettes_json)
        disquettes = data["disquettes"]
        
        max_id = len(disquettes)
        duplicate = False
        
        for disquette in disquettes:
            if disquette["disquette"] == disquette:
                duplicate = True
        
        if not duplicate:        
            default_disquette["id"] = max_id
            default_disquette["author"] = author
            default_disquette["disquette"] = message

            disquettes.append(default_disquette)
            write_json(data, "disquettes.json")
            
def pick_random_disquette():
    disquette = None
    
    with open('disquettes.json') as disquettes_json:
        data = json.load(disquettes_json)
        disquettes = data["disquettes"]
        
        max_id = len(disquettes) - 1
        id = rand.randint(0, max_id)
        
        disquette = disquettes[id]
        
    return toString(disquette)

def toString(disquette):
    message = disquette["disquette"]
    return message