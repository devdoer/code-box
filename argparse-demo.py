import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-D','--define', help='define var' ,required = True, action='append')
ns = parser.parse_args(sys.argv[1:])
print ns.define
