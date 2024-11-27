from math import floor
# from tkinter import *
import cv2 
import time
from math import floor, radians, cos, sin

import numpy as np

class Ball():
    
    def __init__(self, screen_width, screen_height):
        self.cam = cv2.VideoCapture(0)
        self.x = 0
        self.y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        self.winner=False
        

        # Parametri pallina
        self.raggio = 20
        self.colore_pallina1 = (255, 0, 0)  # Blu in BGR
        self.colore_pallina2 = (0,0,255) # Rosso in BGR
    
    # loop che continua ad aggioranre il frame della telecamera   
    def cv2Loop(self, camera):
        while self.running:
            # Legge un frame dalla telecamera
            if camera: 
                ret, frame = self.cam.read()
            else:
                ret, frame = (True, np.ones((self.screen_height, self.screen_width, 3), dtype=np.uint8) * 245)  
            
            
          
            if ret:
                # Ridimensiona il frame alle dimensioni della finestra
                frame = cv2.flip(frame, 1)
                frame = cv2.resize(frame, (self.screen_width, self.screen_height))
           
            # Crea una finestra con il frame e fa in modo che sia fullscreen
            cv2.namedWindow('Camera',cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('Camera',cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.setWindowProperty('Camera', cv2.WND_PROP_TOPMOST, 1)
            
            # Disegna una pallina sul frame (ad esempio, una pallina rossa al centro)
            centro_x, centro_y = frame.shape[1] // 2, frame.shape[0] // 2
            
            # Disegna una pallina blu fissa al centro dello schermo
            cv2.circle(frame, (centro_x, centro_y), self.raggio, self.colore_pallina1, -1)
            # Disegna una pallina rossa che si muove in base alle coordinate ricevute
            cv2.circle(frame, (self.x, self.y), self.raggio, self.colore_pallina2, -1)
            
            # frase di vittoria in caso di contatto tra le due palline
            if self.winner:
                scale = abs(int(time.time() * 1000) % 2000 - 1000) / 1000.0
                font_scale = 4 + 2 * scale
                thickness = 8 + int(6 * scale)
                cv2.putText(frame, 'Hai vinto!!', (centro_x - 350, centro_y - 150), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (220, 188, 0), thickness, cv2.LINE_AA)
                
            # Mostra il frame nella finestra
            cv2.imshow('Camera', frame)
            
            # modo per chiudere la finestra "forzatamente" in caso ci siano problemi con il client
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break   
        
        # quando il ciclo si interrompe, rilascia la telecamera e chiude la finestra 
        self.cam.release()
        cv2.destroyAllWindows()
        
    # funzione per muovere la pallina   
    def update_coords(self, x, y):
        self.x = x
        self.y = y
    
    
    # funzione per fermare 
    def close(self):
        self.running = False
    
    # funzione per controllare se la pallina è in movimento
    def is_running(self):
        return self.running

    