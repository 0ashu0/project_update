import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt

def wiener_process(dt = 0.1, x0 = 0, n = 10000):
    # W(t=0)=0
    # initialize W(t) with zero
    W = np.zeros(n+1)

    # we create N+1 timesteps: t=0,1,2,3...N
    t = np.linspace(x0, n, n+1)

    # use cumulative sum: on every step the additional values is drwan
    # from a normal distribution with mean 0 and variance dt .. N(0,dt)
    # N(0,dt) = sqrt(dt)*N(0,1)

    W[1:n+1] = np.cumsum(np.random.normal(0, np.sqrt(dt), n))
    print(W[:10])

    return t, W

def plot_process(t, W):
    plt.plot(t,W)
    plt.xlabel('Time(t)')
    plt.ylabel('Wiener process W(t)')
    plt.title('Wiener-process')
    plt.show()

if __name__ == '__main__':
    time, data = wiener_process()
    plot_process(time, data)
