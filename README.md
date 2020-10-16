# svgpath-normalizer
A simple program for scaling svgpaths
 
## How to use:
1. Start / import svgpathnormalizer.py.
2. Use the method normalize(svgpath, scalar)

## Example:

path = 'M 100 300 Q 150 50 200 300 Q 250 550 300 300 Q 350 50 400 300 C 450 550 450 50 500 300 C 550 50 550 550 600 300 A 50 50 0 1 1 700 300 '
scalar = 1

normalized_path = normalize(path, scalar)
