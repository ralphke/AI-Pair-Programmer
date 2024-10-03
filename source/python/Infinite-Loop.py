from PIL import Image, ImageDraw

# Create an image with white background
width, height = 200, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple Möbius strip-like loop
draw.ellipse((50, 50, 150, 150), outline='black', width=4)
draw.line((100, 50, 100, 35), fill='black', width=4)
draw.line((100, 150, 100, 165), fill='black', width=4)

# Save the image
image.save('infinite_loop.png')