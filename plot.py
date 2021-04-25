from manim import *


class PlotFunctions(GraphScene):

    def __init__(self, **kwargs):
        GraphScene.__init__(self, x_min=-10, x_max=10, y_min=-2, y_max=2,
                            x_line_frequency=5, graph_origin=ORIGIN,
                            x_labeled_nums=range(-10, 12, 2))

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph)
        func_graph2 = self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(
            TAU, func_graph, color=YELLOW)
        line1 = self.get_vertical_line_to_graph(1, func_graph2)
        line2 = self.get_vertical_line_to_graph(3, func_graph2)
        area1 = self.get_area(func_graph2, 0.3, 3.6,
                              dx_scaling=0.2, area_color=BLUE)
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\cos(x)^2")
        two_pi = MathTex("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT+UP)

        self.play(Create(func_graph), Create(func_graph2))
        self.play(Create(vert_line), Create(graph_lab), Create(
            graph_lab2), Create(two_pi), Create(line1))
        self.play(Create(area1))
        self.wait(40)

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return (np.cos(x))**2


class Essai(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_min=-2,
            y_max=2,
            y_axis_config={"tick_frequency": 0.2},
            x_min=-2,
            x_max=2,
            x_axis_config={'tick_frequency': .25},
            y_axis_height=3,
            x_axis_width=3,
            **kwargs
        )

    def construct(self):
        self.graph_origin = 3*LEFT

        self.setup_axes(animate=True)
        graphdown = self.get_graph(lambda x: np.cos(x),
                                   color=RED_E)

        self.graph_origin = 2*RIGHT
        self.setup_axes(animate=True)
        graphup = self.get_graph(lambda x: np.arctan(x), color=GOLD_A)
        graphs = VGroup(graphup, graphdown)
        self.play(Create(graphs), run_time=0.10)

        self.wait(10)


class Essai2(GraphScene):
    def construct(self):
        self.setup_axes(animate=True)
        # Make graph
        graphX = self.get_graph(self.functionX)
        labelX = self.get_graph_label(graphX, label="y = x")
        graphXCopy = self.get_graph(self.functionX)

        graphX2 = self.get_graph(self.functionX2)
        labelX2 = self.get_graph_label(graphX2, label="y = x^{2}")
        moving_dot = Dot().move_to(graphX.points[0])
        # Make and move text
        text = TextMobject("and job done.")
        text.shift(1*UP, 1*LEFT)
        # Make animation
        self.play(Create(graphX))
        self.play(MoveAlongPath(moving_dot,graphX),run_time=20)
        
        self.play(Transform(graphX, graphX2))
        self.play(FadeOut(graphX))
        self.play(Write(graphXCopy), Write(graphX2),
                      Write(labelX), Write(labelX2))
        self.play(Write(text))
        self.wait(2)

        # Define functions
    def functionX(self, x):
        return (x)

    def functionX2(self, x):
        return(x**2)

class AddUpdater1(Scene):
    def construct(self):
        dot = Dot()
        text = MathTex("Label").next_to(dot,DOWN,buff=SMALL_BUFF)
        self.add(dot,text)
        #dot.get_center()[0]

        # Update function
        def update_text(obj):
            obj.next_to(dot,DOWN,buff=SMALL_BUFF)

        # Add update function to the objects
        text.add_updater(update_text)

        # Add the object again
        self.add(text)
        self.play(dot.animate.shift(RIGHT))

        # Remove update function
        text.remove_updater(update_text)
        self.wait()
