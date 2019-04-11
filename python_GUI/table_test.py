import tkinter
from  tkinter import ttk  # 导入内部包

win = tkinter.Tk()
win.title('My Window')
# 第3步，设定窗口的大小(长 * 宽)
win.geometry('800x500')  # 这里的乘是小x

button = Button(text='打开文件',command=openxlsx)
button.pack()



tree = ttk.Treeview(win)  # 表格
tree["columns"] = ("姓名", "年龄", "身高")
tree.column("姓名", width=100)  # 表示列,不显示
tree.column("年龄", width=100)
tree.column("身高", width=100)

tree.heading("姓名", text="姓名-name")  # 显示表头
tree.heading("年龄", text="年龄-age")
tree.heading("身高", text="身高-tall")

tree.insert("", 0, text="a", values=("1", "2", "3"))  # 插入数据，
tree.insert("", 1, text="b", values=("1", "2", "3"))
tree.insert("", 2, text="c", values=("1", "2", "3"))
tree.insert("", 3, text="line1", values=("1", "2", "3"))

tree.pack()

tree.mainloop()






# from tkinter import *
# from tkinter import ttk
# import xlrd

#bookList = [('aaa', 123), ('bbb', 123), ('xxx', 123), ('sss', 123), ('ddd', 123)]
#
# root = Tk()
# frame = ttk.Frame(root)
# frame.pack(fill='both', expand='false')
#
# tree = ttk.Treeview(frame, columns=['name', 'price','sss'], show='headings')
#
# #tree = ttk.Treeview(frame)
# tree.heading('name', text='name')
# tree.heading('price', text='price')
# tree.heading('sss', text='sss')
#
#
# fname = r'表格.xlsx'
# bk = xlrd.open_workbook(fname)
#
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
# cell_value = sh.cell_value(1, 1)
# # print cell_value
#
# row_list = []
# # 获取各行数据
# for i in range(0, nrows):
#     row_data = sh.row_values(i)
#     # print(row_data)
#     # t.insert('end',row_data)
#     # t.insert('end', '\n')
#     tree.insert('', 'end', values=row_data)
#     row_list.append(row_data)
# print('111111111111')
#
# tree.pack()
# tree.mainloop()
#

