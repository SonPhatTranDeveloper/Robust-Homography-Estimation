import os

import cv2
import numpy as np


def main():
    # Paths to the two images
    image1_path = "images/Image_1.jpg"
    image2_path = "images/Image_2.jpg"

    # Load the images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None or img2 is None:
        print("Error: Unable to load images.")
        return

    # Define corresponding points in both images
    # Format: [[x1, y1], [x2, y2], ...]
    points_img1 = np.array([[1050, 1163], [2185, 1193], [720, 3058], [2316, 3104]], dtype=np.float32)
    points_img2 = np.array([[1591, 1300], [2674, 1603], [422, 2607], [2107, 3296]], dtype=np.float32)

    # Estimate homography matrix using RANSAC
    H, mask = cv2.findHomography(points_img1, points_img2, cv2.RANSAC)

    if H is None:
        print("Error: Homography could not be computed.")
        return

    # Display the 3x3 homography matrix
    print("Homography Matrix:")
    print(H)

    # Warp the first image using the computed homography
    height, width, _ = img2.shape
    warped_img = cv2.warpPerspective(img1, H, (width, height))

    # Save the warped image into result
    warped_image_path = os.path.join("results", "warped_image.jpg")
    cv2.imwrite(warped_image_path, warped_img)
    print(f"Warped image saved to: {warped_image_path}")

    # Display the original and warped images
    cv2.imshow("Original Image 1", img1)
    cv2.imshow("Original Image 2", img2)
    cv2.imshow("Warped Image 1 to Image 2", warped_img)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
