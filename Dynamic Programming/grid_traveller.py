# Say that you are a traveller on a 2D grid.
# You begin in the top-left corner and your goal is to travel to the bottom-right corner.
# You may only move down or right.
# In how many ways can you travel to the goal on a grid with dimensions (m*n)?
import time

memo = {}


def grid_traveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    # grid_traveller(m-1, n) -> moving down && grid_traveller(m, n-1) -> moving right
    if f"{m},{n}" in memo.keys():
        return memo[f"{m},{n}"]
    else:
        memo.update({f"{m},{n}": grid_traveller(m - 1, n) + grid_traveller(m, n - 1)})
        return memo[f"{m},{n}"]


t1 = time.time()
print(grid_traveller(1, 1))  # 1
print(grid_traveller(2, 3))  # 3
print(grid_traveller(3, 2))  # 3
print(grid_traveller(3, 3))  # 6
print(grid_traveller(18, 18))  # 2333606220
t2 = time.time()
print(t2 - t1)
# print(memo)
