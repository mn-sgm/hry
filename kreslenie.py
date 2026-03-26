import tkinter
canvas = tkinter.Canvas(bg="white", width=800, height=600)
canvas.pack()

x_pink = 100
y_pink = 550
canvas.create_oval(x_pink-30, y_pink-30, x_pink+30, y_pink+30, fill="pink", outline="")

farba = "black"

def klik(suradnice):
    global x_pink, y_pink, farba
    
    x = suradnice.x
    y = suradnice.y
    if (x >= x_pink-30 and x<= x_pink+30 and y >= y_pink-30 and y<= y_pink+30):
        farba = "pink"
    
##def kresli(suradnice):
##    x = suradnice.x
##    y = suradnice.y
##    canvas.create_oval(x-1, y-1, x+1, y+1, fill="black",outline="")
##
posledne_x = None
posledne_y = None

def kresli(suradnice):
    global posledne_x, posledne_y, farba
    
    x = suradnice.x
    y = suradnice.y
    
    if posledne_x is not None:
        # Namiesto ovalu kreslíme čiaru z predchádzajúceho bodu do aktuálneho
        canvas.create_line(posledne_x, posledne_y, x, y, fill=farba, width=2, capstyle="round")
    
    # Aktualizujeme posledné súradnice
    posledne_x = x
    posledne_y = y

def uvolni(suradnice):
    global posledne_x, posledne_y
    # Toto je kľúčové: po pustení myši zabudneme poslednú polohu
    posledne_x = None
    posledne_y = None

canvas.bind("<Button-2>", klik)
canvas.bind("<B1-Motion>", kresli)
canvas.bind("<ButtonRelease-1>", uvolni) # Pustenie ľavého tlačidla ukončí čiaru


x_pink = 100
y_pink = 550
canvas.create_oval(x_pink-30, y_pink-30, x_pink+30, y_pink+30, fill="pink", outline="")

farba = "black"

##def kresli(suradnice):
##    global farba
##    
##    x = suradnice.x
##    y = suradnice.y
##    canvas.create_oval(x-1, y-1, x+1, y+1, fill=farba, outline="")

def zmena(suradnice):
    global farba, x_pink, y_pink
    
    x = suradnice.x
    y = suradnice.y
    if(x >= x_pink-30 and y >= y_pink-30 and x <= x_pink+30 and y <= y_pink+30):
        farba = "pink"
        
    

canvas.bind("<B1-Motion>", kresli)
canvas.bind("<Button-2>", zmena)
