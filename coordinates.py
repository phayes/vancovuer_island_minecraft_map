import pyproj
import sys

# --- Set up coordinate systems ---
wgs84 = pyproj.CRS("EPSG:4326")      # GPS coordinates
bc_albers = pyproj.CRS("EPSG:3005")  # BC Albers projection
transformer = pyproj.Transformer.from_crs(wgs84, bc_albers, always_xy=True)

# --- Transformation from Map A (BC Albers) to Map B ---
def map_a_to_map_b(x_a, y_a):
    x_b =  0.02436555 * x_a - 17751.90027
    y_b = -0.02436555 * y_a + 14876.75207
    return x_b, y_b

# --- Main function ---
def convert_lonlat_to_map_b(lon, lat):
    x_a, y_a = transformer.transform(lon, lat)
    x_b, y_b = map_a_to_map_b(x_a, y_a)
    return x_b, y_b

# --- Example usage ---
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <longitude> <latitude>")
        print("Example: python script.py -125.0 49.5")
        print("Description:")
        print("  - Takes WGS84 longitude and latitude as input")
        print("  - Transforms them to BC Albers (EPSG:3005)")
        print("  - Applies a 40:1 scale + offset transformation to get Vancouver Island Minecraft Map coordinates")
        sys.exit(1)

    lon = float(sys.argv[1])
    lat = float(sys.argv[2])
    x_b, y_b = convert_lonlat_to_map_b(lon, lat)
    print(f"Map B coordinates: x = {x_b:.2f}, y = {y_b:.2f}")
