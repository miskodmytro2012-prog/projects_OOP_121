import tkinter as tk
from tkinter import messagebox

class MageDiary:
    def __init__(self, root):
        self.root = root
        self.root.title("Щоденник мага")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")

        # Змінні гри
        self.mana = 0
        self.mana_per_click = 1
        self.level = 1
        self.upgrade_cost = 20

        # Інтерфейс
        self.label_title = tk.Label(root, text=" Щоденник мага", font=("Arial", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
        self.label_title.pack(pady=20)

        self.label_mana = tk.Label(root, text=f"Мана: {self.mana}", font=("Arial", 18), fg="#3498db", bg="#2c3e50")
        self.label_mana.pack(pady=10)

        self.label_level = tk.Label(root, text=f"Рівень: {self.level}", font=("Arial", 14), fg="#f1c40f", bg="#2c3e50")
        self.label_level.pack()

        # Кнопка медитації (клікер)
        self.btn_click = tk.Button(root, text="Медитувати (МАНА +)", font=("Arial", 14, "bold"),
                                   command=self.collect_mana, bg="#8e44ad", fg="white", width=20, height=2)
        self.btn_click.pack(pady=30)

        # Кнопка покращення
        self.btn_upgrade = tk.Button(root, text=f"Вивчити закляття ({self.upgrade_cost} мани)",
                                     command=self.upgrade, bg="#27ae60", fg="white")
        self.btn_upgrade.pack(pady=10)

    def collect_mana(self):
        self.mana += self.mana_per_click
        self.update_ui()

    def upgrade(self):
        if self.mana >= self.upgrade_cost:
            self.mana -= self.upgrade_cost
            self.mana_per_click += 1
            self.level += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)
            self.update_ui()
            messagebox.showinfo("Нове закляття!", f"Ви досягли {self.level} рівня!")
        else:
            messagebox.showwarning("Мало енергії", "Тобі потрібно більше мани!")

    def update_ui(self):
        self.label_mana.config(text=f"Мана: {self.mana}")
        self.label_level.config(text=f"Рівень: {self.level}")
        self.btn_upgrade.config(text=f"Вивчити закляття ({self.upgrade_cost} мани)")

if __name__ == "__main__":
    root = tk.Tk()
    game = MageDiary(root)
    root.mainloop()