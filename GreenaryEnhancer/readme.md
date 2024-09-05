# Green Color Enhancer

This project provides a tool to enhance green-dominant pixels in images by adjusting their saturation and lightness values using OpenCV. This is especially useful for making greenery in images more vibrant and visually appealing.

## Features
- **Real-Time Adjustments**: Users can adjust the saturation and lightness of green areas in real-time using trackbars.
- **Image Enhancement**: Modify the color intensity of greenery to make it more vivid and visually striking.

## Algorithm

1. **Image Loading**: The image is loaded into the program using OpenCV.
2. **Color Space Conversion**: The image is converted from BGR (default in OpenCV) to HSV (Hue, Saturation, Value) for easier manipulation of color properties.
3. **Green-Dominant Detection**: The program identifies green-dominant pixels by comparing the green channel against the red and blue channels.
4. **Saturation and Lightness Adjustment**:
    - A trackbar interface is provided to adjust the saturation and lightness values for only the green-dominant pixels.
5. **Enhancement**: Changes are applied  as the user adjusts the trackbars, allowing for instant feedback.

## Output Image

Below is an example of an output image after enhancing the greenery:

![Enhanced Greenery](output_1.jpg)
![Enhanced Greenery](output_2.jpg)

