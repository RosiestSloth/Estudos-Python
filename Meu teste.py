import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('song.mp3')
resposta = str(input('Você quer tocar a música idontwannabeyouanymore de Billie Eilish? S/N').upper())

print('Tocando...')
sleep(2)
pygame.mixer.music.play()
pygame.event.wait()