# PRODIGY_CS_02
This code offers a simple yet effective way to encrypt and decrypt images by manipulating pixel values. You can experiment with different keys and operations to make the encryption stronger or add layers of complexity.

### The Encryption and Decryption Process

The image encryption tool uses a simple yet effective technique involving pixel manipulation and the XOR bitwise operation. Let’s break down how this works step by step.

#### 1. **Loading the Image**

```python
def load_image(image_path):
    return Image.open(image_path)
```
- **`Image.open(image_path)`**: This function from the `PIL` (Pillow) library loads an image from the specified file path and returns it as a Pillow `Image` object.

#### 2. **Converting the Image to a Numpy Array**

```python
pixels = np.array(image)
```
- **Numpy Array**: The image is converted into a numpy array. This array represents the image as a grid of pixel values. Each pixel in a grayscale image is typically an integer between 0 and 255 (where 0 is black and 255 is white). In a color image, each pixel might have three components (Red, Green, Blue), each ranging from 0 to 255.

#### 3. **Encryption using XOR Operation**

```python
encrypted_pixels = pixels ^ key
```
- **XOR Operation**: XOR (exclusive OR) is a bitwise operation that takes two binary inputs and returns `1` if the inputs are different, and `0` if they are the same. Here, each pixel value in the numpy array is XORed with the key (which is `42` in this case).
  
  - **Example**: Consider a pixel value of `200` (in binary: `11001000`) and a key of `42` (in binary: `00101010`). 
    - XOR: `11001000` (200)
          ^ `00101010` (42)
          = `11100010` (226)
  - The pixel value `200` is transformed into `226` through the XOR operation.

- **Effect of XOR**: XORing effectively scrambles the pixel values. Since XOR is a reversible operation, applying XOR with the same key again during decryption will restore the original pixel values.

#### 4. **Converting the Encrypted Array Back to an Image**

```python
encrypted_image = Image.fromarray(encrypted_pixels)
```
- **Image Reconstruction**: The numpy array (which now contains the encrypted pixel values) is converted back into an image using `Image.fromarray()`. This function takes a numpy array and converts it into a Pillow `Image` object that can be saved or displayed.

#### 5. **Decrypting the Image**

```python
decrypted_pixels = encrypted_pixels ^ key
```
- **Reversing XOR**: To decrypt the image, the XOR operation is applied again with the same key. Since XOR is symmetric:
  - `A ^ B ^ B = A`
  - Thus, if you XOR the encrypted pixel value with the key, you get back the original pixel value.

- **Example**:
  - Encrypted pixel value: `226` (in binary: `11100010`)
  - Key: `42` (in binary: `00101010`)
  - XOR: `11100010` (226)
        ^ `00101010` (42)
        = `11001000` (200) — the original pixel value.

- The pixel values are restored to their original state, resulting in the original image.

#### 6. **Saving or Displaying the Images**

```python
save_image(encrypted_image, "encrypted_image.png")
save_image(decrypted_image, "decrypted_image.png")
```
- **Saving**: The encrypted and decrypted images are saved to disk as files (`encrypted_image.png` and `decrypted_image.png`).

- **Displaying**: The `show()` function is used to open the image in the default image viewer on your system.

### Summary

- **XOR as Encryption**: The XOR operation is a fundamental tool in many encryption algorithms due to its simplicity and reversibility. By applying XOR with a key, the pixel values in the image are scrambled, making the image unreadable without the key.

- **Reversibility**: The same XOR operation is applied during decryption to restore the original pixel values, demonstrating the symmetric nature of the XOR operation.

- **Practical Usage**: While this is a simple example, more complex encryption schemes in real-world scenarios often involve multiple layers of XOR operations combined with other cryptographic techniques.

This method, while educational and effective for basic encryption, is not secure against advanced attacks and should not be used for protecting sensitive data in practice.
