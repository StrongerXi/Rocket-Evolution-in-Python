
import settings
from Simulation import evaluator
from Simulation import evolution
from basics import initiator
from rocket_game.game_runner import GameRunner
from rocket_game.game_state import GameState


# TODO: debug Evaluator and Evolution Classes
# check evaluators and stuff...
# clean up algorithms


# count represents the number of simulations requested
class Simulator():

    closed = False

    def __init__(self, log = initiator.initiate_random_log(settings.POPULATION, settings.GENE_LENGTH)):
        self.log = log

    def simulate(self,count):

        while(count > 0):
            print(count)

            self.initiate()
            self.gs = self.runner.run()

            tuple_of_gene_and_fitness = evaluator.evaluate_fitness_lor(self.gs.lor,self.gs.lobs)

            self.log = evolution.evolve_all(tuple_of_gene_and_fitness)

            count -= 1
            #stop all simulation if the window/game runner is force closed
            if GameRunner.forceQuit:
                count = 0

        return self.gs.get_log()



    def simulate_without_gui(self, count):

        if count == 0:
            return [[]]

        while (count > 0):

            print(count)

            self.initiate()
            self.gs = self.runner.run_without_render()

            tuple_of_gene_and_fitness = evaluator.evaluate_fitness_lor(self.gs.lor, self.gs.lobs)

            self.log = evolution.evolve_all(tuple_of_gene_and_fitness)

            count -= 1
        return self.gs.get_log()


    # converting self's list of gene into a new list of rocket
    # then use lor to set up a new game state, and feed the state to runner
    def initiate(self):
        self.lor = initiator.initiate_lor(self.log)
        self.game = GameState(lor=self.lor)
        self.runner = GameRunner(self.game)
