boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    for i in range(len(boys)):
        print(boys[i], 'и', girls[i])
else:
    print('Внимание, кто-то может остаться без пары.')