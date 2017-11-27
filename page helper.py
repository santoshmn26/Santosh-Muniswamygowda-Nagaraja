class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.total_collection = collection
        self.total_items = self.item_count()
        self.total_items_per_page = items_per_page
        self.total_pages = self.page_count()
        j, self.book = 0, list()
        # data to the pages
        while (j < self.total_items):
            a = list()
            for i in range(items_per_page):
                if (j < self.total_items):
                    a.append(j)
                    j += 1
            self.book.append(a)

    def item_count(self):
        if (collection == []):
            return (-1)
        else:
            return (int(math.ceil(len(collection))))

    def page_count(self):
        if (collection == []):
            return (-1)
        self.total_page = float((len(collection)) / float(self.total_items_per_page * 1.0))
        return (int(math.ceil(self.total_page)))

    def page_item_count(self, page_index):
        if (collection == []):
            return (-1)
        elif (page_index < (self.page_count())):
            return (len(self.book[page_index][:]))
        else:
            return (-1)

    def page_index(self, item_index):
        if (self.total_collection != []):
            for i in range((self.page_count())):
                if (item_index in self.book[i][:]):
                    return (i)
        return (-1)


collection = range(1, 25)
helper = PaginationHelper(collection, 10)