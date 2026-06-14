#avatar maker

import tkinter as tk

from PIL import Image, ImageTk
#listas
bp = ["1bp", "2bp", "3bp", "4bp","5bp","6bp"]
ojos = ["1ojo", "2ojo", "3ojo", "4ojo"]
chas = ["1chas", "2chas", "3chas", "4chas","5chas"]
colores =[1,2,3,4,5,6,7,8,9,10,11]

# variables 
v_piel = 0
v_ropa = 0
v_boca = 0
v_ceja = 0

v_ojo = 0
c_ojo = 0

v_bp = 0
c_bp = 0

v_chas = 0
c_chas = 0

#listas con las fotos
imagenes_1bp = []
imagenes_2bp = []
imagenes_3bp = []
imagenes_4bp = []
imagenes_5bp = []
imagenes_6bp = []
imagenes_1ojo = []
imagenes_2ojo = []
imagenes_3ojo = []
imagenes_4ojo = []
img_cejas = ["dibujos2/cejas1.png", "dibujos2/cejas2.png", "dibujos2/cejas3.png", "dibujos2/cejas4.png"]
imagenes_cejas = []
img_piel = ["dibujos2/piel1.png", "dibujos2/piel2.png", "dibujos2/piel3.png", "dibujos2/piel4.png"]
imagenes_piel = []
img_ropa = ["dibujos2/ropa1.png","dibujos2/ropa2.png","dibujos2/ropa3.png","dibujos2/ropa4.png","dibujos2/ropa5.png","dibujos2/ropa6.png","dibujos2/ropa7.png","dibujos2/ropa8.png","dibujos2/ropa9.png","dibujos2/ropa10.png","dibujos2/ropa11.png","dibujos2/ropa12.png"]
imagenes_ropa = []
img_boca = ["dibujos2/boca1.png", "dibujos2/boca2.png", "dibujos2/boca3.png", "dibujos2/boca4.png"]
imagenes_boca = []
imagenes_1chas = []
imagenes_2chas = []
imagenes_3chas = []
imagenes_4chas = []
imagenes_5chas = []
lenbp = len(bp)
lenpiel = len(img_piel)
lenropa = len(img_ropa)
lenboca = len(img_boca)
lenojos = len(ojos)
lencejas = len(img_cejas)
lenchas = len(chas) 
lencolores = len(colores)

ventana = tk.Tk()
ventana.title("Avatar maker")
ventana.geometry("400x680")

canvas = tk.Canvas(ventana, width = "350", height= "350", bg="beige")
canvas.pack()
#creando imagenes 
for i in range(lenpiel):
    img = Image.open(img_piel[i])
    img = img.resize((350,350))
    img = ImageTk.PhotoImage(img)
    imagenes_piel.append(img)
for i in range(lenropa):
    img = Image.open(img_ropa[i])
    img = img.resize((350,350))
    img = ImageTk.PhotoImage(img)
    imagenes_ropa.append(img)
for i in range(lenboca):
    img = Image.open(img_boca[i])
    img = img.resize((350,350))
    img = ImageTk.PhotoImage(img)
    imagenes_boca.append(img)
for i in range(lencejas):
    img = Image.open(img_cejas[i])
    img = img.resize((350,350))
    img = ImageTk.PhotoImage(img)
    imagenes_cejas.append(img)  
for i in range(lenbp):
    for j in range(lencolores):
        if i == 0:
            img = Image.open(f"dibujos/1bp{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_1bp.append(img)
        if i == 1:
            img = Image.open(f"dibujos/2bp{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_2bp.append(img)
        if i == 2:
            img = Image.open(f"dibujos/3bp{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_3bp.append(img)
        if i == 3:
            img = Image.open(f"dibujos/4bp{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_4bp.append(img)
        if i == 4:
            img = Image.open(f"dibujos2/5bp{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_5bp.append(img)
        if i == 5:
            img = Image.open(f"dibujos2/6bp{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_6bp.append(img)       

for i in range(lenojos):
    for j in range(lencolores):
        if i == 0:
            img = Image.open(f"dibujos2/1ojo{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_1ojo.append(img)
        if i == 1:
            img = Image.open(f"dibujos2/2ojo.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_2ojo.append(img)
        if i == 2:
            img = Image.open(f"dibujos2/3ojo{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_3ojo.append(img)
        if i == 3:
            img = Image.open(f"dibujos2/4ojo{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_4ojo.append(img)
for i in range(lenchas):
    for j in range(lencolores):
        if i == 0:
            img = Image.open(f"dibujos/1chas{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_1chas.append(img)
        if i == 1:
            img = Image.open(f"dibujos/2chas{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_2chas.append(img)
        if i == 2:
            img = Image.open(f"dibujos/3chas{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_3chas.append(img)
        if i == 3:
            img = Image.open(f"dibujos/4chas{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_4chas.append(img)
        if i == 4:
            img = Image.open(f"dibujos/5chas{colores[j]}.png")
            img = img.resize((350,350))
            img = ImageTk.PhotoImage(img)
            imagenes_5chas.append(img)

#contadores

def color_piel():
    global v_piel
    v_piel += 1
    if v_piel == 4:
        v_piel = 0
    canvas.itemconfig(
    skin_capa,
    image = imagenes_piel[v_piel]
    )
    return v_piel  
def color_ropa():
    global v_ropa
    v_ropa += 1
    if v_ropa == 12:
        v_ropa = 0
    canvas.itemconfig(
    clothes_capa,
    image = imagenes_ropa[v_ropa]
    ) 
    return v_ropa
def diseno_ceja():
    global v_ceja
    v_ceja += 1
    if v_ceja == 4:
        v_ceja = 0
    canvas.itemconfig(
    eyebrow_capa,
    image = imagenes_cejas[v_ceja]
    ) 
    return v_ceja
def diseno_boca():
    global v_boca
    v_boca += 1
    if v_boca == 4:
        v_boca = 0 
    canvas.itemconfig(
    mouth_capa,
    image = imagenes_boca[v_boca]
    ) 
    return v_boca
id_ojos = 0
def diseno_ojos():
    global v_ojo
    v_ojo += 1
    if v_ojo == 4:
            v_ojo = 0
    id_ojos = (v_ojo * 11) + c_ojo
    if id_ojos == 44:
        id_ojos = 0
    canvas.itemconfig(
    eyes_capa,
    image = imagenes_ojos[id_ojos]
    ) 
    return v_ojo
    return id_ojos
def color_ojos():
    global c_ojo
    c_ojo += 1
    if c_ojo == 11:
        c_ojo = 0
    id_ojos = (v_ojo * 11) + c_ojo
    if id_ojos == 44:
        id_ojos = 0
    canvas.itemconfig(
    eyes_capa,
    image = imagenes_ojos[id_ojos]
    ) 
    return c_ojo
    return id_ojos
id_bp = 0
def diseno_bp():
    global v_bp
    v_bp += 1
    if v_bp == 6:
        v_bp = 0
    t_bp = (v_bp * 11) 
    id_bp = t_bp + c_bp 
    if id_bp == 66:
        id_bp = 0

    canvas.itemconfig(
    bp_capa,
    image = imagenes_bp[id_bp]
    )
    return v_bp
    return id_bp
def color_bp():
    global c_bp
    c_bp += 1
    if c_bp == 11:
        c_bp = 0

    t_bp = (v_bp * 11) 
    id_bp = t_bp + c_bp
    if id_bp == 66:
        id_bp = 0
    canvas.itemconfig(
    bp_capa,
    image = imagenes_bp[id_bp]
    )   
    return c_bp
    return id_bp

id_chas = 0
def diseno_chas():
    global v_chas
    v_chas += 1
    if v_chas == 5:
        v_chas = 0
    id_chas = (v_chas * 11) + c_chas
    if id_chas == 55:
        id_chas = 0
    canvas.itemconfig(
    front_hair_capa,
    image = imagenes_chas[id_chas]
    ) 
    return v_chas
    return id_chas

def color_chas():
    global c_chas
    c_chas += 1
    if c_chas == 11:
        c_chas = 0
    id_chas = (v_chas * 11) + c_chas
    if id_chas == 55:
        id_chas = 0
    canvas.itemconfig(
    front_hair_capa,
    image = imagenes_chas[id_chas]
    ) 
    return c_chas
    return id_chas

imagenes_bp = imagenes_1bp + imagenes_2bp + imagenes_3bp + imagenes_4bp + imagenes_5bp + imagenes_6bp
imagenes_ojos = imagenes_1ojo + imagenes_2ojo + imagenes_3ojo + imagenes_4ojo
imagenes_chas = imagenes_1chas + imagenes_2chas + imagenes_3chas + imagenes_4chas + imagenes_5chas  
print(len(imagenes_ojos))
bp_capa = canvas.create_image(175,175, image = imagenes_bp[id_bp])
skin_capa = canvas.create_image(175,175, image = imagenes_piel[v_piel])
clothes_capa = canvas.create_image(175,175, image = imagenes_ropa[v_ropa])
mouth_capa = canvas.create_image(175,175, image = imagenes_boca[v_boca])
eyebrow_capa = canvas.create_image(175,175, image = imagenes_cejas[v_ceja])
eyes_capa = canvas.create_image(175,175, image = imagenes_ojos[id_ojos])
front_hair_capa = canvas.create_image(175,175, image = imagenes_chas[id_chas])


boton_piel = tk.Button(
    ventana,
    text="skin",
    command= color_piel)
boton_piel.pack()

boton_ropa = tk.Button(
    ventana,
    text="clothes",
    command= color_ropa)
boton_ropa.pack()

boton_boca = tk.Button(
    ventana,
    text="Mouth",
    command= diseno_boca)
boton_boca.pack()

boton_cejas = tk.Button(
    ventana,
    text="Eyebrow",
    command= diseno_ceja)
boton_cejas.pack()

boton_ojos = tk.Button(
    ventana,
    text="Eyes",
    command= diseno_ojos)
boton_ojos.pack()

boton_colojos = tk.Button(
    ventana,
    text="Eyes colour",
    command= color_ojos)
boton_colojos.pack()

boton_bp = tk.Button(
    ventana,
    text="Back hair",
    command= diseno_bp)
boton_bp.pack()

boton_colbp = tk.Button(
    ventana,
    text="Back hair colour",
    command= color_bp)
boton_colbp.pack()

boton_chas = tk.Button(
    ventana,
    text="Front hair",
    command= diseno_chas)
boton_chas.pack()

boton_colchas = tk.Button(
    ventana,
    text="Front hair colour",
    command= color_chas)
boton_colchas.pack()



ventana.mainloop()


