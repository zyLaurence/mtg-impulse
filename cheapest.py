"""
User interface for getting cheapest version of a card.

When ran as a script, prompts user for exact card name.
Returns the lowest price and what set it comes from.

Author: Laurence Lo
Date: Jul 12 2022
"""

import scry
import re
import time


total = 0
with open('buy.txt', 'r') as rf:
    with open('output.txt', 'w') as wf:
        for readline in rf:
            readline.strip()
            if readline=='\n':
                wf.write('\n')
                continue
            find_count = re.findall('(\d+)', readline)
            if find_count:
                count = int(find_count[0])
            else:
                count = 1
            find_name = re.findall("([a-zA-Z,/'_-]+)", readline)
            name = ' '.join(find_name)
            price, set = scry.get_cheapest(name)
            wf.write(f'{count} {name} [{set}] \t {price}\n')
            total += count * float(price)
        wf.write('\nTotal Price = ' + str(round(total, 2)))
        wf.write('\nPrices as of ' + time.strftime("%H:%M:%S") + ' on ' + time.strftime("%m/%d/%Y"))
        #wf.write('\nDisclaimer: Prices are updated once daily by Scryfall using TCGPlayer Market Low')
