from PIL import Image

image = Image.open("monro.jpg")
red_image, green_image, blue_image = image.convert("RGB").split()

cropped_red_image_1 = red_image.crop((50, 0, red_image.width, red_image.height))
cropped_red_image_2 = red_image.crop((25, 0, red_image.width-25, red_image.height))
red_image = Image.blend(cropped_red_image_1, cropped_red_image_2, 0.5)

cropped_blue_image_1 = blue_image.crop((0, 0, blue_image.width-50, blue_image.height))
cropped_blue_image_2 = blue_image.crop((25, 0, blue_image.width-25, blue_image.height))
blue_image = Image.blend(cropped_blue_image_1, cropped_blue_image_2, 0.5)

green_image = green_image.crop((25, 0, green_image.width-25, green_image.height))

end_image = Image.merge("RGB", (red_image, green_image, blue_image))
end_image.thumbnail((80, 80))
end_image.save("avatar.jpg")

