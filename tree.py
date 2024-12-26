def draw_christmas_tree(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

    base = ' ' * (height - 1) + '|'
    print(base)

tree_height = int(input("Digite a altura da árvore: "))
draw_christmas_tree(tree_height)