import datetime

# Get the current date
current_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Gather tire information from the user
width = input("Enter the width of the tire: ")
aspect_ratio = input("Enter the aspect ratio of the tire: ")
diameter = input("Enter the diameter of the wheel: ")

# Calculate the volume of the tire
volume = calculate_tire_volume(float(width), float(aspect_ratio), float(diameter))

# Append the information to the text file
with open('volumes.txt', 'a') as file:
    file.write(f"{current_date} | Width: {width}, Aspect Ratio: {aspect_ratio}, Diameter: {diameter}, Volume: {volume:.2f}\n")

print("Data appended to volumes.txt.")

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Calculate the volume of the tire using a simplified formula
    radius = (width * aspect_ratio * 0.01 + diameter * 0.0254) / 2
    volume = (22 / 7) * radius ** 2 * diameter / 1000000  # Assuming π as 22/7

    return volume
