from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def locate_text(image_path, target_text):
    # Perform OCR to get bounding box coordinates of the text
    img = Image.open(image_path)
    text_data = pytesseract.image_to_boxes(img)

    # Extracting bounding box coordinates
    box_coordinates = []
    for line in text_data.splitlines():
        _, x, y, w, h, _ = line.split()
        text = line.split()[-1]
        box_coordinates.append((int(x), int(y), int(w), int(h), text))
        print(text)

    # Find coordinates for the target text
    target_coordinates = [(x, y, w, h) for x, y, w, h, text in box_coordinates if text == target_text]

    return target_coordinates

def crop_image(image_path, coordinates, output_path, crop_width, crop_height):
    if not coordinates:
        print(f"Text not found: {target_text}")
        return

    # Open the original image
    img = Image.open(image_path)

    # Get the bounding box coordinates for the target text
    x, y, w, h = coordinates[0]

    # Crop the image based on the target text location
    cropped_img = img.crop((x, y, x + w, img.size[1]))

    # Save the cropped image
    cropped_img.save(output_path)

    # Re-crop the image with the specified width and height
    final_cropped_img = cropped_img.crop((0, 0, crop_width, crop_height))

    # Save the final cropped image
    final_cropped_img.save(output_path)

if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with the actual path to your image file
    input_image_path = 'src/test.png'

    # Replace 'IT - Cargo Van' with the target text you are looking for
    target_text = 'Cargo Van'

    # Replace 'path/to/your/output/image.jpg' with the desired output path
    output_image_path = 'src/Croppedimage.png'

    # Replace 100 and 200 with the desired width and height for the final cropped image
    final_width = 100
    final_height = 200

    # Locate text in the image
    text_coordinates = locate_text(input_image_path, target_text)

    # Crop and save the image based on the text location
    crop_image(input_image_path, text_coordinates, output_image_path, final_width, final_height)
    print(f"Image cropped successfully. Output saved at: {output_image_path}")
