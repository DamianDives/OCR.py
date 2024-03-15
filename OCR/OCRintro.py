from PIL import Image

im_file = "data/japanese.png"

im = Image.open(im_file)
print ( im )
# im.show() ( This will show the image in normal form)
im.rotate(180).show()
im.save("temp/japanese.png")