# AUTHOR: AVHB
# DEPENDENCY: `pip install "python-barcode[images]"`

import barcode
from barcode.writer import ImageWriter
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--content", help="barcode content (ascii)", default="8675309")
parser.add_argument("--output", help="output filename (ascii)", default="out")
parser.add_argument("--height", help="height of barcode (int)", type=int, default=5.0)
parser.add_argument("--textvisible", help="write text under barcode (true/false)", default="false")

args = parser.parse_args()

# print(f"Height: {args.height}, Text {args.textvisible}")
# print(f"Content: {args.content}, Output: {args.output}")

code128 = barcode.get("code128", str(args.content), writer=ImageWriter())

# https://stackoverflow.com/a/715455
filename = code128.save(str(args.output), options={'write_text': args.textvisible.lower() in ["true"], 'module_height': args.height})

print(f"Barcode exported: {filename}")