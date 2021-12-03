import pandas as pd

filename = 'day_03/input1.txt'

# Part 1
report = pd.read_csv(filename, header=None, dtype=object)

report[0] = report[0].apply(lambda x: list(x))
cols = len(report.iloc[0][0])
report = pd.DataFrame(report[0].tolist(), columns=range(cols))

gamma = ''.join(str(report[n].mode()[0]) for n in range(cols))
epsilon = ''.join(['1' if n == '0' else '0' for n in gamma])

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print('gamma ', gamma, 'epsilon ', epsilon)

result = gamma * epsilon
print('Part 1: ', result)

# Part 2
report = pd.read_csv(filename, header=None, dtype=object)
report[0] = report[0].apply(lambda x: list(x))
cols = len(report.iloc[0][0])
report = pd.DataFrame(report[0].tolist(), columns=range(cols))

for n in range(cols):
    values = dict(report[n].value_counts())
    if values['1'] == values['0']:
        keep = '1'
    else:
        keep = report[n].mode()[0]
    report = report[report[n] == keep]

    rows = report.shape[0]
    if rows == 1:
        oxygen = int(''.join(report.iloc[0]), 2)
        break

report = pd.read_csv(filename, header=None, dtype=object)
report[0] = report[0].apply(lambda x: list(x))
cols = len(report.iloc[0][0])
report = pd.DataFrame(report[0].tolist(), columns=range(cols))

for n in range(cols):
    values = dict(report[n].value_counts())
    if values['1'] == values['0']:
        keep = '0'
    else:
        keep = report[n].value_counts().idxmin()
    report = report[report[n] == keep]

    rows = report.shape[0]
    if rows == 1:
        co2 = int(''.join(report.iloc[0]), 2)
        break

print('oxygen ', oxygen, 'co2', co2)

result = oxygen * co2
print('Part 2: ', result)