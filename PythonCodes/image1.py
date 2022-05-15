# # Third party modules
# import numpy
# from PIL import Image


# def get_image(image_path):
#     """Get a numpy array of an image so that one can access values[x][y]."""
#     image = Image.open(image_path, "r")
#     width, height = image.size
#     pixel_values = list(image.getdata())
#     image = image.convert("RGB")
#     if image.mode == "RGB":
#         channels = 3
#     elif image.mode == "L":
#         channels = 1
#     else:
#         print("Unknown mode: %s" % image.mode)
#         return None
#     pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
#     return pixel_values


# # image = get_image("C:\Users\Shreyansh Jain\Downloads\wp4676584-4k-pc-wallpapers.jpg")
# image = "C:/Users/Shreyansh Jain/Downloads/png-clipart-light-rgb-color-model-cmyk-color-model-additive-color-rgb-blue-color.png"
# image = get_image(image)
# print(image[0])
# print(image.shape)
# # from PIL import Image

# # img = Image.open(
# #     'C:/Users/Shreyansh Jain/Downloads/ILTQq.png')
# # imgWidth, imgHeight = img.size
# # img = img.convert("RGB")
# # print(3, img.mode)
# # imgdata = img.getdata()

# # x_pos = 0
# # y_pos = 1

# # pixel_value = []
# # x = []
# # y = []

# # for item in imgdata:
# #     if (x_pos) == imgWidth:
# #         x_pos = 1
# #         y_pos += 1
# #     else:
# #         x_pos += 1

# #     if item[3] != 0:
# #         pixel_value.append(item[2])
# #         x.append(x_pos)
# #         y.append(y_pos)

# # pixel_value, x, y = zip(*sorted(zip(pixel_value, x, y), reverse=True))

# # print(f'{pixel_value}\n{x}\n{y}')
import os
import sys
from PIL import Image

# define a function for
# compressing an image


def compressMe(file, verbose=False):

    # Get the path of the file
    filepath = os.path.join(os.getcwd(),
                            file)

    # open the image
    picture = Image.open(filepath)

    # Save the picture with desired quality
    # To change the quality of image,
    # set the quality variable at
    # your desired level, The more
    # the value of quality variable
    # and lesser the compression
    picture.save("Compressed_"+file,
                 "JPEG",
                 optimize=True,
                 quality=10)
    return

# Define a main function


def main():

    verbose = False

    # checks for verbose flag
    if (len(sys.argv) > 1):

        if (sys.argv[1].lower() == "-v"):
            verbose = True

    # finds current working dir
    cwd = os.getcwd()

    formats = ('.jpg', '.jpeg')

    # looping through all the files
    # in a current directory
    for file in os.listdir(cwd):

        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file, verbose)

    print("Done")


# Driver code
if __name__ == "__main__":
    main()
