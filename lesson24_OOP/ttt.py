warrior = {'здоровье': 100,
           'атака': 30,
           'защита': 25,
           'навыки': {'щит': 10}}
archer = {'здоровье': 50, 'атака': 40, 'защита': 20, 'навыки': {'убежать': 10}, 'инвентарь': ['стрелы', 'меч', 'еда']}
wizard = {'здоровье': 30, 'атака': 50, 'защита': 15, 'навыки': {'магический щит': 10, 'лечение': 5}}


def print_dict(a):
    for i in a:
        print(f"{i}: {a[i]}")

# Не удаляй этот код, он нужен для тестирования
for item in [warrior, archer, wizard]:
    print_dict(item)
