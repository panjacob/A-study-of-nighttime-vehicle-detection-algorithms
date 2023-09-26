import cv2

# Load the image
image = cv2.imread('wykres_czujnik_original_kopia.png')

# Define the x-coordinate for the vertical line
x = 365  # Adjust this value according to your requirements

# Define line parameters
line_thickness = 2  # Adjust the line thickness as needed
line_length = image.shape[0]  # Set the line length to match the height of the image

# Define stripe parameters
stripe_width = 7  # Adjust the width of each stripe
stripe_color1 = (255, 0, 0)  # BGR color for the first stripe (red in this example)

# Draw a vertical striped line with alternating colors
for y in range(16, line_length - 55, stripe_width * 2):
    cv2.line(image, (x, y), (x, y + stripe_width), stripe_color1, line_thickness)

# Save the image with the striped line
cv2.imwrite('wykres_czujnik.png', image)

# Display the image with the striped line (optional)
cv2.imshow('Image with Striped Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
