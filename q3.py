
import turtle
import math

def draw_recursive_edge(t, length, depth):
    """
    Recursively draw an edge with outward-pointing triangular bumps.
    
    The pattern divides each edge into 3 equal parts and replaces the middle
    third with two sides of an equilateral triangle pointing outward.
    This creates the classic snowflake fractal pattern.
    
    Args:
        t: turtle object
        length: length of the current edge
        depth: recursion depth remaining
    """
    if depth == 0:
        # Base case: draw a straight line
        t.forward(length)
    else:
        # Recursive case: create the outward bump pattern
        segment_length = length / 3
        
        # Draw first third normally
        draw_recursive_edge(t, segment_length, depth - 1)
        
        # Create the outward bump (equilateral triangle)
        # Turn right 60 degrees to go outward
        t.right(60)
        draw_recursive_edge(t, segment_length, depth - 1)
        
        # Turn left 120 degrees to complete the triangle
        t.left(120)
        draw_recursive_edge(t, segment_length, depth - 1)
        
        # Turn right 60 degrees to return to original direction
        t.right(60)
        
        # Draw the final third
        draw_recursive_edge(t, segment_length, depth - 1)

def calculate_polygon_radius(num_sides, side_length):
    """Calculate the radius of circumscribed circle for better centering."""
    return side_length / (2 * math.sin(math.pi / num_sides))

def draw_koch_snowflake(side_length, depth):
    """
    Draw the snowflake starting with an equilateral triangle.
    
    Args:
        side_length: length of each side in pixels
        depth: recursion depth for the fractal pattern
    """
    # Create screen with optimized settings
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title(f"snowflake - depth {depth}")
    screen.setup(width=1000, height=800)
    screen.setworldcoordinates(-500, -400, 500, 400)  # Center coordinate system
    screen.tracer(0)  # Turn off animation for speed
    
    # Create turtle with optimized settings
    t = turtle.Turtle()
    t.speed(0)
    t.color("white")  # Classic white snowflake
    t.pensize(1)
    t.hideturtle()  # Hide turtle for better performance
    
    # For snowflake, we always use a triangle (3 sides)
    num_sides = 3
    
    # Calculate the circumradius for the triangle
    circumradius = side_length / (2 * math.sin(math.pi / num_sides))
    
    # Position turtle at the center of the screen (0, 0)
    t.penup()
    
    # Start at the top vertex of the equilateral triangle
    first_vertex_angle = math.pi / 2  # 90 degrees - top of the circle
    start_x = circumradius * math.cos(first_vertex_angle)
    start_y = circumradius * math.sin(first_vertex_angle)
    
    # Move to the starting vertex
    t.goto(start_x, start_y)
    
    # Calculate the angle to point toward the second vertex (bottom right)
    vertex_angle_step = 2 * math.pi / num_sides
    second_vertex_angle = first_vertex_angle - vertex_angle_step  # Moving clockwise
    
    # Calculate direction to point toward second vertex
    direction_x = math.cos(second_vertex_angle) - math.cos(first_vertex_angle)
    direction_y = math.sin(second_vertex_angle) - math.sin(first_vertex_angle)
    
    # Set turtle heading to point from first vertex to second vertex
    heading_angle = math.atan2(direction_y, direction_x) * 180 / math.pi
    t.setheading(heading_angle)
    
    t.pendown()
    
    print(f"Drawing snowflake with depth {depth}...")
    if depth > 3:
        print("High depth detected - this may take a while...")
    
    # Draw the three sides of the triangle with Koch fractal pattern
    for side in range(3):
        print(f"Drawing side {side + 1}/3")
        draw_recursive_edge(t, side_length, depth)
        t.right(120)  # Turn 120 degrees for equilateral triangle
    
    # Update screen and finish
    screen.update()
    print("snowflake complete! Click on the window to close.")
    screen.exitonclick()

def draw_polygon_pattern(num_sides, side_length, depth):
    """
    Draw a polygon with recursive fractal edges, perfectly centered in the window.
    
    Args:
        num_sides: number of sides in the starting polygon
        side_length: length of each side in pixels
        depth: recursion depth for the pattern
    """
    # For the classic snowflake, always use triangle
    if num_sides == 3:
        draw_koch_snowflake(side_length, depth)
        return
    
    # Create screen with optimized settings for other polygons
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title(f"Recursive Pattern - {num_sides} sides, depth {depth}")
    screen.setup(width=1000, height=800)
    screen.setworldcoordinates(-500, -400, 500, 400)  # Center coordinate system
    screen.tracer(0)  # Turn off animation for speed
    
    # Create turtle with optimized settings
    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")
    t.pensize(2)
    t.hideturtle()  # Hide turtle for better performance
    
    # Calculate the circumradius (distance from center to vertex)
    circumradius = side_length / (2 * math.sin(math.pi / num_sides))
    
    # Position turtle at the center of the screen (0, 0)
    t.penup()
    
    # For proper centering, start at the top vertex of the polygon
    # Calculate the position of the first vertex (top vertex)
    first_vertex_angle = math.pi / 2  # 90 degrees - top of the circle
    start_x = circumradius * math.cos(first_vertex_angle)
    start_y = circumradius * math.sin(first_vertex_angle)
    
    # Move to the starting vertex
    t.goto(start_x, start_y)
    
    # Calculate the angle to point toward the second vertex
    # The angle between adjacent vertices
    vertex_angle_step = 2 * math.pi / num_sides
    second_vertex_angle = first_vertex_angle - vertex_angle_step  # Moving clockwise
    
    # Calculate direction to point toward second vertex
    direction_x = math.cos(second_vertex_angle) - math.cos(first_vertex_angle)
    direction_y = math.sin(second_vertex_angle) - math.sin(first_vertex_angle)
    
    # Set turtle heading to point from first vertex to second vertex
    heading_angle = math.atan2(direction_y, direction_x) * 180 / math.pi
    t.setheading(heading_angle)
    
    t.pendown()
    
    print(f"Drawing {num_sides}-sided polygon with depth {depth}...")
    if depth > 3:
        print("High depth detected - this may take a while...")
    
    # Calculate the exterior angle for turning between sides
    exterior_angle = 360 / num_sides
    
    # Draw each side of the polygon with recursive pattern
    for side in range(num_sides):
        print(f"Drawing side {side + 1}/{num_sides}")
        draw_recursive_edge(t, side_length, depth)
        t.right(exterior_angle)  # Turn for next side (clockwise)
    
    # Update screen and finish
    screen.update()
    print("Pattern complete! Click on the window to close.")
    screen.exitonclick()

def estimate_complexity(num_sides, depth):
    """Estimate the number of line segments that will be drawn."""
    # Each recursive call creates 4 segments from 1
    segments_per_side = 4 ** depth
    total_segments = num_sides * segments_per_side
    return total_segments

def main():
    """
    Main function to get user input and generate the pattern.
    """
    print("Recursive Geometric Pattern Generator")
    print("=====================================")
    print("Creates fractal patterns including the classic snowflake!")
    print("• Enter 3 sides for the traditional snowflake")
    print("• Try other numbers for different fractal patterns")
    print()
    
    try:
        # Get user input with validation
        while True:
            num_sides = int(input("Enter the number of sides (3 or more): "))
            if num_sides >= 3:
                break
            print("Number of sides must be at least 3.")
        
        while True:
            side_length = float(input("Enter the side length (pixels): "))
            if side_length > 0:
                break
            print("Side length must be positive.")
        
        while True:
            depth = int(input("Enter the recursion depth (0-5 recommended): "))
            if depth >= 0:
                break
            print("Recursion depth must be non-negative.")
        
        # Estimate complexity and warn user
        complexity = estimate_complexity(num_sides, depth)
        print(f"\nEstimated line segments to draw: {complexity:,}")
        
        if complexity > 50000:
            print("⚠️  WARNING: This will create a very complex pattern!")
            print("   Consider reducing the depth or number of sides.")
            response = input("Continue anyway? (y/n): ")
            if response.lower() != 'y':
                print("Pattern generation cancelled.")
                return
        elif complexity > 5000:
            print("ℹ️  This will create a moderately complex pattern.")
        
        print("\nStarting pattern generation...")
        print("The turtle graphics window will appear shortly.")
        
        # Generate the pattern
        draw_polygon_pattern(num_sides, side_length, depth)
        
    except ValueError:
        print("❌ Please enter valid numeric values.")
    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()