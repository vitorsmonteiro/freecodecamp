import copy
import random
from re import A
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self._initial_contents = kwargs
        self.get_contents()
        
    def get_contents(self):
        for key, item in self._initial_contents.items():
            for i in range(item):
                self.contents.append(key)
    
    def draw(self, num):
        _draws = []
        for i in range(num):
            _draw = random.choice(self.contents)
            _draws.append(_draw)
            self.contents.remove(_draw) 
        return _draws
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    if num_balls_drawn > len(hat.contents):
        return 1
    for exp in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        draw = test_hat.draw(num_balls_drawn)
        expected = []
        for key, item in expected_balls.items():
            for i in range(item):
                expected.append(key)
        aux_draw = copy.deepcopy(draw)
        aux_expected = copy.deepcopy(expected)
        for item in expected:
            if item in aux_draw:
                aux_expected.remove(item)
                aux_draw.remove(item)
        if len(aux_expected) == 0:
            num_success += 1 
    return num_success / num_experiments
