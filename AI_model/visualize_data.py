import matplotlib.pyplot as plt


def prepare_observation_data(groups, state):
    desired_state_group = None
    for group in groups:
        if group[0] == state:
            desired_state_group = group

    y = desired_state_group[1].loc[:, "OBSERVATION COUNT"]
    x = desired_state_group[1].apply(lambda row: str(row['MONTH']) + "-" + str(row['YEAR']), axis=1)

    return x, y


def draw_plot(x, y, x_tick_interval=12):
    plt.plot(x, y)
    plt.xticks(x[0::x_tick_interval], rotation=45)
    plt.show()


def visualize_prediction_results(dates, train, test, predict, x_tick_interval=12):
    split_index = train[0].shape[0]
    plt.plot(dates[:split_index], train[0])
    plt.plot(dates[split_index:], test[0], color="red")
    plt.plot(dates[split_index:], predict[0], color="green")
    plt.xticks(dates[0::x_tick_interval], rotation=45)
    plt.show()