def find_outlier(integers):
    odds = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]
print(find_outlier([1,3,5,6,7]))