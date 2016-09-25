#!/usr/bin/env bash
python a.py &
python b.py &
python c.py &
python d.py &
wait
echo "programs finished"

# to run: bash run_parallel.sh
