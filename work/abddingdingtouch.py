# -*- coding:utf-8 -*-
# @Time    : 2022/3/30 17:05
# @Author  : unkown
# @File    : adbdingdingtouch.py
# @License : Unkown

import os
import time, datetime
import uiautomator2 as u2
import requests
import json

print('------------------编写函数----------------')

# d = u2.connect_usb('dc1fa629')
d = u2.connect_adb_wifi('192.168.1.105:5555')


# def runtime():
#     print(datetime.time)


def connectPhone():
    d = u2.connect_adb_wifi('192.168.1.105:5555')
    d.app_start("com.alibaba.android.rimet")
    d1 = d(text="工作台").exists(timeout=3)
    print("进入工作台",d1)
    d(text="工作台").click()
    time.sleep(5)
    d2 = d(text="考勤打卡").exists(timeout=3)
    print("进入考勤打卡", d2)
    d(text="考勤打卡").click()
    time.sleep(5)
    # if d(text="上班打卡").exists(timeout=3):
    #     print("上班打卡成功")
    #     return "上班打卡成功"
    # elif d(text="下班打卡").exists(timeout=3):
    #     print("下班打卡成功")
    #     return "下班打卡成功"
    # print(d3)
    # touch
    # 手机截屏
    d.screenshot("dingding.jpg")
    # 将截屏信息发送至当前目录
    d.push("dingding.jpg", "/sdcard/0/dingding.jpg")
    time.sleep(5)
    d.app_stop("com.alibaba.android.rimet")


def send_info(runningData):
    feishuwebhook = "https://open.feishu.cn/open-apis/bot/v2/hook/413f4033-2758-4776-bcb1-219f933248bb"

    payload_message = {
        "msg_type": "text",
        "content": {
            "text": "test",
        }
    }

    payload_message['content']['text'] = '{runningData_content}'.format(runningData_content=runningData)
    headers = {
        'Content-Type': 'application/json'
    }
    print(payload_message)
    # requests.request()
    print(json.dumps(payload_message))
    response = requests.request("POST", feishuwebhook, headers=headers, data=json.dumps(payload_message))
    # print(response.content)


def onClick(x, y):
    os.system('adb shell input tap {x1} {y1}'.format(x1=x, y1=y))


def slide(x, y, ex, ey):
    os.system('adb shell input swipe {x1} {y1} {x2} {y2}'.format(x1=x, y1=y, x2=ex, y2=ey))


def touch(key):
    if key == "back":
        print("> 返回按键")
        os.system('adb shell input keyevent 4')
    elif key == "light":
        print("> 开屏按键")
        os.system('adb shell input keyevent 26')
        slide(500, 2260, 500, 1200)
    elif key == "lock":
        print("> 锁屏")
        os.system('adb shell input keyevent 26')
    time.sleep(1)


def is_black():
    d = u2.connect()
    screen = d.info
    # print(screen)
    if not screen["screenOn"]:
        return True


def device_battery():
    device_all = d.device_info
    # device_level = device_all['battery']['level']
    if device_all['battery']['level'] > 40:
        # print("当前手机电量 {level1} ，满足使用需求".format(level1=device_all['battery']['level']))
        return "当前手机电量 {level1} ，满足使用需求".format(level1=device_all['battery']['level'])
    elif device_all['battery']['level'] <= 40:
        # print("当前手机电量 {level1}，手机电量不足，需要进行充电".format(level1=device_all['battery']['level']))
        return "当前手机电量 {level1}，手机电量不足，需要进行充电".format(level1=device_all['battery']['level'])
    else:
        return "手机异常，请检查"


print("--------------------------------------")
print("---------------主函数------------------")


def startMain():
    if is_black():
        touch("light")
        connectPhone()
        # send_info()
        time.sleep(5)
        touch("lock")
        return "手机锁屏状态运行"

    else:
        connectPhone()
        # send_info()
        time.sleep(5)
        touch("lock")
        return "手机未锁屏状态运行"


if __name__ == '__main__':
    runningData = ['http://dd.pitalk.cn/usr/uploads/work/dingding.jpg', device_battery(), startMain()]
    send_info(runningData)
