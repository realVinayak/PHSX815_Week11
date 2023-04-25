import math
from generate_mixed_gaussian import generate_mixed_gaussian
from matplotlib import pyplot as plt

N_points = 800
STD_DEV = 1
MEAN_1 = (1, 1)
MEAN_2 = (5, 5)


class DataPoint:
    def __init__(self, data_value, assigned_cluster):
        self.data_value = data_value
        self.assigned_cluster = assigned_cluster

    def set_cluster(self, new_cluster):
        self.assigned_cluster = new_cluster

    def __str__(self):
        return f'Cluster: {self.assigned_cluster}. Data Value: {self.data_value}'


class ClusterPoint:
    def __init__(self, index, point_x, point_y):
        self.data_value = (point_x, point_y)
        self.index = index

    def __str__(self):
        return f'Index: {self.index}. Data Value: {self.data_value}'


def distance_metric(point_1, point_2):
    x_0 = point_1[0]
    y_0 = point_1[1]

    x_1 = point_2[0]
    y_1 = point_2[1]

    return math.sqrt(math.pow((x_0 - x_1), 2) + math.pow((y_0 - y_1), 2))


def assignment_loop(data_points, cluster_points):
    for data_point_index in range(len(data_points)):
        selected_cluster_index = 0
        selected_cluster_distance = float('inf')
        for cluster_point_index in range(len(cluster_points)):
            new_distance = distance_metric(
                data_points[data_point_index].data_value,
                cluster_points[cluster_point_index].data_value)
            if new_distance < selected_cluster_distance:
                selected_cluster_index = cluster_point_index
                selected_cluster_distance = new_distance
        data_points[data_point_index].set_cluster(selected_cluster_index)


def update_cluster_loop(data_points, cluster_points):
    for cluster_point_index in range(len(cluster_points)):
        new_x = 0
        new_y = 0
        counter = 0
        for data_point_index in range(len(data_points)):
            if cluster_points[cluster_point_index].index == data_points[
                data_point_index].assigned_cluster:
                counter += 1
                new_x += data_points[data_point_index].data_value[0]
                new_y += data_points[data_point_index].data_value[1]
        new_x = new_x / counter
        new_y = new_y / counter
        cluster_points[cluster_point_index].data_value = (new_x, new_y)


def print_nodes(node_list):
    for node in node_list:
        print(node)


def plot_scatter_plots(data_points):
    zero_points = []
    one_points = []
    for point in data_points:
        if point.assigned_cluster == 0:
            zero_points.append(point)
        else:
            one_points.append(point)
    plt.scatter([zero_point.data_value[0] for zero_point in zero_points],
                [zero_point.data_value[1] for zero_point in zero_points],
                s=0.75, c='r')
    plt.scatter([one_point.data_value[0] for one_point in one_points],
                [one_point.data_value[1] for one_point in one_points],
                s=0.75, c='g')


def main():
    data_points = generate_mixed_gaussian(N_points, [(MEAN_1, STD_DEV),
                                                     (MEAN_2, STD_DEV)],
                                          [0.4, 0.6])
    data_points_nodes = [DataPoint((x[0], x[1]), 0) for x in data_points]

    cluster_points = [(-2, 8), (8, -2)]

    cluster_point_nodes = [
        ClusterPoint(x, cluster_points[x][0], cluster_points[x][1]) for x in
        range(len(cluster_points))]

    plt.scatter(cluster_point_nodes[0].data_value[0],
                cluster_point_nodes[0].data_value[1], s=100, c='r', marker='*')
    plt.scatter(cluster_point_nodes[1].data_value[0],
                cluster_point_nodes[1].data_value[1], s=100, c='g', marker='*')
    plot_scatter_plots(data_points_nodes)
    plt.savefig(f'./outputs/cluster_plots_step_0.png')
    plt.clf()

    for counter in range(10):
        assignment_loop(data_points_nodes, cluster_point_nodes)
        update_cluster_loop(data_points_nodes, cluster_point_nodes)
        plt.scatter(cluster_point_nodes[0].data_value[0], cluster_point_nodes[0].data_value[1], s=100, c='r', marker='*')
        plt.scatter(cluster_point_nodes[1].data_value[0], cluster_point_nodes[1].data_value[1], s=100, c='g', marker='*')
        plot_scatter_plots(data_points_nodes)
        plt.savefig(f'./outputs/cluster_plots_step_{counter+1}.png')
        plt.clf()
        print_nodes(cluster_point_nodes)
        print("iteration: ", counter)
        print('##################################')



if __name__ == '__main__':
    main()
