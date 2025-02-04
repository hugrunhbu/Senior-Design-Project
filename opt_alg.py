

# item's dimensions (mm) (made up for now)
item_height = 100
item_width = 50
item_length = 30

# constraints
tolerance = 5   # Extra space for the item to fit inside the box
material_thickness = 3    # thickness of cardboard
flap_ratio = 0.2    # flap length as a fraction of external height/width

# Internal dimensions
H_internal = item_height + tolerance
W_internal = item_width + tolerance
L_internal = item_length + tolerance

# External dimensions
H_external = H_internal + 2 * material_thickness
W_external = W_internal + 2 * material_thickness
L_external = L_internal + 2 * material_thickness

# Flap lengths (top/bottom flaps)
flap_height = flap_ratio * H_external
flap_width = flap_ratio * W_external

# Base panel dimensions
base_panel = (H_external, W_external)

# Side panels (with flaps)
side_panel_height = H_external
side_panel_length = L_external + 2 * flap_width  # Flaps on both ends

# Front/back panels (with flaps)
front_panel_height = H_external + 2 * flap_height  # Flaps on top and bottom
front_panel_width = W_external