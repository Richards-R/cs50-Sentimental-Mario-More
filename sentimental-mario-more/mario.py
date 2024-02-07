from cs50 import get_int

height = 0
blocks = 1

while height < 1 or height > 8:
    height = get_int('Height: ')

spaces = height - 1

for n in range(height):
    block_group = '#' * blocks
    space_group = ' ' * spaces
    pyramid = block_group + '  ' + block_group
    print(space_group + pyramid)
    blocks += 1
    spaces -= 1
