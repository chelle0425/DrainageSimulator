# DrainageSim
### Simulation of rainfall drainage patterns in a given terrain

A simulation that takes terrain model data and simulates waterflow by tracking individual tain droplets, assuming an evenly distributed rainfall

For any n x m sized terrain, this program creates an array of "rain droplets" of the same dimension, iterates through every block and tracks each individual droplet flowing downhill

Droplets flows to the lowest adjacent square (including diagonals), choosing one at random if there are multiple directions that are lower

If a droplet is on a plateau, it simply doesn't flow anywhere (lakes should appear as black bodies)

Code takes about 1 min 30 to run for a 200x200 array

Version 1.02

</br>

Initialize the environment
'''

'''


rochelle.pun21@imperial.ac.uk, 2021
