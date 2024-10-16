import socket
import segno
import io
import matplotlib.pyplot as plt
from PIL import Image



def qr_code():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    qrcode = segno.make_qr(IPAddr)
    buffer = io.BytesIO()
    qrcode.save(buffer, kind='png', scale=13)
    buffer.seek(0)

    img = Image.open(buffer)
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()  

if __name__ == '__main__':
    qr_code()


