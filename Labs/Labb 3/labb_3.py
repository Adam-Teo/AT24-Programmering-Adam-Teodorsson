
import matplotlib.pyplot as plt
import numpy as np
import re

# Reads the file data and uses regex and list comprehension 
# to store each point as a dict and save it to a list.
def read_data(path, expression):
    with open(path, "r") as file:
        points = list()
        for row in file:
            points.append( *[
                {"x":float(li[0]), 
                 "y":float(li[1]),} 
                for li in re.findall(expression, row)  
                ] )
    return points


def write_data(file_name, data):
    with open(file_name, "w") as file:
         file.write("".join([f"{obj["x"]},{obj["y"]},{obj["label"]}\n" for obj in data]))


# 1 == Above/Right of the Line 0 == Below/Left of the Line
# When the point's y is smaller then equation's y, the point is to the left / below the line.
# However when the k value is positive as in the case of 'h(x) = 800x - 120' it will look 
# like the 1s are to the left and the 0s are to the right of the line on the graph.
#
# You could also add a third value like 0.5 for points that are on the line
def determine_position(point, line):
    y = line["k"]*point["x"]+line["m"]
    p = point["y"]
    return 0 if p < y else 1

# Loops through and classifies all the points using the determine_position function
def classify_points(points, line):
     return [ obj|{ "label" : determine_position(obj, line) } for obj in points ]


# Displays the label of the points by associating a label with a color
def set_color(points):
     for obj in points:
          rtl = obj["label"]
          obj["color"] = "white" if rtl == 0 else "red" 
     return points


def draw_plot(points, lines, title):
    fig, ax = plt.subplots( dpi=100, figsize=(18, 9)) 
    fig.set_facecolor((0.12, 0.12, 0.12))
    
    ax.set_ylim(-5.9, 5.9)
    ax.set_facecolor((0.1, 0.1, 0.1))
    ax.set_xlim(-5.9, 5.9)
    ax.tick_params(axis='x', colors=(0.8, 0.8, 0.8))
    ax.tick_params(axis='y', colors=(0.8, 0.8, 0.8))
    ax.yaxis.label.set_color((0.8, 0.8, 0.8))
    ax.xaxis.label.set_color((0.8, 0.8, 0.8))
    ax.spines['bottom'].set_color((0.8, 0.8, 0.8))
    ax.spines['left'].set_color((0.8, 0.8, 0.8))
    ax.spines['top'].set_color((0.12, 0.12, 0.12))
    ax.spines['right'].set_color((0.12, 0.12, 0.12))
    ax.set_ylabel("y", fontsize=14, color=(0.8, 0.8, 0.8))
    ax.set_xlabel("x", fontsize=14, color=(0.8, 0.8, 0.8))
    ax.set_title(title, color=(0.8, 0.8, 0.8), size=14, family="consolas")
    ax.grid(visible=None, which='major', axis='both', color=(0.2, 0.2, 0.2))
    
    
    props = { "boxstyle":"round", "facecolor":(0.1, 0.1, 0.1), "alpha":1, "edgecolor":(0.4, 0.4, 0.4) }
    box_txt="            Point Location\n   Red : Right / Above the Line (1)\nWhite : Left / Belowe the Line (0)"
    ax.text(-5.5 , 4.5, box_txt, color=(0.8, 0.8, 0.8), bbox=props)
    
    
    ax.scatter([obj["x"] for obj in points], [obj["y"] for obj in points], color=[obj["color"] for obj in points], marker=".", s=10, zorder=3)
    
    # This loop allows for multiple plot lines
    for line in lines:
        x = np.linspace(-6, 6, 10)
        y = line["k"]*x+line["m"]
        ax.plot(x, y, label=f"y = {line["k"]}*x{line["m"]}")

    plt.show()
    plt.close()


def main():
    # I simply picked the line by using k=-1 as a starting position and 
    # then nudged m until the line that split the points 50/50
    line = {"k":-1, "m":0.3}
    
    points = read_data("unlabelled_data.csv", r"(.*?),(.*)")
    
    points = classify_points(points, line)
    
    write_data("labelled_data.csv", points)

    points = set_color(points)

    draw_plot(points, [line], f"y = {line["k"]}*x-{line["m"]}")

main()