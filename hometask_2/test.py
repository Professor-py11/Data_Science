limit = 100

# Створюємо словник для зберігання кількості входжень кожного добутку x * y до їх розмови.
allowable_products_before = {} 
for x in range(2, limit): 
    for y in range(x + 1, limit - x): 
        product = x * y
        # Якщо цей добуток ще не був зустрінутий, додаємо його до словника.
        if product not in allowable_products_before: 
            allowable_products_before[product] = 1 
        # Якщо цей добуток вже був, збільшуємо кількість його входжень.
        else:
            allowable_products_before[product] += 1

# Створюємо словник для зберігання заборонених сум x + y, коли P говорить "Я не знаю".
not_allowed_say_p = {}  
for x in range(2, limit): 
    for y in range(x + 1, limit - x): 
        product = x * y
        # Якщо кількість входжень цього добутку дорівнює 1, то сума x + y недопустима.
        if allowable_products_before[product] == 1 :
            not_allowed_say_p[x + y] = 1  

# Створюємо словник для зберігання кількості входжень кожного добутку x * (n - x),
# де n є сумою x і y, яка не була відмічена як недопустима.
allowable_products_after_p = {} 
for n in range(2, limit):
    if n not in not_allowed_say_p:
       for x in range(2, n // 2 + 1):
            product = x * (n - x)
            # Якщо цей добуток входить до списку розмови та має більше одного входження,
            # додаємо його до словника.
            if product in allowable_products_before and allowable_products_before[product] > 1:
               if product in allowable_products_after_p:
                   allowable_products_after_p[product] += 1
               else:
                   allowable_products_after_p[product] = 1 

# Створюємо словник для зберігання кількості входжень суми x + y,
# яка може бути поділена на x і (n - x), коли S говорить "Я не знаю".
allowable_say_s = {}  
for n in range(2, limit):
    if n not in not_allowed_say_p:
       for x in range(2, n // 2 + 1):
           product = x * (n - x)
           # Якщо цей добуток входить до списку розмови та має тільки одне входження,
           # додаємо його до словника.
           if product in allowable_products_after_p and allowable_products_after_p[product] == 1:
               if n in allowable_say_s:
                   allowable_say_s[n] += 1
               else:
                   allowable_say_s[n] = 1

# Виводимо результати, де кількість входжень суми n дорівнює 1.
for n in allowable_say_s: 
    if allowable_say_s[n] == 1:
        for x in range(2, n // 2 + 1):
            product = x * (n - x)
            # Якщо цей добуток входить до списку розмови та має тільки одне входження,
            # виводимо його разом з значеннями x та (n - x).
            if product in allowable_products_after_p and allowable_products_after_p[product] == 1:
                print('(Сума, Добуток) = (%d, %d), (x, y) = (%d, %d)' % (n, product, x, n - x))