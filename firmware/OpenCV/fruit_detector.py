
import cv2
import numpy as np

raw = np.array([0,0,100])
ripe = np.array([10,255,255])

PATH_to_Model="..\\model.txt"
PATH_to_Caffe="..\\Caffe.prototxt"
CONFIDENCE =.02
try:
    net = cv2.dnn.readNetFromCaffe(PATH_to_Caffe,PATH_to_Model)
except:
    print("no file found")
    
def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    
        
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
            (h, w) = img.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843,(300, 300), 127.5)            
            #cv2.imshow('my webcam', img)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, ripe, raw) 
            cv2.imshow('Image',img)
            cv2.imshow('Result',mask)   
            
            print("[INFO] computing object detections...")
            net.setInput(blob)
            detections = net.forward()
            for i in np.arange(0, detections.shape[2]):   # extract the confidence (i.e., probability) associated with the prediction               
                confidence = detections[0, 0, i, 2] 
                if confidence > CONFIDENCE:  # filter out weak detections by ensuring the `confidence` is greater than the minimum confidence
                    
                    idx = int(detections[0, 0, i, 1])
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                    print("[INFO] {}".format(label))
                    cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)            
            
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()
