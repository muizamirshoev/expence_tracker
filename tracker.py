"""I started this project on November 13th 2026"""

import json

class expense_tracker:
    def __init__(self, file):
        self.file = file

    def clear(self):
        with open(self.file, 'w') as f:
            json.dump([], f, indent=4)             
        print('File cleaned successfully!')

    def check_file(self):
        with open(self.file, 'r') as f:
            return json.load(f)

    #adding new expenses to the file
    def add_expenses(self, amount, category, description):      
        
        try:
            content = self.check_file()
            key=content[-1]['key']+1
        except (FileNotFoundError, IndexError):
            key=1
            content=[]
        except json.JSONDecodeError:
            print ('File is damaged!')
            return

        #if all good, add the new info
        with open(self.file, 'w') as w:
            #adding the new information
            info={
                'key': key,
                'amount': amount,
                'category': category,
                'description': description,
            }
            content.append(info)
            json.dump(content, w, indent=4)    #dumping it into the file

        print('Successfully added!')

    #listing the data to the console
    def list_expenses(self):
        try:   
            content= self.check_file()
            if content==[]:
                print('The file is empty!')
                return
            for expense in content:
                for tipe in expense:
                    print(f'{tipe.capitalize()}: {expense[tipe]}')
                print()
                
        except FileNotFoundError:
            print('File not found!')
        except json.JSONDecodeError:
            print('JSON File is damaged!')

    #deleting expense with the given key  
    def delete_expense(self, key):
        try:
            key =int(key)
        except ValueError:
            print('ID must be an integer: ')
            return
        try:
            content=self.check_file()
            new_content=[]
            for expense in content:
                if expense['key']==key:
                    continue
                new_content.append(expense)

        except FileNotFoundError:
            print('File was not found!')
            return
        except json.JSONDecodeError:
            print('File is damaged!')
            return
        with open(self.file, 'w') as w:
            json.dump(new_content, w, indent=4)
            if len(new_content)==len(content):
                print('Expense with the given id was not found!')
            else:
                print('Deleted successfully!')

#testing 
#variables
file='expenses.json'
condition=0

tracker=expense_tracker('expenses.json')

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
            tracker.add_expenses(amount, category, description)

        #case for listing expenses
        case 2:
            tracker.list_expenses()
        
        #case for deleting expense using id
        case 3:
            key=input('Enter the id for the expense you want to delete: ')
            tracker.delete_expense(key)
        
        #case for cleaering
        case 0:
            tracker.clear()
        
        #case for exiting the loop
        case _:
            condition=input('\nWould you like to exit? 1 for YES, anything else for NO: ')
    
    print('\n')
    try:
        condition=int(condition)
    except ValueError:
        continue
   