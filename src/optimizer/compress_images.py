from PIL import Image
import os


def compress_png(image_path, output_path, output_size, quality):
    with Image.open(image_path) as img:
        width, height = img.size
        new_width = int(width * (output_size / height))
        # Resize the image
        img = img.resize((new_width, output_size), resample=Image.LANCZOS)
        # Compress the image
        img.save(output_path, quality=quality, optimize=True)


def compress_images(image_quality: int, compress_after: int):
    images_path = os.path.abspath('temp/Images/')
    images = [images_path + "\\" + i for i in os.listdir(images_path)]
    print(os.path.getsize(images[0]))

    for image in images:
        if os.path.getsize(image) > compress_after*1000:
            compress_png(image, image, 720, image_quality)

    print("Images compressed!")
