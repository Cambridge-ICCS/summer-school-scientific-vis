"""Script containing code for exercise 2."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


def generate_synthetic_ocean_current_data(num_frames, nx, ny):
    """Generate synthetic ocean current data."""
    data = []
    for t in range(num_frames):
        u = np.sin(2 * np.pi * (np.linspace(0, 1, nx)[:, None] + t / num_frames)) * 2
        v = np.cos(2 * np.pi * (np.linspace(0, 1, ny)[None, :] + t / num_frames)) * 2
        data.append((u, v))
    return data


# Parameters
num_frames = 60
nx, ny = 50, 50  # Grid size
num_particles = 200

# Generate synthetic ocean current data
ocean_current_data = generate_synthetic_ocean_current_data(num_frames, nx, ny)

# Initialize particle positions
rng = np.random.default_rng()
particle_positions = rng.random((num_particles, 2))
particle_positions[:, 0] *= nx
particle_positions[:, 1] *= ny

# Create figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, nx)
ax.set_ylim(0, ny)
(particles,) = ax.plot(
    particle_positions[:, 0], particle_positions[:, 1], "bo", markersize=2
)


def update_particles(frame):
    """Update particle positions for animation."""
    u, v = ocean_current_data[frame]
    for i in range(num_particles):
        x = int(particle_positions[i, 0]) % nx
        y = int(particle_positions[i, 1]) % ny
        particle_positions[i, 0] += u[x, y] * 0.1
        particle_positions[i, 1] += v[x, y] * 0.1
        particle_positions[i, 0] %= nx
        particle_positions[i, 1] %= ny
    particles.set_data(particle_positions[:, 0], particle_positions[:, 1])
    return (particles,)


# Create animation
ani = animation.FuncAnimation(
    fig, update_particles, frames=num_frames, interval=100, blit=True
)

# Show animation
plt.show()
