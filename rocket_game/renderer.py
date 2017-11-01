from pyglet import window, image, sprite, graphics

import settings


class Renderer(window.Window):

    # Attribute: game_window, game_state,
    #               background, target_image, rocket_sprites, rocket_batch

    def __init__(self, game_state):

        self.game_state = game_state

        self.game_window = window.Window(settings.BACKG_WIDTH, settings.BACKG_HEIGHT)
        self.background = sprite.Sprite(settings.BACKG_IMAGE)

        self.prepare_target_image()

        self.prepare_rockets_image()

        self.prepare_obstacles_image()



    def prepare_obstacles_image(self):

        lobs = self.game_state.lobs
        self.obstacle_batch = graphics.Batch()

        self.lobs_images = []

        for obs in lobs:
            center(obs.image)
            self.lobs_images.append(sprite.Sprite(obs.image, batch=self.obstacle_batch, x = obs.x, y = obs.y))



    def prepare_target_image(self):
        self.target = image.load(settings.TARGET_IMAGE_PATH)
        center(self.target)

        self.target_image = sprite.Sprite(self.target, settings.TARGET_X, settings.TARGET_Y)
        scale_to_width(self.target_image, 2 * settings.TARGET_RADIUS)

        self.target = None  # no longer needed after having created a sprite for target image


    # organize rocket images into a batch of sprites
    def prepare_rockets_image(self):

        self.rocket_image = image.load(settings.ROCKET_IMAGE_PATH)
        center(self.rocket_image)

        self.rocket_batch = graphics.Batch()

        self.rocket_sprites = []

        self.initiate_rocket_sprites(self.rocket_batch)

        self.rocket_image = None  # no longer needed after having created the rocket sprites


    def initiate_rocket_sprites(self,batch):

        for i in range(0, len(self.game_state.get_lor())):

            self.rocket_sprites.append(sprite.Sprite(self.rocket_image, batch=batch))
            scale_to_width(self.rocket_sprites[i], 2 * settings.ROCKET_RADIUS)


    # This function will be scheduled in Game_Runner to render the game state onto background
    # It also updates the xy fields of the sprites.

    def draw_all(self,*args):
        self.game_window.clear()
       # print("1")
        self.update_sprites()
      #  print("2")
        self.background.draw()
      #  print("2.5")
        self.target_image.draw()
      #  print("3")
        self.rocket_batch.draw()
      #  print("4")
        self.obstacle_batch.draw()




        # Update the xy fields of Sprite based on its corresponding Rocket's current position
    def update_sprites(self):

        for i in range(0,len(self.game_state.lor)):
            self.rocket_sprites[i].set_position(*self.game_state.lor[i].pos)



    def close_window(self):
        self.game_window.close()




# Loaded Image, move the anchor point of the image to its center
def center(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

# Using scale to resize a sprite to a new width
def scale_to_width(a_sprite , new_width):
    scale_factor = new_width / a_sprite.width
    a_sprite.scale = scale_factor


