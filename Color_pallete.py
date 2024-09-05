import cv2
import numpy as np
def emptyFunction(position):# Callback function.
    pass
def main():
    image = np.zeros((512, 512, 3), np.uint8)#Create an image,npunit8-range 0 to 255
    cv2.namedWindow("OpenCV HSL Color Palette")#Create an Window.
    cv2.createTrackbar('Hue', windowName, 50, 179, emptyFunction)
    fixed_saturation = 50#Fixed Saturation.
    fixed_lightness = 50#Fixed Lightness.
    while True:
        hue = cv2.getTrackbarPos('Hue', windowName)#Get the current position of the trackbar.
        hsl_color = np.uint8([[[hue, fixed_saturation, fixed_lightness]]])#Create the HSL image.
        bgr_color = cv2.cvtColor(hsl_color, cv2.COLOR_HLS2BGR)#Convert HSL to BGR.
        image[:] = bgr_color[0][0]#Fill the image with the selected BGR.
        text = f'Hue: {hue}, Saturation: {fixed_saturation}, Lightness: {fixed_lightness}'
        cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow(windowName, image)#Display the image in the window.
        if cv2.waitKey(1) == 27:#Exit when ESC key is pressed.
            break
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
