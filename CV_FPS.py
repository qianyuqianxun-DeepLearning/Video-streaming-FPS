# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

print(time.asctime())

# 读取视频
cap = cv2.VideoCapture("C:\\Users\\LENOVO\\Desktop\\vid.mp4")
# 获取FPS(每秒传输帧数(Frames Per Second))
fps = cap.get(cv2.CAP_PROP_FPS)
# 获取总帧数
totalFrameNumber = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print("FPS: {:.2f}".format(fps))
print("sum: {:.2f}".format(totalFrameNumber))
# 当前读取到第几帧
COUNT = 0

# 若小于总帧数则读一帧图像
while COUNT < totalFrameNumber:
    # 一帧一帧图像读取
    ret, frame = cap.read()
    # 把每一帧图像保存成jpg格式（这一行可以根据需要选择保留）

    cv2.rectangle(frame, (0, 0), (150, 150), (0, 0, 255), 10)
    cv2.line(frame, (0, 0), (150, 150), (0, 0, 255), 10)
    cv2.imwrite(str(COUNT) + '.jpg', frame)
    # 显示这一帧地图像
    COUNT = COUNT + 1
    cv2.imshow('FPS_infer', frame)

    # 延时一段33ms（1s➗30帧）再读取下一帧，如果没有这一句便无法正常显示视频
    cv2.waitKey(33)

cap.release()
cv2.destroyAllWindows()
