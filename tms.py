#!/usr/bin/env python

"""

Today's time in miiliseconds
"""

import time

def tms():
    millis = int(round(time.time() * 1000))
    print millis


def main():
    t = tms()


if __name__ == "__main__":
    main()
