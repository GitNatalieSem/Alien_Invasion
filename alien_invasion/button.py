import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (255, 218, 53)
        self.text_color = (128, 128, 128)
        self.font = pygame.font.SysFont(None, 48)
        # Outline width is created by using a larger background rect, needs to be double in value
        outline_width = 4.0

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.outline_rect = pygame.Rect(0, 0, self.width + outline_width, self.height + outline_width)
        self.rect.center = self.screen_rect.center
        self.outline_rect.center = self.screen_rect.center
        self.outline_rect_color = (128, 128, 128)

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.outline_rect_color, self.outline_rect)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
