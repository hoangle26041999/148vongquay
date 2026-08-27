from PIL import Image
import sys

# Mở logo
img = Image.open(r'd:\LUMI-HOME\148vongquay\logo.jpg').convert('RGBA')
pixels = img.load()
w, h = img.size

# Ngưỡng: pixel trắng nếu R,G,B đều > threshold
threshold = 235

new_pixels = []
for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        # Nếu gần trắng -> xóa (alpha=0)
        if r > threshold and g > threshold and b > threshold:
            new_pixels.append((255, 255, 255, 0))
        else:
            # Giữ nguyên nhưng tăng saturation nhẹ để bớt trắng viền
            new_pixels.append((r, g, b, a))

img.putdata(new_pixels)
img.save(r'd:\LUMI-HOME\148vongquay\logo.png', 'PNG')
print(f'Done: {w}x{h}')