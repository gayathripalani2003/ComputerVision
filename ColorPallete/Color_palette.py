import cv2
import numpy as np

def emptyFunction(position):  # Callback function.
    pass

def main():
    image = np.zeros((512, 512, 3), np.uint8)  # Create an image, npunit8-range 0 to 255
    windowName = "OpenCV HSL Color Palette"  # Define the window name
    cv2.namedWindow(windowName)  # Create a window with the defined name
    cv2.createTrackbar('Hue', windowName, 50, 179, emptyFunction)  # Create the Hue trackbar
    
    fixed_saturation = 50  # Fixed Saturation
    fixed_lightness = 50  # Fixed Lightness
    
    while True:
        # Get the current position of the Hue trackbar
        hue = cv2.getTrackbarPos('Hue', windowName)
        
        # Create an HSL image with the selected Hue and fixed Saturation and Lightness
        hsl_color = np.uint8([[[hue, fixed_saturation, fixed_lightness]]])
        
        # Convert the HSL color to BGR for displaying in the OpenCV window
        bgr_color = cv2.cvtColor(hsl_color, cv2.COLOR_HLS2BGR)
        
        # Fill the image with the selected BGR color
        image[:] = bgr_color[0][0]
        
        # Display the text in the window (with smaller font size)
        text = f'Hue: {hue}, Saturation: {fixed_saturation}, Lightness: {fixed_lightness}'
        cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
        
        # Display the image in the window
        cv2.imshow(windowName, image)
        
        # Break the loop if the ESC key is pressed
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

# Run the main function
if __name__ == "__main__":
    main()
