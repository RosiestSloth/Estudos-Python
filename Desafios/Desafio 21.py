import pygame

pygame.init()

pygame.mixer.music.load('Desafios/songs/song.ogg')
pygame.mixer.music.play()
pygame.event.wait()