#!/bin/bash

python prepare_cube.py --name hnRNPA1LCD --replica 200 --gpu_id 0

python hnRNPA1LCD_200/run.py --path hnRNPA1LCD_200