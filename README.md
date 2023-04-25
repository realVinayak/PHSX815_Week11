# PHSX815_Week11

In this homework, k-means clustering is used to perform unsupervised
learning on data generated from mixture model. </br>
To run the code, type `python3 driver.py`. First, it will generate 
a sample of `N_points = 800` points from a mixture model composed of
two 2-D gaussian distributions. The mean of the 2-D gaussian distribution is 
`MEAN_1 = (1,1)` and `MEAN_2 = (5,5)` respectively. Additionally, the covariance matrix
of both of the 2-D gaussian distributions is a 2-D identity matrix. The probability that
the first gaussian chosen is `0.4`. 
</br>
Then, K-means clustering is applied to assign clusters back to the data points,
and to learn the cluster position themselves. This is done by `assignment_loop()` and
`update_cluster_loop()`. The initial cluster points (as a guess) is chosen to be `(-2, 8), (8, -2)` </br> 
The `assignment_loop(data_points, cluster_points)` function iterates through each data_point 
and assigns the closest cluster to each data point. The `update_cluster_loop(data_points, cluster_points)`
function iterates through each cluster and update the cluster position to average of the data points assigned
to the cluster. These two functions are applied one after the another 10 times. 
</br>
In this code, step refers to application of `assignment_loop(data_points, cluster_points)` followed by `update_cluster_loop(data_points, cluster_points)`.
The figures in `./outputs/` show the cluster points, and allocations. The red star and green star are the guess of the cluster points.
The points are color-coded. If a point is red, it means it has been assigned to first cluster. Initially, all the points are 
assigned to first cluster. </br>
Step 0 is the initial state without any k-means step. </br>
It can be seen that as the steps increase, the red and green star move towards `(1,1)` and `(5,5)` respectively - which were the
true means. Additionally, the points closer to `(1,1)` are allocated red and points closer to `(5,5)` are allocated green, indicating
that cluster allocations of points is largely accurate.