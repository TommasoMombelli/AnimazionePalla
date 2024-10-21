import socket
import segno
import io
import matplotlib.pyplot as plt
from PIL import Image



def qr_code():

    # ottenimento dell'indirizzo IP del server
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    # creazione del qr code
    qrcode = segno.make_qr(IPAddr)

    # salvataggio del qr code in un buffer
    buffer = io.BytesIO()
    qrcode.save(buffer, kind='png', scale=13)
    buffer.seek(0)

    # visualizzazione del qr code
    img = Image.open(buffer)
    plt.imshow(img)
    plt.axis('off') 
    plt.show()  

if __name__ == '__main__':
    qr_code()


