"""I started this project on november 13th 2026"""

import json


def add_expenses(file, amount, category, description):
    #checking for the file
    try:  
        with open(file, 'r') as f:
            content=json.load(f)
            id=content[-1]['id']+1                      #getting the id for the next expense
    except FileNotFoundError or IndexError:
        id=1
        content=[]        

    with open(file, 'w') as w:
        #adding the new information
        info={
            'id': id,
            'amount': amount,
            'category': category,
            'description': description,
        }
        content.append(info)
        json.dump(content, w, indent=4)    #dumping it into the file

    print('Successfully added!')

#clearing the data from the 'expenses file

def clear(file):
    with open(file, 'w') as f:
        pass
    print('File cleaned successfully!')



#new data
amount=20
category='food'
description='lunch'

# add_expenses('expenses.json', amount, category, description)


clear('expenses.json')