from tkinter import *
root = Tk()

grid = {}
for i in range(1,10):
    for j in range(1,10):
        grid.update({'r'+str(i)+'c'+str(j) : [1,2,3,4,5,6,7,8,9]})

to_be_checked = []
checked = []
loop_count = 0

boxes = [['r1c1', 'r1c2', 'r1c3', 'r2c1', 'r2c2', 'r2c3', 'r3c1', 'r3c2', 'r3c3'], ['r4c4', 'r4c5', 'r4c6', 'r5c4', 'r5c5', 'r5c6', 'r6c4', 'r6c5', 'r6c6'],
['r7c7', 'r7c8', 'r7c9', 'r8c7', 'r8c8', 'r8c9', 'r9c7', 'r9c8', 'r9c9'], ['r1c4', 'r1c5', 'r1c6', 'r2c4', 'r2c5', 'r2c6', 'r3c4', 'r3c5', 'r3c6'],
['r1c7', 'r1c8', 'r1c9', 'r2c7', 'r2c8', 'r2c9', 'r3c7', 'r3c8', 'r3c9'], ['r4c1', 'r4c2', 'r4c3', 'r5c1', 'r5c2', 'r5c3', 'r6c1', 'r6c2', 'r6c3'],
['r4c7', 'r4c8', 'r4c9', 'r5c7', 'r5c8', 'r5c9', 'r6c7', 'r6c8', 'r6c9'], ['r7c1', 'r7c2', 'r7c3', 'r8c1', 'r8c2', 'r8c3', 'r9c1', 'r9c2', 'r9c3'],
['r7c4', 'r7c5', 'r7c6', 'r8c4', 'r8c5', 'r8c6', 'r9c4', 'r9c5', 'r9c6']]

q = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def insert(string):
    global popup, button_insert_0, button_insert_1, button_insert_2, button_insert_3, button_insert_4, button_insert_5, button_insert_6, button_insert_7, button_insert_8, button_insert_9
    popup = Tk()
    button_insert_0 = Button(popup, text = 'Empty' , command = lambda: user_input(string, 0))
    button_insert_1 = Button(popup, text = 1 , command = lambda: user_input(string, 1))
    button_insert_2 = Button(popup, text = 2 , command = lambda: user_input(string, 2))
    
    button_insert_3 = Button(popup, text = 3 , command = lambda: user_input(string, 3))
    button_insert_4 = Button(popup, text = 4 , command = lambda: user_input(string, 4))
    button_insert_5 = Button(popup, text = 5 , command = lambda: user_input(string, 5))
    button_insert_6 = Button(popup, text = 6 , command = lambda: user_input(string, 6))
    button_insert_7 = Button(popup, text = 7 , command = lambda: user_input(string, 7))
    button_insert_8 = Button(popup, text = 8 , command = lambda: user_input(string, 8))
    button_insert_9 = Button(popup, text = 9 , command = lambda: user_input(string, 9))

    button_insert_0.grid(row = 0, columnspan = 3)
    button_insert_1.grid(row = 1, columnspan = 3)
    button_insert_2.grid(row = 2, columnspan = 3)
    button_insert_3.grid(row = 3, columnspan = 3)
    button_insert_4.grid(row = 4, columnspan = 3)
    button_insert_5.grid(row = 5, columnspan = 3)
    button_insert_6.grid(row = 6, columnspan = 3)
    button_insert_7.grid(row = 7, columnspan = 3)
    button_insert_8.grid(row = 8, columnspan = 3)
    button_insert_9.grid(row = 9, columnspan = 3)
       
def user_input(x, num):
    x = str(x)
    exec('button' + str(x) + '.config(text = ' + "'" + str(num) + "')")
    q[int(x[0])-1][int(x[1])-1] = int(num)
    for i in [button_insert_0, button_insert_1, button_insert_2, button_insert_3, button_insert_4, button_insert_5, button_insert_6, button_insert_7, button_insert_8, button_insert_9,popup]:
        i.destroy()
    return;
       
def makegrid():
    global button_2, button11, button12, button13, button14, button15, button16, button17, button18, button19, button21, button22, button23, button24, button25, button26, button27, button28, button29, button31, button32, button33, button34, button35, button36, button37, button38, button39, button41, button42, button43, button44, button45, button46, button47, button48, button49, button51, button52, button53, button54, button55, button56, button57, button58, button59, button61, button62, button63, button64, button65, button66, button67, button68, button69, button71, button72, button73, button74, button75, button76, button77, button78, button79, button81, button82, button83, button84, button85, button86, button87, button88, button89, button91, button92, button93, button94, button95, button96, button97, button98, button99
    button11 = Button(root, text = "-", command = lambda : insert(11), width = 2, height = 1)
    button11.grid(row = 1, column = 1)
    button12 = Button(root, text = "-", command = lambda : insert(12), width = 2, height = 1)
    button12.grid(row = 1, column = 2)
    button13 = Button(root, text = "-", command = lambda : insert(13), width = 2, height = 1)
    button13.grid(row = 1, column = 3)
    button14 = Button(root, text = "-", command = lambda : insert(14), width = 2, height = 1)
    button14.grid(row = 1, column = 4)
    button15 = Button(root, text = "-", command = lambda : insert(15), width = 2, height = 1)
    button15.grid(row = 1, column = 5)
    button16 = Button(root, text = "-", command = lambda : insert(16), width = 2, height = 1)
    button16.grid(row = 1, column = 6)
    button17 = Button(root, text = "-", command = lambda : insert(17), width = 2, height = 1)
    button17.grid(row = 1, column = 7)
    button18 = Button(root, text = "-", command = lambda : insert(18), width = 2, height = 1)
    button18.grid(row = 1, column = 8)
    button19 = Button(root, text = "-", command = lambda : insert(19), width = 2, height = 1)
    button19.grid(row = 1, column = 9)
    button21 = Button(root, text = "-", command = lambda : insert(21), width = 2, height = 1)
    button21.grid(row = 2, column = 1)
    button22 = Button(root, text = "-", command = lambda : insert(22), width = 2, height = 1)
    button22.grid(row = 2, column = 2)
    button23 = Button(root, text = "-", command = lambda : insert(23), width = 2, height = 1)
    button23.grid(row = 2, column = 3)
    button24 = Button(root, text = "-", command = lambda : insert(24), width = 2, height = 1)
    button24.grid(row = 2, column = 4)
    button25 = Button(root, text = "-", command = lambda : insert(25), width = 2, height = 1)
    button25.grid(row = 2, column = 5)
    button26 = Button(root, text = "-", command = lambda : insert(26), width = 2, height = 1)
    button26.grid(row = 2, column = 6)
    button27 = Button(root, text = "-", command = lambda : insert(27), width = 2, height = 1)
    button27.grid(row = 2, column = 7)
    button28 = Button(root, text = "-", command = lambda : insert(28), width = 2, height = 1)
    button28.grid(row = 2, column = 8)
    button29 = Button(root, text = "-", command = lambda : insert(29), width = 2, height = 1)
    button29.grid(row = 2, column = 9)
    button31 = Button(root, text = "-", command = lambda : insert(31), width = 2, height = 1)
    button31.grid(row = 3, column = 1)
    button32 = Button(root, text = "-", command = lambda : insert(32), width = 2, height = 1)
    button32.grid(row = 3, column = 2)
    button33 = Button(root, text = "-", command = lambda : insert(33), width = 2, height = 1)
    button33.grid(row = 3, column = 3)
    button34 = Button(root, text = "-", command = lambda : insert(34), width = 2, height = 1)
    button34.grid(row = 3, column = 4)
    button35 = Button(root, text = "-", command = lambda : insert(35), width = 2, height = 1)
    button35.grid(row = 3, column = 5)
    button36 = Button(root, text = "-", command = lambda : insert(36), width = 2, height = 1)
    button36.grid(row = 3, column = 6)
    button37 = Button(root, text = "-", command = lambda : insert(37), width = 2, height = 1)
    button37.grid(row = 3, column = 7)
    button38 = Button(root, text = "-", command = lambda : insert(38), width = 2, height = 1)
    button38.grid(row = 3, column = 8)
    button39 = Button(root, text = "-", command = lambda : insert(39), width = 2, height = 1)
    button39.grid(row = 3, column = 9)
    button41 = Button(root, text = "-", command = lambda : insert(41), width = 2, height = 1)
    button41.grid(row = 4, column = 1)
    button42 = Button(root, text = "-", command = lambda : insert(42), width = 2, height = 1)
    button42.grid(row = 4, column = 2)
    button43 = Button(root, text = "-", command = lambda : insert(43), width = 2, height = 1)
    button43.grid(row = 4, column = 3)
    button44 = Button(root, text = "-", command = lambda : insert(44), width = 2, height = 1)
    button44.grid(row = 4, column = 4)
    button45 = Button(root, text = "-", command = lambda : insert(45), width = 2, height = 1)
    button45.grid(row = 4, column = 5)
    button46 = Button(root, text = "-", command = lambda : insert(46), width = 2, height = 1)
    button46.grid(row = 4, column = 6)
    button47 = Button(root, text = "-", command = lambda : insert(47), width = 2, height = 1)
    button47.grid(row = 4, column = 7)
    button48 = Button(root, text = "-", command = lambda : insert(48), width = 2, height = 1)
    button48.grid(row = 4, column = 8)
    button49 = Button(root, text = "-", command = lambda : insert(49), width = 2, height = 1)
    button49.grid(row = 4, column = 9)
    button51 = Button(root, text = "-", command = lambda : insert(51), width = 2, height = 1)
    button51.grid(row = 5, column = 1)
    button52 = Button(root, text = "-", command = lambda : insert(52), width = 2, height = 1)
    button52.grid(row = 5, column = 2)
    button53 = Button(root, text = "-", command = lambda : insert(53), width = 2, height = 1)
    button53.grid(row = 5, column = 3)
    button54 = Button(root, text = "-", command = lambda : insert(54), width = 2, height = 1)
    button54.grid(row = 5, column = 4)
    button55 = Button(root, text = "-", command = lambda : insert(55), width = 2, height = 1)
    button55.grid(row = 5, column = 5)
    button56 = Button(root, text = "-", command = lambda : insert(56), width = 2, height = 1)
    button56.grid(row = 5, column = 6)
    button57 = Button(root, text = "-", command = lambda : insert(57), width = 2, height = 1)
    button57.grid(row = 5, column = 7)
    button58 = Button(root, text = "-", command = lambda : insert(58), width = 2, height = 1)
    button58.grid(row = 5, column = 8)
    button59 = Button(root, text = "-", command = lambda : insert(59), width = 2, height = 1)
    button59.grid(row = 5, column = 9)
    button61 = Button(root, text = "-", command = lambda : insert(61), width = 2, height = 1)
    button61.grid(row = 6, column = 1)
    button62 = Button(root, text = "-", command = lambda : insert(62), width = 2, height = 1)
    button62.grid(row = 6, column = 2)
    button63 = Button(root, text = "-", command = lambda : insert(63), width = 2, height = 1)
    button63.grid(row = 6, column = 3)
    button64 = Button(root, text = "-", command = lambda : insert(64), width = 2, height = 1)
    button64.grid(row = 6, column = 4)
    button65 = Button(root, text = "-", command = lambda : insert(65), width = 2, height = 1)
    button65.grid(row = 6, column = 5)
    button66 = Button(root, text = "-", command = lambda : insert(66), width = 2, height = 1)
    button66.grid(row = 6, column = 6)
    button67 = Button(root, text = "-", command = lambda : insert(67), width = 2, height = 1)
    button67.grid(row = 6, column = 7)
    button68 = Button(root, text = "-", command = lambda : insert(68), width = 2, height = 1)
    button68.grid(row = 6, column = 8)
    button69 = Button(root, text = "-", command = lambda : insert(69), width = 2, height = 1)
    button69.grid(row = 6, column = 9)
    button71 = Button(root, text = "-", command = lambda : insert(71), width = 2, height = 1)
    button71.grid(row = 7, column = 1)
    button72 = Button(root, text = "-", command = lambda : insert(72), width = 2, height = 1)
    button72.grid(row = 7, column = 2)
    button73 = Button(root, text = "-", command = lambda : insert(73), width = 2, height = 1)
    button73.grid(row = 7, column = 3)
    button74 = Button(root, text = "-", command = lambda : insert(74), width = 2, height = 1)
    button74.grid(row = 7, column = 4)
    button75 = Button(root, text = "-", command = lambda : insert(75), width = 2, height = 1)
    button75.grid(row = 7, column = 5)
    button76 = Button(root, text = "-", command = lambda : insert(76), width = 2, height = 1)
    button76.grid(row = 7, column = 6)
    button77 = Button(root, text = "-", command = lambda : insert(77), width = 2, height = 1)
    button77.grid(row = 7, column = 7)
    button78 = Button(root, text = "-", command = lambda : insert(78), width = 2, height = 1)
    button78.grid(row = 7, column = 8)
    button79 = Button(root, text = "-", command = lambda : insert(79), width = 2, height = 1)
    button79.grid(row = 7, column = 9)
    button81 = Button(root, text = "-", command = lambda : insert(81), width = 2, height = 1)
    button81.grid(row = 8, column = 1)
    button82 = Button(root, text = "-", command = lambda : insert(82), width = 2, height = 1)
    button82.grid(row = 8, column = 2)
    button83 = Button(root, text = "-", command = lambda : insert(83), width = 2, height = 1)
    button83.grid(row = 8, column = 3)
    button84 = Button(root, text = "-", command = lambda : insert(84), width = 2, height = 1)
    button84.grid(row = 8, column = 4)
    button85 = Button(root, text = "-", command = lambda : insert(85), width = 2, height = 1)
    button85.grid(row = 8, column = 5)
    button86 = Button(root, text = "-", command = lambda : insert(86), width = 2, height = 1)
    button86.grid(row = 8, column = 6)
    button87 = Button(root, text = "-", command = lambda : insert(87), width = 2, height = 1)
    button87.grid(row = 8, column = 7)
    button88 = Button(root, text = "-", command = lambda : insert(88), width = 2, height = 1)
    button88.grid(row = 8, column = 8)
    button89 = Button(root, text = "-", command = lambda : insert(89), width = 2, height = 1)
    button89.grid(row = 8, column = 9)
    button91 = Button(root, text = "-", command = lambda : insert(91), width = 2, height = 1)
    button91.grid(row = 9, column = 1)
    button92 = Button(root, text = "-", command = lambda : insert(92), width = 2, height = 1)
    button92.grid(row = 9, column = 2)
    button93 = Button(root, text = "-", command = lambda : insert(93), width = 2, height = 1)
    button93.grid(row = 9, column = 3)
    button94 = Button(root, text = "-", command = lambda : insert(94), width = 2, height = 1)
    button94.grid(row = 9, column = 4)
    button95 = Button(root, text = "-", command = lambda : insert(95), width = 2, height = 1)
    button95.grid(row = 9, column = 5)
    button96 = Button(root, text = "-", command = lambda : insert(96), width = 2, height = 1)
    button96.grid(row = 9, column = 6)
    button97 = Button(root, text = "-", command = lambda : insert(97), width = 2, height = 1)
    button97.grid(row = 9, column = 7)
    button98 = Button(root, text = "-", command = lambda : insert(98), width = 2, height = 1)
    button98.grid(row = 9, column = 8)
    button99 = Button(root, text = "-", command = lambda : insert(99), width = 2, height = 1)
    button99.grid(row = 9, column = 9)


    button_2 = Button(root, text = 'Submit', command = lambda : algorithm()     )
    button_2.grid(row = 10,column = 3, columnspan = 5)


def count():
    x = 0
    for i in grid.keys():
        if type(grid[i]) == int:
            x += 1
    return x;


def algorithm():
    
    global grid, checked, loop_count

    for row in range(1,10):  
        for column in range(1, 10):
            if q[row-1][column-1]:
                    val = q[row-1][column-1]
                    grid.update({'r'+str(row)+'c'+str(column): val})
                    to_be_checked.append('r'+str(row)+'c'+str(column))
    run = 0
    loop_count = 0
    remove_possibilities()
    
        
def remove_possibilities():
    while len(to_be_checked) > 0:
        element = str(to_be_checked[0])

        row = int(element[1])
        column = int(element[3])
        val = grid[element]
        checked.append(element)
        to_be_checked.remove(element)

        for i in grid.keys():#row
            if str(i)[1] == str(row):
                if (type(grid[i]) == list) and (val in grid[i]):
                    if len(grid[i]) == 1:
                        grid[i] = int(grid[i][0])
                        to_be_checked.append(str(i))
                    else:
                        grid[i].remove(val)

                    
        for i in grid.keys():#column
            if (type(grid[i]) == list) and (str(i)[3] == str(column)):
                if val in grid[i]:
                    if len(grid[i]) == 1:
                        grid[i] = int(grid[i][0])
                        to_be_checked.append(str(i))
                    else:
                        grid[i].remove(val)


        for i in grid.keys():#box
            if type(grid[i]) == list:
                if ( ( int(str(i)[1])-1 ) //3 == (row-1)//3) and ( ( int(str(i)[3]) -1) //3 == (column-1)//3):
                    if val in grid[i]:
                        if len(grid[i]) == 1:
                            grid[i] = int(grid[i][0])
                            to_be_checked.append(str(i))                            
                        else:
                            grid[i].remove(val)                       
        for i in grid.keys():
            if type(grid[i]) == list and len(grid[i]) == 1:
                grid[i] = int(grid[i][0])

                to_be_checked.append(str(i))
    assign()





def assign(): #check for unique elements
    global loop_count
    #rows
    for row in range(1,10):
        posib = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

        for col in range(1,10):
            element = 'r'+str(row)+'c'+str(col)
            if type(grid[element]) == list:
                for i in grid[element]:
                    posib[i].append(element) 
            else:
                posib[grid[element]].append(element)
                
        for x in posib.keys():
            if len(posib[x]) == 1:
                if type(grid[str(posib[x][0])]) == list:
                    grid[str(posib[x][0])] = x
                    to_be_checked.append(str(posib[x][0]))

    #columns
    for col in range(1,10):
        posib = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

        for row in range(1,10):
            element = 'r'+str(row)+'c'+str(col)
            if type(grid[element]) == list:
                for i in grid[element]:
                    posib[i].append(element)
            else:
                posib[grid[element]].append(element)

        for x in posib.keys():
            if len(posib[x]) == 1:
                if type(grid[str(posib[x][0])]) == list:
                    grid[str(posib[x][0])] = x
                    to_be_checked.append(str(posib[x][0]))

    #boxes
    for box in boxes:
        posib = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

        for cell in box:
            element = cell
            if type(grid[element]) == list:
                for i in grid[element]:
                    posib[i].append(element)
            else:
                posib[grid[element]].append(element)

        for x in posib.keys():
            if len(posib[x]) == 1:
                if type(grid[str(posib[x][0])]):
                    grid[str(posib[x][0])] = x
                    to_be_checked.append(str(posib[x][0]))

    loop_count += 1

    if loop_count == 15:
        display()
    else:
        remove_possibilities()

      
def display():
    popup2()
    list_buttons = ['button11', 'button12', 'button13', 'button14', 'button15', 'button16', 'button17', 'button18', 'button19', 'button21', 'button22', 'button23', 'button24', 'button25', 'button26', 'button27', 'button28', 'button29', 'button31', 'button32', 'button33', 'button34', 'button35', 'button36', 'button37', 'button38', 'button39', 'button41', 'button42', 'button43', 'button44', 'button45', 'button46', 'button47', 'button48', 'button49', 'button51', 'button52', 'button53', 'button54', 'button55', 'button56', 'button57', 'button58', 'button59', 'button61', 'button62', 'button63', 'button64', 'button65', 'button66', 'button67', 'button68', 'button69', 'button71', 'button72', 'button73', 'button74', 'button75', 'button76', 'button77', 'button78', 'button79', 'button81', 'button82', 'button83', 'button84', 'button85', 'button86', 'button87', 'button88', 'button89', 'button91', 'button92', 'button93', 'button94', 'button95', 'button96', 'button97', 'button98', 'button99']
    for button in list_buttons:
        if q[int(button[-2])-1][int(button[-1])-1] == 0 :
             enter = grid['r'+button[6]+'c'+ button[7]]
             if enter in [1,2,3,4,5,6,7,8,9]:
                exec(button+'.configure(text = ' + str(enter) + ', bg = \'yellow\' )')


def popup2():
    global t
    pop2 = Tk()
    t = "Your Sudoku puzzle has been solved!"
    for i in grid.keys():
        if type(grid[i]) != int or grid[i] == 0:
            t = "Insufficient data!"  
            break

    button_3 = Button(pop2, text = 'OK', command = lambda: pop2.destroy())
    
    label1 = Label(pop2, text = t)
    label1.grid(row = 0, padx = 20 , pady = 20)
    button_3.grid(row = 1, padx = 20, pady = 20)
            
makegrid()
