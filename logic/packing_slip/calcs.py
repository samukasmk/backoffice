from functools import lru_cache

@lru_cache(maxsize=1)
def calculate_total_price(price, quantity):
    return price * quantity

@lru_cache(maxsize=1)
def calculate_total_weigth(weight, quantity):
    return weight * quantity

@lru_cache(maxsize=1)
def calculate_total_seller_commission(total_price, seller_commission_tax):
    return total_price * (seller_commission_tax/100)

