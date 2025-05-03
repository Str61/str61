magnit = {'молоко','соль','сахар'}
paterochka = {'мясо','молоко','сыр'}

if magnit not in paterochka:
    products_paterochka = magnit - paterochka
    print("Данные товары отсутствуют в пятёрочке,но есть в магните",products_paterochka)

if paterochka not in magnit:
    products_magnit = paterochka - magnit
    print("Данные товары отсутствуют в магните,но есть в пятёрочке", products_magnit)

products_all = magnit|paterochka
print("Полный перечень всех товаров из двух магазинов" , products_all)

if len(magnit) == len(paterochka):
    print("Перечни товаров равны")
elif len(magnit) != len(paterochka):
    print("Перечни товаров не равны")
