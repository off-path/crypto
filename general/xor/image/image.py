from PIL import Image, ImageChops

i = Image.open("lemur.png")
i2 = Image.open("flag.png")
res = ImageChops.difference(i,i2)
res.show()
res.save("vamos.png")

#crypto{X0Rly_n0t!}