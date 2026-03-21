#Hardcoded Solution
cell = 4
hline = "+ " + ("- " * cell) + "+ " + ("- " * cell) + "+"
vline = "| " + ("  " * cell) + "| " + ("  " * cell) + "|"

print(hline)
for _ in range(cell):
    print(vline)
print(hline)
for _ in range(cell):
    print(vline)
print(hline)

#Solution with user input
n_rows = int(input("Rows: "))
n_cols = int(input("Cols: "))
cell_size = int(input("Cell size: "))

hline = ("+".ljust(cell_size*2+2, "-") + " ") * n_cols + "+"
vline = ("|" + " " * (cell_size*2+1) + " ") * n_cols + "|"

for r in range(n_rows):
    print(hline)
    for _ in range(cell_size):
        print(vline)
print(hline)