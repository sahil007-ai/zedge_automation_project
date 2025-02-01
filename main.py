from PIL import Image, ImageDraw, ImageFont

def quoteGen():
    return "everything will work the you want it to be."

def size(height = 1080, width= 2340):

    s = (height, width)
    return s

def main():
    height = 1080
    width = 2340

    # creates a new image
    black = Image.new('L',size(height,width), 0)

    # add 2d graphic to the image
    draw = ImageDraw.Draw(black)

    # add text to the image
    draw.text(size(height//2,width//2) ,f"{quoteGen()}","white")

    # saves the image
    black.save("black.jpg")

main()

if __name__ == '__main__':
    print('khatam')

