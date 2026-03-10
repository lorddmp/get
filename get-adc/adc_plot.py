import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage = 3.22):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)

    plt.title('Красивый график зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.ylim(0, max_voltage*1.1)
    plt.grid()

    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)
    plt.figure(figsize=(10,6))
    plt.title("Красивое распределение периодов дискретизации измерений по времени на одно измерение")
    plt.hist(sampling_periods)
    plt.xlim(0, 0.06)
    plt.grid()
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")
    plt.show()