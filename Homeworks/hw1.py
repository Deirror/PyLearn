#homework 1

def main():
    viktors_ingredients = ['чушки', 'домати', 'моркови', 'ябълки', 'сол', 'черен пипер', 'кимион', 'зехтин']

    georgis_ingredients = ('чушки', 'домати', 'пaтладжан', 'люти чушки', 'олио', 'захар',
                           'чубрица', 'черен пипер', 'врачанска ракия')

    shopping_list = list(viktors_ingredients + list(georgis_ingredients))
    shopping_list.reverse()

    unique_ingredients = set(shopping_list)

    ingredient_quantities = {ingredient: 5 for ingredient in unique_ingredients}
    ingredient_quantities['skyr'] = 1

    number_of_ingredients_to_buy = len(ingredient_quantities)

    print(ingredient_quantities)
    print(number_of_ingredients_to_buy)

if __name__ == '__main__':
    main()
