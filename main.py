# Задание 1
from typing import List, Dict, TypedDict


class DishIngredient(TypedDict):
    ingredient_name: str
    quantity: int
    measure: str


class ShoplistIngredient(TypedDict):
    quantity: int
    measure: str


CookBook = Dict[str, List[DishIngredient]]
ShopList = Dict[str, ShoplistIngredient]


def read_cookbook(filename: str) -> CookBook:
    result_cookbook = {}
    with open(filename, encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        start = 0
        while start < len(lines) and lines[start]:
            dish = lines[start]
            start += 1
            result_cookbook[dish] = []
            for _ in range(int(lines[start])):
                start += 1
                name, quantity, measure = [word.strip() for word in lines[start].split('|')]
                result_cookbook[dish].append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
            start += 2
    return result_cookbook


# Задание 2
def get_shop_list_by_dishes(dishes: List[str], person_count: int) -> ShopList:
    shoplist = {}
    for dish in dishes:
        for dish_ingredient in cookbook.get(dish, []):
            if dish_ingredient['ingredient_name'] in shoplist:
                shoplist[dish_ingredient['ingredient_name']]['quantity'] += person_count * dish_ingredient['quantity']
            else:
                shoplist[dish_ingredient['ingredient_name']] = {'measure': dish_ingredient['measure'],
                                                                'quantity': dish_ingredient['quantity'] * person_count}
    return shoplist


if __name__ == '__main__':
    cookbook = read_cookbook('cookbook.txt')
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
