categories=['food','travel','entertainment','education']
expense_store={}

def getExpense():
    '''get all the required parameters for output'''
    print('Hello there!')
    print('What category would you like to add your expense to?')
    
    for index, item in enumerate(categories):
        print (index,item)

    categoryIndex=int(input('Enter the index of any above mentioned category:'))
    
    expense=int(input('enter the amount you spent in Npr: '))

    print(f"you spent {expense} in {categories[categoryIndex]}")



def storeExpense():
    pass

def addToList():
    pass

def showAll():
    pass

def main():
    '''entry of the main program'''
    getExpense()
