"""I started this project on November 13th 2026"""

import json

#clearing the data from the 'expenses file
def clear(file):
    with open(file, 'w') as f:
        json.dump([], f, indent=4)              #to clear dump an empty list
    print('File cleaned successfully!')

#adding new expenses to the file
def add_expenses(file, amount, category, description):      
    #checking for the file
    try:  
        with open(file, 'r') as f:
            content=json.load(f)                        #loading the info so that it is not lost when writing 
            id=content[-1]['id']+1                      #getting the id for the next expense
    
    #if file doesn't exist or has an emppty list
    except (FileNotFoundError, IndexError):             
        id=1
        content=[]

    #if the file is damaged
    except json.JSONDecodeError:
        print('Your json file is damaged!')
        return        

    #if all good, add the new info
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

#listing the data to the console
def list_expenses(file):
    try:
        with open(file, 'r') as f:
            content=json.load(f)
            if content==[]:
                print('The file is empty!')
                return
            for expense in content:
                for type in expense:
                    print(f'{type.capitalize()}: {expense[type]}')
                print()
            

    except FileNotFoundError:
        print('File not found!')
    except json.JSONDecodeError:
        print('JSON File is damaged!')

#deleting expense with the given id  
def delete_expense(file, id):
    try:
        id =int(id)
    except ValueError:
        print('ID must be an integer: ')
        return
    try:
        with open(file, 'r') as f:
            content=json.load(f)
            new_content=[]
            for expense in content:
                if expense['id']==id:
                    continue
                new_content.append(expense)

    except FileNotFoundError:
        print('File was not found!')
        return
    except json.JSONDecodeError:
        print('File is damaged!')
        return
    with open(file, 'w') as w:
        json.dump(new_content, w, indent=4)
        if len(new_content)==len(content):
            print('Expense with the given id was not found!')
        else:
            print('Deleted successfully!')

#testing 
#variables
file='expenses.json'
condition=0

#loop for testing different functions
while condition!=1:
    operation=input('What would you like to do? ')
    try:
        operation=int(operation)
    except ValueError:
        pass
        
    print()
    match operation:
        #case for adding expenses
        case 1:
            while True:
                try:
                    amount=int(input('Enter the amount: '))
                    break
                except ValueError:
                    print('Amount should only be interger!')

            category=input('Define the category: ')
            description=input('Porvide some description: ')
            add_expenses('expenses.json', amount, category, description)

        #case for listing expenses
        case 2:
            list_expenses(file)
        
        #case for deleting expense using id
        case 3:
            id=input('Enter the id for the expense you want to delete: ')
            delete_expense(file, id)
        
        #case for cleaering
        case 0:
            clear(file)
        
        #case for exiting the loop
        case _:
            condition=input('\nWould you like to exit? 1 for YES, anything else for NO: ')
    
    print('\n')
    try:
        condition=int(condition)
    except ValueError:
        continue
    