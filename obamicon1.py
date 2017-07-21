from PIL import Image

# RGB values for recoloring.
darkestPink = (204, 0, 0)
darkerPink= (255, 128, 0)
lighterPink = (255, 255, 0)
lightestPink = (255, 255, 102)

# Import image.
my_image = Image.open("emma.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

#recolored = [] #list that will hold the pixel data for the new image.
recolored = []

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

pixelColor=0
def intensify():
    for i in image_list:
        pixelColor=(i[0]+ i[1] + i[2])
        if pixelColor <182:
            recolored.append(darkestPink)
            # recolored[0] = 0
            # recolored[1] = 51
            # recolored[2]= 76
        elif 182<=pixelColor<364:
            recolored.append(darkerPink)
            # recolored[0] = 217
            # recolored[1] = 26
            # recolored[2] = 33
        elif 364<=pixelColor<546:
            recolored.append(lighterPink)
            # recolored[0] = 112
            # recolored[1] = 150
            # recolored[2] = 158
        elif pixelColor>=546:
            recolored.append(lightestPink)
            # recolored[0] = 252
            # recolored[1] = 227
            # recolored[2] = 166
    return recolored


intensify()

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
