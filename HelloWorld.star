load("render.star", "render")
def main():
    return render.Plot(
  data = [
    (0, 3.35),
    (1, 2.15),
    (2, 2.37),
    (3, -0.31),
    (4, -3.53),
    (5, 1.31),
    (6, -1.3),
    (7, 4.60),
    (8, 3.33),
    (9, 5.92),
  ],
  width = 64,
  height = 32,
  color = "#0f0",
  color_inverted = "#f00",
  x_lim = (0, 9),
  y_lim = (-5, 7),
  fill = True,
),
)
