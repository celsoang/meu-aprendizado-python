import pygame
import random

# Inicialização
pygame.init()

# Cores
PRETO, BRANCO, VERMELHO, AMARELO = (0, 0, 0), (255, 255, 255), (213, 50, 80), (255, 255, 102)
VERDE, AZUL = (0, 255, 0), (50, 153, 213)

# Configurações de Tela
LARGURA, ALTURA = 1000, 800
TAMANHO_BLOCO = 20
VELOCIDADE = 10

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake Arena - Solo vs Multiplayer')
relogio = pygame.time.Clock()

# Fontes
fonte_menu = pygame.font.SysFont("arial", 60)
fonte_texto = pygame.font.SysFont("arial", 30)
fonte_placar = pygame.font.SysFont("consolas", 22)


def mostrar_texto(txt, cor, pos_x, pos_y, fonte):
    render = fonte.render(txt, True, cor)
    tela.blit(render, [pos_x, pos_y])


def gerar_comida():
    x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / 20.0) * 20.0
    y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / 20.0) * 20.0
    return x, y


def pegar_nome(num_jogador, cor):
    nome = ""
    while True:
        tela.fill(PRETO)
        mostrar_texto(f"NOME DO JOGADOR {num_jogador}", cor, LARGURA / 3.5, 250, fonte_menu)
        mostrar_texto("Digite e aperte ENTER:", BRANCO, LARGURA / 3.5, 350, fonte_texto)
        pygame.draw.rect(tela, cor, [LARGURA / 3.5, 400, 400, 50], 2)
        mostrar_texto(nome + "|", AMARELO, LARGURA / 3.5 + 10, 410, fonte_texto)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome != "":
                    return nome
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                else:
                    if len(nome) < 12: nome += evento.unicode


def menu_principal():
    while True:
        tela.fill(PRETO)
        mostrar_texto("SNAKE ARENA", VERDE, LARGURA / 3.5, 200, fonte_menu)
        mostrar_texto("1 - Solo (Setas) | 2 - Competição (WASD vs Setas)", BRANCO, LARGURA / 5, 350, fonte_texto)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1: return 1
                if evento.key == pygame.K_2: return 2


def jogo(modo, nome1, nome2):
    x1, y1 = 200, ALTURA / 2
    x1_mov, y1_mov = 0, 0
    corpo1, tam1, pontos1 = [], 1, 0

    x2, y2 = 800, ALTURA / 2
    x2_mov, y2_mov = 0, 0
    corpo2, tam2, pontos2 = [], 1, 0

    cx1, cy1 = gerar_comida()
    cx2, cy2 = gerar_comida()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: return "SAIR"
            if evento.type == pygame.KEYDOWN:
                # --- CONTROLES INTELIGENTES ---
                if modo == 1:  # Modo Solo usa SETAS
                    if evento.key == pygame.K_LEFT and x1_mov == 0: x1_mov, y1_mov = -TAMANHO_BLOCO, 0
                    if evento.key == pygame.K_RIGHT and x1_mov == 0: x1_mov, y1_mov = TAMANHO_BLOCO, 0
                    if evento.key == pygame.K_UP and y1_mov == 0: x1_mov, y1_mov = 0, -TAMANHO_BLOCO
                    if evento.key == pygame.K_DOWN and y1_mov == 0: x1_mov, y1_mov = 0, TAMANHO_BLOCO
                else:  # Modo Multiplayer: P1 usa WASD
                    if evento.key == pygame.K_a and x1_mov == 0: x1_mov, y1_mov = -TAMANHO_BLOCO, 0
                    if evento.key == pygame.K_d and x1_mov == 0: x1_mov, y1_mov = TAMANHO_BLOCO, 0
                    if evento.key == pygame.K_w and y1_mov == 0: x1_mov, y1_mov = 0, -TAMANHO_BLOCO
                    if evento.key == pygame.K_s and y1_mov == 0: x1_mov, y1_mov = 0, TAMANHO_BLOCO
                    # P2 sempre usa SETAS
                    if evento.key == pygame.K_LEFT and x2_mov == 0: x2_mov, y2_mov = -TAMANHO_BLOCO, 0
                    if evento.key == pygame.K_RIGHT and x2_mov == 0: x2_mov, y2_mov = TAMANHO_BLOCO, 0
                    if evento.key == pygame.K_UP and y2_mov == 0: x2_mov, y2_mov = 0, -TAMANHO_BLOCO
                    if evento.key == pygame.K_DOWN and y2_mov == 0: x2_mov, y2_mov = 0, TAMANHO_BLOCO

        x1 += x1_mov;
        y1 += y1_mov
        if modo == 2: x2 += x2_mov; y2 += y2_mov

        vencedor = None
        if x1 >= LARGURA or x1 < 0 or y1 >= ALTURA or y1 < 0: vencedor = nome2
        if modo == 2 and (x2 >= LARGURA or x2 < 0 or y2 >= ALTURA or y2 < 0): vencedor = nome1

        cabeca1 = [x1, y1]
        corpo1.append(cabeca1)
        if len(corpo1) > tam1: del corpo1[0]

        if modo == 2:
            cabeca2 = [x2, y2]
            corpo2.append(cabeca2)
            if len(corpo2) > tam2: del corpo2[0]

        # Colisões de corpo
        for s in corpo1[:-1]:
            if s == cabeca1: vencedor = nome2
            if modo == 2 and s == cabeca2: vencedor = nome1
        if modo == 2:
            for s in corpo2[:-1]:
                if s == cabeca2: vencedor = nome1
                if s == cabeca1: vencedor = nome2

        if vencedor:
            while True:
                tela.fill(PRETO)
                msg = f"VITÓRIA DE {vencedor}!" if modo == 2 else "GAME OVER!"
                mostrar_texto(msg, VERMELHO, LARGURA / 4, ALTURA / 3, fonte_menu)
                if modo == 2:
                    mostrar_texto("PAGUE SUA APOSTA!", AMARELO, LARGURA / 3, ALTURA / 3 + 80, fonte_texto)
                mostrar_texto(f"{nome1}: {pontos1} | {nome2}: {pontos2}", BRANCO, LARGURA / 3, ALTURA / 2, fonte_texto)
                mostrar_texto("C - Reiniciar | Q - Sair", BRANCO, LARGURA / 3, ALTURA / 1.5, fonte_texto)
                pygame.display.update()
                for e in pygame.event.get():
                    if e.type == pygame.QUIT: return "SAIR"
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_q: return "SAIR"
                        if e.key == pygame.K_c: return "REINICIAR"

        tela.fill(PRETO)

        # --- DESENHO DE COMIDA DINÂMICO ---
        pygame.draw.rect(tela, VERMELHO, [cx1, cy1, TAMANHO_BLOCO, TAMANHO_BLOCO])
        if modo == 2:  # Só desenha a segunda comida no multiplayer
            pygame.draw.rect(tela, VERMELHO, [cx2, cy2, TAMANHO_BLOCO, TAMANHO_BLOCO])

        for s in corpo1: pygame.draw.rect(tela, VERDE, [s[0], s[1], TAMANHO_BLOCO, TAMANHO_BLOCO])
        if modo == 2:
            for s in corpo2: pygame.draw.rect(tela, AZUL, [s[0], s[1], TAMANHO_BLOCO, TAMANHO_BLOCO])

        # --- LÓGICA DE COMER DINÂMICA ---
        if x1 == cx1 and y1 == cy1: cx1, cy1 = gerar_comida(); tam1 += 1; pontos1 += 10
        if modo == 2:
            if x2 == cx1 and y2 == cy1: cx1, cy1 = gerar_comida(); tam2 += 1; pontos2 += 10
            if x1 == cx2 and y1 == cy2: cx2, cy2 = gerar_comida(); tam1 += 1; pontos1 += 10
            if x2 == cx2 and y2 == cy2: cx2, cy2 = gerar_comida(); tam2 += 1; pontos2 += 10

        mostrar_texto(f"{nome1}: {pontos1}", VERDE, 20, 20, fonte_placar)
        if modo == 2: mostrar_texto(f"{nome2}: {pontos2}", AZUL, LARGURA - 250, 20, fonte_placar)

        pygame.display.update()
        relogio.tick(VELOCIDADE)


# --- FLUXO PRINCIPAL ---
try:
    m = menu_principal()
    n1 = pegar_nome(1, VERDE)
    n2 = "CPU" if m == 1 else pegar_nome(2, AZUL)

    executando = True
    while executando:
        resultado = jogo(m, n1, n2)
        if resultado == "SAIR":
            executando = False
finally:
    pygame.quit()