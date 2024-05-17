from PIL import Image

def pixelate(image_path, output_path, pixelation_level):
    image = Image.open(image_path)
    image_small = image.resize(
        (image.width // pixelation_level, image.height // pixelation_level),
        resample=Image.NEAREST
    )
    result = image_small.resize(image.size, Image.NEAREST)
    result.save(output_path)

def main():
    image_path = 'poster.jpg'  # Path to your input image
    output_paths = [
        'poster_pixelated_1.jpg',
        'poster_pixelated_2.jpg',
        'poster_pixelated_3.jpg',
        'poster_pixelated_4.jpg',
        'poster_pixelated_5.jpg'
    ]
    pixelation_levels = [10, 20, 30, 40, 50]  # Different levels of pixelation

    for output_path, level in zip(output_paths, pixelation_levels):
        pixelate(image_path, output_path, level)
        print(f'Created {output_path} with pixelation level {level}')

if __name__ == '__main__':
    main()
