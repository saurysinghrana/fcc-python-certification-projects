"""
Probability Calculator

Estimates probabilities through repeated random experiments
using Monte Carlo simulation.

Completed as part of the freeCodeCamp Scientific Computing
with Python certification.
"""

import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []

        for color, count in balls.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, number):
        if number >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn

        drawn = []

        for _ in range(number):
            index = random.randrange(len(self.contents))
            drawn.append(self.contents.pop(index))

        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn = new_hat.draw(num_balls_drawn)

        success = True

        for color, required in expected_balls.items():
            if drawn.count(color) < required:
                success = False
                break

        if success:
            successes += 1

    return successes / num_experiments


if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)

    probability = experiment(
        hat=hat,
        expected_balls={"red": 2, "green": 1},
        num_balls_drawn=5,
        num_experiments=2000,
    )

    print(f"Estimated probability: {probability:.3f}")