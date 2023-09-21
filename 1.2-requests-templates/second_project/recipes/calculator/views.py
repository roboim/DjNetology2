from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
    # можете добавить свои рецепты ;)
}


def recipe_calculator(request, item):
    multiply = request.GET.get('servings')
    if multiply is None:
        multiply = 1
    recipe = dict()
    recipe_out = dict()
    if item.lower() in DATA:
        recipe = DATA[item.lower()]
    try:
        for component in recipe:
            print(component, recipe[component])
            recipe_out[component] = float(recipe[component]) * int(multiply)
    except Exception as error:
        print(f'Ошибка данных {error}')
        recipe_out = {}
    context = dict()
    context['recipe'] = recipe_out
    return render(request, 'calculator/index.html', context=context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }