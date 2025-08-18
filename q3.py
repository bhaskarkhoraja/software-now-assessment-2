import turtle
import math

def draw_recursive_edge(t, length, depth):
    """
    Recursively draw an edge with fractal-like indentations.
    
    Args:
        t: turtle object
        length: length of the current edge
        depth: recursion depth remaining
    """
    if depth == 0:
        # Base case: draw a straight line
        t.forward(length)
    else:
        # Recursive case: divide edge into 4 segments with indentation
        segment_length = length / 3
        
        # First segment (1/3 of original)
        draw_recursive_edge(t, segment_length, depth - 1)
        
        # Turn inward 60 degrees for the indentation
        t.right(60)
        
        # Second segment (side of inward triangle)
        draw_recursive_edge(t, segment_length, depth - 1)
        
        # Turn 120 degrees to create the triangle point
        t.left(120)
        
        # Third segment (other side of inward triangle)
        draw_recursive_edge(t, segment_length, depth - 1)
        
        # Turn back to original direction
        t.right(60)
        
        # Fourth segment (final 1/3 of original)
        draw_recursive_edge(t, segment_length, depth - 1)

def draw_polygon_pattern(num_sides, side_length, depth):
    """
    Draw a polygon with recursive fractal edges.
    
    Args:
        num_sides: number of sides in the starting polygon
        side_length: length of each side in pixels
        depth: recursion depth for the pattern
    """
    # Create turtle and screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Recursive Pattern - {num_sides} sides, depth {depth}")
    screen.setup(width=800, height=800)
    
    # Create turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.color("blue")
    t.pensize(1)
    
    # Calculate the exterior angle for the polygon
    exterior_angle = 360 / num_sides
    
    # Position turtle to center the polygon better
    t.penup()
    # Move to a starting position that will center the shape better
    if num_sides == 3:  # Triangle
        t.goto(-side_length/2, -side_length/3)
    elif num_sides == 4:  # Square
        t.goto(-side_length/2, -side_length/2)
    else:  # Other polygons
        t.goto(-side_length/2, 0)
    t.pendown()
    
    print(f"Drawing {num_sides}-sided polygon with recursive depth {depth}...")
    print("This may take a moment for higher depths...")
    
    # Draw each side of the polygon with recursive pattern
    for side in range(num_sides):
        draw_recursive_edge(t, side_length, depth)
        t.left(exterior_angle)  # Turn for next side
    
    # Hide turtle and keep window open
    t.hideturtle()
    print("Pattern complete! Click on the window to close.")
    screen.exitonclick()

def main():
    """
    Main function to get user input and generate the pattern.
    """
    print("Recursive Geometric Pattern Generator")
    print("=====================================")
    
    try:
        # Get user input
        num_sides = int(input("Enter the number of sides: "))
        if num_sides < 3:
            print("Number of sides must be at least 3.")
            return
        
        side_length = float(input("Enter the side length: "))
        if side_length <= 0:
            print("Side length must be positive.")
            return
        
        depth = int(input("Enter the recursion depth: "))
        if depth < 0:
            print("Recursion depth must be non-negative.")
            return
        
        # Warn for high depth values
        if depth > 4:
            response = input(f"Depth {depth} will create a very complex pattern. Continue? (y/n): ")
            if response.lower() != 'y':
                return
        
        # Generate the pattern
        draw_polygon_pattern(num_sides, side_length, depth)
        
    except ValueError:
        print("Please enter valid numeric values.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()