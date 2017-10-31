from Simulation import simulator



sim = simulator.Simulator()

print("pleast enter how many simulations WITHOUT gui you would like")
no_gui_sim = int(input())

print("pleast enter how many simulations WITH gui you would like\n")
gui_sim = int(input())




sim.simulate_without_gui(no_gui_sim)

sim.simulate(gui_sim)

input("press enter to proceed and watch the final simulation\n")

sim.simulate(1)