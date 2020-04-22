# -*- coding: utf-8 -*-
# @Author: wlp
# @Date:   2020-04-13 10:16:04
# @Last Modified by:   wlp
# @Last Modified time: 2020-04-20 13:12:58

'''
基本上使用tkinter来开发GUI应用需要以下5个步骤：

1.导入tkinter模块中我们需要的东西。
2.创建一个顶层窗口对象并用它来承载整个GUI应用。
3.在顶层窗口对象上添加GUI组件。
4.通过代码将这些GUI组件的功能组织起来。
5.进入主事件循环(main loop)。
'''

import tkinter
from tkinter import messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        # nonlocal只能在封装函数中使用，在外部函数先进行声明，在内部函数进行nonlocal声明，
        # 这样在main()函数中的flag与change_label_text()中的flag是同一个变量。
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'hello world!') if flag else ('blue', 'goodbye world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    #在同一个函数内，内部函数可以使用在调用前定义的变量
    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title("title")
    # 创建标签对象，并添加到顶层窗口
    label = tkinter.Label(top, text="hello world!", font='Arial -32', fg='red')
    label.pack(expand=1)

    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text="按钮1", command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text="按钮2", command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    

    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()

    top = tkinter.Tk()
    top.geometry('240x180')
    top.resizable(1, 1)
    top.update()
    top.title('hello,gui')
    #top.quit()

    label = tkinter.Label(top, text = 'hello,world', font = 'Arial -32', fg = 'red')
    label.pack(side = 'top', anchor = 'ne')#右上,默认为居中

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text = '确认')
    button1.pack(side = 'left')
    panel.pack(side = 'right', anchor = 'ne')


    tkinter.mainloop()

