def search_fruit(shops, fruit_targ):
    for shop, departaments in zip(shops.keys(), shops.values()):
        for departament in departaments:
            for fruit in departament:
                if fruit == fruit_targ:
                    return shop, departament
    return None, None
