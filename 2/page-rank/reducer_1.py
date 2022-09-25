#!/usr/bin/env python3

import sys

""" Reducer for Task 1 """


def read_from_mapper(w_file_path: str) -> None:
    """ Reads input from the mapper as stdin """

    # initialization
    node = None
    adj_list = list()

    # open 'w' file with write permission
    with open(w_file_path, "w") as w_file:
        for line in sys.stdin:

            line = line.strip()
            src, dest = line.split("\t")

            try:
                src = int(src)
                dest = int(dest)
            except ValueError:
                continue

            if node is None:
                node = src
                adj_list.append(dest)
            elif(node == src):
                adj_list.append(dest)
            else:
                # print
                print(f"{node}\t{adj_list}")

                # writing to w file
                w_file.write(f"{node},1\n")

                adj_list.clear()  # reset

                node = src  # move to next node
                # print(node,dest)
                adj_list.append(dest)

        # For last line
        print(f"{node}\t{adj_list}")
        w_file.write(f"{node}, 1\n")


def main():

    # path of the 'w' file
    w_file_path = sys.argv[1].strip()

    read_from_mapper(w_file_path)


""" Start Reducer task """
main()
