import pandas as pd
import plotly.graph_objects as pg
import plotly.figure_factory as ff
import statistics
import random

reader = pd.read_csv("medium_data.csv")
data = reader.to_list()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    stdev = statistics.stdev(dataset)

    return(mean,stdev)

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    

def show_fig(mean_list):
    figure = ff.create_distplot([mean_list],["Population"],show_hist=False)
    figure.show()

    first_std_deviation_start, first_std_deviation_end = mean - stdev, mean + stdev
    second_std_deviation_start, second_std_deviation_end = mean - (2*stdev), mean + (2*stdev)
    third_std_deviation_start, third_std_deviation_end = mean - (3*stdev), mean + (3*stdev)

    fig = ff.create_distplot([mean_list],["Students Marks"],show_hist = False)
    fig.add_trace(pg.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
    fig.add_trace(pg.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="1st Stdev start"))
    fig.add_trace(pg.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="2nd Stdev start"))
    fig.add_trace(pg.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="3rd Stdev start"))
    fig.add_trace(pg.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="1st Stdev end"))
    fig.add_trace(pg.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="2nd Stdev end"))
    fig.add_trace(pg.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="3rd Stdev end"))
    fig.show()

    Zscore = (mean - mean_list)/stdev
    print(Zscore)

show_fig()