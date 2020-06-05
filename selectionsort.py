import pygame
pygame.init()
screen=pygame.display.set_mode((750,600))
pygame.display.set_caption("selection sort")
exit=False
font1=pygame.font.SysFont(pygame.font.get_fonts()[0],25,True,False)
sorting=True
l=[500,400,300,200,150,50,100,30]
screen.fill((255,255,255))
clock=pygame.time.Clock()
def updatelist(l,current):
    screen.fill((255,255,255))
    xcord=50
    for i in range(len(l)):
        if i==current:
            pygame.draw.rect(screen,(0,255,0),(xcord,3,30,l[current]),0)
        else:
            pygame.draw.rect(screen,(255,0,0),(xcord,3,30,l[i]),0)
        xcord+=100
while not(exit):
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                sorting=False
        if sorting:
            updatelist(l,0)
            text=font1.render("Press space to sort",1,(0,0,255))
            screen.blit(text,(400,550))
            pygame.display.update()
        elif sorting==False:
                for j in range(len(l)):
                    for k in range(j+1,len(l)):
                        if l[j]>l[k]:
                            l[j],l[k]=l[k],l[j]
                            updatelist(l,j)
                            pygame.time.delay(200)
                            pygame.display.update()
pygame.quit()
