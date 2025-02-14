import turtle
import time

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Pong Arcade")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Selección de dificultad
def seleccionar_dificultad():
    dificultad = wn.textinput("Dificultad", "Elige dificultad: facil, normal, dificil").lower()
    if dificultad == "facil":
        return 1
    elif dificultad == "normal":
        return 2
    elif dificultad == "dificil":
        return 3
    else:
        return 2  # Por defecto normal

velocidad_pelota = seleccionar_dificultad()

# Paleta izquierda
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Paleta derecha
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Pelota
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = velocidad_pelota
ball.dy = velocidad_pelota

# Funciones para mover las paletas
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 20)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        left_paddle.sety(y - 20)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        right_paddle.sety(y - 20)

# Controles del teclado
wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")

# Bucle principal del juego
while True:
    wn.update()
    time.sleep(0.01)
    
    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Rebote en los bordes superiores e inferiores
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    # Reinicio de la pelota si sale de los límites
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    # Colisiones con las paletas
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 60 and ball.ycor() > right_paddle.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 60 and ball.ycor() > left_paddle.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1