from django.utils import timezone


def define_sku_code(product_type_name):
    sku_prefix = '-'.join([initials.upper()[:3] for initials in product_type_name.split(' ')[:2]])
    sku_id = timezone.now().strftime('%y%m%d-%H%M%S-%f')[:17]
    return f'{sku_prefix}-{sku_id}'
