import matplotlib.pyplot as plt
from typing import List

from src.Point import Point


class ChartWizard:
    marker_a: str = 's'
    marker_b: str = '^'
    new_elements_marker = '*'
    color_a: str = 'red'
    color_b: str = 'blue'
    new_element_color: str = 'green'

    @staticmethod
    def draw_chart() -> None:
        plt.show()

    @staticmethod
    def set_chart_labels(x_label_name: str, y_label_name: str) -> None:
        plt.xlabel(x_label_name)
        plt.ylabel(y_label_name)

    def add_points_a_and_b_points(self, points_a: List[Point], points_b: List[Point]) -> None:
        x_points_of_a = Point.get_only_x_points(points_a)
        y_points_of_a = Point.get_only_y_points(points_a)
        x_points_of_b = Point.get_only_x_points(points_b)
        y_points_of_b = Point.get_only_y_points(points_b)
        plt.scatter(x=x_points_of_a, y=y_points_of_a, c=self.color_a, marker=self.marker_a)
        plt.scatter(x=x_points_of_b, y=y_points_of_b, c=self.color_b, marker=self.marker_b)

    def append_point_with_annotation_to_chart(self, point: Point, annotation) -> None:
        plt.scatter(x=point.x, y=point.y, c=self.new_element_color, marker=self.new_elements_marker)
        plt.annotate(annotation, (point.x, point.y))
