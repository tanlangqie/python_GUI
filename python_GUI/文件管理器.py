from tkinter import *
import os
import xlrd
from tkinter import ttk
import tkinter as tk  # 使用Tkinter前需要先导入

window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('800x500')  # 这里的乘是小x
#
# frame = tk.Frame(window)
# frame.pack(fill='both', expand='false')
tree = ttk.Treeview(window, columns=['name', 'price','sss'], show='headings')

tree.heading('name', text='name')
tree.heading('price', text='price')
tree.heading('sss', text='sss')

def openxlsx():

    fname = r'表格.xlsx'
    bk = xlrd.open_workbook(fname)

    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print ("no sheet in %s named Sheet1" % fname)
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print ("nrows %d, ncols %d" % (nrows, ncols))
    # 获取第一行第一列数据
    cell_value = sh.cell_value(1, 1)
    # print cell_value

    row_list = []
    # 获取各行数据
    for i in range(0, nrows):
        row_data = sh.row_values(i)
        #print(row_data)
        # t.insert('end',row_data)
        # t.insert('end', '\n')
        tree.insert('', 'end', values=row_data )
        row_list.append(row_data)
    print('111111111111')

button = Button(text='打开文件',command=openxlsx)
button.pack()

#定义一个多行文本区域
# t = tk.Text(window, height=8)
# t.pack()

#定义一个表格窗体

tree.pack()

tree.mainloop()

# fname = r'E:\pypractice\ML_learn\other\data\调参过程.xlsx'
# bk = xlrd.open_workbook(fname)
# shxrange = range(bk.nsheets)
# try:
#     sh = bk.sheet_by_name("Sheet1")
# except:
#     print ("no sheet in %s named Sheet1" % fname)
# # 获取行数
# nrows = sh.nrows
# # 获取列数
# ncols = sh.ncols
# print ("nrows %d, ncols %d" % (nrows, ncols))
# # 获取第一行第一列数据
# cell_value = sh.cell_value(3, 3)
# print (cell_value)
# print (type(cell_value))
#
# row_list = []
# # 获取各行数据
# for i in range(1, nrows):
#     row_data = sh.row_values(i)
#     # print(row_data)
#     # t.insert('end', row_data)
#     # t.insert('end', '\n')
#     row_list.append(row_data)

