import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def extract_colors(image_path, num_colors=5):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((-1, 3))  # Flatten the image (pixels) for clustering

    # Use KMeans clustering to find the dominant colors
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(image)

    # Get the cluster centers (dominant colors)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

def plot_color_palette(colors):
    # Create a figure for displaying the color palette
    plt.figure(figsize=(8, 2))
    plt.title("Color Palette")

    # Create a color patch for each extracted color
    for i, color in enumerate(colors):
        plt.subplot(1, len(colors), i + 1)
        plt.imshow([[color / 255]])
        plt.axis('off')

    plt.show()

def main():
    # Specify the path to the input image
    image_path = 'image.png'

    # Extract the dominant colors
    print("Extracting colors from the image...")
    colors = extract_colors(image_path)

    # Display the color palette
    print("Displaying the color palette...")
    plot_color_palette(colors)

if __name__ == "__main__":
    main()
