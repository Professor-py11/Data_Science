"""The Two Wise Men Problem

Two wise men, Sage P and Sage S, are given two different natural numbers x and y, where 1<x,y<100.

Sage P is told the product P=x⋅y, while Sage S is told the sum S=x+y. Neither of them knows the actual values of x and y.

The following conversation takes place:

Sage P: "I don't know what the numbers are."

Sage S: "I knew that already."

Sage P: "Oh, now I know the numbers!"

Sage S: "And now I do too!"

What are the numbers x and y?"""


limit = 100

# Створюємо словник для зберігання кількості входжень кожного добутку x * y до їх розмови.
product_counts = {}
for x in range(2, limit):
    for y in range(x + 1, limit - x):
        product = x * y
        product_counts[product] = product_counts.get(product, 0) + 1 

# Створюємо словник для зберігання заборонених сум x + y, коли P говорить "Я не знаю".
not_allowed_sums = {}  
for x in range(2, limit): 
    for y in range(x + 1, limit - x): 
        product = x * y
        # Якщо кількість входжень цього добутку дорівнює 1, то сума x + y недопустима.
        if product_counts[product] == 1 :
            not_allowed_sums[x + y] = 1 

# Підрахунок кількості появ добутків після виключення заборонених сум
valid_product_counts = {}
for n in range(2, limit):
    if n not in not_allowed_sums:
        for x in range(2, n // 2 + 1):
            product = x * (n - x)
            if product in product_counts and product_counts[product] > 1:
                valid_product_counts[product] = valid_product_counts.get(product, 0) + 1

# Визначаємо допустимі суми після другого висловлювання
valid_sums = {}
for n in range(2, limit):
    if n not in not_allowed_sums:
        for x in range(2, n // 2 + 1):
            product = x * (n - x)
            if valid_product_counts.get(product, 0) == 1:
                valid_sums[n] = valid_sums.get(n, 0) + 1

# Виводимо пари (сума, добуток) та відповідні значення x, y
for n, count in valid_sums.items():
    if count == 1:
        for x in range(2, n // 2 + 1):
            product = x * (n - x)
            if valid_product_counts.get(product, 0) == 1:
                print(f'(Сума, Добуток) = ({n}, {product}), (x, y) = ({x}, {n - x})')