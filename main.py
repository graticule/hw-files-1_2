# Задание 1
def read_cookbook(filename):
    cookbook = {}
    with open(filename, encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        start = 0
        while start < len(lines) and lines[start]:
            dish = lines[start]
            start += 1
            cookbook[dish] = []
            for _ in range(int(lines[start])):
                start += 1
                name, quantity, measure = [word.strip() for word in lines[start].split('|')]
                cookbook[dish].append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
            start += 2
    return cookbook

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for dish_inredient in cookbook.get(dish,[]):
            if dish_inredient['ingredient_name'] in shop_list:
                shop_list[dish_inredient['ingredient_name']]['quantity'] += person_count*dish_inredient['quantity']
            else:
                shop_list[dish_inredient['ingredient_name']] = {'measure': dish_inredient['measure'], 'quantity': dish_inredient['quantity']*person_count}
    return shop_list


if __name__ == '__main__':
    cookbook = read_cookbook('cookbook.txt')
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
