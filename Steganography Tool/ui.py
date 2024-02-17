import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("Steganography tool!")
label=tk.Label(root, text="Choose Encryption or Decryption", font=('Sans Serif' , 14))
label.pack()
bgimg= tk.PhotoImage(file = "G:\Sem 3\Mini Project\desktop-wallpaper-cryptography.ppm")
limg= tk.Label(root, i=bgimg)
limg.pack()


but_enc1=tk.Button(root,text="Encryption",font=('Sans Serif' , 14))
but_enc1.place(x=350,y=150)
but_dec1=tk.Button(root,text="Decryption",font=('Sans Serif' ,14))
but_dec1.place(x=350,y=250)

root.mainloop()

