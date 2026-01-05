import turtle


def setup_canvas():
    """Налаштування вікна для малювання"""
    window = turtle.Screen()
    window.setup(width=900, height=500)
    window.bgcolor("#F4F4F4")
    window.title("AI Brand Identity Designs")
    return turtle.Turtle()


def draw_abstract_aurum(t, x, y):
    """Перша емблема: Золота Корона (Влада та Якість)"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#D4AF37")
    t.begin_fill()
    for _ in range(5):
        t.forward(40)
        t.left(144)
    t.end_fill()
    t.penup()
    t.goto(x + 20, y - 40)
    t.write("AURUM", align="center", font=("Verdana", 12, "bold"))


def draw_dynamic_echo(t, x, y):
    """Друга емблема: Хвильовий Вихор (Зв'язок та Ехо)"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    colors = ["#1A5276", "#2980B9", "#5499C7"]
    for i in range(15):
        t.pencolor(colors[i % 3])
        t.circle(i * 3)
        t.left(20)
    t.penup()
    t.goto(x, y - 60)
    t.pencolor("black")
    t.write("ECHO", align="center", font=("Verdana", 12, "bold"))


def draw_tech_fortis(t, x, y):
    """Третя емблема: Щит Технологій (Захист та Сила)"""
    t.penup()
    t.goto(x - 25, y + 25)
    t.pendown()
    t.color("#C0392B")
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(x, y + 5)
    t.color("white")
    t.write("F", align="center", font=("Arial", 20, "bold"))
    t.penup()
    t.setheading(0)
    t.goto(x, y - 60)
    t.color("black")
    t.write("FORTIS", align="center", font=("Verdana", 12, "bold"))


def run_branding_process():
    """Головна функція запуску візуалізації"""
    artist = setup_canvas()
    artist.speed(0)
    artist.pensize(2)

    # Виклик функцій для кожної емблеми
    draw_abstract_aurum(artist, -250, 50)
    draw_dynamic_echo(artist, 0, 50)
    draw_tech_fortis(artist, 250, 50)

    artist.hideturtle()


if __name__ == "__main__":
    run_branding_process()