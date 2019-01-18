from useful_functions import is_prime

cubes = [x**3 for x in range(1, int(1000000000 ** (1/3)) + 1)]

print(cubes)

number_cubes = len(cubes)

prime_cubs_diffs = []

for i in range(number_cubes):
    for j in range(i, number_cubes):
        cube_diff = cubes[j] - cubes[i]
        if is_prime(cube_diff):
            if cube_diff < 1000000:
                prime_cubs_diffs.append(cube_diff)
            print(cubes[i], cubes[j], cube_diff)

print(prime_cubs_diffs, len(prime_cubs_diffs))