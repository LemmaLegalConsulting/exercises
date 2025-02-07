# -*- coding: utf-8 -*-

MIN = 0
MAX = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Aged Brie":
                if item.quality < MAX:
                    item.quality += 1
                if item.sell_in < 1 and item.quality < MAX:
                    item.quality += 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < MAX:
                    item.quality += 1
                    if item.sell_in < 11 and item.quality < MAX:
                        item.quality += 1
                    if item.sell_in < 6 and item.quality < MAX:
                        item.quality += 1
                    if item.sell_in < 1:
                        item.quality = MIN
            elif item.name == "Conjured Mana Cake":
                if item.sell_in > MIN:
                    item.quality += -2
                else:
                    item.quality += -4
                
                item.quality = MIN if item.quality < MIN else item.quality
            else:
                if item.quality > MIN:
                    item.quality += -1
                if item.sell_in < 1 and item.quality > MIN:
                    item.quality += -1
                
                

            item.sell_in += -1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)