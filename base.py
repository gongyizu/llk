import random

WIDTH = 20
HEIGHT = 14
ROWS = HEIGHT - 2
COLS = WIDTH - 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


data = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]


def gen_data():
    """
    数组填充数据
    """
    tmpData = []

    for i in range(ROWS):
        numbs = list(range(1, COLS + 1))
        random.shuffle(numbs)
        tmpData.extend(numbs)

    random.shuffle(tmpData)

    index = 0
    for i in range(1, HEIGHT - 1):
        for j in range(1, WIDTH - 1):
            data[i][j] = tmpData[index]
            index += 1


def isHLinked(point1, point2):
    """
    横向是否相连
    """
    if point1.y != point2.y:
        # 横向不在一条线
        return False

    minX = min(point1.x, point2.x)
    maxX = max(point1.x, point2.x)

    # 从左往右检查中间的点是不是空的
    for i in range(minX + 1, maxX):
        if data[point1.y][i] != 0:
            return False

    return True


def isVLinked(point1, point2):
    """
    纵向是否相连
    """
    if point1.x != point2.x:
        # 纵向不在一条线
        return False

    minY = min(point1.y, point2.y)
    maxY = max(point1.y, point2.y)

    # 从上往下检查中间的点是不是空的
    for i in range(minY + 1, maxY):
        if data[i][point1.x] != 0:
            return False

    return True


def isZeroTurnLinked(point1, point2):
    """
    是否 0 转折连接
    """
    if isHLinked(point1, point2):
        return True

    if isVLinked(point1, point2):
        return True

    return False


def isOneTurnLinked(point1, point2):
    """
    是否 1 转折连接
    """
    pointTmp1 = Point(point1.x, point2.y)
    if (
        data[pointTmp1.y][pointTmp1.x] == 0
        and isZeroTurnLinked(pointTmp1, point1)
        and isZeroTurnLinked(pointTmp1, point2)
    ):
        return (True, pointTmp1)

    pointTmp2 = Point(point2.x, point1.y)
    if (
        data[pointTmp2.y][pointTmp2.x] == 0
        and isZeroTurnLinked(pointTmp2, point1)
        and isZeroTurnLinked(pointTmp2, point2)
    ):
        return (True, pointTmp2)

    return (False, None)


def isTwoTurnLinked(point1, point2):
    """
    是否 2 转折连接
    """
    # 遍历点1的纵向
    for j in range(HEIGHT):
        # 临时点1
        tmpP1 = Point(point1.x, j)
        if data[tmpP1.y][tmpP1.x] > 0:
            continue

        if j == point1.y:
            # 与点1重合
            continue

        if j == point2.y and point1.x == point2.x:
            # 与点2重合
            continue

        # 临时点2
        tmpP2 = Point(point2.x, j)
        if data[tmpP2.y][tmpP2.x] > 0:
            continue

        if (
            isZeroTurnLinked(point1, tmpP1)
            and isZeroTurnLinked(tmpP1, tmpP2)
            and isZeroTurnLinked(tmpP2, point2)
        ):
            return (True, tmpP1, tmpP2)

    # 遍历点1的横向
    for i in range(WIDTH):
        # 临时点1
        tmpP1 = Point(i, point1.y)
        if data[tmpP1.y][tmpP1.x] > 0:
            continue

        if i == point1.x:
            # 与点1重合
            continue

        if i == point2.x and point1.y == point2.y:
            # 与点2重合
            continue

        # 临时点2
        tmpP2 = Point(i, point2.y)
        if data[tmpP2.y][tmpP2.x] > 0:
            continue

        if (
            isZeroTurnLinked(point1, tmpP1)
            and isZeroTurnLinked(tmpP1, tmpP2)
            and isZeroTurnLinked(tmpP2, point2)
        ):
            return (True, tmpP1, tmpP2)
    return (False, None, None)
