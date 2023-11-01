import os

import cv2

# Define the directory containing the images
img_dir = "path/to/directory"

# Define the output directory for the processed images
out_dir = "path/to/output/directory"

# Define the image size for cropping
crop_size = (224, 224)

# Loop through each image in the directory
for img_file in os.listdir(img_dir):
  # Read the image
  img_path = os.path.join(img_dir, img_file)
  img = cv2.imread(img_path)

  # Flip the image horizontally
  flipped_img = cv2.flip(img, 1)

  # Rotate the image by 90 degrees
  (h, w) = img.shape[:2]
  center = (w // 2, h // 2)
  M = cv2.getRotationMatrix2D(center, 90, 1.0)
  rotated_img = cv2.warpAffine(img, M, (w, h))

  # Crop the image
  (h, w) = img.shape[:2]
  (c_h, c_w) = crop_size
  x = (w - c_w) // 2
  y = (h - c_h) // 2
  cropped_img = img[y:y+c_h, x:x+c_w]

  # Write the processed images to the output directory
  cv2.imwrite(os.path.join(out_dir, "flipped_" + img_file), flipped_img)
  cv2.imwrite(os.path.join(out_dir, "rotated_" + img_file), rotated_img)
  cv2.imwrite(os.path.join(out_dir, "cropped_" + img_file), cropped_img)
