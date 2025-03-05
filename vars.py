import os

work_dir = os.getcwd()
print("当前工作目录: ",work_dir)

version = '1.0.0'
main_canvas = None

class Window_Properties:
    window_width = 400
    window_height = 400

class Imagesets_Paths:
    null_image = "./src/null_image.png"
    background_image = os.path.join(work_dir,"src\\background.jpg") 
    print(background_image)