# Настройки игрового поля
WIDTH = 10  # Ширина игрового поля (в блоках)
HEIGHT = 20  # Высота игрового поля (в блоках)
BLOCK_SIZE = 30  # Размер одного блока (в пикселях)

# Скорость игры
FPS = 60

# Фигуры (Тетромино)
TETRIMINOES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Цвета для фигур
COLORS = [
    (0, 255, 255),  # I - голубой
    (255, 255, 0),  # O - желтый
    (128, 0, 128),  # T - фиолетовый
    (255, 165, 0),  # L - оранжевый
    (0, 0, 255),    # J - синий
    (0, 255, 0),    # S - зеленый
    (255, 0, 0)     # Z - красный
]
