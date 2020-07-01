import json
import os.path
from model.group import Group
import random
import string
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + '_'.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="testname", header="testheader", footer="testfooter")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15)) for i
    in range(15)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
