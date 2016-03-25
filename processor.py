"""Elevator Problem for BofA Code Review"""
import re

class Processor():
    filename = ''
    el_input = []

    # constructor
    def __init__(self, filename):
        self.filename = filename

    # method to process the file into usable format for elevator class
    def process_text(self):
        with open(self.filename) as f:
            self.el_input = f.read().splitlines()

        # split text into initial floor, and <start floor> - <end floor> style instructions
        results = []
        for line in self.el_input:
            log = []
            l = re.split(':', line)
            i_floor = l[0]
            line = l[1]
            log.append(int(i_floor))

            l2 = re.split(',', line)

            temp = []
            for x in l2:
                y = re.split('-', x)
                temp.append(y)

            for m in range(len(temp)):
                temp[m] = map(int, temp[m])

            for n in temp:
                log.append(n)

            results.append(log)

        return results
