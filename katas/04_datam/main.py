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


def weather(infile='weather.dat'):
    min_spread, mday = 1 << 10, -1
    rc = ColumnReader(infile, r'^ +\d+ ', {0:int, 1:int, 2:int})
    for dc in rc:
        if dc:
            day, mx, mi = dc
            sp = mx - mi
            if sp < min_spread:
                min_spread, mday = sp, day
    return mday


def soccer(infile='football.dat'):
    min_spread, wteam = 1 << 10, None
    rc = ColumnReader(infile, r'^ +\d\d?\.', {1:str, -4:int, -2:int})
    for ln in rc:
        if ln:
            team,gf,ga = ln
            sp = abs(gf - ga)
            if sp < min_spread:
                min_spread, wteam = sp, team
    return wteam



if __name__ == '__main__':
    for method in (weather, soccer):
        print(
            'Running: ', method.__name__, 'result: ', method()
        )
