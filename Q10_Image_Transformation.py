# Q10 - Image Transformation using Linear Transformations
# Uses PIL, NumPy and Matplotlib. No OpenCV (cv2).

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Enter the image file name
file_name = input("Enter image file name (JPG/PNG): ")

# Open the image
image = Image.open(file_name).convert("RGB")
img = np.array(image)

# Transformation matrices
A1 = np.array([[2, 0], [0, 0.5]])
A2 = np.array([[0, -1], [1, 0]])
A3 = np.array([[1, 1], [0, 1]])
A4 = np.array([[-1, 0], [0, 1]])
A5 = np.array([[1, 0], [0, 0]])

matrices = [A1, A2, A3, A4, A5]


# Transform the image about its centre
def transform_image(img, A):
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

    return result


# Basis vectors
e1 = np.array([1, 0])
e2 = np.array([0, 1])

# Apply all transformations
for number, A in enumerate(matrices, 1):
    print("\nTransformation A" + str(number))
    print(A)

    print("T(e1) =", A @ e1)
    print("T(e2) =", A @ e2)

    rank = np.linalg.matrix_rank(A)
    print("Rank =", rank)

    if rank < 2:
        print("Information is lost.")
    else:
        print("No dimension is lost.")

    transformed = transform_image(img, A)

    plt.figure(figsize=(6, 4))
    plt.imshow(transformed)
    plt.title("Transformation A" + str(number))
    plt.axis("off")
    plt.show()

# A5 is true projection onto the x-axis.
# It has rank 1, so one dimension/information is lost.
