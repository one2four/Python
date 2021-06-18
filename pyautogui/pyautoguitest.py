import pyautogui

width, height = pyautogui.size()  # 屏幕的宽度和高度
print(width, height)


currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
print(currentMouseX, currentMouseY)
 
# 控制鼠标移动,duration为持续时间
for i in range(3):
    pyautogui.moveTo(100, 100, duration=0.25)  # 移动到 (100,100)
    pyautogui.moveTo(300, 100, duration=0.25)
    pyautogui.moveTo(400, 400, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

 # 按住鼠标左键，把鼠标拖拽到(100, 200)位置
pyautogui.dragTo(100, 200, button='left')
# 按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
pyautogui.dragTo(300, 400, 2, button='left')
# 按住鼠标左键，用0.2秒钟把鼠标向上拖拽
pyautogui.dragRel(0, -60, duration=0.2)

