# 1

warehouse = {
    "Olma": {"narx": 12000, "soni": 50},
    "Banan": {"narx": 18000, "soni": 30},
    "Uzum": {"narx": 15000, "soni": 40},
}

max_price_product = None
total_count = 0

for name, product in warehouse.items():
    total_count += product["soni"]
    if max_price_product is None:
        max_price_product = (name, product,)
    elif product["narx"] > max_price_product[1]["narx"]:
        max_price_product = (name, product,)

print(max_price_product[0], max_price_product[1])
print(total_count)


# purchases = {
#     "Ali": [("Olma", 30, 12000), ("Banan", 2, 18000)],
#     "Vali": [("Uzum", 5, 15000), ("Olma", 2, 12000)],
#     "Gani": [("Uzum", 500, 15000), ("Olma", 2, 12000)],
# }

# max_client = None
# for client, orders in purchases.items():
#     if max_client is None:
#         max_client = (client, orders,)
#     else:
#         total_price = 0
#         for order in orders:
#             total_price += order[1] * order[2]

#         max_total_price = 0
#         for order in max_client[1]:
#             max_total_price += order[1] * order[2]

#         if total_price > max_total_price:
#             max_client = (client, orders)

# print(max_client)


#3
# students = {
#     "Aziz": {"Matematika": 4, "Fizika": 5, "Ingliz tili": 3},
#     "Bekzod": {"Matematika": 5, "Fizika": 4, "Ingliz tili": 5},
#     "Gulnoza": {"Matematika": 3, "Fizika": 4, "Ingliz tili": 4},
# }

# best_student = ""
# highest_avg = 0

# for name, subjects in students.items():
#     total = sum(subjects.values())
#     print(total)
#     avg = total / len(subjects)
#     if avg > highest_avg:
#         highest_avg = avg
#         best_student = name

# print(f"Eng yaxshi talaba: {best_student}, O‘rtacha bahosi: {highest_avg}")


# students = {
#     "Aziz": {"Matematika": 4, "Fizika": 5, "Ingliz tili": 3},
#     "Bekzod": {"Matematika": 5, "Fizika": 4, "Ingliz tili": 5},
#     "Gulnoza": {"Matematika": 3, "Fizika": 4, "Ingliz tili": 4},
# }

# for name, subject in students.items():
#     for key, values in subject.items():
#         pass
#     print(subject.values())
#     print(max(subject.values()))