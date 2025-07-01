#!/bin/bash

python prepare_cube.py --name RLP --replica 200 --gpu_id 0

python RLP_200/run.py --path RLP_200