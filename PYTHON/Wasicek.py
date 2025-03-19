import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np

# Hull-White model parameters
sigma = 0.1          # Volatility
a = 0.1              # Mean reversion
timestep = 360       # Number of time steps in the simulation
length = 30          # Total length of the simulation (in years)
forward_rate = 0.05  # Initial forward rate
day_count = ql.Thirty360(ql.Thirty360.BondBasis)  # Day-count convention
todays_date = ql.Date(15, 1, 2024)  # Evaluation date

# Setting the evaluation date in QuantLib
ql.Settings.instance().evaluationDate = todays_date

# Create a flat forward curve
spot_curve = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)

# Define the Hull-White process
hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, length, timestep, rng, False)

# Function to generate paths
def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr

# Generate and plot 10 paths
num_paths = 10
time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()

# Generate and visualize the variance of short rates over time
num_paths = 1000
time, paths = generate_paths(num_paths, timestep)
vol = [np.var(paths[:, i]) for i in range(timestep+1)]
plt.plot(time, vol, "r-.", lw=3, alpha=0.6)
plt.plot(time, sigma * sigma / (2 * a) * (1.0 - np.exp(-2.0 * a * np.array(time))), "b-", lw=2, alpha=0.5)
plt.title("Variance of Short Rates")
plt.show()

# Function to calculate theoretical mean under Hull-White model
def alpha(forward, sigma, a, t):
    return forward + 0.5 * np.power(sigma / a * (1.0 - np.exp(-a * t)), 2)

# Generate and visualize the mean of short rates over time
avg = [np.mean(paths[:, i]) for i in range(timestep+1)]
plt.plot(time, avg, "r-.", lw=3, alpha=0.6)
plt.plot(time, alpha(forward_rate, sigma, a, time), "b-", lw=2, alpha=0.6)
plt.title("Mean of Short Rates")
plt.show()
