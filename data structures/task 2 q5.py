grid = [["x" for i in range(0, 4)] for x in range(0, 6)]

row = int(input("enter new row value"))
column = int(input("enter new column value"))
grid[row-1][column-1] = "O"
print(grid)

