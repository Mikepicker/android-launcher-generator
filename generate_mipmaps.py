import os, sys
from PIL import Image

def usage():
    print('Usage: python generate_mipmaps.py <image_file>')

# Check args
if len(sys.argv) != 2:
    usage()
    exit()

# Create res directory
if not os.path.exists('res'):
    os.makedirs('res')

# Create mipmaps directories
if not os.path.exists('res/mipmap-mdpi'):
    os.makedirs('res/mipmap-mdpi')
if not os.path.exists('res/mipmap-hdpi'):
    os.makedirs('res/mipmap-hdpi')
if not os.path.exists('res/mipmap-xhdpi'):
    os.makedirs('res/mipmap-xhdpi')
if not os.path.exists('res/mipmap-xxhdpi'):
    os.makedirs('res/mipmap-xxhdpi')
if not os.path.exists('res/mipmap-xxxhdpi'):
    os.makedirs('res/mipmap-xxxhdpi')

# Generate mipmaps
infile = sys.argv[1]
try:
    im = Image.open(infile)
except IOError:
    print("Unable to read file: '%s'" % infile)


# Generate xxxhdpi
size = 192, 192
im.thumbnail(size, Image.ANTIALIAS)
im.save('res/mipmap-xxxhdpi/ic_launcher.png')

# Generate xxhdpi
size = 144, 144 
im.thumbnail(size, Image.ANTIALIAS)
im.save('res/mipmap-xxhdpi/ic_launcher.png')

# Generate xhdpi
size = 96, 96 
im.thumbnail(size, Image.ANTIALIAS)
im.save('res/mipmap-xhdpi/ic_launcher.png')

# Generate hdpi
size = 72, 72
im.thumbnail(size, Image.ANTIALIAS)
im.save('res/mipmap-hdpi/ic_launcher.png')

# Generate mdpi
size = 48, 48
im.thumbnail(size, Image.ANTIALIAS)
im.save('res/mipmap-mdpi/ic_launcher.png')
