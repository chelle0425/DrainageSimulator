import random
import imageio as im
import numpy as np
from numpy import loadtxt

# opening terrain data
# for demo terrain model file (DTM50.txt):
# 200 x 200, with 50m intervals over 10 x 10 km space seperated and in logical order


# opening terrain txt file and converting into array
# each value represents a "block" at terrain height h

terrain_array = loadtxt("demo/DTM50.txt", dtype="float")
# line from: https://www.statology.org/python-read-text-file-into-list/
# make sure terrain model file (for demo- dtm50.txt) is in same folder as this code


# creating array simulating rainfall

rain_array = np.ones(terrain_array.shape)
# each "block" has 1 unit of rainfall (droplet)
# starting at 1 so log scaling at the end works


# now we simulate rain droplets hitting the terrain
# if any neighbouring 8 blocks has a lower height value than the original block
# the water flows towards the block with a lower height value


# FUNCTIONS
# function that tracks whether a neighbouring block is lower

def compare_neighbours_3x3(j, i, h):
    # j = x, i = y, h = block height

    bool_array = np.zeros((3, 3), dtype=bool)
    # 3 x 3 boolean array set to false by default
    # diagonal movement is allowed

    if terrain_array[j-1, i-1] < h:
        # if left top corner block has a lower height value than the block..
        bool_array[0, 0] = 1
        # this sets the square to True

    if terrain_array[j-1, i] < h:
        # continue, iterating over all of the 8 neighbouring blocks
        bool_array[0, 1] = 1

    if terrain_array[j-1, i+1] < h:
        bool_array[0, 2] = 1

    if terrain_array[j, i-1] < h:
        bool_array[1, 0] = 1

    if terrain_array[j, i+1] < h:
        bool_array[1, 2] = 1

    if terrain_array[j+1, i-1] < h:
        bool_array[2, 0] = 1

    if terrain_array[j+1, i] < h:
        bool_array[2, 1] = 1

    if terrain_array[j+1, i+1] < h:
        bool_array[2, 2] = 1

    return bool_array


# function that takes the cords of a block and tells us whether its on an edge

def is_block_at_edge(x, y):
    if x == 0:
        return True

    elif x == terrain_array.shape[0] - 1:
        # tests for bottom edge
        return True

    elif y == 0:
        return True

    elif y == terrain_array.shape[1] - 1:
        # tests for far right edge
        return True

    else:
        return False


# main code

for (x, y), height in np.ndenumerate(terrain_array):
    # this gives the cords of block b and iterates over each block in array
    # line from https://codereview.stackexchange.com/questions/178603/compare-neighbors-in-array

    block = (x, y)

    tracking_array = np.zeros(terrain_array.shape)
    # anti-loop 1: this tracks whether the rain droplet has been in the block
    # will add 1 to each block that have been visited by droplet

    tracking_set = set()
    # anti-loop 2: this tracks by coords

    is_block_at_edge_Fn = is_block_at_edge(block[0], block[1])

    while is_block_at_edge_Fn is False:
        # while droplet isnt at an edge block

        lower_blocks_list = []
        # empty list to contain neighbouring blocks that are lower

        for (column, row), is_this_block_lower in\
                np.ndenumerate(compare_neighbours_3x3(block[0],
                                                      block[1],
                                                      terrain_array[block])):
            # for each neighbouring block..

            if is_this_block_lower == True:
                lower_blocks_list.append((column, row))
                # adds all neighbouring blocks that are lower to list

        if len(lower_blocks_list) != 0:
            # if there IS a block that is lower..
            random_block = random.choice(lower_blocks_list)
            # chooses random block from lower_blocks_list

            droplet_block = (block[0] + random_block[0] - 1,
                             block[1] + random_block[1] - 1)
            # converts the random block into terrain coords

            # now that we have a random neighbouring block that is lower
            # we move on to water flow

            if tracking_array[droplet_block] == 0 and\
                    droplet_block not in tracking_set:
                # anti-loop: if the block has never had water flow
                # (tracking_array = 0)
                # ..and if the block is not in tracking_set

                tracking_array[droplet_block] = 1
                tracking_set.add(droplet_block)

                rain_array[droplet_block] += 1
                # adds 1 to neighbouring block to simulate water gain

                block = droplet_block
                # changes droplet block to block and loops

                is_block_at_edge_Fn = is_block_at_edge(block[0], block[1])
                # checking if block is an edge block
            else:
                print("error: sink point detected or something went wrong")

        elif len(lower_blocks_list) == 0:
            # else if the droplet is on a plateau / lake..

            rain_array[block] += 1
            # + 1 for stagnant water
            is_block_at_edge_Fn = True
            # get out of inner loop

        else:
            print("error: something else went wrong")
            # never had to get to here..


# output time!!

output_array = np.log10(rain_array)
# log scaling-- best fitted for presenting environmental problems like these

output_array = 255 * (output_array / np.amax(output_array))
# expresses everything as fractions and rescales everything to 0-255


im.imwrite("outputimage_Rochelle.png", (output_array).astype(np.uint8))
# .astype(np.uint8) gets rid of the lossy conversion warning


print("done, file name: outputimage_Rochelle.png")
