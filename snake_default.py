import tkinter as tk
import random

SIRKA, VYSKA = 400, 400
VELKOST_STVORCA = 10
RYCHLOST = 50 

class Hadik:
    def __init__(self):
        self.okno = tk.Tk()
        self.okno.title("Hadík so skóre")
        
        self.canvas = tk.Canvas(self.okno, width=SIRKA, height=VYSKA, bg="black")
        self.canvas.pack()

        self.had = [[100, 100], [80, 100], [60, 100]]
        self.smer = "Right"
        self.skore = 0
        self.jedlo = self.vytvor_jedlo()
        
        # Vytvorenie textu skóre
        self.text_skore = self.canvas.create_text(10, 10, text=f"Skóre: {self.skore}", fill="white", font=("Arial", 14), anchor="nw")
        
        self.okno.bind("<Key>", self.zmen_smer)
        self.pohyb()
        self.okno.mainloop()

    def vytvor_jedlo(self):
        x = random.randint(0, (SIRKA // VELKOST_STVORCA) - 1) * VELKOST_STVORCA
        y = random.randint(0, (VYSKA // VELKOST_STVORCA) - 1) * VELKOST_STVORCA
        return [x, y]

    def zmen_smer(self, event):
        novy_smer = event.keysym
        zakazane = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if novy_smer in zakazane and novy_smer != zakazane.get(self.smer):
            self.smer = novy_smer

    def pohyb(self):
        hlava_x, hlava_y = self.had[0]

        if self.smer == "Up": hlava_y -= VELKOST_STVORCA
        elif self.smer == "Down": hlava_y += VELKOST_STVORCA
        elif self.smer == "Left": hlava_x -= VELKOST_STVORCA
        elif self.smer == "Right": hlava_x += VELKOST_STVORCA

        nova_hlava = [hlava_x, hlava_y]

        if (hlava_x < 0 or hlava_x >= SIRKA or hlava_y < 0 or hlava_y >= VYSKA 
            or nova_hlava in self.had):
            self.canvas.create_text(SIRKA/2, VYSKA/2, text=f"GAME OVER\nSkóre: {self.skore}", fill="white", font=("Arial", 25), justify="center")
            return

        self.had.insert(0, nova_hlava)

        if hlava_x == self.jedlo[0] and hlava_y == self.jedlo[1]:
            self.skore += 1
            self.canvas.itemconfig(self.text_skore, text=f"Skóre: {self.skore}")
            self.jedlo = self.vytvor_jedlo()
        else:
            self.had.pop()

        self.vykresli()
        self.okno.after(RYCHLOST, self.pohyb)

    def vykresli(self):
        # Vymažeme všetko okrem textu skóre, aby sme ho nemuseli stále vytvárať nanovo
        self.canvas.delete("had", "jedlo")
        
        self.canvas.create_oval(self.jedlo[0], self.jedlo[1], 
                                self.jedlo[0]+VELKOST_STVORCA, self.jedlo[1]+VELKOST_STVORCA, fill="red", tags="jedlo")
        
        for cast in self.had:
            self.canvas.create_rectangle(cast[0], cast[1], 
                                         cast[0]+VELKOST_STVORCA, cast[1]+VELKOST_STVORCA, fill="green", tags="had")

if __name__ == "__main__":
    Hadik()
