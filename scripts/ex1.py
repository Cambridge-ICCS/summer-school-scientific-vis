import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import cartopy.crs as ccrs
import matplotlib.animation as animation

# Load the netCDF file
file_path = "MERRA2_400.tavg1_2d_lnd_Nx.20240401.nc4"
dataset = nc.Dataset(file_path)

# Extract the variables
lats = dataset.variables["lat"][:]
lons = dataset.variables["lon"][:]
temps = dataset.variables["EVLAND"][:]
times = dataset.variables["time"][:]

# Close the dataset
dataset.close()

# Create a figure and an orthographic projection
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(
    projection=ccrs.Orthographic(central_longitude=0.0, central_latitude=90.0)
)

# Add features for better visualization
ax.coastlines()
ax.gridlines()

# Plot the data
# Create a meshgrid for lats and lons
lon_grid, lat_grid = np.meshgrid(lons, lats)
print(f"size = {np.size(lon_grid)}")
print(f"size = {np.size(lat_grid)}")
print(f"size = {np.size(temps)}")
print(f"size = {np.size(times)}")
# Plot the temperature data
temp_plot = ax.pcolormesh(
    lon_grid, lat_grid, temps[0], transform=ccrs.PlateCarree(), cmap="coolwarm"
)

# Add a colorbar
# cbar = plt.colorbar(temp_plot, orientation='vertical', pad=0.05, aspect=50)
# cbar.set_label('Land Surface Temperature (K)')

ax.coastlines
ax.gridlines

# Show the plot
# plt.show()


def update_plot(frame):
    ax.coastlines()
    ax.gridlines()
    temp_plot = ax.pcolormesh(
        lon_grid,
        lat_grid,
        temps[frame, :, :],
        transform=ccrs.PlateCarree(),
        cmap="coolwarm",
    )
    # cbar = plt.colorbar(temp_plot, orientation='vertical', pad=0.05, aspect=50)
    # cbar.set_label('Land Surface Temperature (K)')
    ax.set_title(f"Time: {times[frame]}")


# Create the animation
ani = animation.FuncAnimation(fig, update_plot, frames=len(times), repeat=False)

# Save the animation
ani.save("land_surface_temp_animation.mp4", writer="ffmpeg", fps=45)

# Show the animation
plt.show()
