'''
messageBox：消息框，用于显示你应用程序的消息框。(Python2中为tkMessagebox)，
其实这里的messageBox就是我们平时看到的弹窗。 我们首先需要定义一个触发功能，来触发这个弹窗，
这里我们就放上以前学过的button按钮，通过触发功能，调用messagebox吧，点击button按钮就会弹出提示对话框。
下面给出messagebox提示信息的几种形式：
tkinter.messagebox.showinfo(title='Hi', message='你好！')            # 提示信息对话窗
tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'

什么时候用：

　　在比如像软件或网页交互界面等，有不同的界面逻辑层级和功能区域划分时可以用到，让交互界面逻辑更加清晰。
'''
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox  # 要使用messagebox先要导入模块

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x


# 第5步，定义触发函数功能
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')  # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'


# 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

# 第6步，主窗口循环显示
window.mainloop()
