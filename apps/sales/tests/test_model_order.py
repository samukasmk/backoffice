from unittest.mock import patch

import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_total_price_order(customer_order, ordered_products, ordered_products_total_price):
    assert customer_order.total_price() == ordered_products_total_price

@pytest.mark.django_db
def test_total_weight_order(customer_order, ordered_products, ordered_products_total_weight):
    assert customer_order.total_weigth() == ordered_products_total_weight