from darknet import *

def find_ed():
    import cv2
    net = load_network("cfg/yolov3_training.cfg", "data/obj.data", "backup/nibble.weights")
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # detect 'ED'
        detections = detect_image(net[0], net[1], nparray_to_image(frame))
        # return img with boxes
        frame = draw_boxes(detections, frame, net[2])
        # show frame
        if detections:
            points = []
            for _, _, bbox in detections:
                left, top, right, bottom = bbox2points(bbox)
                points.append([left, top, right, bottom])
            break
        
        cv2.imshow('frame', frame)
    cv2.destroyAllWindows()
    cap.release()
    cv2.imwrite("../capture.jpg", frame)
    return points

def change_braille(num):
    braille = [14, 1, 5, 3, 11, 9, 7, 15, 13, 6]
    return braille[int(num)]

def encode_braille(num):
    return ''.join(format(num, 'b').zfill(6))

def divide_point(point):
    return point[0], point[1], point[2], point[3]

def pick_num():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    import pytesseract 
    points = find_ed()
    img_ori = cv2.imread("../capture.jpg")
    x, y, w, h = divide_point(points[0])
    img_ori = img_ori[y: h, x: w]
    gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
    
    img_blurred = cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)
    img_thresh = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)
    invert = cv2.bitwise_not(img_thresh)
    img_re = cv2.morphologyEx(invert, cv2.MORPH_TOPHAT, None)
    kenels = np.ones((3, 3), np.uint8)
    img_dil = cv2.dilate(invert, kenels, iterations=2)
    cv2.imwrite('../cp.jpg', img_dil)

    result_chars = pytesseract.image_to_string(invert, lang='kor+eng')
    return result_chars

def make_ed(result_chars):
    stack = []
    for c in result_chars:
        if c.isdigit():
            stack.append(int(c))
        if len(stack) >= 8:
            break
    
    if len(stack) == 8:
        return stack[2:]
    else:
        return stack

