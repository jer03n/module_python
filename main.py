# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_maker1 = 'Gullit'
goal_maker2 = 'Van Basten'

goal_0 = '32'
goal_1 = '54'

scorers = goal_maker1 + " " + goal_0,  goal_maker2 + " " + goal_1

print(scorers)

report = f'{goal_maker1} scored in the {goal_0}nd minute\n \n{goal_maker2} scored in the {goal_1}th minute'

print(report)

player = 'Ronald Koeman'
first_name = player[:player.find(" ")]
print(first_name)

last_name_with_space = player[player.find(" "):]
last_name = last_name_with_space.replace(" ","")
print(last_name)
last_name_len = len(last_name)
print(last_name_len)

name_short = f'{first_name[:1]}. {last_name}' 
print(name_short)

chant = f'{first_name}!' ' '* last_name_len

good_chant = chant
print(chant)
print(good_chant != ' ')





