import pygame


from network import Network

from player import Player

width = 500

height = 500

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")


def redrawWindow(win,players):
    win.fill((255,255,255))
    for player in players:
        player.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        print(p2)

        live_locations=[(player.x,player.y) for player in p2]

        print(live_locations)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        print("my coordinates:",p.x,p.y)
        redrawWindow(win, p2)

main()