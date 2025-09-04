import turtle
 
def draw_edge(length, depth):
    """Recursively draw one edge with inward indentations."""
    if depth == 0:
        turtle.forward(length)
    else:
        segment = length / 3
 
        # 1st segment
        draw_edge(segment, depth - 1)
 
        # Inward indentation (turns reversed)
        turtle.right(60)
        draw_edge(segment, depth - 1)
 
        turtle.left(120)
        draw_edge(segment, depth - 1)
 
        turtle.right(60)
        draw_edge(segment, depth - 1)
 
 
def draw_polygon(sides, length, depth):
    """Draw the entire polygon with recursive edges."""
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)
 
 
def main():
    # Take user input
    sides = int(input("Enter the number of sides: "))
    length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))
 
    # Configure turtle
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-length / 2, length / 2)
    turtle.pendown()
 
    draw_polygon(sides, length, depth)
 
    turtle.done()
 
 
if __name__ == "__main__":
    main()