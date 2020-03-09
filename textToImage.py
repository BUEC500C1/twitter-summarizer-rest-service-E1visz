from twittwer_api import Get_twitter
from PIL import Image, ImageDraw, ImageFont
import os
import re


def textToImg(TwText,hashtag,num):
  img = Image.new('RGB', (1000, 450), color = (0, 0, 0))
  draw = ImageDraw.Draw(img)
  Font1 = ImageFont.truetype("font.otf", 36)
  Font2 = ImageFont.truetype("font.otf", 14)

  #modify the input text
  url_reg = r'[a-z]*[:.]+\S+'
  TwText = re.sub(url_reg, '', TwText)
  TwText = TwText.encode('ascii','ignore').decode('ascii')
  TwText = TwText.replace(". ", ".\n")
  TwText = TwText.replace(", ", ",\n")
  TwText = TwText.replace("! ", "!\n")
  TwText = TwText.replace("; ", ";\n")
  TwText = TwText.replace("? ", "?\n")
  TwText = TwText.replace("  ", " \n")

  draw.text((80,60), "#" + hashtag, fill=(255, 255, 255), font = Font1)
  draw.text((120,150), TwText, fill=(255, 255, 255), font = Font2)
  fileName = "img/" + hashtag + str(num) + ".png"
  img.save(fileName)


def setAllImg(hashtag):
  textArr = Get_twitter(hashtag)
  num = 1
  for text in textArr:
    textToImg(text, hashtag, num)
    num = num + 1


