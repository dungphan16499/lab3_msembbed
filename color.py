import numpy as np
import cv2
import tkinter as tk
 
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink max-buffers=1 drop=true"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def process(frame, frame2, frame3):
    black = (255,255,255)
    #create  rect in screen's centre
    rect_size = 100
    width, height, channels = frame.shape
    start_point = (int(height/2 - rect_size/2), int(width/2 - rect_size/2))
    end_point = (int(height/2 + rect_size/2), int(width/2 + rect_size/2))
    color = (255, 255, 0)
    thickness = 2
    rect = cv2.rectangle(frame, start_point, end_point, color, thickness)
    h_sensivity = 20
    
    width2, height2, channels2 = frame2.shape
    start_point2 = (int(height/1.3 - rect_size/2), int(width/1.3 - rect_size/2))
    end_point2 = (int(height/1.3 + rect_size/2), int(width/1.3 + rect_size/2))
    color = (255, 255, 0)
    #thickness = 2
    rect2 = cv2.rectangle(frame2, start_point2, end_point2, color, thickness)
    
    
    width3, height3, channels = frame.shape
    start_point3 = (int(height/3.4 - rect_size/2), int(width/3.4 - rect_size/2))
    end_point3 = (int(height/3.4 + rect_size/2), int(width/3.4 + rect_size/2))
    color = (255, 255, 0)
    #thickness = 2
    rect3 = cv2.rectangle(frame3, start_point3, end_point3, color, thickness)
    
    s_h = 255
    v_h = 255
    s_l = 50
    v_l = 50
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_upper = np.array([60 + h_sensivity, s_h, v_h])
    green_lower = np.array([60 - h_sensivity, s_l, v_l])
    mask_frame = hsv_frame[start_point[1]:end_point[1] + 1, start_point[0]:end_point[0] + 1]
    mask_frame2 = hsv_frame[start_point2[1]:end_point2[1] + 1, start_point2[0]:end_point2[0] + 1]
    mask_frame3 = hsv_frame[start_point3[1]:end_point3[1] + 1, start_point3[0]:end_point3[0] + 1]
    mask_green = cv2.inRange(mask_frame, green_lower, green_upper)
    mask_green2 = cv2.inRange(mask_frame2, green_lower, green_upper)
    mask_green3 = cv2.inRange(mask_frame3, green_lower, green_upper)
    green_rate = np.count_nonzero(mask_green)/(rect_size*rect_size)
    green_rate2 = np.count_nonzero(mask_green2)/(rect_size*rect_size)
    green_rate3 = np.count_nonzero(mask_green3)/(rect_size*rect_size)
    
    red_upper = np.array([5 + 7, s_h, v_h])
    red_lower = np.array([5 - 7, s_l, v_l])
    mask_frame = hsv_frame[start_point[1]:end_point[1] + 1, start_point[0]:end_point[0] + 1]
    mask_frame2 = hsv_frame[start_point2[1]:end_point2[1] + 1, start_point2[0]:end_point2[0] + 1]
    mask_frame3 = hsv_frame[start_point3[1]:end_point3[1] + 1, start_point3[0]:end_point3[0] + 1]
    mask_red = cv2.inRange(mask_frame, red_lower, red_upper)
    mask_red2 = cv2.inRange(mask_frame2, red_lower, red_upper)
    mask_red3 = cv2.inRange(mask_frame3, red_lower, red_upper)
    red_rate = np.count_nonzero(mask_red)/(rect_size*rect_size)
    red_rate2 = np.count_nonzero(mask_red2)/(rect_size*rect_size)
    red_rate3 = np.count_nonzero(mask_red3)/(rect_size*rect_size)
    
    blue_upper = np.array([120 + 10, s_h, v_h])
    blue_lower = np.array([120- 10, s_l, v_l])
    mask_frame = hsv_frame[start_point[1]:end_point[1] + 1, start_point[0]:end_point[0] + 1]
    mask_frame2 = hsv_frame[start_point2[1]:end_point2[1] + 1, start_point2[0]:end_point2[0] + 1]
    mask_frame3 = hsv_frame[start_point3[1]:end_point3[1] + 1, start_point3[0]:end_point3[0] + 1]
    mask_blue = cv2.inRange(mask_frame, blue_lower, blue_upper)
    mask_blue2 = cv2.inRange(mask_frame2, blue_lower, blue_upper)
    mask_blue3 = cv2.inRange(mask_frame3, blue_lower, blue_upper)
    blue_rate = np.count_nonzero(mask_blue)/(rect_size*rect_size)
    blue_rate2 = np.count_nonzero(mask_blue2)/(rect_size*rect_size)
    blue_rate3 = np.count_nonzero(mask_blue3)/(rect_size*rect_size)

    yellow_upper = np.array([30 + 3, s_h, v_h])
    yellow_lower = np.array([30 - 3, s_l, v_l])
    mask_frame = hsv_frame[start_point[1]:end_point[1] + 1, start_point[0]:end_point[0] + 1]
    mask_frame2 = hsv_frame[start_point2[1]:end_point2[1] + 1, start_point2[0]:end_point2[0] + 1]
    mask_frame3 = hsv_frame[start_point3[1]:end_point3[1] + 1, start_point3[0]:end_point3[0] + 1]
    mask_yellow = cv2.inRange(mask_frame, yellow_lower, yellow_upper)
    mask_yellow2 = cv2.inRange(mask_frame2, yellow_lower, yellow_upper)
    mask_yellow3 = cv2.inRange(mask_frame3, yellow_lower, yellow_upper)
    yellow_rate = np.count_nonzero(mask_yellow)/(rect_size*rect_size)
    yellow_rate2 = np.count_nonzero(mask_yellow2)/(rect_size*rect_size)
    yellow_rate3 = np.count_nonzero(mask_yellow3)/(rect_size*rect_size)
    
    orange_upper = np.array([18+ 8, s_h, v_h])
    orange_lower = np.array([18 - 8, s_l, v_l])
    mask_frame = hsv_frame[start_point[1]:end_point[1] + 1, start_point[0]:end_point[0] + 1]
    mask_frame2 = hsv_frame[start_point2[1]:end_point2[1] + 1, start_point2[0]:end_point2[0] + 1]
    mask_frame3 = hsv_frame[start_point3[1]:end_point3[1] + 1, start_point3[0]:end_point3[0] + 1]
    mask_orange = cv2.inRange(mask_frame, orange_lower, orange_upper)
    mask_orange2 = cv2.inRange(mask_frame2, orange_lower, orange_upper)
    mask_orange3 = cv2.inRange(mask_frame3, orange_lower, orange_upper)
    orange_rate = np.count_nonzero(mask_orange)/(rect_size*rect_size)
    orange_rate2 = np.count_nonzero(mask_orange2)/(rect_size*rect_size)
    orange_rate3 = np.count_nonzero(mask_orange3)/(rect_size*rect_size)
    
    purple_upper = np.array([147 + 10, s_h, v_h])
    purple_lower = np.array([147 - 10, s_l, v_l])
    mask_frame = hsv_frame[start_point[1]:end_point[1] + 1, start_point[0]:end_point[0] + 1]
    mask_frame2 = hsv_frame[start_point2[1]:end_point2[1] + 1, start_point2[0]:end_point2[0] + 1]
    mask_frame3 = hsv_frame[start_point3[1]:end_point3[1] + 1, start_point3[0]:end_point3[0] + 1]
    mask_purple = cv2.inRange(mask_frame, purple_lower, purple_upper)
    mask_purple2 = cv2.inRange(mask_frame2, purple_lower, purple_upper)
    mask_purple3 = cv2.inRange(mask_frame3, purple_lower, purple_upper)
    purple_rate = np.count_nonzero(mask_purple)/(rect_size*rect_size)
    purple_rate2 = np.count_nonzero(mask_purple2)/(rect_size*rect_size)
    purple_rate3 = np.count_nonzero(mask_purple3)/(rect_size*rect_size)
    
    sky_upper = np.array([99 + 9, s_h, v_h])
    sky_lower = np.array([99 - 9, s_l, v_l])
    mask_frame = hsv_frame[start_point[1]:end_point[1] + 1, start_point[0]:end_point[0] + 1]
    mask_frame2 = hsv_frame[start_point2[1]:end_point2[1] + 1, start_point2[0]:end_point2[0] + 1]
    mask_frame3 = hsv_frame[start_point3[1]:end_point3[1] + 1, start_point3[0]:end_point3[0] + 1]
    mask_sky = cv2.inRange(mask_frame, sky_lower, sky_upper)
    mask_sky2 = cv2.inRange(mask_frame2, sky_lower, sky_upper)
    mask_sky3 = cv2.inRange(mask_frame3, sky_lower, sky_upper)
    sky_rate = np.count_nonzero(mask_sky)/(rect_size*rect_size)
    sky_rate2 = np.count_nonzero(mask_sky2)/(rect_size*rect_size)
    sky_rate3 = np.count_nonzero(mask_sky3)/(rect_size*rect_size)

    org = end_point
    org2 = end_point2
    org3 = end_point3
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.7
	
    if green_rate > 0.9:
        text = cv2.putText(rect, ' green ', org, font, fontScale, black, thickness, cv2.LINE_AA)
    elif green_rate2 > 0.9:
        text = cv2.putText(rect2, ' green ', org2, font, fontScale, black, thickness, cv2.LINE_AA)
    elif green_rate3 > 0.9:
        text = cv2.putText(rect3, ' green ', org3, font, fontScale, black, thickness, cv2.LINE_AA)
        
    if red_rate > 0.9:
        text = cv2.putText(rect, ' red ', org, font, fontScale, black, thickness, cv2.LINE_AA)
    elif red_rate2 > 0.9:
        text = cv2.putText(rect2, ' red ', org2, font, fontScale, black, thickness, cv2.LINE_AA)
    elif red_rate3 > 0.9:
        text = cv2.putText(rect3, ' red ', org3, font, fontScale, black, thickness, cv2.LINE_AA)
    
    if blue_rate > 0.9:
        text = cv2.putText(rect2, ' blue ', org, font, fontScale, black, thickness, cv2.LINE_AA)
    elif blue_rate2 > 0.9:
        text = cv2.putText(rect, ' blue ', org2, font, fontScale, black, thickness, cv2.LINE_AA)
    elif blue_rate3 > 0.9:
        text = cv2.putText(rect3, ' blue ', org3, font, fontScale, black, thickness, cv2.LINE_AA)
    
    if yellow_rate > 0.9:
        text = cv2.putText(rect, ' yellow ', org, font, fontScale, black, thickness, cv2.LINE_AA)
    elif yellow_rate2 > 0.9:
        text = cv2.putText(rect2, ' yellow ', org2, font, fontScale, black, thickness, cv2.LINE_AA)
    elif yellow_rate3 > 0.9:
        text = cv2.putText(rect3, ' yellow ', org3, font, fontScale, black, thickness, cv2.LINE_AA)
    
    if orange_rate > 0.9:
        text = cv2.putText(rect, ' orange ', org, font, fontScale, black, thickness, cv2.LINE_AA)
    elif orange_rate2 > 0.9:
        text = cv2.putText(rect2, ' orange ', org2, font, fontScale, black, thickness, cv2.LINE_AA)
    elif orange_rate3 > 0.9:
        text = cv2.putText(rect3, ' orange ', org3, font, fontScale, black, thickness, cv2.LINE_AA)
    
    if purple_rate > 0.9:
        text = cv2.putText(rect, ' purple ', org, font, fontScale, black, thickness, cv2.LINE_AA)
    elif purple_rate2 > 0.9:
        text = cv2.putText(rect2, ' purple ', org2, font, fontScale, black, thickness, cv2.LINE_AA)
    elif purple_rate3 > 0.9:
        text = cv2.putText(rect3, ' purple ', org3, font, fontScale, black, thickness, cv2.LINE_AA)
    
    if sky_rate > 0.9:
        text = cv2.putText(rect, ' sky_blue ', org, font, fontScale, black, thickness, cv2.LINE_AA)
    elif sky_rate2 > 0.9:
        text = cv2.putText(rect2, ' sky_blue ', org2, font, fontScale, black, thickness, cv2.LINE_AA)
    elif sky_rate3 > 0.9:
        text = cv2.putText(rect3, ' sky_blue ', org3, font, fontScale, black, thickness, cv2.LINE_AA)

    av_hue = np.average(mask_frame[:,:,0])
    av_sat = np.average(mask_frame[:,:,1])
    av_val = np.average(mask_frame[:,:,2])
    average = [int(av_hue),int(av_sat),int(av_val)]
    
    text = cv2.putText(rect, str(average) , (10,50), font, fontScale, color, thickness, cv2.LINE_AA)
    text2 = cv2.putText(rect2, str(average) , (10,50), font, fontScale, color, thickness, cv2.LINE_AA)
    text3 = cv2.putText(rect3, str(average) , (10,50), font, fontScale, color, thickness, cv2.LINE_AA)
    frame2 = text2
    frame = text
    frame3 = text3
    return frame2


print('Press 4 to Quit the Application\n')

#Open Default Camera
cap = cv2.VideoCapture(0)#gstreamer_pipeline(flip_method=4), cv2.CAP_GSTREAMER)

cnt = 0

while(cap.isOpened()):
    #Take each Frame
    ret, frame2 = cap.read()
    ret, frame = cap.read()
    ret, frame3 = cap.read()
    

    #Flip Video vertically (180 Degrees)
    frame2 = cv2.flip(frame2, 180)
    frame = cv2.flip(frame, 180)
    frame3 = cv2.flip(frame3, 180)

    invert = process(frame, frame2, frame3)
    
    # Show video
    if cnt == 1:
        cv2.imshow('Cam', frame)
    elif cnt == 2:
        cv2.imshow('Cam', frame2)
    elif cnt == 0:
        cv2.imshow('Cam', frame3)
    
    
    k = cv2.waitKey(1) & 0xFF
    if k == 97 :
        cnt = cnt -1
        cnt = cnt % 3
    elif k == 100:
        cnt = cnt+1
        cnt = cnt % 3
    # Exit if "4" is pressed  
    if k == 52:
        #Quit
        print ('Good Bye!')
        break

#Release the Cap and Video   
cap.release()
cv2.destroyAllWindows()
