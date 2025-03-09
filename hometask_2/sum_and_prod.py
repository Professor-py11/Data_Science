# """The Two Wise Men Problem
# Two wise men, Sage P and Sage S, are given two different natural numbers x and y, where 1<x,y<100.
# Sage P is told the product P=x⋅y, while Sage S is told the sum S=x+y. Neither of them knows the actual values of x and y.
# The following conversation takes place:
# Sage P: "I don't know what the numbers are."
# Sage S: "I knew that already."
# Sage P: "Oh, now I know the numbers!"
# Sage S: "And now I do too!"
# What are the numbers x and y?"""

limit = 100

# Створюємо словник для зберігання кількості входжень кожного добутку x * y.
product_counts = {}
for x in range(2, limit):
    for y in range(x + 1, limit - x):
        product = x * y
        product_counts[product] = product_counts.get(product, 0) + 1 

# Множина для заборонених сум (коли P не знає x та y)
not_allowed_sums = set()
for x in range(2, limit): 
    for y in range(x + 1, limit - x): 
        if product_counts[x * y] == 1:
            not_allowed_sums.add(x + y) 

# Підрахунок валідних добутків після виключення заборонених сум
valid_product_counts = {}
for n in range(2, limit):
    if n not in not_allowed_sums:
        for x in range(2, n // 2 + 1):
            product = x * (n - x)
            if product_counts.get(product, 0) > 1:
                valid_product_counts[product] = valid_product_counts.get(product, 0) + 1

# Визначаємо допустимі суми після другого висловлювання
valid_sums = set()
for n in range(2, limit):
    if n not in not_allowed_sums:
        unique_product = None
        for x in range(2, n // 2 + 1):
            product = x * (n - x)
            if valid_product_counts.get(product, 0) == 1:
                if unique_product is not None:
                    unique_product = None
                    break
                unique_product = product
        if unique_product is not None:
            valid_sums.add(n)

# Виводимо пари (сума, добуток) та відповідні значення x, y
for n in valid_sums:
    for x in range(2, n // 2 + 1):
        product = x * (n - x)
        if valid_product_counts.get(product, 0) == 1:
            print(f'(x, y) = ({x}, {n - x}) \n(Сума, Добуток) = ({n}, {product})')
