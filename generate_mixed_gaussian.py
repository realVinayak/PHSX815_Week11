import numpy as np


def generate_mixed_gaussian(num_points, gaussian_list, prob_list):
    points = []
    for point_counter in range(num_points):
        gaussian_to_choose = gaussian_list[
            np.random.choice(range(len(prob_list)), 1, p=prob_list)[0]]
        mean = gaussian_to_choose[0]
        std_dev = np.asarray(
            [[gaussian_to_choose[1], 0], [0, gaussian_to_choose[1]]])
        new_point = np.random.multivariate_normal(mean, std_dev)
        points.append(new_point)
    return points


def main():
    print(generate_mixed_gaussian(10, [([0, 0], 1), ([5, 5], 1)], [0.01, 0.99]))


if __name__ == '__main__':
    main()
