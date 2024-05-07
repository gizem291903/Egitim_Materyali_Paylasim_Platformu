import tkinter as tk
from tkinter import simpledialog, messagebox

class Öğrenci:
    def __init__(self, ad, kullanıcı_adı, şifre):
        self.ad = ad
        self.kullanıcı_adı = kullanıcı_adı
        self.şifre = şifre

class Öğretmen:
    def __init__(self, ad, soyad, branş):
        self.ad = ad
        self.soyad = soyad
        self.branş = branş

class Ders:
    def __init__(self, ad):
        self.ad = ad
        self.materyal = ""

class EğitimUygulaması:
    def __init__(self, kök):
        self.kök = kök
        self.kök.title("Eğitim Materyali Paylaşım Platformu")

        self.öğrenciler = [
            Öğrenci("Ahmet Yılmaz", "ahmet123", "123456"),
            Öğrenci("Ayşe Kaya", "ayse456", "abcdef"),
            Öğrenci("Mehmet Demir", "mehmet789", "qwerty"),
            Öğrenci("Zeynep Şahin", "zeynep321", "zxcvbn")
        ]

        self.öğretmenler = [
            Öğretmen("Ali", "Sönmez", "Matematik"),
            Öğretmen("Fatma", "Işıl", "Türkçe"),
            Öğretmen("Hasan", "Esin", "Fen Bilgisi"),
            Öğretmen("Zeynep", "Ergül", "Tarih")
        ]

        self.dersler = [
            Ders("Matematik"),
            Ders("Türkçe"),
            Ders("Fen Bilgisi"),
            Ders("Tarih")
        ]

        self.kullanıcı_adı_etiket = tk.Label(kök, text="Kullanıcı Adı:")
        self.kullanıcı_adı_etiket.grid(row=0, column=0)
        self.kullanıcı_adı_giriş = tk.Entry(kök)
        self.kullanıcı_adı_giriş.grid(row=0, column=1)

        self.şifre_etiket = tk.Label(kök, text="Şifre:")
        self.şifre_etiket.grid(row=1, column=0)
        self.şifre_giriş = tk.Entry(kök, show="*")
        self.şifre_giriş.grid(row=1, column=1)

        self.giriş_button = tk.Button(kök, text="Giriş", command=self.giriş_yap)
        self.giriş_button.grid(row=2, column=0, columnspan=2)

        self.soru_etiket = tk.Label(kök, text="Soru:")
        self.soru_etiket.grid(row=3, column=0)
        self.soru_giriş = tk.Entry(kök)
        self.soru_giriş.grid(row=3, column=1)

        self.ders_seçimi_etiket = tk.Label(kök, text="Hangi Ders:")
        self.ders_seçimi_etiket.grid(row=4, column=0)
        self.ders_seçimi = tk.StringVar(kök)
        self.ders_seçimi.set("Seçiniz")
        self.ders_dropdown = tk.OptionMenu(kök, self.ders_seçimi, *["Seçiniz"] + [ders.ad for ders in self.dersler])
        self.ders_dropdown.grid(row=4, column=1)

        self.soru_sor_button = tk.Button(kök, text="Soru Sor", command=self.soru_sor)
        self.soru_sor_button.grid(row=5, column=0, columnspan=2)

        self.öğrenci_listesi_göster()
        self.öğretmen_listesi_göster()
        self.ders_listesi_göster()

        self.öğrenci_ekle_button = tk.Button(kök, text="Öğrenci Ekle", command=self.öğrenci_ekle)
        self.öğrenci_ekle_button.grid(row=10, column=0)

        self.öğretmen_ekle_button = tk.Button(kök, text="Öğretmen Ekle", command=self.öğretmen_ekle)
        self.öğretmen_ekle_button.grid(row=10, column=1)

        self.materyal_ekle_button = tk.Button(kök, text="Materyal Ekle", command=self.materyal_ekle)
        self.materyal_ekle_button.grid(row=10, column=2)

        self.ders_liste.bind("<<ListboxSelect>>", self.materyal_göster)

        self.kılavuz_button = tk.Button(kök, text="Kullanım Kılavuzu", command=self.kılavuz_göster)
        self.kılavuz_button.grid(row=11, column=0, columnspan=3)

    def giriş_yap(self):
        kullanıcı_adı = self.kullanıcı_adı_giriş.get()
        şifre = self.şifre_giriş.get()

        for öğrenci in self.öğrenciler:
            if öğrenci.kullanıcı_adı == kullanıcı_adı and öğrenci.şifre == şifre:
                messagebox.showinfo("Başarılı", "Giriş başarılı.")
                return

        messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")

    def soru_sor(self):
        soru = self.soru_giriş.get()
        seçili_ders = self.ders_seçimi.get()

        if soru and seçili_ders != "Seçiniz":
            messagebox.showinfo("Başarılı", f"{seçili_ders} dersine soru başarıyla gönderildi.")
        else:
            messagebox.showerror("Hata", "Lütfen soru ve ders seçimi yapınız.")

    def öğrenci_listesi_göster(self):
        self.öğrenci_liste_etiket = tk.Label(self.kök, text="Öğrenci Listesi:")
        self.öğrenci_liste_etiket.grid(row=6, column=0)

        self.öğrenci_liste = tk.Listbox(self.kök)
        self.öğrenci_liste.grid(row=7, column=0, rowspan=3, columnspan=2, padx=10, pady=10)

        for öğrenci in self.öğrenciler:
            self.öğrenci_liste.insert(tk.END, öğrenci.ad)

    def öğretmen_listesi_göster(self):
        self.öğretmen_liste_etiket = tk.Label(self.kök, text="Öğretmen Listesi:")
        self.öğretmen_liste_etiket.grid(row=6, column=2)

        self.öğretmen_liste = tk.Listbox(self.kök)
        self.öğretmen_liste.grid(row=7, column=2, rowspan=3, columnspan=2, padx=10, pady=10)

        for öğretmen in self.öğretmenler:
            self.öğretmen_liste.insert(tk.END, f"{öğretmen.ad} {öğretmen.soyad} - {öğretmen.branş}")

    def ders_listesi_göster(self):
        self.ders_liste_etiket = tk.Label(self.kök, text="Dersler:")
        self.ders_liste_etiket.grid(row=6, column=4)

        self.ders_liste = tk.Listbox(self.kök)
        self.ders_liste.grid(row=7, column=4, rowspan=3, columnspan=2, padx=10, pady=10)

        for ders in self.dersler:
            self.ders_liste.insert(tk.END, ders.ad)

    def öğrenci_ekle(self):
        ad = simpledialog.askstring("Yeni Öğrenci Ekle", "Öğrenci Adı:")
        kullanıcı_adı = simpledialog.askstring("Yeni Öğrenci Ekle", "Öğrenci Kullanıcı Adı:")
        şifre = simpledialog.askstring("Yeni Öğrenci Ekle", "Öğrenci Şifre:")
        if ad and kullanıcı_adı and şifre:
            self.öğrenciler.append(Öğrenci(ad, kullanıcı_adı, şifre))
            self.öğrenci_liste.insert(tk.END, ad)

    def öğretmen_ekle(self):
        ad = simpledialog.askstring("Yeni Öğretmen Ekle", "Öğretmen Adı:")
        soyad = simpledialog.askstring("Yeni Öğretmen Ekle", "Öğretmen Soyadı:")
        branş = simpledialog.askstring("Yeni Öğretmen Ekle", "Öğretmen Branşı:")
        if ad and soyad and branş:
            self.öğretmenler.append(Öğretmen(ad, soyad, branş))
            self.öğretmen_liste.insert(tk.END, f"{ad} {soyad} - {branş}")

    def materyal_ekle(self):
        seçili_ders = self.ders_liste.curselection()
        if seçili_ders:
            seçili_ders = self.ders_liste.get(seçili_ders[0])
            materyal = simpledialog.askstring("Materyal Ekle", f"{seçili_ders} Dersine Materyal Ekle:", parent=self.kök)
            if materyal:
                for ders in self.dersler:
                    if ders.ad == seçili_ders:
                        ders.materyal = materyal
                        messagebox.showinfo("Başarılı", "Materyal başarıyla eklendi.")
        else:
            messagebox.showerror("Hata", "Lütfen bir ders seçin.")

    def materyal_göster(self, event):
        seçili_ders = self.ders_liste.get(self.ders_liste.curselection()[0])
        for ders in self.dersler:
            if ders.ad == seçili_ders:
                if ders.materyal:
                    messagebox.showinfo("Materyal", ders.materyal)
                else:
                    messagebox.showinfo("Materyal", "Bu derse materyal eklenmemiş.")

    def kılavuz_göster(self):
        kılavuz_metni = """
        Eğitim Materyali Paylaşım Platformu Kullanım Kılavuzu

        Bu uygulama, öğrencilerin, öğretmenlerin ve ders materyallerinin yönetimini kolaylaştırmak için tasarlanmıştır. Aşağıda, platformun temel özelliklerini ve kullanım adımlarını bulabilirsiniz:

        Giriş Yapma: Kullanıcı adınızı ve şifrenizi girdikten sonra "Giriş" düğmesine tıklayarak sisteme giriş yapabilirsiniz.
        Soru Sorma: "Soru Sor" düğmesine tıklayarak istediğiniz bir ders için bir soru gönderebilirsiniz. Ancak, soru sormadan önce bir ders seçmelisiniz.
        Öğrenci Ekleme: "Öğrenci Ekle" düğmesine tıklayarak yeni bir öğrenci ekleyebilirsiniz. Açılan pencerede öğrencinin adını, kullanıcı adını ve şifresini girmeniz gerekmektedir.
        Öğretmen Ekleme: "Öğretmen Ekle" düğmesine tıklayarak yeni bir öğretmen ekleyebilirsiniz. Açılan pencerede öğretmenin adını, soyadını ve branşını girmeniz gerekmektedir.
        Materyal Ekleme: "Materyal Ekle" düğmesine tıklayarak bir ders için materyal ekleyebilirsiniz. İlgili dersi seçtikten sonra açılan pencerede materyali girebilirsiniz.
        Öğrenci Katılım Bilgileri: Öğrencilerin adlarına çift tıklayarak, öğrencinin hangi derslerin materyaline baktığı ve hangi dersle ilgili soru sorduğuna dair katılım bilgilerini görebilirsiniz.
        """
        messagebox.showinfo("Kullanım Kılavuzu", kılavuz_metni)

if __name__ == "__main__":
    kök = tk.Tk()
    uygulama = EğitimUygulaması(kök)
    kök.mainloop()
