#!/bin/bash
rm -rf banner.py
rm -rf __pycache__
rm -rf Killer_install.sh
rm update.sh
rm -rf Killer.py
cd ..
rm -rf Blu_Death/
git clone https://github.com/Exelka/Blu_Death
ls 
cd Blu_Death/
python3 Killer.py
