#tocando mp3 com python
#deve-se sempre iniciar o pygame com o comando logo abaixo:
import pygame
pygame.init()
pygame.mixer.music.load('desafio021b.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass
