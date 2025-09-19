import pygame
pygame.init()


# settings
DEFAULT_VEL_xy = (2, 2)
VELOCITY_INCREMENT = 1
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600


# setup
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.RESIZABLE)
clock = pygame.Clock()

class Block:
    def __init__(self, coord_x: int, coord_y: int, vel_x: int = DEFAULT_VEL_xy[0], vel_y: int = DEFAULT_VEL_xy[1], color: tuple = (255, 255, 255)):
        self.rect = pygame.Rect(coord_x, coord_y, 50, 50)
        self.velocity_x = vel_x
        self.velocity_y = vel_y
        self.color = color
        self.defaults = (coord_x, coord_y, vel_x, vel_y, color)
    
    def reset(self):
        self.rect = pygame.Rect(self.defaults[0], self.defaults[1], 50, 50)
        self.velocity_x = self.defaults[2]
        self.velocity_y = self.defaults[3]
        self.color = self.defaults[4]
    
    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)

blocks = [Block(100, 300, color=(0, 200, 200))] # set starter blocks


# main loop
while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for block in blocks:
                    block.reset()
            
            if event.key == pygame.K_UP:
                blocks.append(Block(300, 100))
            
            if event.key == pygame.K_DOWN:
               if len(blocks) > 1: del blocks[-1]
            
            if event.key == pygame.K_LEFT:
                for block in blocks:
                    block.velocity_x -= VELOCITY_INCREMENT if block.velocity_x > 0 else -VELOCITY_INCREMENT
                    block.velocity_y -= VELOCITY_INCREMENT if block.velocity_y > 0 else -VELOCITY_INCREMENT
            
            if event.key == pygame.K_RIGHT:
                for block in blocks:
                    block.velocity_x += VELOCITY_INCREMENT if block.velocity_x >= 0 else -VELOCITY_INCREMENT
                    block.velocity_y += VELOCITY_INCREMENT if block.velocity_y >= 0 else -VELOCITY_INCREMENT

    for i, block in enumerate(blocks):
        if block.rect.top <= 0 or block.rect.bottom >= DISPLAY_HEIGHT:
            block.velocity_y = -block.velocity_y
            block.rect.top = 0 if block.rect.top <= 0 else DISPLAY_HEIGHT - block.rect.height
        
        if block.rect.left <= 0 or block.rect.right >= DISPLAY_WIDTH:
            block.velocity_x = -block.velocity_x
            block.rect.left = 0 if block.rect.left <= 0 else DISPLAY_WIDTH - block.rect.width
        
        for other in blocks[i+1:]:
            if block is other:
                continue
            elif block.rect.colliderect(other.rect):
                top = abs(block.rect.top - other.rect.bottom)
                bottom = abs(block.rect.bottom - other.rect.top)
                left = abs(block.rect.left - other.rect.right)
                right = abs(block.rect.right - other.rect.left)
                side = min(top, bottom, left, right)

                if side == top or side == bottom:
                    hold = block.velocity_y
                    block.velocity_y = other.velocity_y
                    other.velocity_y = hold
                    block.rect.top = other.rect.bottom if side == top else other.rect.top - block.rect.height
                else:
                    hold = block.velocity_x
                    block.velocity_x = other.velocity_x
                    other.velocity_x = hold
                    block.rect.left = other.rect.right if side == left else other.rect.left - block.rect.width
        
        block.rect.left += block.velocity_x
        block.rect.top += block.velocity_y
        
        block.draw()
    
    DISPLAY_WIDTH, DISPLAY_HEIGHT = display.get_size()
    pygame.display.flip()

    clock.tick(120)
