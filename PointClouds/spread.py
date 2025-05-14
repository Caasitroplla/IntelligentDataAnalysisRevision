import random

def generate_random_point_cloud(num_points=random.randint(10, 100)):
    """
    Generates a random point cloud in 3D space.
    Returns a list of tuples representing the points.
    """
    point_cloud = [(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_points)]
    return point_cloud

def generate_trended_point_cloud(num_points=random.randint(10, 100), trend=random.uniform(-1, 1)):
    """
    Generates a random point cloud in 3D space with a linear trend.
    Returns a list of tuples representing the points.
    """
    point_cloud = [(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1) + trend * i) for i in range(num_points)]
    return point_cloud


def avg(point_cloud) -> list[float]:
    return [sum(coord) / len(point_cloud) for coord in zip(*point_cloud)]

def variance(point_cloud) -> float:
    # Calculating the variance of the point cloud
    mean = avg(point_cloud)
    length = len(point_cloud)

    # Calculate the variance for each axis
    variances = []

    axis = len(point_cloud[0])

    for i in range(axis):
        variance = sum((point[i] - mean[i]) ** 2 for point in point_cloud) / length
        variances.append(variance)

    return sum(variances) / axis


def covariance(point_cloud_a, point_cloud_b) -> float:
    # Calculating the covariance of the point cloud
    if len(point_cloud_a) != len(point_cloud_b):
        raise ValueError("Point clouds must have the same number of points")

    mean_a = avg(point_cloud_a)
    mean_b = avg(point_cloud_b)
    length = len(point_cloud_a)
    # Calculate the covariance for each axis
    covariances = []

    axis = len(point_cloud_a[0])

    for i in range(axis):
        covariance = sum((point_cloud_a[j][i] - mean_a[i]) * (point_cloud_b[j][i] - mean_b[i]) for j in range(length)) / length
        covariances.append(covariance)

    return sum(covariances) / axis


if __name__ == "__main__":
    point_cloud = generate_random_point_cloud()
    print("Variance of a Point Cloud:", variance(point_cloud))

    point_cloud_a = generate_random_point_cloud(num_points=100)
    point_cloud_b = generate_random_point_cloud(num_points=100)
    print("Covariance between two random Point Clouds:", covariance(point_cloud_a, point_cloud_b))

    point_cloud_a = generate_trended_point_cloud(num_points=100, trend=0.5)
    point_cloud_b = generate_trended_point_cloud(num_points=100, trend=0.5)
    print("Covariance between two trended together Point Clouds:", covariance(point_cloud_a, point_cloud_b))

    point_cloud_a = generate_trended_point_cloud(num_points=100, trend=0.5)
    point_cloud_b = generate_trended_point_cloud(num_points=100, trend=-0.5)
    print("Covariance between two trended opposite Point Clouds:", covariance(point_cloud_a, point_cloud_b))
