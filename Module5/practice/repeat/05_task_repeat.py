# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination(num_items, items_on_page):
    return (num_items // items_on_page) + 1


def last_page(num_items, pages, items_on_page):
    last_page_items = (pages * items_on_page) - num_items
    return last_page_items


num_items = 134
items_on_page = 6
pages = pagination(num_items, items_on_page)
print(f"{last_page(num_items, pages, items_on_page)} объектов на последней странице")
