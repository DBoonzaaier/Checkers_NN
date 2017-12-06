import random
import math

class PSO:
    def __init__(self):
        self.r1 = random.Random()
        self.r2 = random.Random()

        self.d = 2                               # Dimension of problem to be solved
        self.s = 10                              # Size of swarm, no. of particles

        self.maxIter = 0
        self.x = []                              # position of particles
        self.v = []                              # velocity of particles

        self.x_pbest = []                        # personal best positions
        self.pbest = []                          # personal best of particles

        self.fitness = []
        self.index = 0

        self.x_Gbest = []                        # global best position
        self.bVector = []
        self.gbest = 0

        self.constrictFact = 1.0
        self.c1 = 2.0
        self.c2 = 2.0
        self.error = 1.0e-6

    def func(self, arr):
        return (arr[0] * arr[0]) + (arr[1] * arr[1])

    def performPSO(self):
        self.maxIter = int(1000/self.s)

        x_min = -100.0
        x_max = 100.0
        v_max = 100.0

        # Create 's' 2-dimensional particles
        # --------------------------------------------------------------------------------------------------------------

        self.x = [[(self.r1.random() * (x_max - x_min) + x_min) for j in range(self.d)] for i in range(self.s)]
        self.v = [[self.r2.random() * v_max if (self.r2.random() > 0.5 ) else self.r2.random() * -1 * v_max for j in range(self.d)] for i in range(self.s)]

        self.bVector = self.x[0][:]
        self.x_Gbest = self.x[0][:]

        bestFitness = self.func(self.bVector)

        for i in range(self.s):
            self.bVector = self.x[i][:]
            fit = self.func(self.bVector)

            self.fitness.append(fit)
            self.pbest.append(fit)

            self.x_pbest.append(self.x[i][:])                                   # save position as pbest at start

            if self.fitness[i] <= bestFitness:
                bestFitness = self.fitness[i]
                self.x_Gbest = self.bVector                                     # save best pbest as global best
                self.index = i                                                  # save particles index

        self.gbest = bestFitness

        # End of creation of 's' 2-dimensional particles
        # --------------------------------------------------------------------------------------------------------------
        i = 0
        while i < self.maxIter:
            w = 1.0 - i * ((1.0 - 0.1) / self.maxIter)
            i += 1
            print(i, "  \t\t", self.gbest)

            for j in range(self.s):
                self.bVector = self.x[j][:]
                val = self.func(self.bVector)

                self.fitness[j] = val

                if self.fitness[j] < self.pbest[j]:
                    self.pbest[j] = self.fitness[j]
                    self.x_pbest[j] = self.x[j][:]

                if self.fitness[j] < self.gbest:
                    self.gbest = self.fitness[j]
                    self.x_Gbest = self.x[j][:]
                    self.index = j

            for j in range(self.s):
                for k in range(self.d):
                    r_1 = self.r1.random()
                    r_2 = self.r2.random()

                    social = self.c1 * r_1 * (self.x_Gbest[k] - self.x[j][k])
                    cognitive = self.c2 * r_2 * (self.x_pbest[j][k] - self.x[j][k])
                    self.v[j][k] = (self.constrictFact * (w * self.v[j][k] + social + cognitive))

                    if math.fabs(self.v[j][k]) >= v_max:
                        if(self.v[j][k] > 0):
                            self.v[j][k] = v_max
                        else:
                            self.v[j][k] = v_max * -1

                    self.x[j][k] += self.v[j][k]
        return self.gbest

class CheckersPSO:
    # x is the array of particles.
    # fit is the initial fitness array.
    def __init__(self, x, fit, indexOfBestFit):
        self.r1 = random.Random()
        self.r2 = random.Random()

        self.d = 171                                            # Dimension of problem to be solved.
        self.s = 40                                             # Size of swarm, no. of particles.

        self.x = x[:]                                           # position of particles.
        self.v = [[self.r2.random() if (self.r2.random() > 0.5) else self.r2.random() * -1 for j in
                   range(self.d)] for i in range(self.s)]       # Velocity of particles

        self.x_pbest = [self.x[i][:] for i in range(self.s)]    # personal best positions of particles.
        self.pbest = fit                                        # personal best fitness of particles.

        self.index = indexOfBestFit

        self.x_Gbest = self.x[self.index][:]                    # global best position. Particle.
        self.gbest = self.pbest[self.index]                     # Fitness.

        self.constrictFact = 1.0
        self.c1 = 1.0
        self.c2 = 1.0
        self.v_max = 0.15

    # Update the particles' personal bests positions and the global best.
    # Variable fit refers to an array of new fitness values.
    def updateParticles(self, fit):
        for j in range(self.s):
            if fit[j] >= self.pbest[j]:
                self.pbest[j] = fit[j]
                self.x_pbest[j] = self.x[j][:]

            if fit[j] >= self.gbest:
                self.gbest = fit[j]
                self.x_Gbest = self.x[j][:]
                self.index = j

    # Update the velocity of each particle based on the velocity function.
    def updateVelocity(self):
        for j in range(self.s):
            for k in range(self.d):
                r_1 = self.r1.random()
                r_2 = self.r2.random()

                social = self.c1 * r_1 * (self.x_Gbest[k] - self.x[j][k])
                cognitive = self.c2 * r_2 * (self.x_pbest[j][k] - self.x[j][k])
                self.v[j][k] = (self.constrictFact * self.v[j][k] + social + cognitive)

                if math.fabs(self.v[j][k]) > self.v_max:
                    if self.v[j][k] > 0:
                        self.v[j][k] = self.v_max
                    else:
                        self.v[j][k] = self.v_max * -1


                self.x[j][k] += self.v[j][k]
                self.x[j][k] = round(self.x[j][k], 10)

'''
test = PSO()
gbest = test.performPSO()
print("\ng best =\t",gbest)
'''
