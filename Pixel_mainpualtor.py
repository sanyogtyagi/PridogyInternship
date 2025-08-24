from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, shift_value):
    # Load image
    image = Image.open(input_path)
    # Convert to numpy array
    data = np.array(image)
    # Add shift value to pixel data with wrap-around (mod 256)
    encrypted_data = (data + shift_value) % 256
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, shift_value):
    # Load encrypted image
    image = Image.open(input_path)
    # Convert to numpy array
    data = np.array(image)
    # Subtract shift value from pixel data with wrap-around
    decrypted_data = (data - shift_value) % 256
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Simple Image Encryption/Decryption Tool")
    choice = input("Enter 'encrypt' or 'decrypt': ").strip().lower()
    input_image_path = input("Enter path to the image: ")
    output_image_path = input("Enter output path for the result: ")
    shift_value = int(input("Enter shift value (integer): "))

    if choice == 'encrypt':
        encrypt_image(input_image_path, output_image_path, shift_value)
    elif choice == 'decrypt':
        decrypt_image(input_image_path, output_image_path, shift_value)
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

# if __name__ == "__main__":
#     main()
