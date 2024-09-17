import cv2

# Path to the image
pat = r'C:\Users\gollu\Desktop\Pics\Sank.jpg'

# Read the image in grayscale
img1 = cv2.imread(pat, 0)

# Resize the image to the desired dimensions
img1 = cv2.resize(img1, (560, 560))

# Display the image
cv2.imshow('converter', img1)

# Wait indefinitely for a key press to close the window
k=cv2.waitKey(0)
if k==ord('s'):
    cv2.imwrite(r"C:\Users\gollu\Desktop\Pics\dupli.jpg",img1)
else :
    pass

# Destroy all windows
cv2.destroyAllWindows()
