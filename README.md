# Readme

## Description

This script parses log files

## Running the script

1. Have `flow_logs.txt` and `lookup_table.csv` files in the same folder as the script
2. Run the `parser.py` script
3. Check the `output.txt` file for results

## Assumptions/requirements


* Input file as well as the file containing tag mappings are plain text (ascii) files
* The flow log file size can be up to 10 MB
* The lookup file can have up to 10000 mappings
* The tags can map to more than one port, protocol combinations.  for e.g. sv_P1 and sv_P2 in the sample above.
* The matches should be case insensitive 
