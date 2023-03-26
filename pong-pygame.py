import pygame, random
from pong.modules import Paddle, Ball
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

spriteList = pygame.sprite.Group()
spriteList.add(paddleA, paddleB, ball)

gameExit = False

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameExit = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    spriteList.update()

    if ball.rect.x>=690:
        scoreA += 1
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity = [random.choice([random.randint(3, 6), random.randint(-6, -3)]), random.randint(-4, 4)]
    if ball.rect.x<=0:
        scoreB += 1
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity = [random.randint(3, 6), random.randint(-4, 4)]
    if ball.rect.y>490 or ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]
    
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
    
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    spriteList.draw(screen)

    font = pygame.font.Font(None, 74)
    scoreAText = font.render(str(scoreA), 1, WHITE)
    screen.blit(scoreAText, (250,10))
    scoreBText = font.render(str(scoreB), 1, WHITE)
    screen.blit(scoreBText, (420,10))

    pygame.display.flip()

    clock.tick(120)

pygame.quit()