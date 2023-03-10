import pygame as pg


def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 40)
    gray = pg.Color('gray19')
    blue = pg.Color('dodgerblue')
    # The clock is used to limit the frame rate
    # and returns the time since last tick.
    clock = pg.time.Clock()
    timer = 10*60  # Decrease this to count down.
    dt = 0  # Delta time (time since last tick).
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        timer -= dt
        min=timer//60
        sec=timer%60
        ms=timer-int(timer)
        if timer <= 0:
            timer = 10  # Reset it to 10 or do something else.
            

        screen.fill(gray)
        txt = font.txt = font.render(str(int(min))+":"+str(int(sec)+round(ms,1)), True, blue)
        screen.blit(txt, (70, 70))
        pg.display.flip()
        dt = clock.tick() / 1000  # / 1000 to convert to seconds.
if __name__ == '__main__':
    main()
    pg.quit()
