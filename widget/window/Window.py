import tkinter as tk
from data.renkler import RENKLER
from data.geometri import GEOMETRI

class Window:
    """
    Tkinter window nesnesi yaratan class.
    Window nesnesi root yani en temel nesnedir.
    """

    # __init__ metodunda tkinter window yaratalım
    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.configure(bg=RENKLER.SIYAH)
        self.yukseklik_ayarla()

    # tkinter window başlaması için
    def start_window(self):
        self.window.mainloop()

    def yukseklik_ayarla(self):
        w, h = GEOMETRI.ANA_SAYFA_GENISLIK, GEOMETRI.ANA_SAYFA_YUKSEKLIK
        self.window.geometry('%dx%d' % (w, h))

