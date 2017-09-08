#!/bin/bash
cd server
python3 main.py &
cd ../client
sudo python3 -m http.server 80 --bind 0.0.0.0 &
cd ..
