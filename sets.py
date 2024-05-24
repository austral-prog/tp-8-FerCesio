from sets_categories_data import (ALCOHOLS)


def clean_ingredients(x,y):
    tuple = x,set(y)
    return tuple
clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])


def check_drinks(x,y):
    if set(y).intersection(ALCOHOLS):
        return f"{x} Cocktail"
    else:
        return f"{x} Mocktail"
check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])

