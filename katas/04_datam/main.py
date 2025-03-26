#http://codekata.com/kata/kata04-data-munging/
'''
Part One: Weather Data
In weather.dat you’ll find daily weather data for Morristown, NJ for June 2002. Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).

Part Two: Soccer League Table
The file football.dat contains the results from the English Premier League for 2001/2. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
'''
import re

class ColumnReader:
    def __init__(self, file, data_filter, *cols):
        self.fp = open(file)
        self.filt = data_filter
        self.cols = cols

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
        for col in self.cols:
            data.append(line[col])
        return data


def weather(infile='weather.dat'):
    min_spread, mday = 1 << 10, -1
    rc = ColumnReader(infile, r'^ +\d+ ', 0, 1, 2)
    for dc in rc:
        try:
            day, mx, mi = map(lambda x: int(x),  dc)
        except:
            continue
        else:
            sp = mx - mi
            if sp < min_spread:
                min_spread, mday = sp, day
    return mday


def soccer(infile='football.dat'):
    min_spread, wteam = 1 << 10, None
    with open(infile) as fp:
        _ = fp.readline()
        for ln in fp:
            try:
                data = ln.split()
                team,gf,ga = data[1], int(data[-4]), int(data[-2])
            except:
                pass
            else:
                sp = abs(gf - ga)
                if sp < min_spread:
                    min_spread, wteam = sp, team
        return wteam



if __name__ == '__main__':
    for method in (weather, soccer):
        print(
            'Running: ', method.__name__, 'result: ', method()
        )
