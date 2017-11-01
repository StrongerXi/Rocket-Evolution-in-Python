import settings


class Updater():

    # Takes in a Game_State
    def __init__(self,game_state):

        self.gs = game_state
        self.lor = game_state.lor


    # Update the position, velocity and ages of all rockets.
    # It also increments the tick_count for game_state
    # the dt optional parameter is required for schedule functions for clock(see game_runner)
    def update_all(self,dt):

        dt = settings.DEFAULT_UNIT_TIME

        for rocket in self.lor:
            if rocket.is_flying():
                rocket.update_pos(dt)
                rocket.update_vel(dt)
                self.update_age(rocket)

        self.gs.tick_count += 1


    # Rocket -> Void
    # Updates the rocket's age based on current gs.tick_count and the gene_interval constant in settings
    # if a rocket uses up all its gene's acceleration vectors, change its state accordingly.
    def update_age(self,rocket):

        if (self.gs.tick_count % settings.GENE_INTERVAL) == 0 and self.gs.tick_count != 0:

            if rocket.age == settings.GENE_LENGTH - 1:
                rocket.set_state(settings.State.used_up_gene)  # having used up its last gene
            else:
                rocket.increment_age()

