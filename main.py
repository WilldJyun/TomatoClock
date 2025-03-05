import tkclock
import vars

if __name__ == '__main__':
    win = tkclock.Window()
    win.showclock()
    win.set_backgroundpic(pic_path=vars.Imagesets_Paths.background_image)
    win.add_button("开始",command=win.drawcircle)
    win.set_transparency(1)
    win.show()