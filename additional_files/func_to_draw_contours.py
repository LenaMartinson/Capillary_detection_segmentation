import cv2
import numpy as np


def create_image_from_txt(txt_file_path, image_size):
    # Initialize an empty image with zeros
    image = np.zeros((image_size[0], image_size[1]), dtype=np.uint8)

    with open(txt_file_path, 'r') as file:
        for line in file:
            numbers = [float(num) for num in line.strip().split()]
            
            # Extract class (value for pixels)
            pixel_value = int(numbers[0]) + 254
            
            # Loop through the (x, y) coordinates in pairs
            for i in range(1, len(numbers) - 1, 2):
                # Denormalize x and y coordinates
                x = int(numbers[i] * image_size[1])
                y = int(numbers[i + 1] * image_size[0])
                
                # Set the pixel value for the specified coordinates
                image[y, x] = pixel_value

    return image


def save_contours(picture_name, label_name=None):
    # Input paths
    if label_name is None:
        label_name = picture_name
    image_path = '/home/martinson/data_2/images_seg/' + picture_name + '.png'
    label_path = '/home/martinson/data_2/labels_seg/' + label_name + '.txt'
    
    # Load the image and ground truth label
    image = cv2.imread(image_path)
    ground_truth = create_image_from_txt(label_path, image_size=image.shape)
    ground_truth = cv2.cvtColor(ground_truth,cv2.COLOR_GRAY2RGB)
    
    # # Colors for visualization (B, G, R)
    ground_truth_color_sharp = (0, 0, 255)  # (SHARP)
    ground_truth_color_blurry = (0, 255, 0)  # (BLURRY)
    
    # # Apply the colors for visualization
    predicted_truth_colored_sharp = ((ground_truth == 255) * ground_truth_color_sharp)
    predicted_truth_colored_blurry = ((ground_truth == 254) * ground_truth_color_blurry)
    # # predicted_mask_colored = cv2.merge((predicted_mask == 255) * prediction_color)
    
    # # Blend the original image with the ground truth and prediction
    overlayed_image = cv2.addWeighted(predicted_truth_colored_sharp, 1, 
                                      predicted_truth_colored_blurry, 1, 0, dtype=cv2.CV_64F)
    overlayed_image = cv2.addWeighted(image, 0.4, overlayed_image, 1, 0, dtype=cv2.CV_64F)

    cv2.imwrite("viz_" + picture_name + ".png", overlayed_image)