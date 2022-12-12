import math
def areas(r, a):
    """
    :param r: (float) The radius of the circle.
    :param a: (float) The angle of the segment.
    :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
    """
    area_of_circle = math.pi * r * r
    area_of_segment = (r**2/2)* ((a*math.pi/180)-math.sin(a*math.pi/180)) 

    return (area_of_segment,area_of_circle-area_of_segment)

print(areas(10, 90))