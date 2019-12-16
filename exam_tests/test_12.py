# Implement the function sort_by_price_ascending, which:
# - Accepts a string in JSON format, as in the example below
# - Orders items by price in ascending Order
# - If two products have the same price, it orders them by their name in alphabetical orders
# - Returns a string in JSON format that is equivalent to the one in the input format
# Example>
# Products.sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')

# Should return
# '[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'

import json
from operator import itemgetter, attrgetter

class Products:

    @staticmethod
    def sort_by_price_ascending(json_string):
        objs_1 = json.loads(json_string)

        objs_2 = json.dumps(objs_1, sort_keys=True)
        lines = sorted(objs_1, key=lambda Price: Price['price'])
        # print(lines)
        items_tuples = []
        for each in lines:
            # print(each['name'], " ", each['price'])
            items = (each['name'],each['price'])
            items_tuples.append(items)

        items_tuples = sorted(items_tuples, key=itemgetter(1,0))

        string = "["
        for items in items_tuples:
            # print(items[0], " ", items[1])
            string = string + '{"name":"' + items[0] + '","price":' + str(items[1]) + "},"

        string = string[0:len(string)-1]
        string += "]"
        return string

print(Products.sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
print(Products.sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"tomato","price":1},{"name":"rice","price":4.04},{"name":"carrot","price":1}]'))
