#!/usr/bin/python3

import base64
import json
import sys

if len(sys.argv) < 3:
    raise ValueError("invalid arguments, first argument: file name for archive to be created, second argument: file name for JSON file with export API output")

output_filename = sys.argv[1] # file name/path of the archive to be created
export_json_file = sys.argv[2] # file path with response from export API {'export': 'base64 encoded exported archive data string' }

with open(output_filename, 'wb') as f:
    data = json.load(open(export_json_file))['export']
    b_data = data.encode('utf-8')
    f.write(base64.decodebytes(b_data))

print("done")
