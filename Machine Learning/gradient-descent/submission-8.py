class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations >=0 and 1>learning_rate>0:
            for iter in range(0, iterations):
                x_new = init - learning_rate*(2*init)
                init = x_new          
        else:
            print("invalid input arguments")
            exit()

        return round(init, 5)