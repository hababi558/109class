import random
import statistics as stats
import plotly.figure_factory as pff

diceresult = []

for i in range(1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)

mean = sum(diceresult)/len(diceresult)

stdDeviation = stats.stdev(diceresult)
median = stats.median(diceresult)
mode = stats.mode(diceresult)

print('Mean: '+str(mean))
print('Median: '+str(median))
print('Mode: '+str(mode))
print('stdDeviation: '+str(stdDeviation))

fig = pff.create_distplot(
    [diceresult],['result'],show_hist=False
)

#fig.show()