from numpy import result_type
import pandas as pd
import csv
import statistics as stats

df = pd.read_csv('data.csv')
heightList = df['Height(Inches)'].to_list()
weightList = df['Weight(Pounds)'].to_list()

heightMean,weightMean=stats.mean(heightList),stats.mean(weightList)
heightMedian,weightMedian=stats.median(heightList),stats.median(weightList)
heightMode,weightMode=stats.mode(heightList),stats.mode(weightList)

heightStdDeviation,weightStdDeviation = stats.stdev(heightList),stats.stdev(weightList)

print('mean,median,mode of height is {} {} {} respectively'.format(heightMean,heightMedian,heightMode))
print('mean,median,mode of weight is {} {} {} respectively'.format(weightMean,weightMedian,weightMode))

heightFirstStdDeviationStart,heightFirstStdDeviationEnd = heightMean - heightStdDeviation,heightMean + heightStdDeviation
weightFirstStdDeviationStart,weightFirstStdDeviationEnd = weightMean - weightStdDeviation,weightMean + weightStdDeviation

heightListOfDataWithin1StdDev = [result for result in heightList if (result > heightFirstStdDeviationStart and result < heightFirstStdDeviationEnd)]
weightListOfDataWithin1StdDev = [result for result in weightList if (result > weightFirstStdDeviationStart and result < weightFirstStdDeviationEnd)]

print('{}% of Data for height lies within 1 stdDev '.format(len(heightListOfDataWithin1StdDev)*100/len(heightList)))
print('{}% of Data for weight lies within 1 stdDev '.format(len(weightListOfDataWithin1StdDev)*100/len(weightList)))

heightSecondStdDeviationStart,heightSecondStdDeviationEnd = heightMean - (2*heightStdDeviation),heightMean + (2*heightStdDeviation)
weightSecondStdDeviationStart,weightSecondStdDeviationEnd = weightMean - (2*weightStdDeviation),weightMean + (2*weightStdDeviation)

heightListOfDataWithin2StdDev = [result for result in heightList if (result > heightSecondStdDeviationStart and result < heightSecondStdDeviationEnd)]
weightListOfDataWithin2StdDev = [result for result in weightList if (result > weightSecondStdDeviationStart and result < weightSecondStdDeviationEnd)]

print('{}% of Data for height lies within 2 stdDev '.format(len(heightListOfDataWithin2StdDev)*100/len(heightList)))
print('{}% of Data for weight lies within 2 stdDev '.format(len(weightListOfDataWithin2StdDev)*100/len(weightList)))


heightThirdStdDeviationStart,heightThirdStdDeviationEnd = heightMean - (3*heightStdDeviation),heightMean + (3*heightStdDeviation)
weightThirdStdDeviationStart,weightThirdStdDeviationEnd = weightMean - (3*weightStdDeviation),weightMean + (3*weightStdDeviation)

heightListOfDataWithin3StdDev = [result for result in heightList if (result > heightThirdStdDeviationStart and result < heightThirdStdDeviationEnd)]
weightListOfDataWithin3StdDev = [result for result in weightList if (result > weightThirdStdDeviationStart and result < weightThirdStdDeviationEnd)]

print('{}% of Data for height lies within 3 stdDev '.format(len(heightListOfDataWithin3StdDev)*100/len(heightList)))
print('{}% of Data for weight lies within 3 stdDev '.format(len(weightListOfDataWithin3StdDev)*100/len(weightList)))
