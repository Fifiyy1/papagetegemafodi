def divider(a, b):
   try:
       return a / b
   except ZeroDivisionError:
       print("делить на 0 нелзя, математика 2 класс !;№!;%")
       return 0
   except TypeError:
       print("делить на такие чтуки незя , я тупой просто кампутер ххывыхвъы")
       return 0
   except ValueError:
       print("Это чо, не цыфра? ay kent rid it im stupid")
       return 0
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
result = []
for key in data:
   res = divider(key, data[key])
   result.append(res)
print(result)