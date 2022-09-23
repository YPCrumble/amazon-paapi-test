from amazon_paapi.models.item_result import Item


def parse_amazon_result(result: Item):
    reveal_type(result)
    print(result.item_info.content_info.publication_date)
