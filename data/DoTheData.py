


import os
from collections import defaultdict


import csv
import sys
import numpy as np
from pathlib import Path


def find_percentiles(csv_file):
    arr = []
    count = 0
    results = {}
    with open(Path(csv_file)) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[0]) < 0:
                percentiles = []
                np_arr = np.array(arr)
                percentiles.append(np.percentile(np_arr, 85))
                percentiles.append(np.percentile(np_arr, 99))
                count += 1
                results[count] = percentiles
            else:
                arr.append(float(row[1]))
        return results



summarized_data = {}

def main():
    # List all files in current directory
    for file in os.listdir():
        if '.' in file:
            continue
        # Check if file is a folder
        if os.path.isdir(file):
            # Print folder name
            folder = file
            print(folder)
            summarized_data[folder] = {}
            # List all files in folder
            for i in range(1, 8):
                # [x[0], x[1]]
                x = list(find_percentiles(folder + f"/Tally {i}.csv").values())
                print(x)
                summarized_data[folder][f"Tally {i}"] = x[0]

    print(summarized_data)
    # write summarized_data to csv
    with open('summarized_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for run_name, tallies in summarized_data.items():
            for tally in tallies:
                writer.writerow([run_name, tally, tallies[tally][0], tallies[tally][1]])




if __name__ == "__main__":
    main()