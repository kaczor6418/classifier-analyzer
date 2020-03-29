import matplotlib.pyplot as plt
from typing import List

from src.Point import Point


class ChartWizard:
    x_label_name: str
    y_label_name: str

    x_marker: str = 's'
    y_marker: str = '^'
    new_elements_marker = '*'
    x_color: str = 'red'
    y_color: str = 'blue'
    new_element_color: str = 'green'

    def __init__(self, x_label_name: str, y_label_name: str):
        self.x_label_name = x_label_name
        self.y_label_name = y_label_name

    def draw_2d_chart(self, points_a: List[Point], points_b: List[Point]):
        x_points_of_a = Point.get_only_x_points(points_a)
        y_points_of_a = Point.get_only_y_points(points_a)
        x_points_of_b = Point.get_only_x_points(points_b)
        y_points_of_b = Point.get_only_y_points(points_b)
        plt.scatter(x=x_points_of_a, y=y_points_of_a, c=self.x_color, marker=self.x_marker)
        plt.scatter(x=x_points_of_b, y=y_points_of_b, c=self.y_color, marker=self.y_marker)
        plt.xlabel(self.x_label_name)
        plt.ylabel(self.y_label_name)
        plt.show()

    def append_element_with_annotation_to_chart(self, point: Point, annotation):
        plt.scatter(x=point.x, y=point.y, c=self.new_element_color, marker=self.new_elements_marker)
        plt.annotate(annotation, (point.x, point.y))
