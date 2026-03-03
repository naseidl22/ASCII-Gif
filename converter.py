from PIL import Image, ImageSequence, ImageFont, ImageDraw
import os
import sys

HTW_R = 1.75

ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def pixel_to_ascii(pixel_value):
    scale = pixel_value / 255
    index = int(scale * (len(ascii_chars) - 1))
    return ascii_chars[index]

def image_to_ascii(image, scale):
    width, height = image.size
    new_width = int(width * scale)
    new_height = int(height / HTW_R * scale)

    image = image.resize((new_width, new_height))
    pixels = image.getdata()

    ascii_str = ''.join([pixel_to_ascii(p) for p in pixels])

    ascii_art = '\n'.join(
        [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
    )

    return ascii_art


def ascii_to_image(ascii_str, font_size=8):
    lines = ascii_str.splitlines()
    width = max(len(line) for line in lines)
    height = len(lines)

    # EXE-safe font loading
    font_path = resource_path("fonts/UbuntuMono-R.ttf")
    font = ImageFont.truetype(font_path, size=font_size)

    img = Image.new("RGB", (width * font_size // 2, height * font_size), "white")
    draw = ImageDraw.Draw(img)

    for i, line in enumerate(lines):
        draw.text((0, i * font_size), line, font=font, fill="black")

    return img

def convert_gif(input_path, output_path, scale=0.65, font_size=8, progress_callback=None):

    gif = Image.open(input_path)

    duration = gif.info.get("duration", 40)
    loop = gif.info.get("loop", 0)

    ascii_frames = []

    total_frames = gif.n_frames

    for i in range(total_frames):
        gif.seek(i)

        frame = gif.convert("RGBA")
        gray = frame.convert("L")

        ascii_art = image_to_ascii(gray, scale)
        ascii_img = ascii_to_image(ascii_art, font_size)

        ascii_frames.append(ascii_img)

        if progress_callback:
            progress = int((i + 1) / total_frames * 100)
            progress_callback(progress)

    print("Frame count:", len(ascii_frames))

    ascii_frames[0].save(
        output_path,
        save_all=True,
        append_images=ascii_frames[1:],
        duration=[duration] * len(ascii_frames),
        loop=loop,
        disposal=2,
        optimize=False
    )