import cellLocator
from math import sin, asin, cos, radians, fabs, sqrt

EARTH_RADIUS = 6371           # 地球平均半径，6371km

# 目前仅支持 www.queclocator.com 域名定位
# 参考 API 文档
# https://python.quectel.com/wiki/#/zh-cn/api/?id=celllocator-%e5%9f%ba%e7%ab%99%e5%ae%9a%e4%bd%8d

def hav(theta):
    s = sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance


def test_cellLocator():
    # 测试地点
    lon1, lat1 = (22.599578, 113.973129)  # 深圳野生动物园(起点）
    lon2, lat2 = (39.9087202, 116.3974799)  # 北京天安门(1938.4KM)
    d2 = get_distance_hav(lon1, lat1, lon2, lat2)
    print(d2)
    # 获取当前位置
    # (latitude, longtitude, accuracy)
    ret = cellLocator.getLocation(
        "www.queclocator.com", 80, "1111111122222222", 8, 1)
    lon3, lat3 = ret[1], ret[0]
    d2 = get_distance_hav(lon3, lat3, lon2, lat2)
    print(d2)


if __name__ == "__main__":
    test_cellLocator()
