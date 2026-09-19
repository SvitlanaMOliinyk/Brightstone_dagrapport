import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Brighstone dagrapport - leest een CSV met orders en produceert een leesbaar rapport.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input',
                        required=True,
                        help='Pad naar CSV orders (verplicht)')
    parser.add_argument('--output', default='rapport_<datum>.md',
                        help='Pad voor het rapport')
    parser.add_argument('--format',
                        choices=['markdown', 'json'],
                        default='markdown',
                        help='Uitvoerformaat: markdown of json')

    args = parser.parse_args()

    if args.output != 'rapport_<datum>.md':
        if args.format == 'markdown':
            if not args.output.endswith('.md'):
                raise ValueError('De bestandsextentie komt niet overeen met het geselecteerde formaat')

        elif args.format == 'json':
            if not args.output.endswith('.json'):
                raise ValueError('De bestandsextentie komt niet overeen met het geselecteerde formaat')

    return args


if __name__ == "__main__":
    main()
