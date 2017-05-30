#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import decision_tree
import find_best


def main(argv):
    # run decision tree classifier
    decision_tree.classify()


if __name__ == "__main__":
    main(sys.argv)