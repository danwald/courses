#http://codekata.com/kata/kata04-data-munging/
'''
Part One: Weather Data
In weather.dat you’ll find daily weather data for Morristown, NJ for June 2002. Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).

Part Two: Soccer League Table
The file football.dat contains the results from the English Premier League for 2001/2. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
'''
import re

class ColumnReader:
    def __init__(self, file, data_filter, cols_conv):
        self.fp = open(file)
        self.filt = data_filter
        self.cols_conv = cols_conv

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.fp.readline()
            if not line:
                raise StopIteration()
            if re.match(self.filt, line):
                break

        line = line.split()
        data = []
        for col,meth in self.cols_conv.items():
            try:
                data.append(meth(line[col]))
            except:
                break
        return data if len(data) == len(self.cols_conv) else None

    def get_min(self, g_x=lambda x,y: x-y, f_g_x=lambda x:x):
        min_k, min_val =  None, float('inf')
        for dc in self:
            if dc:
                key, a, b = dc
                res = f_g_x(g_x(a,b))
                if res < min_val:
                    min_k, min_val, = key, res
        return min_k




def weather(infile='weather.dat'):
    rc = ColumnReader(infile, r'^ +\d+ ', {0:int, 1:int, 2:int})
    return rc.get_min()


def soccer(infile='football.dat'):
    rc = ColumnReader(infile, r'^ +\d\d?\.', {1:str, -4:int, -2:int})
    return rc.get_min(f_g_x=abs)


if __name__ == '__main__':
    for method in (weather, soccer):
        print(
            'Running: ', method.__name__, 'result: ', method()
        )
