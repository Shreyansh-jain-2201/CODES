sudoku = []
i = 0
while True:
    try:
        line = input()
        i +=1
    except EOFError:
        break
    sudoku.append(line)
    if (i == 9):
        break
temp = sudoku
sudoku = []
for i in temp:
    for j in i:
        if(j == '.'):
            sudoku.append(0)
        elif(j.isdigit()):
            sudoku.append(int(j))

temp = sudoku
k = 0
sudoku = []
for i in range(9):
    list1 = []
    for j in range(9):
        list1.append(temp[k])
        k+=1
    sudoku.append(list1)
rows = sudoku
columns = [[0 for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        columns[j][i] = rows[i][j]

boxes = []
for i in range(0,9,3):
    for j in range(0,9,3):
        box = []
        for k in range(i,i+3):
            for l in range(j,j+3):
                box.append(rows[k][l])
        boxes.append(box)
isValid = True
for i in range(9):
    row = []
    column = []
    box = []
    for j in range(9):
        if(rows[i][j] != 0):
            row.append(rows[i][j])
        if(columns[i][j] != 0):
            column.append(columns[i][j])
        if(boxes[i][j] != 0):
            box.append(boxes[i][j])
    if(len(row) != len(set(row))):
        print("Rows", row, i, j, len(row), len(set(row)))
        isValid = False
    if(len(column) != len(set(column))):
        print("Columns", column, i, j, len(column), len(set(column)))
        isValid = False
    if(len(box) != len(set(box))):
        print("Boxes", box, i, j, len(box), len(set(box)))
        isValid = False

if(isValid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
print("Rows: ")
for i in rows:
    print(i)
print("Columns: ")
for i in columns:
    print(i)
print("Boxes: ")
for i in boxes:
    print(i)


# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# [[".",".",".",".","5",".",".","1","."]
#  ,[".","4",".","3",".",".",".",".","."]
#  ,[".",".",".",".",".","3",".",".","1"]
#  ,["8",".",".",".",".",".",".","2","."]
#  ,[".",".","2",".","7",".",".",".","."]
#  ,[".","1","5",".",".",".",".",".","."]
#  ,[".",".",".",".",".","2",".",".","."]
#  ,[".","2",".","9",".",".",".",".","."]
#  ,[".",".","4",".",".",".",".",".","."]]