import pickle


#------------------------------------insyirah lukeman's part================================================
monday = {'AM':
{'Clay Pot': {1: {'Menu': 'Kung Bao Chicken Rice', 'Price': 4.20},
             2: {'Menu': 'Ginger & Onion Pork Rice', 'Price': 4.80},
             3: {'Menu': 'Salted Fish Fried Rice', 'Price': 3.80},
             4: {'Menu': 'Fried Rice with Prawn', 'Price': 3.80}},

 'Beverages': {1: {'Menu': 'Hot Tea O', 'Price': 0.60},
               2: {'Menu': 'Hot Kopi', 'Price': 0.70},
               3: {'Menu': 'Hot Milo', 'Price': 0.80},
               4: {'Menu': 'Traditional Breakfast Set', 'Price': 2.00},
               5: {'Menu': 'Kaya Butter Toast', 'Price': 1.00},
               6: {'Menu': 'Soft Boiled Egg', 'Price': 1.00}},

 'MunChee': {1: {'Menu': 'Mixed Pork Soup', 'Price': 4.00},
             2: {'Menu': 'Pig\'s Liver Soup', 'Price': 4.00},
             3: {'Menu': 'Assorted Soup', 'Price': 3.80},
             4: {'Menu': 'Rice', 'Price': 0.50}},

 'Salad': {1: {'Menu': 'Egg Salad', 'Price' : 3.90},
           2: {'Menu': 'Chicken Salad', 'Price': 3.90},
           3: {'Menu': 'Chicken Bowl', 'Price' : 3.90},
           4: {'Menu': 'Vegan Bowl', 'Price': 3.90}},

 'Xin Mei Ban Mian': {1:{'Menu': 'Thin Bee Hoon', 'Price' : 3.00},
                       2: {'Menu': 'Yi Mian/Koka Mian', 'Price': 3.00},
                       3: {'Menu': 'Sliced FIsh Ban Mian', 'Price': 3.80},
                       4: {'Menu': 'Fried Dumpling(6 pcs)', 'Price': 3.30}}

 },
          'PM':
 {'Clay Pot': {1: {'Menu': 'Chicken Fried Rice', 'Price': 3.80},
              2: {'Menu': 'Fried Beef Hor Fun ', 'Price': 4.80},
              3: {'Menu': 'Sambal Long Bean w/ Pork ', 'Price': 4.50},
              4: {'Menu': 'Seafood Hokkien Mee', 'Price': 3.80},
              5: {'Menu': 'Fried Seafood Hor Fun', 'Price': 3.80}},

'Beverages': {1: {'Menu': 'Iced Tea O', 'Price': 0.80},
              2: {'Menu': 'Iced Tea', 'Price': 0.90},
              3: {'Menu': 'Iced Kopi', 'Price': 0.90},
              4: {'Menu': 'Iced Milo', 'Price': 1.00},
              5: {'Menu': 'Iced Bandung', 'Price': 1.00},
              6: {'Menu': 'Iced Lemon Tea', 'Price': 1.00},
              7: {'Menu': 'Canned drinks', 'Price': 0.80}},

'MunChee': {1: {'Menu': 'Sliced Veg Sliced Fish Soup', 'Price': 3.80},
            2: {'Menu': 'Bak Kut Teh', 'Price': 4.20},
            3: {'Menu': 'Meat Ball Soup', 'Price': 4.00},
            4: {'Menu': 'Lean Meat Soup', 'Price': 4.00},
            5: {'Menu': 'Salted Veg', 'Price': 1.20},
            6: {'Menu': 'Peanuts', 'Price': 1.20},
            7: {'Menu': 'Mee Sua', 'Price': 0.50},
            8: {'Menu': 'Rice', 'Price': 0.50}},

'Salad': {1: {'Menu': 'Tofu Salad', 'Price' : 3.90},
          2: {'Menu': 'Smoked Duck Bowl', 'Price': 4.50},
          3: {'Menu': 'Gyudon Beef Bowl', 'Price' : 4.90},
          4: {'Menu': 'Smoked Salmon Bowl', 'Price': 4.50}},

 'Xin Mei Ban Mian': {1:{'Menu': 'Spicy & Sour Noodle', 'Price' : 3.50},
                      2: {'Menu': 'Zha Jiang Mian', 'Price': 3.50},
                      3: {'Menu': 'Sichuan Veg Ban Mian', 'Price': 3.50},
                      4: {'Menu': 'Ban Mian / Mee Hoon Kway', 'Price': 3.00}}

}
}

# Database for Tuesday Menu
tuesday = {'AM':
{'YT Duck': {1: {'Menu': 'Char Siew Rice', 'Price': 2.80},
             2: {'Menu': 'Roasted Meat Rice', 'Price': 2.80},
             3: {'Menu': 'Lotus Meat Rice', 'Price': 3.00}},

 'Beverages': {1: {'Menu': 'Hot Tea O', 'Price': 0.60},
               2: {'Menu': 'Hot Kopi', 'Price': 0.70},
               3: {'Menu': 'Hot Milo', 'Price': 0.80},
               4: {'Menu': 'Traditional Breakfast Set', 'Price': 2.00},
               5: {'Menu': 'Kaya Butter Toast', 'Price': 1.00},
               6: {'Menu': 'Soft Boiled Egg', 'Price': 1.00}},

 'Indian': {1: {'Menu': 'Plain Prata', 'Price': 1.60},
            2: {'Menu': 'Egg Prata', 'Price': 1.30},
            3: {'Menu': 'Cheese Prata', 'Price': 2.50},
            4: {'Menu': 'Plain Dosa', 'Price': 1.20},
            5: {'Menu': 'Masala Dosa', 'Price': 2.00}},

 'Salad': {1: {'Menu': 'Egg Salad', 'Price' : 3.90},
           2: {'Menu': 'Chicken Salad', 'Price': 3.90},
           3: {'Menu': 'Chicken Bowl', 'Price' : 3.90},
           4: {'Menu': 'Vegan Bowl', 'Price': 3.90}},

 'Vinford Western': {1:{'Menu': 'Chicken Cutlet', 'Price' : 4.80},
                     2: {'Menu': 'Chicken Chop', 'Price': 4.80},
                     3: {'Menu': 'American Breakfast Set', 'Price': 4.30},
                     4: {'Menu': 'Beef Steak Rice', 'Price': 5.30}}

 },
          'PM':
 {'YT Duck': {1: {'Menu': 'Char Siew Rice', 'Price': 2.80},
              2: {'Menu': 'Char Siew Roasted Meat Noodles', 'Price': 4.00},
              3: {'Menu': 'Roasted Duck Noodles', 'Price': 3.30}},

 'Beverages': {1: {'Menu': 'Iced Tea O', 'Price': 0.80},
               2: {'Menu': 'Iced Tea', 'Price': 0.90},
               3: {'Menu': 'Iced Kopi', 'Price': 0.90},
               4: {'Menu': 'Iced Milo', 'Price': 1.00},
               5: {'Menu': 'Iced Bandung', 'Price': 1.00},
               6: {'Menu': 'Iced Lemon Tea', 'Price': 1.00},
               7: {'Menu': 'Canned drinks', 'Price': 0.80}},

'Indian': {1: {'Menu': 'Cheese Muratabak', 'Price': 5.00},
           2: {'Menu': 'Mutton Murtabak', 'Price': 5.00},
           3: {'Menu': 'Cheese Roti John', 'Price': 3.00},
           4: {'Menu': 'Nasi Goreng', 'Price': 3.00},
           5: {'Menu': 'Mee Goreng', 'Price': 3.00},
           6: {'Menu': 'Mutton Briyani', 'Price': 4.50},
           7: {'Menu': 'Chicken Briyani', 'Price': 4.50},
           8: {'Menu': 'Masala Prata', 'Price': 2.00}},

 'Salad': {1: {'Menu': 'Tofu Salad', 'Price' : 3.90},
           2: {'Menu': 'Smoked Duck Bowl', 'Price': 4.50},
           3: {'Menu': 'Gyudon Beef Bowl', 'Price' : 4.90},
           4: {'Menu': 'Smoked Salmon Bowl', 'Price': 4.50}},

 'Vinford Western': {1:{'Menu': 'Beef Steak', 'Price' : 5.00},
                     2: {'Menu': 'Chicken Chop', 'Price': 4.80},
                     3: {'Menu': 'Fish & Chip', 'Price': 4.80},
                     4: {'Menu': 'Chicken Chop Rice', 'Price': 4.80}}

}
}

# Database for Wednesday Menu
wednesday = {'AM':
{'Clay Pot': {1: {'Menu': 'Sambal Chicken Fried Rice', 'Price': 3.80},
              2: {'Menu': 'Kung Bao Chicken Rice', 'Price': 4.20},
              3: {'Menu': 'Ginger & Onion Pork Rice', 'Price': 4.50}},

 'Beverages': {1: {'Menu': 'Hot Tea O', 'Price': 0.60},
               2: {'Menu': 'Hot Kopi', 'Price': 0.70},
               3: {'Menu': 'Hot Milo', 'Price': 0.80},
               4: {'Menu': 'Traditional Breakfast Set', 'Price': 2.00},
               5: {'Menu': 'Kaya Butter Toast', 'Price': 1.00},
               6: {'Menu': 'Soft Boiled Egg', 'Price': 1.00}},

 'MunChee': {1: {'Menu': 'Mixed Pork Soup', 'Price': 4.00},
             2: {'Menu': 'Pig\'s Liver Soup', 'Price': 4.00},
             3: {'Menu': 'Assorted Soup', 'Price': 3.80},
             4: {'Menu': 'Rice', 'Price': 0.50}},

 'Yong Tau Foo': {1: {'Menu': 'Mushroom Minced Meat Noodle', 'Price' : 3.30},
                  2: {'Menu': 'Yong Tau Foo Soup', 'Price': 3.80},
                  3: {'Menu': 'Curry Yong Tau Foo', 'Price' : 4.40},
                  4: {'Menu': 'Fishball Soup', 'Price': 3.50},
                  5: {'Menu': 'Fishball Vermicelli Soup', 'Price': 3.50}},

 'Vinford Western': {1:{'Menu': 'Chicken Cutlet', 'Price' : 4.80},
                     2: {'Menu': 'Chicken Chop', 'Price': 4.80},
                     3: {'Menu': 'Beef Steak Rice', 'Price': 5.30}},

 },
          'PM':
{'Clay Pot': {1: {'Menu': 'Chicken Fried Rice', 'Price': 3.80},
              2: {'Menu': 'Fried Beef Hor Fun', 'Price': 4.80},
              3: {'Menu': 'Sambal Long Bean w/ Pork', 'Price': 4.50}},

'Beverages': {1: {'Menu': 'Iced Tea O', 'Price': 0.80},
              2: {'Menu': 'Iced Tea', 'Price': 0.90},
              3: {'Menu': 'Iced Kopi', 'Price': 0.90},
              4: {'Menu': 'Iced Milo', 'Price': 1.00},
              5: {'Menu': 'Iced Bandung', 'Price': 1.00},
              6: {'Menu': 'Iced Lemon Tea', 'Price': 1.00},
              7: {'Menu': 'Canned drinks', 'Price': 0.80}},

'MunChee': {1: {'Menu': 'Sliced Veg Sliced Fish Soup', 'Price': 3.80},
            2: {'Menu': 'Bak Kut Teh', 'Price': 4.20},
            3: {'Menu': 'Meat Ball Soup', 'Price': 4.00},
            4: {'Menu': 'Lean Meat Soup', 'Price': 4.00},
            5: {'Menu': 'Salted Veg', 'Price': 1.20},
            6: {'Menu': 'Peanuts', 'Price': 1.20},
            7: {'Menu': 'Mee Sua', 'Price': 0.50},
            8: {'Menu': 'Rice', 'Price': 0.50}},

'Yong Tau Foo': {1: {'Menu': 'Mushroom Minced Meat Noodle', 'Price': 3.30},
                 2: {'Menu': 'Yong Tau Foo Soup', 'Price': 3.80},
                 3: {'Menu': 'Curry Yong Tau Foo', 'Price': 4.40},
                 4: {'Menu': 'Fishball Soup', 'Price': 3.50},
                 5: {'Menu': 'Fishball Vermicelli Soup', 'Price': 3.50}},

'Vinford Western': {1: {'Menu': 'Beef Steak', 'Price': 5.00},
                    2: {'Menu': 'Spaghetti w Chicken Chop', 'Price': 4.80},
                    3: {'Menu': 'Chicken Chop', 'Price': 4.80}}

}
}

# Database for Thursday Menu
thursday = {'AM':
{'Xin Mei Ban Mian': {1: {'Menu': 'Dumpling Ban Mian', 'Price': 3.50},
                       2: {'Menu': 'Tom Yam Ban Mian', 'Price': 3.80},
                       3: {'Menu': 'Sliced Fish Bee Hoon', 'Price': 3.80}},

 'Beverages': {1: {'Menu': 'Hot Tea O', 'Price': 0.60},
               2: {'Menu': 'Hot Kopi', 'Price': 0.70},
               3: {'Menu': 'Hot Milo', 'Price': 0.80},
               4: {'Menu': 'Traditional Breakfast Set', 'Price': 2.00},
               5: {'Menu': 'Kaya Butter Toast', 'Price': 1.00},
               6: {'Menu': 'Soft Boiled Egg', 'Price': 1.00}},

 'Salad': {1: {'Menu': 'Egg Salad', 'Price': 3.90},
           2: {'Menu': 'Chicken Salad', 'Price': 3.90},
           3: {'Menu': 'Chicken Bowl', 'Price': 3.90},
           4: {'Menu': 'Vegan Bowl', 'Price': 3.90}},

 'Yong Tau Foo': {1: {'Menu': 'Mushroom Minced Meat Noodle', 'Price' : 3.30},
                  2: {'Menu': 'Yong Tau Foo Soup', 'Price': 3.80},
                  3: {'Menu': 'Curry Yong Tau Foo', 'Price' : 4.40},
                  4: {'Menu': 'Fishball Soup', 'Price': 3.50},
                  5: {'Menu': 'Fishball Vermicelli Soup', 'Price': 3.50}},

 'Vinford Western': {1:{'Menu': 'Chicken Cutlet', 'Price' : 4.80},
                     2: {'Menu': 'Chicken Chop', 'Price': 4.80},
                     3: {'Menu': 'Beef Steak Rice', 'Price': 5.30}},

 },
          'PM':
{'Xin Mei Ban Mian': {1: {'Menu': 'Fried Fish Soup', 'Price': 3.80},
                      2: {'Menu': 'Fish Porridge', 'Price': 3.80},
                      3: {'Menu': 'Tom Yam Ban Mian', 'Price': 4.80}},

'Beverages': {1: {'Menu': 'Iced Tea O', 'Price': 0.80},
              2: {'Menu': 'Iced Tea', 'Price': 0.90},
              3: {'Menu': 'Iced Kopi', 'Price': 0.90},
              4: {'Menu': 'Iced Milo', 'Price': 1.00},
              5: {'Menu': 'Iced Bandung', 'Price': 1.00},
              6: {'Menu': 'Iced Lemon Tea', 'Price': 1.00},
              7: {'Menu': 'Canned drinks', 'Price': 0.80}},

'Salad': {1: {'Menu': 'Tofu Salad', 'Price': 3.90},
          2: {'Menu': 'Smoked Duck Bowl', 'Price': 4.5},
          3: {'Menu': 'Gyudon Beef Bowl', 'Price': 4.90},
          4: {'Menu': 'Smoked Salmon Bowl', 'Price': 4.50}},

'Yong Tau Foo': {1: {'Menu': 'Mushroom Minced Meat Noodle', 'Price': 3.30},
                 2: {'Menu': 'Yong Tau Foo Soup', 'Price': 3.80},
                 3: {'Menu': 'Curry Yong Tau Foo', 'Price': 4.40},
                 4: {'Menu': 'Fishball Soup', 'Price': 3.50},
                 5: {'Menu': 'Fishball Vermicelli Soup', 'Price': 3.50}},

'Vinford Western': {1: {'Menu': 'Beef Steak', 'Price': 5.00},
                    2: {'Menu': 'Spaghetti w Chicken Chop', 'Price': 4.80},
                    3: {'Menu': 'Chicken Chop', 'Price': 4.80}}
}
}

#Database for Friday Menu
friday = {'AM':
{'YT Duck': {1: {'Menu': 'Char Siew Rice', 'Price': 2.80},
             2: {'Menu': 'Roasted Meat Rice', 'Price': 2.80},
             3: {'Menu': 'Lotus Meat Rice', 'Price': 3.00}},

 'Beverages': {1: {'Menu': 'Hot Tea O', 'Price': 0.60},
               2: {'Menu': 'Hot Kopi', 'Price': 0.70},
               3: {'Menu': 'Hot Milo', 'Price': 0.80},
               4: {'Menu': 'Traditional Breakfast Set', 'Price': 2.00},
               5: {'Menu': 'Kaya Butter Toast', 'Price': 1.00},
               6: {'Menu': 'Soft Boiled Egg', 'Price': 1.00}},

 'Indian': {1: {'Menu': 'Plain Prata', 'Price': 1.60},
            2: {'Menu': 'Egg Prata', 'Price': 1.30},
            3: {'Menu': 'Cheese Prata', 'Price': 2.50},
            4: {'Menu': 'Plain Dosa', 'Price': 1.20},
            5: {'Menu': 'Masala Dosa', 'Price': 2.00}},

 'Salad': {1: {'Menu': 'Egg Salad', 'Price' : 3.90},
           2: {'Menu': 'Chicken Salad', 'Price': 3.90},
           3: {'Menu': 'Chicken Bowl', 'Price' : 3.90},
           4: {'Menu': 'Vegan Bowl', 'Price': 3.90}},
 },
          'PM':
 {'YT Duck': {1: {'Menu': 'Char Siew Rice', 'Price': 2.80},
              2: {'Menu': 'Char Siew Roasted Meat Noodles', 'Price': 4.00},
              3: {'Menu': 'Roasted Duck Noodles', 'Price': 3.30},
              4: {'Menu': 'Roasted Duck Rice', 'Price': 3.30}},

  'Beverages': {1: {'Menu': 'Iced Tea O', 'Price': 0.80},
               2: {'Menu': 'Iced Tea', 'Price': 0.90},
               3: {'Menu': 'Iced Kopi', 'Price': 0.90},
               4: {'Menu': 'Iced Milo', 'Price': 1.00},
               5: {'Menu': 'Iced Bandung', 'Price': 1.00},
               6: {'Menu': 'Iced Lemon Tea', 'Price': 1.00},
               7: {'Menu': 'Canned drinks', 'Price': 0.80}},

'Indian': {1: {'Menu': 'Cheese Muratabak', 'Price': 5.00},
           2: {'Menu': 'Mutton Murtabak', 'Price': 5.00},
           3: {'Menu': 'Cheese Roti John', 'Price': 3.00},
           4: {'Menu': 'Nasi Goreng', 'Price': 3.00},
           5: {'Menu': 'Mee Goreng', 'Price': 3.00},
           6: {'Menu': 'Mutton Briyani', 'Price': 4.50},
           7: {'Menu': 'Chicken Briyani', 'Price': 4.50},
           8: {'Menu': 'Masala Prata', 'Price': 2.00}},

 'Salad': {1: {'Menu': 'Tofu Salad', 'Price' : 3.90},
           2: {'Menu': 'Smoked Duck Bowl', 'Price': 4.50},
           3: {'Menu': 'Gyudon Beef Bowl', 'Price' : 4.90},
           4: {'Menu': 'Smoked Salmon Bowl', 'Price': 4.50}},
}
}

# Database for Saturday Menu
saturday = {'AM':
{'Xian Mei Shi': {1: {'Menu': 'Wanton Soup', 'Price': 3.20},
                            2: {'Menu': 'Fried Egg w/ Tamato Noodles', 'Price': 4.20},
                            3: {'Menu': 'Sesame Liang Pi', 'Price': 3.20},
                            4: {'Menu': 'Hot & Dry Noodle', 'Price': 4.20}},

 'Beverages': {1: {'Menu': 'Hot Tea O', 'Price': 0.60},
               2: {'Menu': 'Hot Kopi', 'Price': 0.70},
               3: {'Menu': 'Hot Milo', 'Price': 0.80},
               4: {'Menu': 'Traditional Breakfast Set', 'Price': 2.00},
               5: {'Menu': 'Kaya Butter Toast', 'Price': 1.00},
               6: {'Menu': 'Soft Boiled Egg', 'Price': 1.00}},

 'Indian': {1: {'Menu': 'Plain Prata', 'Price': 1.60},
            2: {'Menu': 'Egg Prata', 'Price': 1.30},
            3: {'Menu': 'Cheese Prata', 'Price': 2.50},
            4: {'Menu': 'Plain Dosa', 'Price': 1.20},
            5: {'Menu': 'Masala Dosa', 'Price': 2.00},
            6: {'Menu': 'Nasi Goreng', 'Price': 3.00},
            7: {'Menu': 'Mee Goreng', 'Price': 3.00}},

 'Salad': {1: {'Menu': 'Egg Salad', 'Price' : 3.90},
           2: {'Menu': 'Chicken Salad', 'Price': 3.90},
           3: {'Menu': 'Chicken Bowl', 'Price' : 3.90},
           4: {'Menu': 'Vegan Bowl', 'Price': 3.90}},
 },
          'PM':
 {'YT Duck': {1: {'Menu': 'Char Siew Rice', 'Price': 2.80},
              2: {'Menu': 'Char Siew Roasted Meat Noodles', 'Price': 4.00},
              3: {'Menu': 'Roasted Duck Noodles', 'Price': 3.30},
              4: {'Menu': 'Roasted Duck Rice', 'Price': 3.30}},

  'Beverages': {1: {'Menu': 'Iced Tea O', 'Price': 0.80},
                2: {'Menu': 'Iced Tea', 'Price': 0.90},
                3: {'Menu': 'Iced Kopi', 'Price': 0.90},
                4: {'Menu': 'Iced Milo', 'Price': 1.00},
                5: {'Menu': 'Iced Bandung', 'Price': 1.00},
                6: {'Menu': 'Iced Lemon Tea', 'Price': 1.00},
                7: {'Menu': 'Canned drinks', 'Price': 0.80}},

'Indian': {1: {'Menu': 'Cheese Muratabak', 'Price': 5.00},
           2: {'Menu': 'Mutton Murtabak', 'Price': 5.00},
           3: {'Menu': 'Cheese Roti John', 'Price': 3.00},
           4: {'Menu': 'Nasi Goreng', 'Price': 3.00},
           5: {'Menu': 'Mee Goreng', 'Price': 3.00},
           6: {'Menu': 'Mutton Briyani', 'Price': 4.50},
           7: {'Menu': 'Chicken Briyani', 'Price': 4.50},
           8: {'Menu': 'Masala Prata', 'Price': 2.00}},
}
}

# Database for Sunday Menu
sunday = {'AM':
{'Clay Pot': {1: {'Menu': 'Sambal Chicken Fried Rice', 'Price': 3.80},
              2: {'Menu': 'Kung Bao Chicken Rice', 'Price': 4.20},
              3: {'Menu': 'Ginger & Onion Pork Rice', 'Price': 4.50}},

 'Beverages': {1: {'Menu': 'Hot Tea O', 'Price': 0.60},
               2: {'Menu': 'Hot Kopi', 'Price': 0.70},
               3: {'Menu': 'Hot Milo', 'Price': 0.80},
               4: {'Menu': 'Traditional Breakfast Set', 'Price': 2.00},
               5: {'Menu': 'Kaya Butter Toast', 'Price': 1.00},
               6: {'Menu': 'Soft Boiled Egg', 'Price': 1.00}},

 'Yong Tau Foo': {1: {'Menu': 'Mushroom Minced Meat Noodle', 'Price' : 3.30},
                  2: {'Menu': 'Yong Tau Foo Soup', 'Price': 3.80},
                  3: {'Menu': 'Curry Yong Tau Foo', 'Price' : 4.40},
                  4: {'Menu': 'Fishball Soup', 'Price': 3.50},
                  5: {'Menu': 'Fishball Vermicelli Soup', 'Price': 3.50}},

 'Vinford Western': {1:{'Menu': 'Chargrill Chicken Set', 'Price' : 4.80},
                     2: {'Menu': 'Chicken Aglio Olio Spicy', 'Price': 4.20},
                     3: {'Menu': 'Karage Aglio Olio Spicy', 'Price': 4.20}},

 },
          'PM':
{ 'Beverages': {1: {'Menu': 'Iced Tea O', 'Price': 0.80},
                2: {'Menu': 'Iced Tea', 'Price': 0.90},
                3: {'Menu': 'Iced Kopi', 'Price': 0.90},
                4: {'Menu': 'Iced Milo', 'Price': 1.00},
                5: {'Menu': 'Iced Bandung', 'Price': 1.00},
                6: {'Menu': 'Iced Lemon Tea', 'Price': 1.00},
                7: {'Menu': 'Canned drinks', 'Price': 0.80}},

'Yong Tau Foo': {1: {'Menu': 'Mushroom Minced Meat Noodle', 'Price': 3.30},
                 2: {'Menu': 'Yong Tau Foo Soup', 'Price': 3.80},
                 3: {'Menu': 'Curry Yong Tau Foo', 'Price': 4.40},
                 4: {'Menu': 'Fishball Soup', 'Price': 3.50},
                 5: {'Menu': 'Fishball Vermicelli Soup', 'Price': 3.50}},

'Vinford Western': {1: {'Menu': 'Grill Fish w/ Italian Herb Set', 'Price': 4.80},
                    2: {'Menu': 'Fried Bread Crumbs Fish Set', 'Price': 4.80},
                    3: {'Menu': 'Grill Slamon Fillet Set', 'Price': 4.80}}

}
}



#using pickle to translate the dictionary into a file for easy access
pickle_out = open("monday.pickle","wb")
pickle.dump(monday, pickle_out)
pickle_out.close()



