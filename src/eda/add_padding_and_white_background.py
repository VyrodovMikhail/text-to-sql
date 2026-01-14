from PIL import Image
from pathlib import Path
import tqdm

images_path = Path("input_images")
output_dir = Path("result_images")
png_files = list(images_path.glob("*.png"))

for png_file in tqdm.tqdm(png_files):
    img = Image.open(png_file)

    # Calculate 10% border on EACH side (20% total per dimension)
    border_width = img.width // 10
    border_height = img.height // 10

    # New dimensions: original + 10% on left + 10% on right
    new_img = Image.new(
        "RGB", (img.width + 2 * border_width, img.height + 2 * border_height), "white"
    )

    # Handle transparency
    if img.mode in ("RGBA", "LA", "P"):
        background = Image.new("RGB", img.size, "white")
        if img.mode == "P" and "transparency" in img.info:
            img = img.convert("RGBA")
        if img.mode in ("RGBA", "LA"):
            background.paste(img, (0, 0), img)
        else:
            background.paste(img, (0, 0))
        img = background
    else:
        img = img.convert("RGB")

    # Paste at position (border_width, border_height) to center it
    new_img.paste(img, (border_width, border_height))

    # Save
    new_img.save(output_dir / png_file.name)
