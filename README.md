# DrainageSimulator
Simulation of rainfall drainage patterns in a given terrain

<img src="https://github.com/chelle0425/DrainageSimulator/blob/main/demo/outputimage_DTM50.png" width="500" />

## About the Project

A simulation that takes terrain model data and simulates waterflow by tracking individual rain droplets, assuming an evenly distributed rainfall. This simulation is multi-variable dependant and to first-order representative of real-life drainage basins.

For any n x m sized terrain, this program creates an array of "rain droplets" of the same dimension, iterates through every block and tracks each individual droplet flowing downhill

Droplets flows to the lowest adjacent square (including diagonals), choosing one at random if there are multiple directions that are lower

The program outputs an appropriately scaled image file in which areas of high flow are brighter than those of low flow.

Code takes about 1 min 30 to run for the demo file `DTM50.txt` (a 200x200 DTM file)

*Version 1.02*

## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites

Initialize the environment
```
conda env create -f environment.yml
conda activate environment.yml
```

### Installation

Clone the repo
```
git clone https://github.com/chelle0425/DrainageSimulator.git
```

## Demo

The demo Digital Terrain Model (DTM) data file `DTM50.txt` represents digital terrain model data (heights) at 50m intervals over a 10km x 10km square of hilly terrain in Scotland. The values are space-separated, in logical order and fixed such that there are no sink points (i.e. there are no squares which are lower than all surrounding squares). The data is visualised below as a greyscale image, where white is high and dark is low.

<img src="https://github.com/chelle0425/DrainageSimulator/blob/main/demo/terrainmodel_DTM50.png" width="200" />

When running the code, make sure that your terrain model file (in this case `DTM50.txt`) is in the same folder as this code. As the code is written with the demo file in mind you don't need to make any changes.

### Output
The program outputs an appropriately scaled image file in which areas of high flow are brighter than those of low flow. If a droplet is on a plateau, it simply doesn't flow anywhere thus bodies of still water (e.g. lakes) should appear as black bodies.

![outputimage_DTM50.png](https://github.com/chelle0425/DrainageSimulator/blob/main/demo/outputimage_DTM50.png "outputimage_DTM50.png")

## Meta
This project was submitted as part of coursework for the 1st year undergraduate module *EART40003 Programming for Geoscientists* in the Department of Earth Science and Engineering at Imperial College London.

This project may be freely copied and distributed provided the source is acknowledged explicitly.

### Acknowledgments 

I would like to thank the Department of Earth Science and Engineering at Imperial College London for providing us with the project requirements and the demo DTM file `DTM50.txt`. Additionally, this project benefited from insightful discussions with Dr Mark Sutton from the department, who helped fix crucial bugs and provided helpful comments and feedback.

*Version 1.02*

<rochelle.pun@gmail.com>, 2021
