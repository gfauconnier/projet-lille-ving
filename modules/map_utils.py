def get_icons_colors():
    colors_dict = {
        'Tribunal' : 'white',
        'government' : 'white',
        'Décheterie' : 'white',
        'public' : 'white',
        'Departement' : 'white',
        'Mairie' : 'white',
        'Pompier' : 'white',
        'police' : 'white',
        'post_office' : 'white',
        'community_centre' : 'white',
        #
        'College' : '#606060',
        'Crèche' : '#606060',
        'Lycée' : '#606060',
        'Maternelle' : '#606060',
        'Primaire' : '#606060',
        'University' : '#606060',
        'music_school' : '#606060',
        #
        'arts_centre' : '#ff6666',
        'cinema' : '#ff6666',
        'library' : '#ff6666',
        'books' : '#ff6666',
        'zoo' : '#ff6666',
        'museum' : '#ff6666',
        'theatre' : '#ff6666',
        'music' : '#ff6666',
        'musical_instrument' : '#ff6666',
        #
        'optician' : '#ff0000',
        'dentist' : '#ff0000',
        'doctors' : '#ff0000',
        'hospital' : '#ff0000',
        'laboratory' : '#ff0000',
        'pharmacy' : '#ff0000',
        #
        'office' : '#b3b3ff',
        'bank' : '#b3b3ff',
        'car' : '#b3b3ff',
        'travel_agency' : '#b3b3ff',
        'vacuum_cleaner' : '#b3b3ff',
        'laundry' : '#b3b3ff',
        #
        'hotel' : '#6600ff',
        'fast_food' : '#6600ff',
        'nightclub' : '#6600ff',
        'pub' : '#6600ff',
        'restaurant' : '#6600ff',
        'bar' : '#6600ff',
        'cafe' : '#6600ff',
        'casino' : '#6600ff',
        #
        'food_court' : '#660033',
        'butcher' : '#660033',
        'cheese' : '#660033',
        'chocolate' : '#660033',
        'deli' : '#660033',
        'greengrocer' : '#660033',
        'seafood' : '#660033',
        'bakery' : '#660033',
        'pastry' : '#660033',
        'commercial' : '#660033',
        'marketplace' : '#660033',
        'supermarket' : '#660033',
        #
        'attraction' : '#009933',
        'park' : '#009933',
        'playground' : '#009933',
        #
        'alcohol' : '#00ffff',
        'wine' : '#00ffff',
        'tobacco' : '#00ffff',
        'tea' : '#00ffff',
        'florist' : '#00ffff',
        'antiques' : '#00ffff',
        'convenience' : '#00ffff',
        'electronics' : '#00ffff',
        'furniture' : '#00ffff',
        'garden_centre' : '#00ffff',
        'interior_decoration' : '#00ffff',
        'retail' : '#00ffff',
        'mall' : '#00ffff',
        #
        'bicycle_parking' : 'blue',
        'bicycle_rental' : 'blue',
        'platform' : 'blue',
        'station' : 'blue',
        #
        'beauty' : '#ff9900',
        'shoes' : '#ff9900',
        'clothes' : '#ff9900',
        'hairdresser' : '#ff9900',
        'cosmetics' : '#ff9900',
        'fashion_accessories' : '#ff9900',
        'watches' : '#ff9900',
        'jewelry' : '#ff9900',
        'perfumery' : '#ff9900',
        #
        'church' : 'yellow',
        'mosque' : 'yellow',
        'cathedral' : 'yellow',
        #
        'fitness_centre' : '#40ff00',
        'sports' : '#40ff00',
        'sports_centre' : '#40ff00',
        'sports_hall' : '#40ff00',
        'swimming_pool' : '#40ff00',
        #
        'vacant' : 'grey'
    }

    return colors_dict

def get_type_local(type_local):
    code_type_local = {
                        'Tous' : 0,
                        'Maisons' : 1.0,
                        'Appartements':2.0
                        }
    return code_type_local[type_local]