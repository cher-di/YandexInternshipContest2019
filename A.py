from collections import namedtuple

DISH = namedtuple("DISH",
                  ("friends", "ingredients"))

INGREDIENTS_IN_THE_DISH = namedtuple("INGREDIENTS_IN_THE_DISH",
                                     ("amount", ))

INGREDIENTS_IN_THE_PRICE_CATALOG = namedtuple("INGREDIENTS_IN_THE_PRICE_CATALOG",
                                              ("price", "amount"))

INGREDIENTS_IN_THE_FOOD_CATALOG = namedtuple("INGREDIENTS_IN_THE_FOOD_CATALOG",
                                             ("amount", "pr", "f", "ch", "fv"))


def get_appropriate_amount(amount: int, u: str) -> int:
    if u in ("kg", "l"):
        return amount * 1000
    elif u == "tens":
        return amount * 10
    else:
        return amount


def get_num_of_packages(total_amount: int, amount_per_pack: int) -> int:
    if total_amount % amount_per_pack == 0:
        return total_amount // amount_per_pack
    else:
        return total_amount // amount_per_pack + 1


def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0


def get_formatted_float(number: float) -> str:
    return str(number) + "0"


if __name__ == '__main__':
    dishes = dict()
    price_catalog = dict()
    food_catalog = dict()
    all_ingredients = dict()

    # dishes
    n = int(input())
    for i in range(n):
        dish_name, friends, z = input().split()
        dishes[dish_name] = DISH(int(friends), dict())
        for j in range(int(z)):
            ing_name, amount, u = input().split()
            amount = get_appropriate_amount(int(amount), u)
            dishes[dish_name].ingredients[ing_name] = INGREDIENTS_IN_THE_DISH(amount)
            all_ingredients[ing_name] = 0

    # price catalog
    k = int(input())
    for i in range(k):
        ing_name, price, amount, u = input().split()
        amount = get_appropriate_amount(int(amount), u)
        price_catalog[ing_name] = INGREDIENTS_IN_THE_PRICE_CATALOG(int(price), amount)

    # food catalog
    m = int(input())
    for i in range(m):
        ing_name, amount, u, pr, f, ch, fv = input().split()
        amount = get_appropriate_amount(int(amount), u)
        food_catalog[ing_name] = INGREDIENTS_IN_THE_FOOD_CATALOG(amount, float(pr), float(f), float(ch), float(fv))

    money = 0
    for ing_name in all_ingredients.keys():
        total_ing_amount = 0
        for dish_name in dishes.keys():
            if ing_name in dishes[dish_name].ingredients:
                total_ing_amount += dishes[dish_name].ingredients[ing_name].amount * dishes[dish_name].friends
        num_pack = get_num_of_packages(total_ing_amount, price_catalog[ing_name].amount)
        all_ingredients[ing_name] = num_pack
        money += num_pack * price_catalog[ing_name].price

    print(money)
    for ing_name, num_pack in all_ingredients.items():
        print(ing_name, num_pack)

    for dish_name in dishes.keys():
        pr, f, ch, fv = 0, 0, 0, 0
        for ing_name in dishes[dish_name].ingredients:
            pr += dishes[dish_name].ingredients[ing_name].amount / food_catalog[ing_name].amount * food_catalog[ing_name].pr
            f += dishes[dish_name].ingredients[ing_name].amount / food_catalog[ing_name].amount * food_catalog[ing_name].f
            ch += dishes[dish_name].ingredients[ing_name].amount / food_catalog[ing_name].amount * food_catalog[ing_name].ch
            fv += dishes[dish_name].ingredients[ing_name].amount / food_catalog[ing_name].amount * food_catalog[ing_name].fv
        pr = int(pr) if int(pr) >= pr else pr
        f = int(f) if int(f) >= f else f
        ch = int(ch) if int(ch) >= ch else ch
        fv = int(fv) if int(fv) >= fv else fv
        print(dish_name, pr, f, ch, fv)
