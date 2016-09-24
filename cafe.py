import random

def preferences():
    """ 
    Determines what kind of drink a customer likes.
    
    The function asks each of the questions in the questions \n 
    dictionary, and gather the responses in a new dictionary. \n
    
    The new dictionary contains the type of ingredient \n
    (for example "Tea", or "Coffee"), mapped to a Boolean value. \n
    
    If the customer answers y or yes to the question then \n 
    the value is set to True, otherwise the value set to False.  
    
    """
    
    questions = {
        'Tea': 'would you like a cup of tea?',
        'Coffee': 'Do you like a cup of coffee?',
        'Juice': 'Would you like a glass of juice?',
        'Mojito': 'Would like a mojito?',
    }

    
    preferenceList = {}
    start = True
    while True:
        for key, value in questions.items(): 
                answer = str(input(value))
                if answer.lower() == "yes" or answer.lower() == "y":
                    preferenceList[key] = True
                else:
                    preferenceList[key] = False
        break;
    start = False
    return preferenceList
    
def drinks(**kwargs):
    """
    Takes dictionary as a parameter.
    
    For each type of ingredient which the customer said they liked, \n
    Appends a corresponding ingredient from the ingredients dictionary. 
    
    Finally the function return list containing the contents of drink.
    
    """
    ingredients = {
        'Tea': ['Ginger', 'cinnamon', 'Fennel seed'],
        'Coffee': ['cardamom', 'Black pepper', 'cream'],
        'Juice': ['Pineapple', 'Mango', 'Passion'],
        'Mojito': ['Sprite', 'Lemon', 'Mint'],
    }
    
    choiceList = []
    contents = []
    for k, v in ingredients.items():
        choiceList.append(k)

    for key, value in kwargs.items():
        choice = random.choice(choiceList)
        if key == choice and value == True:
                contents.append(ingredients[choice])
    return contents
    
    
if __name__ == "__main__":
    preferenceList = preferences()
    print(drinks(**preferenceList))
    
    
    
    
    
    
    
    
    
    
    
    