import numpy as np
import matplotlib.pyplot as plt

def geometric_random_walk(steps, initial_price, up_factor, down_factor, probability):
    # Generate random moves (True for up, False for down)
    moves = np.random.random(steps) < probability
    
    # Create multipliers based on moves
    multipliers = np.where(moves, up_factor, down_factor)
    
    # Calculate prices using cumulative product
    prices = initial_price * np.cumprod(multipliers)
    
    return prices

def arithmetic_random_walk(steps, initial_price, up_move, down_move, probability):
    # Generate random moves (True for up, False for down)
    moves = np.random.random(steps) < probability
    
    # Create price changes based on moves
    changes = np.where(moves, up_move, down_move)
    
    # Calculate prices using cumulative sum
    prices = initial_price + np.cumsum(changes)
    
    return prices

def run_simulation(probability):
    geo_prices = geometric_random_walk(steps, initial_price, up_factor, down_factor, probability)
    arith_prices = arithmetic_random_walk(steps, initial_price, up_move, down_move, probability)
    
    plt.figure(figsize=(10, 6))
    plt.plot(geo_prices, label='Geometric Random Walk')
    plt.plot(arith_prices, label='Arithmetic Random Walk')
    plt.title(f'Random Walk Simulation (p = {probability})')
    plt.xlabel('Time Steps')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'random_walk_p{probability}.png')
    plt.close()

steps = 100
initial_price = 100
up_factor = 1.01
down_factor = 0.99
up_move = 1
down_move = -1
probabilities = [0.3, 0.5, 0.7]  # We'll test different probabilities

for p in probabilities:
    run_simulation(p)

print("Simulations complete. Check the current directory for output images.")
