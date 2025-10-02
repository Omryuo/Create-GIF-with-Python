import imageio.v3 as iio

# List your images here
filenames = ['images/team-pic1.png', 'images/team-pic2.png']
images = []

# Read images
for filename in filenames:
    images.append(iio.imread(filename))

# Create GIF
iio.imwrite('team.gif', images, duration=500, loop=0)

