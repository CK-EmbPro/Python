# import serial
# import pygame 
# import sys

# pygame.init()

# arduinoData = serial.Serial('/dev/ttyACM0', 9600)

# screen_width = 612
# screen_height = 421
# screen = pygame.display.set_mode(screen_width, screen_height)
# bg_image = pygame.image.load("new.jpg")
# pygame.display.set_caption("Characters Movement Game with Arduino")

# black =(0,0,0)
# white = (255,255,255)
# red = (255,0,0)

# character_width = 50
# character_height = 50
# character_x = (screen_width - character_width) // 2
# character_y = (screen_height - character_height) - 10
# scaling_factor = 3

# run = True
# while run:
#     for event pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False


#     if arduinoData.in_waiting:
#         dataPacket = arduinoData.readLine().decode().strip()
#         try:
#             joy_x, joy_y = map(int, dataPacket.split())
#             character_x += (joy_x -500) // 100 *scaling_factor
#             character_y += (joy_y -500) // 100*scaling_factor

#         except ValueError as e:
#             print("Big data packet: " + dataPacket)

#     character_x = max(0, min(screen_width - character_width, character_x))
#     character_y = max(0, min(screen_height - character_height, character_y))


#     screen.blit(bg_image, (0,0))

#     pygame.draw.rect(screen, white, (character_x, character_y, character_width, character_height))

#     pygame.display.flip()

# arduinoData.close()
# pygame.quite()
# sys.exit() 


import serial
import pygame
import sys

# nitialize Pygame
pygame.init()

# Serial communication settings
arduinoData = serial.Serial("/dev/ttyACM0", 9600)  # Change port and baud rate as needed

# Set up display
screen_width = 612
screen_height = 421
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = pygame.image.load("new.jpg")
pygame.display.set_caption("Character Movement Game with Arduino")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Character settings
character_width = 20
character_height = 20
character_x = (screen_width - character_width) // 2
character_y = screen_height - character_height - 10
scaling_factor = 3  # Adjust the scaling factor to control the character's speed

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if arduinoData.in_waiting:
        dataPacket = arduinoData.readline().decode().strip()
        try:
            joy_x, joy_y = map(int, dataPacket.split())
            character_x += (joy_x - 500) // 100 * scaling_factor
            character_y += (joy_y - 500) // 100 * scaling_factor
        except ValueError as e:
            print("Bad data packet: " + dataPacket)

    # Keep character within the screen boundaries
    character_x = max(0, min(screen_width - character_width, character_x))
    character_y = max(0, min(screen_height - character_height, character_y))
    
    # Fill the screen with a color
    screen.blit(bg_image,(0,0))

    # Draw the character as a red rectangle
    pygame.draw.rect(screen, white, (character_x, character_y, character_width, character_height))

    # Update the display
    pygame.display.flip()

# Close the serial connection, quit Pygame, and exit the program
arduinoData.close()
pygame.quit()
sys.exit()