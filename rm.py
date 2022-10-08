try:
    import os, sys
    if len(sys.argv) == 1: sys.exit(f"use: python3 {sys.argv[0]} filename")
    else: parameters = sys.argv[1:]
    for filename in parameters: os.remove(filename)
except Exception as err:
    exit(err)
