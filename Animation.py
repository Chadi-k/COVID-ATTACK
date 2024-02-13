import pygame
import pygame
from pygame import*
from pygame.gfxdraw import*
from random import *
from pygame.time import*
pygame.mixer.init()
pygame.init()
largeur= 1100
hauteur= 550
fenetre = display.set_mode((largeur,hauteur))
display.set_caption("Animation")
rouge = (255,0,0)
blanc = (250,250,250)

fond = image.load("images/earth2.png").convert()
virus= image.load("images/coronavirus.png").convert_alpha()
vaccin1= image.load("images/vaccin.png").convert_alpha()
vaccin2= image.load("images/vaccin2.png").convert_alpha()
vaccin3= image.load("images/vaccin3.png").convert_alpha()
vaccin4= image.load("images/vaccin4.png").convert_alpha()
image_menu= image.load("images/menu3.jpg").convert()
point_rouge= image.load("images/localisation.png").convert_alpha()
game_over= image.load("images/gameover.png").convert_alpha()

cible_son = pygame.mixer.Sound("sons/cible.ogg")
gameover_son = pygame.mixer.Sound("sons/gameover.ogg")

fenetre.blit(image_menu,(0,0))
display.flip()



reponse=True
def mouvement (reponse):        #fonction mouvement qui met en mouvement les vaccins et le virus, elle permet aussi de detecter si l'utilisateur à viser soi un point rouge, qui augmetera son score soit un vaccin qui lui ferra perdre la partie
    reponse=True
    x_vaccin= 0
    y_vaccin= (randint(0,5))*100                  #placement du vaccin aléatoire grâce a randint
    x_vaccin2= 1100
    y_vaccin2= (randint(0,5))*100                   #""
    x_vaccin3=  (randint(0,11))*100                 #""
    y_vaccin3= 0
    y_vaccin4=550
    x_vaccin4= (randint(0,11))*100                  #""
    niveau=0
    niveau=menu(niveau)                             #appel de la variable qui retourne aussi le niveau de la partie
    x_cible=randint(150,1050)                       #""
    y_cible=randint(150,450)                        #""
    point=0                                            #variable point qui permet d'augmenter le score
    while reponse:

        pygame.time.delay(15)

        fenetre.blit(fond,(0,0))
        display.flip()

        souris= mouse.get_pos()
        x=souris[0]-40                  # variable x qui permet de prendre la position de la souris  (-40 pour pouvoir centrer la souris)
        y=souris[1]-40                   #variable y qui permet de prendre la position de la souris  (-40 pour pouvoir centrer la souris)
        fenetre.blit(virus,(x,y))
        display.flip()



        fenetre.blit(point_rouge,(x_cible,y_cible))
        display.flip()
        police = pygame.font.Font(None, 50)

        if x_cible<=souris[0]+20 and x_cible+30>=souris[0]-20 and y_cible<=souris[1]+20 and y_cible+30>=souris[1]-20:  #condition qui permet de savoir quand le virus se situe sur le point_rouge
            cible_son.play()
            point= point+1           #incrémentation du score

            x_cible=randint(150,1000)
            y_cible=randint(150,400)


        scorefinal = police.render("score = "+str(point), 1, rouge)         #affichage du score
        position_scorefinal=(450 ,50)
        fenetre.blit(scorefinal,(position_scorefinal))
        display.flip()

        fenetre.blit(vaccin1,(x_vaccin,y_vaccin))
        time.delay(1)
        display.flip()
        if (souris[0]-30<=x_vaccin+130 and souris[0]+30>=x_vaccin+130) and (souris[1]-30<=y_vaccin+13 and souris[1]+30>=y_vaccin+13): #condition qui permet de savoir quand le virus se situe sur le pique du vaccin 1
            gameover_son.play()
            fenetre.blit(game_over,(410,130))
            display.flip()
            time.delay(2000)
            fenetre.blit(image_menu,(0,0))
            display.flip()
            reponse=False
            break
        elif x_vaccin>1090:             #condition qui permet au vaccin de se remettre sur son point de départ
            x_vaccin=-niveau
            y_vaccin= (randint(0,5))*100

        x_vaccin=x_vaccin+niveau                #changement de la position du vaccin selon le niveau cliquer au menu, cela créé un effet de mouvement



        fenetre.blit(vaccin2,(x_vaccin2,y_vaccin2))
        time.delay(1)
        display.flip()
        if (souris[0]+30>=x_vaccin2 and souris[0]-30<=x_vaccin2) and (souris[1]+30>=y_vaccin2+13 and souris[1]-30<=y_vaccin2+13):   #condition qui permet de savoir quand le virus se situe sur le pique du vaccin 2
            gameover_son.play()
            fenetre.blit(game_over,(410,130))
            display.flip()
            time.delay(2000)
            fenetre.blit(image_menu,(0,0))
            display.flip()
            reponse=False
            break
        elif x_vaccin2<10:                    #condition qui permet au vaccin de se remettre sur son point de départ
            x_vaccin2=1110
            y_vaccin2= (randint(0,5))*100

        x_vaccin2=x_vaccin2-niveau              #changement de la position du vaccin selon le niveau cliquer au menu, cela créé un effet de mouvement




        fenetre.blit(vaccin3,(x_vaccin3,y_vaccin3))
        time.delay(1)
        display.flip()
        if (souris[0]+30>=x_vaccin3+13 and souris[0]-60<=x_vaccin3-13) and (souris[1]+30>=y_vaccin3+130 and souris[1]-30<=y_vaccin3+130):     #condition qui permet de savoir quand le virus se situe sur le pique du vaccin 3
            gameover_son.play()
            fenetre.blit(game_over,(410,130))
            display.flip()
            time.delay(2000)
            fenetre.blit(image_menu,(0,0))
            display.flip()
            reponse=False
            break
        elif y_vaccin3>540:                       #condition qui permet au vaccin de se remettre sur son point de départ
            y_vaccin3=-niveau
            x_vaccin3= (randint(0,11))*100

        y_vaccin3=y_vaccin3+niveau          #changement de la position du vaccin selon le niveau cliquer au menu, cela créé un effet de mouvement




        fenetre.blit(vaccin4,(x_vaccin4,y_vaccin4))
        time.delay(1)
        display.flip()
        if souris[0]+30>=x_vaccin4+13 and souris[0]-30<=x_vaccin4+13 and souris[1]-30<=y_vaccin4 and souris[1]+30>=y_vaccin4:           #condition qui permet de savoir quand le virus se situe sur le pique du vaccin 4
            gameover_son.play()
            fenetre.blit(game_over,(410,130))
            display.flip()
            time.delay(2000)
            fenetre.blit(image_menu,(0,0))
            display.flip()
            reponse=False
            break
        elif y_vaccin4<0:                         #condition qui permet au vaccin de se remettre sur son point de départ
            y_vaccin4=560
            x_vaccin4= (randint(0,11))*100

        y_vaccin4=y_vaccin4-niveau              #changement de la position du vaccin selon le niveau cliquer au menu, cela créé un effet de mouvement




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                continuer=0


def compteur ():                  #fonction compteur qui permet de mettre en garde l'utilisateur sur le début du jeu grâce à un compteur allant de 3 à 0 en 3 sencondes
    a=3
    while a>0:
        fenetre.blit(fond,(0,0))
        display.flip()
        consigne = police.render("Ne te fait pas piquer par les vaccins", 1, blanc)
        position_consigne=(250 ,220)
        fenetre.blit(consigne,(position_consigne))
        display.flip()
        consigne2 = police.render("Contamine au maximum", 1, blanc)
        position_consigne2=(320 ,300)
        fenetre.blit(consigne2,(position_consigne2))
        display.flip()
        compteur = police.render(str(a), 1, blanc)
        position_compteur=(540 ,100)
        fenetre.blit(compteur,(position_compteur))
        display.flip()
        time.delay(1000)
        a=a-1





niveau=0
pointclic=0
def menu (niveau):  #fonction menu pour le menu qui détecte si l'utlisateur a choisi le niveau 1 ou 2 et qui retourne ce dernier
    continuer=1
    while continuer:
        pointclic= mouse.get_pos()
        x2=pointclic[0]
        y2=pointclic[1]
        if  x2<550 and x2>0 and y2<550 and y2>0:
            niveau=12
            continuer=0
        elif x2<1100 and x2>550 and y2<550 and y2>0:
            niveau=18
            continuer=0

    return niveau

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            continuer=0



continuer=1
while continuer :
    for event in pygame.event.get():


        if event.type == MOUSEBUTTONDOWN :
            if mouse.get_pressed()==(1,0,0):
                police = pygame.font.Font(None, 50)
                fenetre.blit(fond,(0,0))
                display.flip()

                compteur()

                mouvement(reponse)

        if event.type == QUIT:
            pygame.quit()
            continuer=0



continuer=1
while continuer:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            continuer=0