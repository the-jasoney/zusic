import generator
import scales
import tomidi


def main():
    tomidi.to_midi(generator.generate(scales.CN_MAJ, 50))


if __name__ == '__main__':
    main()
