import pygame

MAX_HEIGHT = 600
MAX_WIDTH = 800


class Grid:
    def __init__(self, pixels):
        self.validate_grid(pixels)
        self.height = len(pixels)
        self.width = len(pixels[0])
        self.pixels = pixels
        self.keyactions = {}
        self.clock = pygame.time.Clock()
        self.framerate = 60
        self.update_while_draw = False

        # Calculate size of pixels
        plength = min(MAX_HEIGHT / self.height, MAX_WIDTH / self.width)
        screen_size = (self.width * plength, self.height * plength)
        self.plength = plength
        self.screen_size = screen_size

        pygame.init()
        self.screen = pygame.display.set_mode(screen_size, pygame.SCALED)
        self.rects = [[pygame.Rect(i * plength, j * plength, plength, plength)
                       for i in range(self.width)]
                      for j in range(self.height)]

        # Make a separate grid to keep track of which rects need to be updated
        self.prev_pixels = [[None for x in row] for row in self.pixels]

    def validate_grid(self, new_pixels):
        """Verifies that the grid is a rectangular array and that the dimensions
           are the same as when it was initialized."""
        if (not hasattr(self, 'pixels')):
            w = len(new_pixels[0])
            for row in new_pixels:
                if len(row) != w:
                    raise ValueError("Grid must be a rectangular 2d array.")
        else:
            if len(new_pixels) != len(self.pixels):
                raise ValueError("Cannot change dimensions of grid after initializing.")
            for i in range(len(new_pixels)):
                if len(new_pixels[i]) != len(self.pixels[i]):
                    raise ValueError("Cannot change dimensions of grid after initializing.")

    def onkey(self, key, action):
        """Binds keyboard key to action, which must be a function of zero arguments. When
           the drawing is run, pressing that key will call the function."""
        self.keyactions[pygame.key.key_code(key)] = action

    def onclick(self, action):
        """Binds mouse button 1 to the action, which must be a function of two arguments:
           the x and y indices of the pixel that was clicked on."""
        self.onclick = action

    def update(self):
        """Redraws the grid of pixels. Only redraws pixels that have changed since the last
           time this function was called."""
        self.validate_grid(self.pixels)

        to_update = []

        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[i])):
                if self.prev_pixels[i][j] != self.pixels[i][j]:
                    self.prev_pixels[i][j] = self.pixels[i][j]
                    to_update.append(self.rects[i][j])
                    pygame.draw.rect(self.screen, self.pixels[i][j], self.rects[i][j])

        pygame.display.update(to_update)

    def set_framerate(self, r):
        """Sets maximum framerate for grid drawing."""
        self.framerate = r

    def start(self, stepfn):
        """Runs the drawing, calling the step function every frame. Listens for key
           and mouse events setup with onkey and onclick."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    for key, action in self.keyactions.items():
                        if event.key == key:
                            action()
            if pygame.mouse.get_pressed()[0]:
                mousex, mousey = pygame.mouse.get_pos()
                px = int(mousex // self.plength)
                py = int(mousey // self.plength)
                self.onclick(px, py)
                if self.update_while_draw:
                    stepfn()
                    self.clock.tick(self.framerate)
            elif (not self.update_while_draw):
                stepfn()
                # limit framerate to 60 but only for normal frames so drawing with onclick is nicer
                self.clock.tick(self.framerate)
            self.update()

        pygame.quit()
