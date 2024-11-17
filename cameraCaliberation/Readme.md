# Camera Calibration Project

This project demonstrates the process of camera calibration using a checkerboard pattern to determine intrinsic and extrinsic parameters. Calibration helps in understanding the camera's characteristics, enabling accurate 3D to 2D transformations.

---

## 📜 **Overview**

### What is a Camera?
A camera is a device that converts the 3D world into a 2D image.

### What is Camera Calibration?
Camera calibration is the process of determining specific parameters of a camera. It is used to estimate the camera's characteristics, including:
- **Intrinsic Parameters**: These map pixel coordinates in the image frame.
- **Extrinsic Parameters**: These represent the camera's orientation and location (rotation and translation).

---

## 🎯 **Inputs and Outputs of Camera Calibration**

### **Inputs**:
1. 3D object points (checkerboard coordinates)
2. 2D image points (detected corners on the checkerboard)

### **Outputs**:
1. Camera matrix
2. Distortion coefficients
3. Rotational vectors
4. Translational vectors

---

## 📊 **Calibration Results**

### **Camera Matrix**:
