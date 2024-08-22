from bookie import *


def main(*args, **kwargs):
    g= xanges.Gemini()
    print(g.get_book('BTCUSD'))


if __name__ == '__main__':
    main()
