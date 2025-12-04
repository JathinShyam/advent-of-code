"""
--- Part Two ---
Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?

Your puzzle answer was 8768.

"""

import copy

with open('input.txt', 'r') as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))
    
    rows, cols = len(grid), len(grid[0])
    result = 0
    while True:
        new_grid = copy.deepcopy(grid)
        for r in range(rows):
            for c in range(cols):
                count = 0
                if grid[r][c] == '.':
                    continue
                if c - 1 >= 0 and grid[r][c-1] == '@':
                    count += 1
                if c + 1 < cols and grid[r][c+1] == '@':
                    count += 1
                if r - 1 >= 0 and grid[r-1][c] == '@':
                    count += 1
                if r + 1 < rows and grid[r+1][c] == '@':
                    count += 1
                if r - 1 >= 0 and c - 1 >= 0 and grid[r-1][c-1] == '@':
                    count += 1
                if r + 1 < rows and c + 1 < cols and grid[r+1][c+1] == '@':
                    count += 1
                if r - 1 >= 0 and c + 1 < cols and grid[r-1][c+1] == '@':
                    count += 1
                if r + 1 < rows and c - 1 >= 0 and grid[r+1][c-1] == '@':
                    count += 1
                if count < 4:
                    result += 1
                    new_grid[r][c] = '.'
        if new_grid == grid:
            break
        grid = new_grid
    print(result)