import argparse
from src.helper import hello_world, hello

def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description='Process a name')
    parser.add_argument('--name', '-n', metavar='name', type=str,
                        help='name of the user')

    args = parser.parse_args()

    name=args.name
    if name is None:
        hello_world()
    else:
        hello(name)

if __name__=="__main__":
    main()