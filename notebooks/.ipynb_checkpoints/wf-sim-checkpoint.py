import random #need this library for later!!
import numpy as np
import argparse 

class Population: #defined my first python class!!
    def __init__(self, N = 10, f = 0.2, with_np = False): #default values introduced here
        #defining attributes and setting them equal to the passed-in values:
        self.N = N #we set "reasonable default values" for this
        self.f = f #we set "reasonable default values" for this
        self.with_np = with_np #I set a default value for this; making attribute a class object
        
        derived_count = round(N*f)
        
        #this if-else generates a population based on whether 'with_np' = T/F
        if self.with_np: 
            self.pop = np.array([0] * (N - derived_count) + [1] * derived_count) 
        else:
            self.pop = [0] * (N - derived_count) + [1] * derived_count #use regular list 
            
    def __repr__(self):
        return f"Population(N={self.N}, f={self.f})"
    
    def step(self, ngens=1):#Pop class is aware of N and f, so we only need to pass in 1 new argument
        for _ in range(ngens): #new argument; calling on functions in random library 
            #if with_np is true it'll use numpy rc, otherwise just uses random choice
            if self.with_np:
                self.pop = np.random.choice(self.pop, size = self.N)
            else:
                self.pop = random.choices(self.pop, k = self.N)
        
    def isMonomorphic(self):
        return len(set(self.pop)) == 1 #returns true if ALL elements in self.pop are the same 

    def get_population(self): #huhhhhh???
        return self.pop

def init_function(N, f):
    derived_count = round(N*f) #determines derived alleles
    return [0] * (N - derived_count) + [1] * derived_count

def run_sim(N, f, ngens, verbose = False):
    population = init_function(N,f)

    for generation in range(ngens):
        # Simulate one step (generation) of the population
        derived_freq = sum(population) / N
        next_gen = [1 if random.random() < derived_freq else 0 for _ in range(N)]
        population = next_gen
        
        # Optionally print verbose output
        if verbose:
            print(f"Generation {generation + 1}: Population = {population}")

    final_derived_freq = sum(population) / N
    print(f"After {ngens} generations, the derived allele frequency is: {final_derived_freq:.4f}")

def main():
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Run a Wright-Fisher simulation")
    
    # Arguments for the simulation
    parser.add_argument('--N', type=int, default=10, help='Population size (N)')
    parser.add_argument('--f', type=float, default=0.2, help='Frequency of derived allele (f)')
    parser.add_argument('--ngens', type=int, default=10, help='Number of generations')
    
    # Verbose flag for additional debugging
    parser.add_argument('--verbose', action='store_true', help='Print verbose debugging information')
    
    args = parser.parse_args()
    
    # Run the simulation with user-defined arguments
    run_sim(args.N, args.f, args.ngens, verbose=args.verbose)


if __name__ == "__main__":
    main()



