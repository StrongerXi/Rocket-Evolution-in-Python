import settings
from basics import initiator


class GameState:

    #Attributes: lor (list of Rockets)
    #              lob (list of Obstacles
    #            fps (Positive Number)
    #            game_over_flag (a flag)        tickcount
    #               Number of Rockets
    def __init__(self, fps = settings.DEFAULT_FPS, lor = initiator.initiate_random_lor(settings.POPULATION , settings.GENE_LENGTH)):

        self.tick_count = 0
        self.game_over_flag = False
        self.fps = fps
        self.lor = lor
        self.lob = [settings.OBSTACLE_1, settings.OBSTACLE_2, settings.OBSTACLE_3]
        self.numOfRockets = len(self.lor)

    def get_rocket(self,index):
        return self.lor[index]

    def get_log(self):
        log = []
        for rocket in self.lor:
            log.append(rocket.gene)

        return log







