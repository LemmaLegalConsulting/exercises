# -*- coding: utf-8 -*-
import pytest

import gilded_rose as gr


def test_normal_item_before_sell_date():
    item = gr.Item(name='Normal', quality=10, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 9
    assert item.sell_in == 4


def test_normal_item_on_sell_date():
    item = gr.Item(name='Normal', quality=10, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 8
    assert item.sell_in == -1


def test_normal_item_after_sell_date():
    item = gr.Item(name='Normal', quality=10, sell_in=-10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 8
    assert item.sell_in == -11


def test_normal_item_of_zero_quality():
    item = gr.Item(name='Normal', quality=0, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == 4


def test_brie_before_sell_date():
    item = gr.Item(name='Aged Brie', quality=10, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 11
    assert item.sell_in == 4


def test_brie_before_sell_date_with_max_quality():
    item = gr.Item(name='Aged Brie', quality=50, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == 4


def test_brie_on_sell_date():
    item = gr.Item(name='Aged Brie', quality=10, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 12
    assert item.sell_in == -1


def test_brie_on_sell_date_near_max_quality():
    item = gr.Item(name='Aged Brie', quality=49, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == -1


def test_brie_on_sell_date_with_max_quality():
    item = gr.Item(name='Aged Brie', quality=50, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == -1


def test_brie_after_sell_date():
    item = gr.Item(name='Aged Brie', quality=10, sell_in=-10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 12
    assert item.sell_in == -11


def test_brie_after_sell_date_with_max_quality():
    item = gr.Item(name='Aged Brie', quality=10, sell_in=-10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 12
    assert item.sell_in == -11


def test_sulfuras_before_sell_date():
    item = gr.Item(name='Sulfuras, Hand of Ragnaros', quality=80, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 80
    assert item.sell_in == 5


def test_sulfuras_on_sell_date():
    item = gr.Item(name='Sulfuras, Hand of Ragnaros', quality=80, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 80
    assert item.sell_in == 0


def test_sulfuras_after_sell_date():
    item = gr.Item(name='Sulfuras, Hand of Ragnaros', quality=80, sell_in=-10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 80
    assert item.sell_in == -10


def test_backstage_pass_long_before_sell_date():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=10, sell_in=11)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 11
    assert item.sell_in == 10


def test_backstage_pass_long_before_sell_date_at_max_quality():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=50, sell_in=11)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == 10


def test_backstage_pass_medium_close_to_sell_date_upper_bound():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=10, sell_in=10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 12
    assert item.sell_in == 9


def test_backstage_pass_medium_close_to_sell_date_upper_bound_at_max_quality():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=50, sell_in=10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == 9


def test_backstage_pass_medium_close_to_sell_date_lower_bound():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=10, sell_in=6)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 12
    assert item.sell_in == 5


def test_backstage_pass_medium_close_to_sell_date_lower_bound_at_max_quality():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=50, sell_in=6)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == 5


def test_backstage_pass_very_close_to_sell_date_upper_bound():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=10, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 13
    assert item.sell_in == 4


def test_backstage_pass_very_close_to_sell_date_upper_bound_at_max_quality():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=50, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == 4


def test_backstage_pass_very_close_to_sell_date_lower_bound():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=10, sell_in=1)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 13
    assert item.sell_in == 0


def test_backstage_pass_very_close_to_sell_date_lower_bound_at_max_quality():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=50, sell_in=1)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 50
    assert item.sell_in == 0


def test_backstage_pass_on_sell_date():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=10, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == -1


def test_backstage_pass_after_sell_date():
    item = gr.Item(name='Backstage passes to a TAFKAL80ETC concert', quality=10, sell_in=-10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == -11


@pytest.mark.skip(reason="Need to implement")
def test_conjured_item_before_sell_date():
    item = gr.Item(name='Conjured Mana Cake', quality=10, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 8
    assert item.sell_in == 4


@pytest.mark.skip(reason="Need to implement")
def test_conjured_item_before_sell_date_at_zero_quality():
    item = gr.Item(name='Conjured Mana Cake', quality=0, sell_in=5)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == 4


@pytest.mark.skip(reason="Need to implement")
def test_conjured_item_on_sell_date():
    item = gr.Item(name='Conjured Mana Cake', quality=10, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 6
    assert item.sell_in == -1


@pytest.mark.skip(reason="Need to implement")
def test_conjured_item_on_sell_date_at_zero_quality():
    item = gr.Item(name='Conjured Mana Cake', quality=0, sell_in=0)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == -1


@pytest.mark.skip(reason="Need to implement")
def test_conjured_item_after_sell_date():
    item = gr.Item(name='Conjured Mana Cake', quality=10, sell_in=-10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 6
    assert item.sell_in == -11


@pytest.mark.skip(reason="Need to implement")
def test_conjured_item_after_sell_date_at_zero_quality():
    item = gr.Item(name='Conjured Mana Cake', quality=0, sell_in=-10)
    rose = gr.GildedRose([item])
    rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == -11
