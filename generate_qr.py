import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

murali_printers = qrcode.make("https://www.google.com/maps/dir/14.6700255,77.6027827/Murali+Offset+Printers,+opp.+DMS+Offset+Printers,+Kamalanagar,+Anantapur,+Andhra+Pradesh+515001,+India/@14.6754172,77.5924037,15z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3bb14adb8d56a593:0xe4274797cacbccb7!2m2!1d77.6005997!2d14.680588?entry=ttu")
murali_printers.save("murali_printers.png", scale = 8)

b = decode(Image.open("murali_printers.png"))
print(b[0].data.decode("ascii"))
