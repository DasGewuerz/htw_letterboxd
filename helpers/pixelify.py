from PIL import Image
import os

def pixelate(image_path, output_path, pixelation_level):
    image = Image.open(image_path)
    image_small = image.resize(
        (image.width // pixelation_level, image.height // pixelation_level),
        resample=Image.NEAREST
    )
    result = image_small.resize(image.size, Image.NEAREST)
    result.save(output_path)

def main():
    folder_path = '/Users/anischaibi/Downloads/development/htw_letterboxd/posters'
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") and not filename.startswith('pixel'):
            image_path = f'{folder_path}/{filename}'
            output_paths = [
                f'{folder_path}/pixel10_{filename}',
                f'{folder_path}/pixel20_{filename}',
                f'{folder_path}/pixel30_{filename}',
                f'{folder_path}/pixel40_{filename}',
                f'{folder_path}/pixel50_{filename}'
            ]
            pixelation_levels = [10, 20, 30, 40, 50]

        for output_path, level in zip(output_paths, pixelation_levels):
            pixelate(image_path, output_path, level)
            print(f'Created {output_path} with pixelation level {level}')

if __name__ == '__main__':
    main()
