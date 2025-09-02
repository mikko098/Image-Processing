import cv2
import numpy as np

padam = cv2.imread("mykids.jpg")
padam = cv2.cvtColor(padam, cv2.COLOR_BGR2GRAY)
sobelpadamx = cv2.Sobel(padam, cv2.CV_64F, 1, 0, ksize = 3)
sobelpadamy = cv2.Sobel(padam, cv2.CV_64F, 0, 1, ksize = 3)
laplacian = cv2.Laplacian(padam, cv2.CV_64F)
test = np.sqrt(sobelpadamx ** 2 * sobelpadamy ** 2)
sobelorumich = cv2.bitwise_or(sobelpadamx, sobelpadamy)

# Dictionary mapping keys to image names and image variables
image_map = {
    ord('p'): ("Original", padam),
    ord('t'): ("Test", test),
    ord('l'): ("Laplacian", laplacian),
    ord('y'): ("Sobel Y", sobelpadamy),
    ord('x'): ("Sobel X", sobelpadamx),
    ord('o'): ("Sobel Orumich", sobelorumich),
    ord('q'): ("Quit", None)
}

current_key = ord('p')  # Start with original image

while True:
    if current_key in image_map:
        title, img = image_map[current_key]
        if img is not None:
            cv2.imshow("window1", img)
        else:
            break  # Quit if None

    key = cv2.waitKey(0) & 0xFF  # Wait for a key press
    if key in image_map:
        current_key = key
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
