#!/usr/bin/env python

import argparse
import random
import string

def random_password(length=20, verbose=False):
    if args.verbose:
        print(f"Generating password length: {length}")
    #Define the set of available characters to sample from
    chars = string.ascii_letters + string.digits + string.punctuation
    
    #Generate a sample from this list
    password = random.choices(chars, k=length)
    return "".join(password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="Password length in characters", 
                        dest='length', type=int, default=20)
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print(args)
        print(random_password(length=args.length, verbose=args.verbose))