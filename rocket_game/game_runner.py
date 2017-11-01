import pyglet
import settings
from rocket_game import checker
from rocket_game import renderer
from rocket_game import updater


class GameRunner:

    forceQuit = False

    def __init__(self,game_state):

        self.gs = game_state
        self.update = updater.Updater(game_state)
        self.check = checker.Checker(game_state)


    # The Runner method returns the gene list of lor
    # This could be used for evolution in simulator
    def run(self):

        self.render = renderer.Renderer(self.gs)

        print("running game.")

        self.set_up_clock_events()

        pyglet.app.run()

        print("game has ended")

        # window.has_exit becomes true when the pyglet window is forced to close
        if self.render.game_window.has_exit:
            GameRunner.forceQuit = True

        return self.gs


    # This function schedules necessary events for game running with gui
    def set_up_clock_events(self):

        tickrate = 1 / self.gs.fps

        pyglet.clock.schedule_interval(self.render.draw_all, tickrate)
        pyglet.clock.schedule_interval(self.update.update_all, tickrate)
        pyglet.clock.schedule_interval(self.check.check_all, tickrate)
        pyglet.clock.schedule_interval(self.exit_action, tickrate)

    # This Defines what happens when game is over
    # Could be modified conveniently to restart a simulation in simulator Class
    def exit_action(self,*args):

        if self.gs.game_over_flag == True:
            pyglet.clock.unschedule(self.render.draw_all)
            pyglet.clock.unschedule(self.update.update_all)
            pyglet.clock.unschedule(self.check.check_all)
            pyglet.clock.unschedule(self.exit_action)

            self.render.close_window()
            pyglet.app.exit()
        else:
            pass




    # This runs the game without graphic rendering.
    # It speeds up the simulation/evolution significantly
    def run_without_render(self, dt=1 / settings.DEFAULT_FPS):

        while (self.gs.game_over_flag == False):
            self.update.update_all(dt)
            self.check.check_all(dt)

        return self.gs






