from unittest.mock import patch

import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_total_price_order(order, ordered_products, total_price):
    assert order.total_price() == total_price


@pytest.mark.django_db
def test_total_weight_order(order, ordered_products, total_weigth):
    assert order.total_weigth() == total_weigth


@pytest.mark.django_db
def test_total_seller_commission_order(order, ordered_products, total_seller_commission):
    assert order.total_seller_commission() == total_seller_commission
