from CheckersV4 import Checkers
from NeuralN import NeuralNetwork
from ParticleSwarm import CheckersPSO
import random
import time

class Train:
    def __init__(self):
        self.p_size = 40
        self.players = [NeuralNetwork() for i in range(self.p_size)]
        self.fitness = [0 for i in range(self.p_size)]
        self.r = random.Random()
        
    def __init__(self, p):
        self.p_size = 40
        self.players = [NeuralNetwork() for i in range(self.p_size)]
        for i in range(len(p)):
            self.players[i].updateWeights(p[i])
        self.fitness = [0 for i in range(self.p_size)]
        self.r = random.Random()

    # Calculates the fitness of all players in population by playing a number of games vs random opponents.
    def calculateFitness(self):
        opponents = self.r.sample(range(self.p_size), 15)
        for j in range(self.p_size):
            fit = 0
            for i in opponents:
                game = Checkers(True)
                # print("\ngame vs", i)
                result = game.gameTestNN(False, self.players[j], self.players[i])
                if result == 'w':
                    # print("win")
                    fit += 1
                elif result == 'b':
                    # print("loss")
                    fit -= 2
                else:
                    # print("draw")
                    fit += 0
            # print("p" + str(j + 1) + " ", end='', flush=True)
            self.fitness[j] = fit
        # print()

    # Trains the players and returns the player with the best fitness.
    def obtainBestPlayer(self):
        print("\nInitialising.")
        self.calculateFitness()
        indx_of_Best = Checkers.indxOfMax(self.fitness)
        x = [self.players[j].weightVector() for j in range(self.p_size)]
        pso = CheckersPSO(x[:], self.fitness[:], indx_of_Best)
        print("Training")
        for i in range(500):
            print("I"+str(i+1)+ " ", end = '', flush=True)
            '''
            print("\n--------- Before Updates ---------")
            print("particles", pso.x)
            print("personal best", pso.x_pbest)
            print("------current fitness", self.fitness)
            print("personal best fitness", pso.pbest)
            print("global best", pso.gbest, "at index", pso.index)
            '''
            pso.updateParticles(self.fitness[:])
            pso.updateVelocity()

            for i in range(self.p_size):
                self.players[i].updateWeights(pso.x[i])
            '''
            print("\n--------- After Updates ---------")
            print("particles", pso.x)
            print("personal best", pso.x_pbest)
            print("------current fitness", self.fitness)
            print("personal best fitness", pso.pbest)
            print("global best", pso.gbest, "at index", pso.index)
            '''
            self.calculateFitness()
        print("\n")
        # print("best particle", pso.x_Gbest)
        # print("best fit", pso.gbest, "at index", pso.index)
        # print(self.fitness)
        return pso.x_Gbest

    # Test the player with the best fitness on its win rate.
    # Returns percentage of win rate.
    # Variable player refers to the neural network with global best fitness.
    def testPlayerWhite(self, player):
        winw = 0
        winb = 0
        draw = 0
        for i in range(10000):
            game = Checkers(True)
            result = game.gameTestNN_White(False, player)
            if result == 'w':
                # print("win")
                winw += 1
            elif result == 'b':
                # print("loss")
                winb += 1
            else:
                # print("draw")
                draw += 1
        print("white win", winw, "black win", winb, "draw", draw)
        return(winw/100)
    
    # Test the player with the best fitness on its win rate.
    # Returns percentage of win rate.
    # Variable player refers to the neural network with global best fitness.
    def testPlayerBlack(self, player):
        winw = 0
        winb = 0
        draw = 0
        for i in range(10000):
            game = Checkers(True)
            result = game.gameTestNN_Black(False, player)
            if result == 'w':
                # print("win")
                winw += 1
            elif result == 'b':
                # print("loss")
                winb += 1
            else:
                # print("draw")
                draw += 1
        print("white win", winw, "black win", winb, "draw", draw)
        return(winb/100)
    
    def weightVectorToString(self, arr):
        output = ""
        for i in arr:
            output += str(i)+","
        return output

    # Runs the training and checks said players win rate.
    def runner(self):
        start = time.time()
        
        best_player_weights = self.obtainBestPlayer()
        best_player = NeuralNetwork()
        best_player.updateWeights(best_player_weights)
        
        win_rate_w = self.testPlayerWhite(best_player)
        win_rate_b = self.testPlayerBlack(best_player)
        end = time.time()
        print("White win percentage", win_rate_w, "Black win percentage", win_rate_b)
        print("Time taken %.2f" % (end - start))
        f = open("superPlayer.txt", 'a')
        f.write(str(win_rate_w) + "," + str(win_rate_b) + "," + self.weightVectorToString(best_player_weights) + "\n")
        f.close()
        
def getPlayers():
    output = []
    with open("bestPlayers.txt", "r") as fp:
        for line in fp:
            output.append(line.split(","))
    for i in output:
        i.remove("\n")
        i.pop(0)
        i.pop(0)
    for i in range(len(output)):
        for j in range(len(output[i])):
            output[i][j] = float(output[i][j])
    return output

'''
for i in range(1):
    #print("Iteration", i)
    players = getPlayers()
    tester = Train(players)
    tester.runner()
'''


