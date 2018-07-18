#display v1
import pygame
import random
import sys
from libraries import easy, medium, hard

pygame.init()
tmp = pygame.display.set_mode((0,0))

states = [pygame.image.load("state%s.jpg" % i).convert() for i in range(10)]

class Display:
    def __init__(self,difficulty,surface,windowsize,font1,font2): #easy=0,med=1,hard=2
        self.word = list([easy,medium,hard][difficulty]().choose_word())
        self.screen = surface
        self.s = windowsize
        self.font1 = font1
        self.font2 = font2

        self.current = [None]*len(self.word)
        self.correct = []
        self.wrong = []
        self.alphabet = "a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z".split("/")

        self.alphabetSurf = self.get_alphabetSurf()
        self.enterSurf = self.get_enterSurf()

        print(self.word)

    def get_alphabetSurf(self):
        surface = pygame.Surface([self.s[0]//2,self.s[1]])
        surface.fill((0,0,139))

        corr_head = self.font1.render("Corrent letters:",True,(255,140,0))
        corr_body = self.font2.render(",".join(self.correct),True,(255,140,0))

        incorr_head = self.font1.render("Incorrect letters:",True,(255,140,0))
        incorr_body = self.font2.render(",".join(self.wrong),True,(255,140,0))

        remaining_head = self.font1.render("Letters remaining:",True,(255,140,0))
        remaining_body = self.font2.render(",".join([i for i in self.alphabet if not i is None]),True,(255,140,0))

        surface.blit(corr_head,corr_head.get_rect(topleft=[10,(150-corr_head.get_height())/2]))
        surface.blit(corr_body,corr_body.get_rect(topleft=[40,150+((50-corr_body.get_height())/2)]))
        surface.blit(incorr_head,incorr_head.get_rect(topleft=[10,200+((150-incorr_head.get_height())/2)]))
        surface.blit(incorr_body,incorr_body.get_rect(topleft=[40,350+((50-incorr_body.get_height())/2)]))
        surface.blit(remaining_head,remaining_head.get_rect(topleft=[10,400+((150-remaining_head.get_height())/2)]))
        surface.blit(remaining_body,remaining_body.get_rect(topleft=[40,550+((50-remaining_body.get_height())/2)]))

        return surface

    def get_enterSurf(self):
        surface = pygame.Surface([self.s[0]//2,self.s[1]//2])
        surface.fill((0,0,0))
        text = self.font1.render("".join(["_" + (" " if not p == len(self.current)-1 else "") for p,i in enumerate(self.current)]),True,(255,255,255))
        surface.blit(text,text.get_rect(center=[surface.get_width()/2,surface.get_height()/2]))

        return surface

    def update_alphabetSurf(self):
        self.alphabetSurf.fill((0,0,139))
        
        corr_head = self.font1.render("Corrent letters:",True,(255,140,0))
        corr_body = self.font2.render(",".join(self.correct),True,(255,140,0))

        incorr_head = self.font1.render("Incorrect letters:",True,(255,140,0))
        incorr_body = self.font2.render(",".join(self.wrong),True,(255,140,0))

        remaining_head = self.font1.render("Letters remaining:",True,(255,140,0))
        remaining_body = self.font2.render(",".join([i for i in self.alphabet if not i is None]),True,(255,140,0))

        self.alphabetSurf.blit(corr_head,corr_head.get_rect(topleft=[10,(150-corr_head.get_height())/2]))
        self.alphabetSurf.blit(corr_body,corr_body.get_rect(topleft=[40,150+((50-corr_body.get_height())/2)]))
        self.alphabetSurf.blit(incorr_head,incorr_head.get_rect(topleft=[10,200+((150-incorr_head.get_height())/2)]))
        self.alphabetSurf.blit(incorr_body,incorr_body.get_rect(topleft=[40,350+((50-incorr_body.get_height())/2)]))
        self.alphabetSurf.blit(remaining_head,remaining_head.get_rect(topleft=[10,400+((150-remaining_head.get_height())/2)]))
        self.alphabetSurf.blit(remaining_body,remaining_body.get_rect(topleft=[40,550+((50-remaining_body.get_height())/2)]))
        
    def update_imageSurf(self):
        try:
            self.imageSurf = states[len(self.wrong)]
        except:
            self.imageSurf = states[-1]

    def update_enterSurf(self,letter):
        isin = False

        if not chr(letter) in self.alphabet:
            return
        
        for p,i in enumerate(self.word):
            if i == chr(letter):
                self.current[p] = chr(letter)
                
                try:
                    self.alphabet[self.alphabet.index(chr(letter))] = None
                except:
                    pass

                self.correct.append(chr(letter))
                isin = True

        if not isin:
            self.wrong.append(chr(letter))

            try:
                self.alphabet[self.alphabet.index(chr(letter))] = None
            except:
                pass
            
        txt = ""
        for p,i in enumerate(self.current):
            if i is None:
                txt += "_" + (" " if not p == len(self.current)-1 else "")
            else:
                txt += i + (" " if not p == len(self.current)-1 else "")

        text = self.font1.render(txt,True,(255,255,255))
        self.enterSurf.fill((0,0,0))
        self.enterSurf.blit(text,text.get_rect(center=[self.enterSurf.get_width()/2,self.enterSurf.get_height()/2]))

    def run(self):
        while True:
            self.update_imageSurf()
            self.update_alphabetSurf()
            self.events()

            self.screen.blit(self.alphabetSurf,(0,0))
            self.screen.blit(self.imageSurf,(self.s[0]//2,0))
            self.screen.blit(self.enterSurf,(self.s[0]//2,self.s[1]//2))

            pygame.display.flip()

            if len(self.wrong) >= 10 or self.word == self.current:
                return

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.update_enterSurf(event.key)

    def get_results(self):
        return 10-len(self.wrong),"".join(self.word),True if self.current == self.word else False
