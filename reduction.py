from PIL import Image

img = Image.open('image.jpg')

gray = img.convert('L')
gray.save('gray.jpg')

threshold = 128
binary = gray.point(lambda x: 0 if x < threshold else 255, '1')
binary.save('binary.jpg')