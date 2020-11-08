import pygame
import os

pygame.init()
pygame.mixer.init()

directory = os.path.dirname(os.path.realpath(__file__))

# Assets
ASSET_PATH     = (directory+'/asset/')
SFONDO         = pygame.image.load(ASSET_PATH + 'img/fortezza.png')
PERSONAGGIO    = pygame.image.load(ASSET_PATH + 'img/cavaliere3.png')
BASE           = pygame.image.load(ASSET_PATH + 'img/base3.png')
NEMICO         = pygame.image.load(ASSET_PATH + 'img/nemico5.png')
GAMEOVER       = pygame.image.load(ASSET_PATH + 'img/gameover4.png')
DRAGO          = pygame.image.load(ASSET_PATH + 'img/drago2.png')
GAMEOVER_SOUND = pygame.mixer.Sound(ASSET_PATH + 'suoni/gameover.wav')
START_GAME     = pygame.mixer.Sound(ASSET_PATH + 'suoni/gamestart.wav')
SALTO          = pygame.mixer.Sound(ASSET_PATH + 'suoni/salto.wav')
CADUTA         = pygame.mixer.Sound(ASSET_PATH + 'suoni/caduta2.wav')
SOTTOFONDO     = pygame.mixer.music.load(ASSET_PATH + 'suoni/sottofondo_medievale.mp3')
SFONDO2        = pygame.image.load(ASSET_PATH + 'img/castle3.png')
pygame.mixer.music.play(-1)

# Costanti
X_SFONDO = 0
Y_SFONDO = 0
X_PERS_INIT = 100
Y_PERS_INIT = 347 
Y_PERS_MIN = 157
X_BASE_INIT = 0
Y_BASE = 500
X_NEMICO_INIT = 340
Y_NEMICO = 420
PERS_WIDTH = 140
BASE_WIDTH = 500
NEMICO_WIDTH = 87
PERS_HEIGHT = 150
VEL_AVANZ = 4
X_DRAGO = 400
Y_DRAGO = 3
X_PUNTI_INIT = 238
Y_PUNTI = 60
X_MVP_INIT = 350
Y_MVP = 30
X_NOTA_INIT = 345
Y_NOTA = 8
WIDTH = 500
HEIGHT = 650
X_GAMEOVER = 160
Y_GAMEOVER = 150
VEL_SALTO = 5
VEL_DISCESA = VEL_SALTO
X_SFONDO2 = 0
Y_SFONDO2 = 53
R = 8
G = 12
B = 57
FPS_INIT = 30
counter = 0
Y_R = 5
Y_G = 20
Y_B = 35
X_R = 10
X_G = X_R
X_B = X_R
Punteggio_MVP = [0]




fpsClock = pygame.time.Clock()
FONT = pygame.font.SysFont("MEDIEVAL GOTHIC", 100, bold = True)
FONT2 = pygame.font.SysFont("MEDIEVAL GOTHIC", 20, bold = True)
FONT3 = pygame.font.SysFont("MEDIEVAL GOTHIC", 50, bold = True)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("CASTLE RUN")




def inizializza(): # Inizializzo le variabili
    global xBase
    global xPers
    global yPers
    global xNemico
    global punti
    global xPunti
    global fps
    global counter
    global r
    global g
    global b
    global colore
    global rosso
    global blu 
    global verde
    global red  
    global blue
    global green
    global xMvp
    global xNota
    r = R
    g = G
    b = B
    colore = (r ,g ,b)
    fps = FPS_INIT
    xBase = X_BASE_INIT
    xPers = X_PERS_INIT
    yPers = Y_PERS_INIT
    xNemico = X_NEMICO_INIT
    punti = 0
    xPunti = X_PUNTI_INIT
    xMvp = X_MVP_INIT
    xNota = X_NOTA_INIT
    rosso = ("RED = ") + str(r)
    blu = ("BLUE = ") + str(b)
    verde = ("GREEN = ") + str(g)
    red = FONT2.render(str(rosso), 1, (r, 0, 0))
    blue = FONT2.render(str(blu), 1, (0, 0, b))
    green = FONT2.render(str(verde), 1, (0, g, 0))
    
    
inizializza()
    

    
   

def disegna_oggetti():
    SCREEN.fill(colore)
    if counter % 2 == 0:
        SCREEN.blit(SFONDO, (X_SFONDO, Y_SFONDO))
    else:
        SCREEN.blit(SFONDO2, (X_SFONDO2, Y_SFONDO2))
    SCREEN.blit(BASE, (xBase, Y_BASE)) #base 1
    SCREEN.blit(NEMICO, (xNemico, Y_NEMICO)) #nemico1
    SCREEN.blit(PERSONAGGIO, (xPers, yPers))
    SCREEN.blit(BASE, (xBase + BASE_WIDTH, Y_BASE)) #base 2
    SCREEN.blit(NEMICO, (xNemico + (X_NEMICO_INIT + NEMICO_WIDTH), Y_NEMICO)) #nemico 2
    SCREEN.blit(DRAGO, (X_DRAGO, Y_DRAGO))
    PUNTEGGIO = FONT.render(str(punti), 1, (255, 255, 255))
    SCREEN.blit(PUNTEGGIO, (xPunti, Y_PUNTI))
    NOTA = FONT2.render(("MVP"), 1, (255, 255, 255))
    MVP = FONT3.render(str(punteggio_max), 1, (255, 255, 255))
    if punteggio_max <= 9:
        SCREEN.blit(MVP, (xMvp, Y_MVP))
    if punteggio_max >= 10:
        SCREEN.blit(MVP, (339, Y_MVP))
    SCREEN.blit(NOTA, (xNota, Y_NOTA))
            


def movimento_oggetti():
    global xBase
    global xNemico
    xBase -= VEL_AVANZ # La base 1 e 2 si spostano verso sinistra
    xNemico -= VEL_AVANZ # Il nemico 1 e 2 si spostano verso sinistra
    
def traslazione_oggetti():
    global xBase
    global xNemico
    if xBase + BASE_WIDTH < 0: # Quando la base 1 esce completamente dallo schermo viene traslata alla sua posizione iniziale spostando così anche la base 2
        xBase = X_BASE_INIT        
    if xNemico + NEMICO_WIDTH <= 0: # Quando il nemico 1 esce completamente dallo schermo viene traslato alla sua posizione iniziale spostando così anche il nemico 2
        xNemico = X_NEMICO_INIT
    

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(fps)
        
        
        

        


while True:   
    punteggio_max = max(Punteggio_MVP)
    if punti >= 10:
        xPunti = 213
    hai_perso = True
    disegna_oggetti()
    movimento_oggetti()  
    if yPers < Y_PERS_INIT:
        yPers += VEL_DISCESA        
        if yPers == Y_PERS_INIT:
            punti += 1
            Punteggio_MVP.append(punti)
        if yPers >= Y_PERS_INIT:
            yPers = Y_PERS_INIT
            CADUTA.play()
            fps += 15
    
             

    traslazione_oggetti()
    
    
    if ((xPers + PERS_WIDTH == xNemico and yPers == Y_PERS_INIT) or (Y_NEMICO <= yPers + PERS_HEIGHT and xPers + 37 <= xNemico + 52 and xPers + 107 >= xNemico + 52)):
        GAMEOVER_SOUND.play()
        
        while hai_perso:
            inizializza()
            disegna_oggetti()
            fps = FPS_INIT    
            punteggio_max = max(Punteggio_MVP)
            SCREEN.blit(GAMEOVER, (X_GAMEOVER, Y_GAMEOVER))
            SCREEN.blit(red, (X_R, Y_R))
            SCREEN.blit(blue, (X_B, Y_B))
            SCREEN.blit(green, (X_G, Y_G))
            NOTA = FONT2.render(("MVP"), 1, (255, 255, 255))
            MVP = FONT3.render(str(punteggio_max), 1, (255, 255, 255))
            if punteggio_max <= 9:
                SCREEN.blit(MVP, (xMvp, Y_MVP))
            if punteggio_max >= 10:
                SCREEN.blit(MVP, (339, Y_MVP))     
            SCREEN.blit(NOTA, (xNota, Y_NOTA))
            pygame.mixer.music.stop()
            aggiorna()
            
            # Controllo quale tasto viene premuto dal giocatore
            for event in pygame.event.get():
                # Il giocatore chiude la finestra del gioco premendo il pulsante X in alto a destra
                if event.type == pygame.QUIT:
                    quit()
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    R += 5
                    if R >= 255:
                        R = 0
                                        
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    G += 5
                    if G >= 255:
                        G = 0
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    B += 5
                    if B >= 255:
                        B = 0
                    
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    R = 8
                    G = 12
                    B = 57
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    counter += 1
                    
                # Il giocatore inizia una nuova partita premendo la barra spaziatrice
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                    START_GAME.play()
                    pygame.mixer.music.play()
                    hai_perso = False
                

        
    # Controllo quale tato viene premuto dal giocatore
    for event in pygame.event.get():
        # Il giocatore chiude la finestra del gioco premendo il pulsante X in alto a destra
        if event.type == pygame.QUIT:
            quit()
        # il personaggio sale premendo la barra spaziatrice. Il personaggio non può salire se yPers != Y_PERS_INIT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if yPers < Y_PERS_INIT:
                is_running = False 
            else:
                is_running = True 
                
            if is_running == True: 
                SALTO.play()          
                 
            while is_running:
                disegna_oggetti()
                yPers -= VEL_SALTO
                movimento_oggetti()  
                if yPers == Y_PERS_MIN: # yPers raggiunge 158 e poi comincia a scendere
                    break
                traslazione_oggetti()               
                aggiorna()
                
            
                    
    aggiorna()