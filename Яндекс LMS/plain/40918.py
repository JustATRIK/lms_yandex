def search_fruit(shops, fruit_targ):
    for shop, departaments in zip(shops.keys(), shops.values()):
        for departament, fruits in zip(departaments.keys(), departaments.values()):
            for fruit in fruits:
                if fruit_targ in fruit:
                    return shop, departament
    return None, None
    