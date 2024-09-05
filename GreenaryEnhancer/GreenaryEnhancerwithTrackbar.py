import cv2
import numpy as np

# Callback function for trackbars
def emptyFunction(position):
    pass

def enhance_greenery(image):
    
    # Define the Window Name
    windowName = "Green Color Enhancer"
    
    # Create a window with the defined name
    cv2.namedWindow(windowName)
    
    # Create Trackbars for Saturation and Lightness with initial values of 255 and 50
    cv2.createTrackbar('Saturation', windowName, 255, 255, emptyFunction)
    cv2.createTrackbar('Lightness', windowName, 50, 255, emptyFunction)

    while True:
        # Convert the image from BGR to HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Split the components of the HSV image
        h, s, v = cv2.split(hsv_image)

        # Extract the Green Dominant Pixels
        b, g, r = cv2.split(image)
        green_mask = (g > r) & (g > b)

        # Get the current position of the Trackbars
        s_current = cv2.getTrackbarPos('Saturation', windowName)
        v_current = cv2.getTrackbarPos('Lightness', windowName)

        # Change the Saturation and Lightness for green-dominant pixels
        s[green_mask] = s_current
        v[green_mask] = v_current

        # Clip the values to stay within the range [0, 255]
        s = np.clip(s, 0, 255).astype(np.uint8)
        v = np.clip(v, 0, 255).astype(np.uint8)

        # Merge the channels back into an HSV image
        enhanced_hsv_image = cv2.merge([h, s, v])

        # Convert the image back from HSV to BGR
        enhanced_image = cv2.cvtColor(enhanced_hsv_image, cv2.COLOR_HSV2BGR)

        # Display the enhanced image
        cv2.imshow(windowName, enhanced_image)

        # Check for key press (wait 1ms for input)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Save the enhanced image
    cv2.imwrite('enhanced_image.jpg', enhanced_image)
    
    # Destroy the windows
    cv2.destroyAllWindows()

# Read and enhance the image
image1 = cv2.imread('greenary_2.jpg')
enhance_greenery(image1)
