import pyproj

# --- Set up coordinate systems ---
# WGS84 (lon/lat) to BC Albers (EPSG:3005)
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
    # Step 1: Convert to BC Albers
    x_a, y_a = transformer.transform(lon, lat)
    
    # Step 2: Apply transformation to Map B
    x_b, y_b = map_a_to_map_b(x_a, y_a)

    return x_b, y_b

# --- Example usage ---
if __name__ == "__main__":
    lon, lat = -125.0, 49.5  # Example coordinates
    x_b, y_b = convert_lonlat_to_map_b(lon, lat)
    print(f"Map B coordinates: x = {x_b:.2f}, y = {y_b:.2f}")
