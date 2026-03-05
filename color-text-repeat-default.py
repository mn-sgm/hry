import tkinter as tk
import random
import time

# ==============================
# Nastavenia hry
# ==============================
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FONT_SIZE = 48

# Povolené farby
COLORS = [
    "red", "black", "gray", "green", "yellow",
    "brown", "blue", "orange", "pink", "purple"
]

# ==============================
# Generovanie databázy (20 dvojíc, 50% zhoda / 50% nezhoda)
# ==============================
def generate_database():
    pairs = []
    # 10 zhôd
    for _ in range(10):
        color = random.choice(COLORS)
        pairs.append((color, color))
    # 10 nezhôd
    for _ in range(10):
        text = random.choice(COLORS)
        color = random.choice([c for c in COLORS if c != text])
        pairs.append((color, text))
    random.shuffle(pairs)
    return pairs

# ==============================
# Hlavná trieda hry
# ==============================
class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Match Game")
        
        self.canvas = tk.Canvas(
            root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg="white"
        )
        self.canvas.pack()
        
        self.reset_game_state()
        
        # Ovládanie šípkami (funguje celý čas)
        self.root.bind("<Left>", self.left_pressed)
        self.root.bind("<Right>", self.right_pressed)
        
        self.show_start_screen()

    def reset_game_state(self):
        """Resetuje všetko potrebné pre novú hru"""
        self.database = generate_database()
        self.index = 0
        self.score = 0
        self.start_time = None
        self.game_over_flag = False
        self.text_item = None

    def show_start_screen(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2 - 80,
            text="Color Match Game",
            font=("Arial", 36, "bold"),
            fill="navy"
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2 - 10,
            text="Press RIGHT if match\nPress LEFT if mismatch",
            font=("Arial", 24),
            fill="black",
            justify="center"
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2 + 80,
            text="Press any arrow key to start / restart",
            font=("Arial", 18),
            fill="gray"
        )

    def start_game(self):
        self.start_time = time.time()
        self.next_round()

    def next_round(self):
        if self.index >= len(self.database):
            self.end_game(success=True)
            return
            
        self.canvas.delete("all")
        color, text = self.database[self.index]
        
        self.text_item = self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
            text=text.upper(),
            font=("Arial", FONT_SIZE, "bold"),
            fill=color
        )

    def check_answer(self, player_says_match):
        if self.game_over_flag:
            # Ak je hra skončená → šípky spustia novú hru
            self.reset_game_state()
            self.start_game()
            return

        if self.start_time is None:
            # Prvé stlačenie šípky → spustí hru
            self.start_game()
            return

        color, text = self.database[self.index]
        actual_match = (color == text)

        if player_says_match == actual_match:
            self.score += 1
            self.index += 1
            self.next_round()
        else:
            self.end_game(success=False)

    def left_pressed(self, event):
        self.check_answer(False)   # nezhoda

    def right_pressed(self, event):
        self.check_answer(True)    # zhoda

    def end_game(self, success=False):
        self.game_over_flag = True
        self.canvas.delete("all")
        
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2) if self.start_time else 0
        
        if success:
            title = "VÝBORNE! VŠETKO SPRÁVNE!"
            color = "green"
        else:
            title = "CHYBA!"
            color = "red"

        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2 - 80,
            text=title,
            font=("Arial", 36, "bold"),
            fill=color
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2 - 10,
            text=f"Score: {self.score} / 20\nTime: {total_time} s",
            font=("Arial", 28),
            fill="black"
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2 + 80,
            text="Press ← or → to play again",
            font=("Arial", 20),
            fill="gray"
        )

# ==============================
# Spustenie aplikácie
# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()
