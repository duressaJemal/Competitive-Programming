class Solution:
    def kClosest(self, points, k):

        container = []
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            point.insert(0, distance)

        points.sort()

        for point in points:
            point.pop(0)

        return points[:k]
