"""
Author: Son Phat Tran
This script contains the logic that allows user to select a point on the image and see its
coordinates
"""
import cv2


def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")
        # Display the coordinates on the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f"({x},{y})", (x, y), font, 0.5, (255, 0, 0), 1)
        cv2.imshow("Image", img)


if __name__ == "__main__":
    # Load an image
    image_path = "images/Image_2.jpg"  # Replace with your image path
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to load image.")
        exit(1)

    # Display the image
    cv2.imshow("Image", img)

    # Set the callback function
    cv2.setMouseCallback("Image", on_click)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()