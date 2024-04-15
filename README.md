# DrainageSimulator
Simulation of rainfall drainage patterns in a given terrain

## About the Project

A simulation that takes terrain model data and simulates waterflow by tracking individual tain droplets, assuming an evenly distributed rainfall

For any n x m sized terrain, this program creates an array of "rain droplets" of the same dimension, iterates through every block and tracks each individual droplet flowing downhill

Droplets flows to the lowest adjacent square (including diagonals), choosing one at random if there are multiple directions that are lower

If a droplet is on a plateau, it simply doesn't flow anywhere (thus lakes should appear as black bodies)

Code takes about 1 min 30 to run for a 200x200 array

Version 1.02

## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites

Initialize the environment
    test

### Installation

Clone the repo
    git clone https://github.com/chelle0425/DrainageSimulator.git

## Demo

The demo Digital Terrain Model (DTM) data file DTM50.txt represents digital terrain model data (heights) at 50m intervals over a 10km x 10km square of hilly terrain in Scotland. The values are space-separated, in logical order and fixed such that there are no sink points (i.e. there are no squares which are lower than all surrounding squares). The data is visualised below as a greyscale image, where white is high and dark is low.



## Meta
This project was submitted as part of the coursework to the first-year module "Programming for Geoscientists" in the Department of Earth Science and Engineering at Imperial College London.

This project may be freely copied and distributed provided the source is acknowledged explicitly.

### Acknowledgments 

I would like to thank the Department of Earth Science and Engineering at Imperial College London for providing us with the project requirements and the demo DTM file DTM50.txt. Additionally, this project benefited from insightful discussions with Dr Mark Sutton from the department, who not only helped fix crucial bugs but also provided helpful comments and feedback.

Version 1.02
rochelle.pun@gmail.com, 2021

# Project Title

One Paragraph of the project description

Initially appeared on
[gist](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2). But the page cannot open anymore so that is why I have moved it here.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Example 1](https://www.example.com)
- [Example 2](https://www.example.com)

### Installing

A step by step series of examples that tell you how to get a development
environment running

Say what the step will be

    Give the example

And repeat

    until finished

End with an example of getting some data out of the system or using it
for a little demo

## Running the tests

Explain how to run the automated tests for this system

