#!/bin/bash

python prepare.py --name hnRNPA1LCD --replica 100 --gpu_id 0

python hnRNPA1LCD_100/run.py --path hnRNPA1LCD_100