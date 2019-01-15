
from classes.game import Person, bcolors

magic =[{'name': 'AKM', 'cost': 10, 'dmg': 60},
        {'name': 'SCARL', 'cost': 10, 'dmg': 60},
        {'name': 'Thompson', 'cost': 10, 'dmg': 60}]

player = Person(460, 65, 60, 34, magic)

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))