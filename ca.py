import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random 
# %matplotlib inline

u = np.array([[4], [2], [1]])
def step(x, rule_b):
    """Compute a single stet of an elementary cellular
    automaton."""
    # The columns contains the L, C, R values
    # of all cells.
    y = np.vstack((np.roll(x, 1), x,
                   np.roll(x, -1))).astype(np.int8)
    # We get the LCR pattern numbers between 0 and 7.
    z = np.sum(y * u, axis=0).astype(np.int8)
    # We get the patterns given by the rule.
    return rule_b[7 - z]

def generate(rule, size=100, steps=100):
    """Simulate an elementary cellular automaton given
    its rule (number between 0 and 255)."""
    # Compute the binary representation of the rule.
    rule_b = np.array(
        [int(_) for _ in np.binary_repr(rule, 8)],
        dtype=np.int8)
    x = np.zeros((steps, size), dtype=np.int8)
    # Random initial state.
    x[0, :] = np.random.rand(size) < .5
    # Apply the step function iteratively.
    for i in range(steps - 1):
        x[i + 1, :] = step(x[i, :], rule_b)
    return x

def gen_color():
    r = random.random()
    b = random.random()
    g = random.random()
    return [r, g, b]

def load_rules(cap=10000):
    rules = []
    with open("slide_data_random.txt") as f:
        raw = f.readlines()
    for index, rule in enumerate(raw):
        rules.append(int(rule.rstrip('\n')))

        if index == cap:
            break

    return rules

if __name__ == "__main__":

    rules = load_rules()
    print(rules)

    emp = np.zeros((100, 100), dtype=np.int8).astype('float')
    cmap = plt.cm.get_cmap('gray')
    norm = plt.Normalize(emp.min(), emp.max())
    full = cmap(norm(emp))
    
    for index, rule in enumerate(rules):

        x = generate(rule).astype('float')

        cmap = plt.cm.get_cmap('gray')
        norm = plt.Normalize(x.min(), x.max())
        rgba = cmap(norm(x))
        
        color = [0.0, 0.0, 0.0]
        while sum(color) <= 0.5:
            color = gen_color()
        # print(color)
        if index % 100 == 0:
            print("At generation: ", index)

        # for i in range(100):
        #     for j in range(100):
        #         if (full[i, j, :4][3] > 0.0):
        #             full[i, j, :4][3] -= 0.5



        for i in range(100):
            for j in range(100):
                if (rgba[i, j, :3][0] == 1.0 and rgba[i, j, :3][1] == 1.0 and rgba[i, j, :3][2] == 1.0):
                    # print(rgba[i, j, :3])
                    full[i, j, :3][0] = color[0]
                    full[i, j, :3][1] = color[1]
                    full[i, j, :3][2] = color[2]

                    
                    # full[i, j, :3] = rgba[i, j, :3]
    
    plt.axis("off")
    plt.imshow(full, interpolation='none')
    plt.show()