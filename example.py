import svgpathnormalizer as sn

path = 'M 100 300 Q 150 50 200 300 Q 250 550 300 300 Q 350 50 400 300 C 450 550 450 50 500 300 C 550 50 550 550 600 300 A 50 50 0 1 1 700 300 Z'

normalizer = sn.SVGNormalizer()

scaled = normalizer.scale(path, scalar=3)

print('SCALED')
print(scaled)
print('ALSO POSSIBLE')
print(normalizer.prev_scaled_path)
