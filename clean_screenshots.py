#!/usr/bin/python

import os, argparse, glob, time, re
from datetime import datetime


desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
trash = os.path.join(os.path.expanduser('~'), '.Trash')

for filename in glob.glob(os.path.join(desktop, 'Screen Shot*.png')):
    name = os.path.basename(filename)
    try:
        # Screen Shot 2017-08-24 at 10.37.02 AM
        created_time = datetime.strptime(re.sub(r"\s+\(?\d+\)?\.png", '.png', name), 'Screen Shot %Y-%m-%d at %I.%M.%S %p.png')
    except ValueError as ex:
        continue

    if time.time() > (time.mktime(created_time.timetuple()) + (24*60)):
        if os.path.isdir(trash):
            os.rename(filename, os.path.join(trash, name))
