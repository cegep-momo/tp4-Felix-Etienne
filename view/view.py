from view.LCD1602 import lcd1602

class View :
    def __init__(self):
        lcd1602.init_lcd(0x27, 1)
        
    def afficher_message_LCD(self, x, y, message):
        lcd1602.write(x, y, message)
        
    def clear_LCD(self):
        lcd1602.clear()
        