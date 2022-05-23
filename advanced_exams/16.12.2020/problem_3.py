def get_magic_triangle(number: int):
    triangle = [[1], [1, 1]]
    triangle.extend([[1] * x for x in range(3, number+1)])
    for row in range(2, number):
        for col in range(1, len(triangle[row]) - 1):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    return triangle


print(get_magic_triangle(5))
