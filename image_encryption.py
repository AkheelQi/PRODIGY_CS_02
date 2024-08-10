from PIL import Image
import numpy as np

# Function to load the image
def load_image(image_path):
    return Image.open("C:\Users\Muhammed Akheel\OneDrive\Desktop\Posts\input_image.png")

# Function to save the image
def save_image(image, image_path):
    image.save(image_path)

# Function to encrypt the image
def encrypt_image(image, key):
    # Convert the image to numpy array
    pixels = np.array(image)
    
    # Apply XOR operation between the pixel values and the key
    encrypted_pixels = pixels ^ key
    
    # Convert the numpy array back to an image
    encrypted_image = Image.fromarray(encrypted_pixels)
    
    return encrypted_image

# Function to decrypt the image
def decrypt_image(encrypted_image, key):
    # Convert the image to numpy array
    pixels = np.array(encrypted_image)
    
    # Apply XOR operation again to get the original image
    decrypted_pixels = pixels ^ key
    
    # Convert the numpy array back to an image
    decrypted_image = Image.fromarray(decrypted_pixels)
    
    return decrypted_image

# Example usage
if __name__ == "__main__":
    key = 42  # Simple encryption key, can be any integer

    # Load the image
    image_path = "input_image.png"
    image = load_image(image_path)

    # Encrypt the image
    encrypted_image = encrypt_image(image, key)
    encrypted_image.show()  # Display the encrypted image
    save_image(encrypted_image, "encrypted_image.png")

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image.show()  # Display the decrypted image
    save_image(decrypted_image, "decrypted_image.png")
