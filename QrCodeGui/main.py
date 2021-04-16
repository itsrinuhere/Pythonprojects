import qrcode
from PIL import Image
face = Image.open('logo.jpg')
qr= qrcode.QRCode(
                  version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size = 50,
                  border = 2)
val = input("PLEASE ENTER URL\n>> ")
qr.add_data(val)
qr.make(fit=True)
img = qr.make_image(fill_color="black",black_color="white").convert('RGB')
pos = ((img.size[0] - face.size[0]) // 2, (img.size[1] - face.size[1]) // 2)
img.paste(face, pos)
vars = input("\n>>Enter name for file")
print("\nwant yout to save file")
ch = input("\n>>?'Y' || 'y' or N || n")
if ch == 'y' or ch =='Y':
  #print("File saved as " img.save('0'+vars+'.png'))
  img.save('01'+vars+'.png')
#code Developed by srinivas
