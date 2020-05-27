import matplotlib.pyplot as plt
from typing import List

from src.structures.Point import Point


class ChartWizard:

    @staticmethod
    def draw_chart() -> None:
        plt.legend()
        plt.show()

    @staticmethod
    def set_chart_title(title: str) -> None:
        plt.title(title)

    @staticmethod
    def set_chart_labels(x_label_name: str, y_label_name: str) -> None:
        plt.xlabel(x_label_name)
        plt.ylabel(y_label_name)

    @staticmethod
    def append_points(points: List[Point], color: str, marker: str, label: str) -> None:
        only_x_values = Point.get_only_x_points(points)
        only_y_values = Point.get_only_y_points(points)
        plt.scatter(x=only_x_values, y=only_y_values, c=color, marker=marker, label=label)

    @staticmethod
    def append_point_with_annotation_to_chart(point: Point, annotation: str, color: str, marker: str) -> None:
        plt.scatter(x=point.x, y=point.y, c=color, marker=marker)
        plt.annotate(annotation, (point.x, point.y))
