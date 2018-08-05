from Display import Display
import pygame
import random
import sys

s = [800,600]

pygame.init()
screen = pygame.display.set_mode(s,0,32)
pygame.display.set_caption("Hangman v1 by NIP")
finalImages = [pygame.image.load(f"Images/final{i}.jpg").convert() for i in range(11)]

big = pygame.font.SysFont("Garamond MS",50)
med = pygame.font.SysFont("Garamond MS",20)

def startscreen():
    head = big.render("Hangman v1",True,(0,0,0))
    foot = med.render("Click to play",True,(0,0,0))
    
    while True:
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        screen.blit(head,head.get_rect(center=[s[0]/2,s[1]/2-50]))
        screen.blit(foot,foot.get_rect(center=[s[0]/2,s[1]/2+40]))

        pygame.display.flip()

def endscreen(info):
    lives,final,win = info

    head = big.render(f"You {'won' if win else 'lost'} with {lives}/10 {'life' if lives == 1 else 'lives'} remaining!"),True,(0,0,0))
    foot = big.render(f"The final word was: {final}",True,(0,0,0))

    while True:
        screen.blit(finalImages[10-lives],(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                return

        screen.blit(head,(40,40))
        screen.blit(foot,foot.get_rect(bottomleft=[40,s[1]-40]))

        pygame.display.flip()

def input_screen():
    rects = {
    2:[pygame.Rect(2*s[0]/3+10,20,s[0]/3-40,s[1]-40),(255,0,0),big.render("Hard",True,(0,0,0)),[s[0] * (5/6),s[1]/2]],
    1:[pygame.Rect(s[0]/3+20,20,s[0]/3-40,s[1]-40),(255,140,0),big.render("Medium",True,(0,0,0)),[s[0]/2,s[1]/2]],
    0:[pygame.Rect(30,20,s[0]/3-40,s[1]-40),(0,255,0),big.render("Easy",True,(0,0,0)),[s[0]/6,s[1]/2]]
    }
    
    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for k,v in rects.items():
                    if pygame.Rect([i-1 for i in pygame.mouse.get_pos()],(2,2)).colliderect(v[0]):
                        return k

        for i in rects.values():
            pygame.draw.rect(screen,i[1],i[0],0)
            screen.blit(i[2],i[2].get_rect(center=i[3]))

        pygame.display.flip()

def main():
    startscreen()

    while True:
        choice = input_screen()
        
        d = Display(choice,screen,s,big,med)
        d.run()
        endscreen(d.get_results())

if __name__ == "__main__":
    main()
