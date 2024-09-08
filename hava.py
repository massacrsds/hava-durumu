import tkinter as tk
from tkinter import simpledialog

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Python Tkinter Penceresi")
pencere.geometry("400x300")  # Pencere boyutunu ayarlama (genişlik x yükseklik)

# Etiket ekleme
etiket = tk.Label(pencere, text="Merhaba, Dünya!")
etiket.pack()

# Hava durumu kontrol fonksiyonu
def hava_durumu_kontrol():
    hava_durumu = ""  # Buraya hava durumu bilgisini ekleyin
    if hava_durumu == 'yağmurlu':
        sonuc = "Dışarı çıkarken şemsiyenizi almayı unutmayınız"
    elif hava_durumu == 'sıcak':
        sonuc = "Sıcaklık uyarısı! Dikkatli olmanız önerilir"
    elif hava_durumu == 'yoğun kar':
        sonuc = "Yoğun kara dikkat"
    else:
        sonuc = "Bugün normal"
    
    # Sonucu etiket olarak göster
    sonuc_etiketi.config(text=sonuc)

# Ülke ekleme fonksiyonu
def ülke_ekleme():
    ülke = simpledialog.askstring("Ülke Ekle", "Lütfen bir ülke giriniz:")
    if ülke:
        ülke_etiketi.config(text=ülke)

# Buton ekleme
buton_hava = tk.Button(pencere, text="Hava Durumunu Kontrol Et", command=hava_durumu_kontrol)
buton_hava.pack()
buton_ülke = tk.Button(pencere, text="Ülke Ekleyin", command=ülke_ekleme)
buton_ülke.pack()

# Ülke etiketi (en üstte gösterilecek)
ülke_etiketi = tk.Label(pencere, text="", font=("Helvetica", 16))
ülke_etiketi.pack()

# Sonuç etiketi
sonuc_etiketi = tk.Label(pencere, text="")
sonuc_etiketi.pack()

# Pencereyi çalıştırma
pencere.mainloop()
