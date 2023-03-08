from functools import lru_cache


# OrderedProduct model methods with lru cache
@lru_cache(maxsize=1)
def calculate_total_price(price, quantity):
    return price * quantity


@lru_cache(maxsize=1)
def calculate_total_weight(weight, quantity):
    return weight * quantity


@lru_cache(maxsize=1)
def calculate_total_seller_commission(total_price, seller_commission_tax):
    return total_price * (seller_commission_tax / 100)


# Order model methods
def order_total_price(order_model):
    return sum([ordered_product.total_price() for ordered_product in order_model.ordered_products.all()])


def order_total_weight(order_model):
    return sum([ordered_product.total_weight() for ordered_product in order_model.ordered_products.all()])


def order_total_seller_commission(order_model):
    return sum([ordered_product.total_seller_commission() for ordered_product in order_model.ordered_products.all()])


def get_pipeline_tasks(order_model):
    # task_function_names = order_model.ordered_products.all().values_list(
    #     'product__product_type__pipeline_tasks__code', flat=True).distinct()
    # return list(task_function_names)
    return []
