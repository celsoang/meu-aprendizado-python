print('Tocando uma musica em mp3')
from pygame import mixer
mixer.init()
mixer.music.load('sigmamusicart.mp3')
mixer.music.queue('fassoundsescapeyourlove.mp3')
mixer.music.play()
input('Música tocando! Aperte ENTER no teclado para encerrar...')


#correção
#Este código só funcionou com o input la embaixo
import pygame
pygame.init()
pygame.mixer.music.load('sigmamusicart.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('ENTER')






