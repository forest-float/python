
#excel表格操作 读取表格数据
'''
首先，我们需要导入第三方模块 xlrd ，因为是第三方的模块，没有安装的需要先安装。在命令行中输入：
pip install xlrd
'''

import xlrd
import datetime
# 打开execl
filename = '你好.txt'
filename = filename.encode('utf-8')#如果文件名有包含中文，使用编码格式转换

workbook = xlrd.open_workbook('test.xlsx')


# 输出所有 sheet 的名字
print(workbook.sheet_names())
# 获取所有的 sheet
print(workbook.sheets())
# 根据索引获取 sheet
print(workbook.sheet_by_index(1))
# 根据名字获取 sheet
print(workbook.sheet_by_name('1班'))

sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)

# 获取第 2 行内容
print(sheet1.row_values(1))
# 获取第 3 列内容
print(sheet1.col_values(2))

cell1 = sheet1.cell(1, 1).value
# 行索引
cell2 = sheet1.row(1)[1].value     #第二行第二列    row / col  行在前，列在后
cell3 = sheet1.cell(1, 2).value    #第二行第三列    cell行在前，列在后
# 列索引
cell4 = sheet1.col(2)[1].value     #第二行第三列
print(cell1, cell2, cell3, cell4)

#获取的是表格里面的时间数据
date_value = xlrd.xldate_as_datetime(sheet1.cell_value(5, 4),
                                     workbook.datemode)
print(type(date_value), date_value)
#这里是直接通过方法将数据转成了 datetime 类型，
# xlrd 还提供了可以将数据转成元组，然后再将元组转成日期。
date_value = xlrd.xldate_as_tuple(sheet1.cell_value(5, 4), workbook.datemode)
print(type(date_value), date_value)#元组类型
year, month, day, hours, minu, secon = date_value#将元组数据一一赋值给特定的变量
print(datetime.datetime(year, month, day, hours, minu, secon))#转换成时间格式



#写入 Excel    具体说明请看文档https://xlsxwriter.readthedocs.io/
#首先当然是安装第三方模块：
#pip install xlsxwriter

import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')

sheet1 = workbook.add_worksheet('test_sheet')
sheet2 = workbook.add_worksheet('test2_sheet')

workfomat = workbook.add_format()
# 字体加粗
workfomat.set_bold(True)
# 单元格边框宽度
workfomat.set_border(1)
# 对齐方式
workfomat.set_align('left')
# 格式化数据格式为小数点后两位
workfomat.set_num_format('0.00')

heads = ['', '语文', '数学', '英语']
datas = [
    ['小明', 76, 85, 95],
    ['小红', 85, 58, 92],
    ['小王', 98, 96, 91]
]

#sheet1.write_row('A1', heads, workfomat)
sheet1.write_row(0, 0, heads, workfomat)
sheet1.write_row('A2', datas[0], workfomat)
sheet1.write_row('A3', datas[1], workfomat)
sheet1.write_row('A4', datas[2], workfomat)

format1 = workbook.add_format({'num_format': 'YYYY/mm/dd/ hh:mm:ss'})
sheet1.write_datetime('E6', datetime.datetime(2020, 1, 17, 13, 15, 16), format1)
'''
# 字符串类型
sheet1.write_string()
# 数字型
sheet1.wirte_number()
# 空类型
sheet1.write_blank()
# 公式
sheet1.write_formula()
# 布尔型
sheet1.write_boolean()
# 超链接
sheet1.write_url()

'''
sheet1.insert_image('I6', 'wx.jpg')#添加显示图片
''''
insert_image(row, col, image[, options])
row：行坐标，起始索引值为0；
col：列坐标，起始索引值为0；
image：string类型，是图片路径；
options：dict类型，是可选参数，用于指定图片位置，如URL等信息；
'''

chart = workbook.add_chart({'type': 'bar'})
'''
创建的图表的样式
area：面积样式的图表
bar：条形图
column：柱状图
line：线条样式的图表
pie：饼形图
scatter：散点图
stock：股票样式的图表
radar：雷达样式的图表
'''
chart.add_series({'values': '=test_sheet!$B$2:$D$2'})
chart.add_series({'values': '=test_sheet!$B$3:$D$3'})
chart.add_series({'values': '=test_sheet!$B$4:$D$4'})

#chart.add_series({'values': '=test_sheet!$E$2:$E$4'})
sheet1.insert_chart('A7', chart)#插入图表


workbook.close()#关闭Workbook


workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Number', 'Batch 1', 'Batch 2']
data = [
    [2, 3, 4, 5, 6, 7],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

worksheet.write_row('A1', headings, bold)#写入行
worksheet.write_column('A2', data[0])#写入列
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# Create a new chart object. In this case an embedded chart.
chart1 = workbook.add_chart({'type': 'line'})#line：线条样式的图表

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$B$1',#数据的名称
    'categories': '=Sheet1!$A$2:$A$7',#类别
    'values':     '=Sheet1!$B$2:$B$7',#值
})

# Configure second series. Note use of alternative syntax to define ranges.
chart1.add_series({
    'name':       ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 6, 0],#表示起始行，起始列，结束行，结束列
    'values':     ['Sheet1', 1, 2, 6, 2],#相当于‘=sheet1!$C$2:$C$7’
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Results of sample analysis'})#设置图表标题
chart1.set_x_axis({'name': 'Test number'})#设置x轴说明
chart1.set_y_axis({'name': 'Sample length (mm)'})#设置y轴说明

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(10)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})#带有偏移量
workbook.close()






#批处理文件
import os
import shutil

file_names = os.listdir("./")
print(file_names)
try:
    os.mkdir("section1")
    os.mkdir("section2")
    os.mkdir("section3")
except FileExistsError:
    print('文件夹已经存在')
i = 0
for file_name in file_names:
    splited_file_name = file_name.split('.')
    print(splited_file_name)
    if  splited_file_name[0] == 'idea' \
            or 'section' in splited_file_name[0] \
            or splited_file_name[1] != 'bmp':
        continue
    #file_id = int(splited_file_name[0])
    #size_folder = "section"+str((file_id-1)%3+1)
    #shutil.move(file_name, os.path.join(os.getcwd(), file_name))

    os.renames(file_name, str(i)+'.png')#更改名字
    shutil.copyfile(str(i)+'.png', file_name)  # 复制文件

#move(src, dst)： 将src移动至dst目录下。若dst目录不存在，则效果等同于src改名为dst。
#若dst目录存在，将会把src文件夹的所有内容移动至该目录下面
#os.path.join()函数用于路径拼接文件路径。
#os.path.join()函数中可以传入多个路径：
#会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
#以上一种情况为先。在上一种情况确保情况下，若出现”./”开头的参数，
# 会从”./”开头的参数的上一个参数开始拼接。
#使用os.getcwd()函数获得当前的路径。
