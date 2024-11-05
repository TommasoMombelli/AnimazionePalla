import socket
import segno
import io
import matplotlib.pyplot as plt
from PIL import Image

def qr_code():
    # Ottenimento dell'indirizzo IP del server
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    # Creazione del QR code
    qrcode = segno.make_qr(IPAddr)

    # Salvataggio del QR code in un buffer
    buffer = io.BytesIO()
    qrcode.save(buffer, kind='png', scale=13)
    buffer.seek(0)

    # Visualizzazione del QR code
    img = Image.open(buffer)
    
    # Creazione della figura di Matplotlib
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off') 
    
    
    # Modifica del titolo della finestra
    fig.canvas.manager.set_window_title("QR Code per l'indirizzo IP")

    # Mostra la figura
    plt.show()

if __name__ == '__main__':
    qr_code()



