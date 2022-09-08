import random
from matplotlib import pyplot as plt

def randomwalk2d(N, line_width = 1.5):
    
    """

    Parameters
    ----------
    N : integer
        The number of steps.
        
    line_width: float
        The width of path lines in the plot. The default value is 1.5. 
        You can adjust this value greater than zero.
        
        As the number of steps increases, the lines overlap. Thus, by decreasing
        the line width, the plot gets clearer.
        
        For large number of steps (over 10^4), the line width is suggested to be
        set low.
        
    Returns
    -------
    A 2D random walk graph.

    """
        
    x, y = 0, 0
    rrr = []
    for i in range(N):
        rn = random.random()
        
        # move right
        if rn >= 0 and rn < 1/4:
            x += 1
            rrr.append([x, y])
        
        # move left
        elif rn >= 1/4 and rn < 1/2:
            x -= 1
            rrr.append([x, y])
        
        # move up
        elif rn >= 1/2 and rn < 3/4:
            y += 1
            rrr.append([x, y])
            
        # move down
        else:
            y -= 1
            rrr.append([x, y])
    
    xs = [inside[0] for inside in rrr]
    ys = [inside[1] for inside in rrr]
    
    plt.plot(xs, ys, linewidth = line_width)
    plt.xlabel('x - dircetion')
    plt.ylabel('y - direction')
    plt.title('2D Random Walk')
    plt.show()