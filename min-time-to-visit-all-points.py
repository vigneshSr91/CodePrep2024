# https://leetcode.com/problems/minimum-time-visiting-all-points/
class MinTimeVisitingAllPts:
    def solve(self,points):
        answer = 0
        currentPosition = points[0]
        for i in range(1,len(points)):
            targetPosition = points[i]
            # difference in position of x
            dx = targetPosition[0] - currentPosition[0]
            dy = targetPosition[1] - currentPosition[1]
            answer += max(abs(dx), abs(dy))
            currentPosition = targetPosition
        return answer
if __name__ == '__main__':
    points = [[1,1],[3,4],[-1,0]]
    result = MinTimeVisitingAllPts().solve(points)
    print(result)