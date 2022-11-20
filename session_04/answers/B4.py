# B4 - The modern olympics started in 1896, print the years they have been held

for olympic_year in range(1896, 2022, 4):
    print(olympic_year)

# Bonus: skip the years it has not been 1916, 1940, 1944, 2020

not_held = [1916, 1940, 1944, 2020]

for olympic_year in range(1896, 2022, 4):
    if olympic_year not in not_held:
        print(olympic_year)