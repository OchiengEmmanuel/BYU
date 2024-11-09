"""Compute and print the the storage efficiency of a can."""

# Import the standard math module so that
# math.pi can be used in this program.
import math

#Different can sizes

can_sizes = {
    "#1 Picnic": (6.83, 10.16),
    "#1 Tall": (7.78, 11.91),
    "#2": (8.73, 11.59),
    "#2.5": (10.32, 11.91),
    "#3 Cylinder": (10.79, 17.78),
    "#5": (13.02, 14.29),
    "#6Z": (5.40, 8.89),
    "#8Z short": (6.83, 7.62),
    "#10": (15.72, 17.78),
    "#211": (6.83, 12.38),
    "#300": (7.62, 11.27),
    "#303": (8.10, 11.11),
}

def main():


def compute_volume(radius, height):
    #######--
    --

    volume = math.pi * radius**2 * height / 3
    return volume



def compute_surface_area(radius, height):
    #######--
    --

    surface_area = 2 * math.pi * radius * (radius + height)



    storage_efficiency = compute_volume/compute_surface_area




# Start this program by
# calling the main function.
main()