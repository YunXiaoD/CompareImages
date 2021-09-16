import argparse
from SetLog import logger
parser = argparse.ArgumentParser()
parser.add_argument("--file1", "-f1", type=str, default="file1", help="first Files to compare")
parser.add_argument("--file2", "-f2", type=str, default="file2", help="second Files to compare")
parser.add_argument("--output", "-o", type=str, default="./output", help="output file for compare result")
args = parser.parse_args()