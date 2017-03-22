import s

class TorrentItem(scrapy.item):
    url = scrapy.Field()
    name = scrapy.Field()

