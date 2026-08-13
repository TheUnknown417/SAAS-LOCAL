import base64
import os
import glob

# Path inside the container
IMAGE_DIR = "/mnt/extra-addons/pos_grand_gupshup/data/img"

# Get all images
image_paths = glob.glob(os.path.join(IMAGE_DIR, "*"))

skipped = []
updated = []

for path in image_paths:
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    
    # Clean up name for matching
    product_name = name.strip()
    
    # Search for product template (case insensitive exact match)
    templates = env['product.template'].search([('name', '=ilike', product_name)])
    
    if templates:
        try:
            with open(path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            
            # Update all matching templates
            for tmpl in templates:
                tmpl.write({'image_1920': encoded_string})
            updated.append(product_name)
        except Exception as e:
            skipped.append(f"{product_name} (Error: {e})")
    else:
        skipped.append(product_name)

print("=== UPLOAD REPORT ===")
print(f"Updated {len(updated)} products.")
print(f"Skipped {len(skipped)} images.")
print("Skipped items:")
for s in skipped:
    print(f"- {s}")
env.cr.commit()
