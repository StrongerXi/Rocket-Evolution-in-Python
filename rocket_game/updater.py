import settings


class Updater():

    # Takes in a Game_State
    def __init__(self,game_state):

        self.gs = game_state
        self.lor = game_state.lor



    def update_all(self,dt):

        dt = 1 / settings.DEFAULT_FPS

        for r in self.lor:
            if r.stopped :
                continue

            r.update_pos(dt)
            r.update_vel(dt)

            if (self.gs.tick_count % settings.GENE_INTERVAL) == 0 and self.gs.tick_count != 0:
                if r.age == settings.GENE_LENGTH - 1:
                    r.stopped = True #having used up its last gene
                else:
                    r.increment_age()

        self.gs.tick_count += 1



