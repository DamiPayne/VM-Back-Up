'''Demonstarte raiding a refridgerator'''
from contextlib import closing


class RefridgeratorRaider:
    """docstring for RefridgeratorRaider"""

    def open(self):
        print('Open Fridge Door.')

    def take(slef, food):
        print('Finding {}...'.format(food))
        if food == 'pizza':
            raise RuntimeError('Health Warning!')
        print('taking {}'.format(food))

    def close(self):
        print('Closing fidge door...')
        print('Fridge door closed.')


def raid(food):
    with closing(RefridgeratorRaider()) as r:
        r.open()
        r.take(food)

raid('pizza')
