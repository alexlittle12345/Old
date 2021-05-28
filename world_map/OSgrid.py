import cartopy.crs as ccrs
import matplotlib.pyplot as plt

'''
Some code to split the world map into a grid

Latitude = [-90,90], north-south position
Longitude = [-180,180], east-west position, 0.00001 = 1.11 metres
'''

acc = 0.1 # 0.00001 = 1.11 metres approx

grid_coords = []

def grid(long_s, long_e, lat_s, lat_e):
    n1 = long_s
    while long_s <= n1 < long_e:
        n2 = lat_s
        n1 = n1 + acc
        while lat_s <= n2 < lat_e:
            n2 = n2 + acc
            grid_coords.append([n1,n2])
    return grid_coords

#print (grid_coords)
#print (grid_coords[0][0],grid_coords[0][1])

# Long/Lat for UK
long_s = -11
long_e = 3
lat_s = 49
lat_e = 60


grid_corrds = grid(long_s,long_e,lat_s,lat_e)

ax = plt.axes(projection=ccrs.PlateCarree())
plt.title('World')
ax.coastlines(resolution='10m')
ax.set_extent([long_s,long_e,lat_s,lat_e],ccrs.PlateCarree())

n = 1
while long_s+n*acc <= long_e:
    plt.plot([long_s+(n+0.5)*acc,long_s+(n+0.5)*acc],[lat_s,lat_e],linewidth=0.1,color='red')
    n = n+1
k = 1
while lat_s+k*acc <= lat_e:
    plt.plot([long_s,long_e],[lat_s+(k+0.5)*acc,lat_s+(k+0.5)*acc],linewidth=0.1,color='red')
    k = k+1

for i in range(len(grid_coords)):
    plt.plot(grid_corrds[i][0],grid_corrds[i][1],markersize=1,marker='o',color='red')

plt.show()
