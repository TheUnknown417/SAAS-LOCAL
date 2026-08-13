# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def _setup_menu_data(env):
    # This hook will create the products and variants dynamically
    # to ensure prices and attributes are linked perfectly.
    
    # Categories
    categ_karahi = env.ref('pos_grand_gupshup.pos_category_karahi').id
    categ_handi = env.ref('pos_grand_gupshup.pos_category_handi').id
    categ_biryani = env.ref('pos_grand_gupshup.pos_category_biryani').id
    categ_naan = env.ref('pos_grand_gupshup.pos_category_naan').id
    categ_nashta = env.ref('pos_grand_gupshup.pos_category_nashta').id
    categ_lunch = env.ref('pos_grand_gupshup.pos_category_lunch').id
    categ_beef = env.ref('pos_grand_gupshup.pos_category_beef').id

    # Attributes
    attr_portion = env.ref('pos_grand_gupshup.product_attribute_portion')
    val_single = env.ref('pos_grand_gupshup.product_attribute_value_single')
    val_half = env.ref('pos_grand_gupshup.product_attribute_value_half')
    val_full = env.ref('pos_grand_gupshup.product_attribute_value_full')

    menu_data = [
        # Karahi Point
        {'name': 'Special Chicken Karahi', 'categ': categ_karahi, 'prices': {'Half': 1000, 'Full': 1900}},
        {'name': 'Chicken Achari Karahi', 'categ': categ_karahi, 'prices': {'Half': 1100, 'Full': 2100}},
        {'name': 'Chicken White Karahi', 'categ': categ_karahi, 'prices': {'Half': 1100, 'Full': 2100}},
        {'name': 'Chicken Malai Karahi', 'categ': categ_karahi, 'prices': {'Half': 1150, 'Full': 2300}},
        {'name': 'Chicken Sunwari Karahi', 'categ': categ_karahi, 'prices': {'Half': 1200, 'Full': 2400}},
        {'name': 'Special Desi Chicken Karahi', 'categ': categ_karahi, 'prices': {'Half': 2000, 'Full': 3800}},
        {'name': 'Desi Chicken Achari Karahi', 'categ': categ_karahi, 'prices': {'Half': 2000, 'Full': 3800}},
        {'name': 'Desi Chicken Malai Karahi', 'categ': categ_karahi, 'prices': {'Half': 2000, 'Full': 4000}},
        {'name': 'Mutton Karahi', 'categ': categ_karahi, 'prices': {'Half': 2000, 'Full': 3900}},
        {'name': 'Mutton White Karahi', 'categ': categ_karahi, 'prices': {'Half': 2100, 'Full': 4000}},
        {'name': 'Malai White Mutton Karahi', 'categ': categ_karahi, 'prices': {'Half': 2100, 'Full': 4000}},
        {'name': 'Special Beef Karahi', 'categ': categ_karahi, 'prices': {'Half': 1300, 'Full': 2600}},
        {'name': 'Beef White Karahi', 'categ': categ_karahi, 'prices': {'Half': 1400, 'Full': 2800}},
        {'name': 'Beef Malai Karahi', 'categ': categ_karahi, 'prices': {'Half': 1500, 'Full': 3000}},

        # Handi Point
        {'name': 'Special Chicken Handi', 'categ': categ_handi, 'prices': {'Half': 1100, 'Full': 2100}},
        {'name': 'Chicken Achari Handi', 'categ': categ_handi, 'prices': {'Half': 1000, 'Full': 2000}},
        {'name': 'Chicken Jalfrezi Handi', 'categ': categ_handi, 'prices': {'Half': 1000, 'Full': 2000}},
        {'name': 'Chicken Boonless Handi', 'categ': categ_handi, 'prices': {'Half': 1050, 'Full': 2100}},
        {'name': 'Chicken White Handi', 'categ': categ_handi, 'prices': {'Half': 1100, 'Full': 2200}},
        {'name': 'Chicken Makhan Handi', 'categ': categ_handi, 'prices': {'Half': 1200, 'Full': 2300}},
        {'name': 'Special Mutton Handi', 'categ': categ_handi, 'prices': {'Half': 2000, 'Full': 4000}},
        {'name': 'Mutton Makhan Handi', 'categ': categ_handi, 'prices': {'Half': 2100, 'Full': 4100}},
        {'name': 'Mutton Malai Handi', 'categ': categ_handi, 'prices': {'Half': 2100, 'Full': 4100}},
        {'name': 'Special Beef Handi', 'categ': categ_handi, 'prices': {'Half': 1500, 'Full': 3000}},
        {'name': 'Beef Makhan Handi', 'categ': categ_handi, 'prices': {'Half': 1600, 'Full': 3100}},
        {'name': 'Beef Malai Handi', 'categ': categ_handi, 'prices': {'Half': 1600, 'Full': 3100}},

        # Biryani Point
        {'name': 'Biryani Full Chicken', 'categ': categ_biryani, 'prices': {'Half': 200, 'Full': 350}},
        {'name': 'Full Sada Biryani', 'categ': categ_biryani, 'prices': {'Half': 150, 'Full': 300}},
        {'name': 'Full Matranjan Zarda', 'categ': categ_biryani, 'prices': {'Half': 350, 'Full': 200}}, # Might be a typo in image (H=350, F=200?), I'll use as is
        {'name': 'GupSup Biryani Deal', 'categ': categ_biryani, 'prices': {'Standard': 500}},

        # Special Naan
        {'name': 'Sada Naan', 'categ': categ_naan, 'prices': {'Standard': 30}},
        {'name': 'Roghni Naan', 'categ': categ_naan, 'prices': {'Standard': 100}},
        {'name': 'Dhaniya Naan', 'categ': categ_naan, 'prices': {'Standard': 40}},
        {'name': 'Kalwangi Naan', 'categ': categ_naan, 'prices': {'Standard': 60}},
        {'name': 'Kulcha', 'categ': categ_naan, 'prices': {'Standard': 40}},
        {'name': 'Garli Naan', 'categ': categ_naan, 'prices': {'Standard': 100}},
        {'name': 'Cheese Naan', 'categ': categ_naan, 'prices': {'Standard': 150}},
        {'name': 'Milki Naan', 'categ': categ_naan, 'prices': {'Standard': 120}},
        {'name': 'Aloo Wala Naan', 'categ': categ_naan, 'prices': {'Standard': 150}},
        {'name': 'Keema Naan', 'categ': categ_naan, 'prices': {'Standard': 300}},
        {'name': 'Raita', 'categ': categ_naan, 'prices': {'Standard': 50}},
        {'name': 'Khamiri Roti', 'categ': categ_naan, 'prices': {'Standard': 30}},
        {'name': 'Sada Roti', 'categ': categ_naan, 'prices': {'Standard': 15}},

        # Nashta Point
        {'name': 'Halwa Puri Platter', 'categ': categ_nashta, 'prices': {'Standard': 200}},
        {'name': 'Meetha Pura', 'categ': categ_nashta, 'prices': {'Standard': 100}},
        {'name': 'Special Chanay', 'categ': categ_nashta, 'prices': {'Half': 150, 'Full': 300}},
        {'name': 'Murgh Chanay', 'categ': categ_nashta, 'prices': {'Half': 300, 'Full': 450}},
        {'name': 'Anda Chanay', 'categ': categ_nashta, 'prices': {'Half': 200, 'Full': 350}},
        {'name': 'Kofta Chanay', 'categ': categ_nashta, 'prices': {'Half': 220, 'Full': 370}},
        {'name': 'Bary Paye', 'categ': categ_nashta, 'prices': {'Half': 500, 'Full': 1000}},
        {'name': 'Choty Paye', 'categ': categ_nashta, 'prices': {'Half': 550, 'Full': 1100}},
        {'name': 'Bong Paye', 'categ': categ_nashta, 'prices': {'Half': 500, 'Full': 1000}},
        {'name': 'Sada Paratha', 'categ': categ_nashta, 'prices': {'Standard': 100}},
        {'name': 'Aloo Paratha', 'categ': categ_nashta, 'prices': {'Standard': 150}},
        {'name': 'Saag Paratha', 'categ': categ_nashta, 'prices': {'Standard': 150}},
        {'name': 'Mooli Paratha', 'categ': categ_nashta, 'prices': {'Standard': 200}},
        {'name': 'Chicken Paratha', 'categ': categ_nashta, 'prices': {'Standard': 300}},
        {'name': 'Cheese Paratha', 'categ': categ_nashta, 'prices': {'Standard': 300}},
        {'name': 'Chicken Cheese Paratha', 'categ': categ_nashta, 'prices': {'Standard': 400}},
        {'name': 'Anda Paratha', 'categ': categ_nashta, 'prices': {'Standard': 180}},
        {'name': 'Omelette Anda', 'categ': categ_nashta, 'prices': {'Standard': 100}},
        {'name': 'Full Fry Egg', 'categ': categ_nashta, 'prices': {'Standard': 80}},
        {'name': 'Half Fry Egg', 'categ': categ_nashta, 'prices': {'Standard': 80}},
        {'name': 'Milk', 'categ': categ_nashta, 'prices': {'Standard': 200}},
        {'name': 'Dahi', 'categ': categ_nashta, 'prices': {'Standard': 220}},
        {'name': 'Lassi', 'categ': categ_nashta, 'prices': {'Standard': 150}},
        {'name': 'Chai', 'categ': categ_nashta, 'prices': {'Standard': 80}}, # Ignoring the +100 for simplicity

        # Lunch Point
        {'name': 'Dal Chana', 'categ': categ_lunch, 'prices': {'Half': 150, 'Full': 300}},
        {'name': 'Dal Mash', 'categ': categ_lunch, 'prices': {'Half': 200, 'Full': 350}},
        {'name': 'Lobia', 'categ': categ_lunch, 'prices': {'Half': 150, 'Full': 300}},
        {'name': 'Chicken Sabzi', 'categ': categ_lunch, 'prices': {'Half': 150, 'Full': 300}},
        {'name': 'Beef Keema', 'categ': categ_lunch, 'prices': {'Half': 300, 'Full': 500}},
        {'name': 'Chicken Korma', 'categ': categ_lunch, 'prices': {'Half': 250, 'Full': 450}},
        {'name': 'Kadhi Pakora', 'categ': categ_lunch, 'prices': {'Half': 150, 'Full': 300}},
        {'name': 'Chicken Palak', 'categ': categ_lunch, 'prices': {'Half': 250, 'Full': 450}},

        # Beef Main Course
        {'name': 'Chicken Kabab', 'categ': categ_beef, 'prices': {'Single': 200, 'Half': 1000, 'Full': 2000}},
        {'name': 'Beef Kabab', 'categ': categ_beef, 'prices': {'Single': 220, 'Half': 1150, 'Full': 2200}},
        {'name': 'Reshmi Kabab', 'categ': categ_beef, 'prices': {'Single': 230, 'Half': 1150, 'Full': 2200}},
        {'name': 'Afghani Kabab', 'categ': categ_beef, 'prices': {'Single': 230, 'Half': 1150, 'Full': 2200}},
        {'name': 'Hara Bhara Kabab', 'categ': categ_beef, 'prices': {'Single': 230, 'Half': 1150, 'Full': 2200}},
        {'name': 'Tikka boti', 'categ': categ_beef, 'prices': {'Single': 400, 'Half': 800, 'Full': 1600}},
        {'name': 'Malai Boti', 'categ': categ_beef, 'prices': {'Single': 500, 'Half': 900, 'Full': 1800}},
        {'name': 'Green Boti', 'categ': categ_beef, 'prices': {'Single': 500, 'Half': 900, 'Full': 1800}},
        {'name': 'Cheese Boti', 'categ': categ_beef, 'prices': {'Single': 500, 'Half': 1000, 'Full': 2000}},
        {'name': 'Leg Piece', 'categ': categ_beef, 'prices': {'Standard': 400}},
        {'name': 'Chest Piece', 'categ': categ_beef, 'prices': {'Standard': 500}},
        {'name': 'Malai Chest', 'categ': categ_beef, 'prices': {'Standard': 550}},
        {'name': 'Malai Leg', 'categ': categ_beef, 'prices': {'Standard': 600}},
    ]

    ProductTemplate = env['product.template'].with_context(tracking_disable=True)
    
    for item in menu_data:
        prices = item['prices']
        
        if 'Standard' in prices:
            # Simple product without variants
            ProductTemplate.create({
                'name': item['name'],
                'list_price': prices['Standard'],
                'available_in_pos': True,
                'pos_categ_ids': [(4, item['categ'])],
                'type': 'consu',
            })
        else:
            # Product with variants
            # Base price will be the lowest price (e.g. Single or Half)
            base_price = 0
            if 'Single' in prices:
                base_price = prices['Single']
            elif 'Half' in prices:
                base_price = prices['Half']
                
            vals = {
                'name': item['name'],
                'list_price': base_price,
                'available_in_pos': True,
                'pos_categ_ids': [(4, item['categ'])],
                'type': 'consu',
            }
            template = ProductTemplate.create(vals)
            
            # Create Attribute Line
            attr_values = []
            if 'Single' in prices: attr_values.append(val_single.id)
            if 'Half' in prices: attr_values.append(val_half.id)
            if 'Full' in prices: attr_values.append(val_full.id)
            
            line = env['product.template.attribute.line'].create({
                'product_tmpl_id': template.id,
                'attribute_id': attr_portion.id,
                'value_ids': [(6, 0, attr_values)],
            })
            
            # Set extra prices on generated values
            for ptav in line.product_template_value_ids:
                if ptav.product_attribute_value_id.id == val_single.id:
                    ptav.price_extra = prices['Single'] - base_price
                elif ptav.product_attribute_value_id.id == val_half.id:
                    ptav.price_extra = prices['Half'] - base_price
                elif ptav.product_attribute_value_id.id == val_full.id:
                    ptav.price_extra = prices['Full'] - base_price
