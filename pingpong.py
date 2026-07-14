import turtle
import time

# --- Configurações de Tela ---
win = turtle.Screen()
win.title("Pong Pro - Aposta em Jogo")
win.bgcolor("black")
win.setup(width=1200, height=600)  # Largura de 1200
win.tracer(0)

# Estados globais
keys = {"w": False, "s": False, "Up": False, "Down": False}
game_on = False
nome_a = ""
nome_b = ""
score_a = 0
score_b = 0
last_time = time.time()

# --- Objetos ---
paddle_a = turtle.Turtle("square")
paddle_a.speed(0);
paddle_a.color("white");
paddle_a.shapesize(5, 1);
paddle_a.penup()

paddle_b = turtle.Turtle("square")
paddle_b.speed(0);
paddle_b.color("white");
paddle_b.shapesize(5, 1);
paddle_b.penup()

ball = turtle.Turtle("circle")
ball.speed(0);
ball.color("white");
ball.penup()

pen = turtle.Turtle()
pen.speed(0);
pen.color("white");
pen.penup();
pen.hideturtle()


# --- Funções de Teclado ---
def k_up(): keys["w"] = True


def k_down(): keys["s"] = True


def k_up_off(): keys["w"] = False


def k_down_off(): keys["s"] = False


def kb_up(): keys["Up"] = True


def kb_down(): keys["Down"] = True


def kb_up_off(): keys["Up"] = False


def kb_down_off(): keys["Down"] = False


win.listen()
win.onkeypress(k_up, "w");
win.onkeyrelease(k_up_off, "w")
win.onkeypress(k_down, "s");
win.onkeyrelease(k_down_off, "s")
win.onkeypress(kb_up, "Up");
win.onkeyrelease(kb_up_off, "Up")
win.onkeypress(kb_down, "Down");
win.onkeyrelease(kb_down_off, "Down")


def iniciar_partida():
    global nome_a, nome_b, score_a, score_b, game_on, last_time

    nome_a = win.textinput("Jogador 1", "Nome da Esquerda:") or "Player 1"
    nome_b = win.textinput("Jogador 2", "Nome da Direita:") or "Player 2"

    score_a = 0
    score_b = 0

    # AJUSTE: Raquetes mais longe (550 de distância do centro)
    paddle_a.goto(-550, 0)
    paddle_b.goto(550, 0)

    ball.goto(0, 0)
    ball.dx = 700
    ball.dy = 700

    win.listen()
    last_time = time.time()
    game_on = True
    loop_principal()


def loop_principal():
    global score_a, score_b, game_on, last_time

    if not game_on: return

    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time

    if dt > 0.1: dt = 0.016

    # Movimento das Raquetes
    p_speed = 900 * dt
    if keys["w"] and paddle_a.ycor() < 250: paddle_a.sety(paddle_a.ycor() + p_speed)
    if keys["s"] and paddle_a.ycor() > -250: paddle_a.sety(paddle_a.ycor() - p_speed)
    if keys["Up"] and paddle_b.ycor() < 250: paddle_b.sety(paddle_b.ycor() + p_speed)
    if keys["Down"] and paddle_b.ycor() > -250: paddle_b.sety(paddle_b.ycor() - p_speed)

    # Movimento da Bola
    ball.setx(ball.xcor() + ball.dx * dt)
    ball.sety(ball.ycor() + ball.dy * dt)

    # Colisões Teto e Chão
    if abs(ball.ycor()) > 290:
        ball.dy *= -1

    # AJUSTE: Colisões Raquetes (Baseadas nas novas posições)
    # Direita
    if (ball.xcor() > 530 and ball.distance(paddle_b) < 50):
        ball.setx(530);
        ball.dx *= -1
    # Esquerda
    elif (ball.xcor() < -530 and ball.distance(paddle_a) < 50):
        ball.setx(-530);
        ball.dx *= -1

    # AJUSTE: Pontos (Agora a bola precisa passar de 590 para pontuar)
    if ball.xcor() > 590:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -590:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1

    # Placar
    pen.clear()
    pen.goto(0, 250)
    pen.write(f"{nome_a}: {score_a}   |   {nome_b}: {score_b}", align="center", font=("Courier", 20, "bold"))

    # Checar vitória
    if score_a >= 5 or score_b >= 5:
        vencedor = nome_a if score_a >= 5 else nome_b
        game_on = False
        pen.goto(0, 0)
        pen.write(f"{vencedor} VENCEU!\nPague sua aposta!", align="center", font=("Courier", 24, "bold"))
        win.update()
        time.sleep(2)

        resposta = win.textinput("Fim de Jogo", "Jogar de novo? (sim/nao)")
        if resposta and resposta.lower() in ["sim", "s"]:
            iniciar_partida()
        else:
            turtle.bye()
            return

    win.update()
    win.ontimer(loop_principal, 10)


iniciar_partida()
win.mainloop()