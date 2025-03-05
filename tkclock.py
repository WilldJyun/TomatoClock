import tkinter as tk  # Tkinter 是 Python 的标准 GUI 库
import random         # 用于生成随机数或选择随机项
import vars           # 全局变量
from PIL import Image, ImageTk

# 说明：
# 一切组件都在canvas上进行。窗口只是个载体，组件的绘制由画布完成。

# 定义主窗口类，继承自 tk.Tk
class Window(tk.Tk):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.background_photo = None
        self.geometry(f"{vars.Window_Properties.window_height}x{vars.Window_Properties.window_width}")  # 设置窗口大小为 400x300 像素
        
    # 添加按钮的方法
    def add_button(self, text, command=lambda: print("按钮被按下")):
        # 创建一个按钮并设置其文本和命令（点击事件）
        button = tk.Button(vars.main_canvas, text=text, command=command)
        vars.main_canvas.create_window(10, 10, anchor="nw", window=button)

    # 显示时钟的方法
    def showclock(self):
        # 初始化画布并绘制时钟
        canvas = Clock.init_circle(self)
        vars.main_canvas = canvas  # 将画布置为全局变量以便其他地方使用

    # 绘制圆形的方法
    def drawcircle(self):
        # 调用 Clock 类的 drawclock 方法在指定画布上绘制圆形
        Clock.drawclock(self, vars.main_canvas)

    # 启动主循环，显示窗口
    def show(self):
        self.mainloop()

    def set_backgroundpic(self,pic_path=""):
        '''
        如果path为空，则不设置
        '''
        if pic_path=="":
            return
        print("背景图：",pic_path)
        self.background_photo = ImageTk.PhotoImage(file=pic_path)

        vars.main_canvas.create_image(0,0,anchor="nw",image=self.background_photo)
    def set_transparency(self,rate=None):
        """
        rate 透明度，从 0~1
        """
        if rate == None:
            return
        self.attributes("-alpha",rate)


# 定义时钟类，包含静态方法用于初始化和绘制时钟
class Clock:
    @staticmethod
    def init_circle(window):
        # 创建一个 Canvas 画布，宽度和高度均为 300 像素，背景透明
        canvas = tk.Canvas(window, width=300, height=300)
        canvas.pack(fill="both", expand=True)  # 设置画布填充整个窗口并随窗口大小调整
        return canvas

    @staticmethod
    def drawclock(window, canvas):
        # 在画布上绘制两个嵌套的椭圆，颜色随机选择
        canvas.create_oval(10, 10, 290, 290, fill=random.choice(["red", "blue", "green", "yellow"]))
        canvas.create_oval(30, 30, 270, 270, fill=random.choice(["red", "blue", "green", "yellow"]))
        return True  # 返回 True 表示绘制成功