from pygame import Rect


def getAABB(clickarea):
    lx = [p[0] for p in clickarea]  # Create Sublist with only X values
    ly = [p[1] for p in clickarea]  # Create Sublist with only Y values

    x_min = min(lx)
    x_max = max(lx)

    y_min = min(ly)
    y_max = max(ly)

    return Rect((x_min, y_min), (x_max - x_min, y_max - y_min))


# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs.
def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside
