import json
from cat import Cat

def check_cat(elem, item):
    if elem[item]['code'] == 'cat':
	    return True

with open('f.json', encoding='utf8') as file:
    templates = json.load(file)

for elem in templates['results']:
    for item in elem:
        if item == 'species' and check_cat(elem, item):
            obj_Cat = Cat(elem['name'], elem['gender']['name'], elem['age'])
            print(obj_Cat.name)