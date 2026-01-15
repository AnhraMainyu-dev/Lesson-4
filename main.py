from PIL import Image

image = Image.open("monro.jpg")
red_image, green_image, blue_image = image.convert("RGB").split()

coordinates_1 = (50, 0, red_image.width, red_image.height)
coordinates_2 = (25, 0, red_image.width-25, red_image.height)

cropped_red_image1 = red_image.crop(coordinates_1)
cropped_red_image2 = red_image.crop(coordinates_2)
red_blended_image = Image.blend(cropped_red_image1, cropped_red_image2, 0.7)

cropped_blue_image1 = blue_image.crop(coordinates_1)
cropped_blue_image2 = blue_image.crop(coordinates_2)
blue_blended_image = Image.blend(cropped_blue_image1, cropped_blue_image2, 0.7)

cropped_green_image1 = green_image.crop(coordinates_2)

end_image = Image.merge("RGB", (red_blended_image, blue_blended_image, cropped_green_image1))
end_image.thumbnail((80, 80))
end_image.save("avatar.jpg")
