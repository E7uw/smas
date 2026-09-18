# Q11 - Simple Image Transformation Toolbox
# Basic Python program using PIL, NumPy and Matplotlib
# No OpenCV (cv2) is used.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Enter the image file name
file_name = input("Enter image file name (JPG/PNG): ")

# Open the image
original = Image.open(file_name).convert("RGB")
image = original.copy()


# Function for custom matrix transformation
def apply_matrix(image, A):
    img = np.array(image)
    h, w = img.shape[:2]

    cx = w // 2
    cy = h // 2

    result = np.zeros_like(img)

    for y in range(h):
        for x in range(w):
            point = np.array([x - cx, y - cy])
            new_point = A @ point

            new_x = int(new_point[0] + cx)
            new_y = int(new_point[1] + cy)

            if 0 <= new_x < w and 0 <= new_y < h:
                result[new_y, new_x] = img[y, x]

    return Image.fromarray(result)


# Keep showing the menu
while True:

    print("\n--- IMAGE TRANSFORMATION TOOLBOX ---")
    print("1. Rotate")
    print("2. Resize")
    print("3. Flip")
    print("4. Shear")
    print("5. Custom Matrix")
    print("6. Reset")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Rotate
    if choice == "1":
        angle = float(input("Enter angle: "))
        image = image.rotate(angle, expand=True)

    # Resize
    elif choice == "2":
        factor = float(input("Enter resize factor: "))

        w, h = image.size
        new_w = int(w * factor)
        new_h = int(h * factor)

        image = image.resize((new_w, new_h))

    # Flip
    elif choice == "3":
        print("1. Horizontal")
        print("2. Vertical")

        direction = input("Enter direction: ")

        if direction == "1":
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        elif direction == "2":
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        else:
            print("Invalid direction.")

    # Horizontal shear
    elif choice == "4":
        shear = float(input("Enter shear value: "))

        A = np.array([[1, shear],
                      [0, 1]])

        image = apply_matrix(image, A)

    # Custom 2 x 2 matrix
    elif choice == "5":
        print("Enter the 2 x 2 matrix:")

        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        d = float(input("d = "))

        A = np.array([[a, b],
                      [c, d]])

        print("\nMatrix:")
        print(A)

        print("T(e1) =", A @ np.array([1, 0]))
        print("T(e2) =", A @ np.array([0, 1]))
        print("Rank =", np.linalg.matrix_rank(A))

        image = apply_matrix(image, A)

    # Reset
    elif choice == "6":
        image = original.copy()
        print("Image reset successfully.")

    # Exit
    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
        continue

    # Show the current image
    plt.imshow(image)
    plt.axis("off")
    plt.show()
