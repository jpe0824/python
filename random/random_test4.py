import pyautogui as pg
import random

def get_random_position():
    screen_size = pg.size()
    x = random.randint(0, screen_size[0]/2)
    y = random.randint(0, screen_size[1]/2)
    return x, y

def main():
    while True:
        rand_x, rand_y = get_random_position()
        pg.moveTo(rand_x,rand_y, duration=60)

if __name__ == "__main__":
    main()