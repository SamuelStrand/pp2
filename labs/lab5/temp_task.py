with open('row.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    if 'мл' in line or 'фл' in line:
        print(line.strip())
