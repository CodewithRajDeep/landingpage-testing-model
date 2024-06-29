results = experiment.analyze()
print(f"Profile Picture Upload Rate:")
print(f"  Control: {results['control']['lift']:.2%}")
print(f"  Variation: {results['variation']['lift']:.2%}")