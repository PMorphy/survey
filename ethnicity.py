import csv
from collections import defaultdict, Counter

with open( 'survey_results_public.csv' ) as f:
    csv_reader = csv.DictReader( f )
    ethnicity_data = {}
    for line in csv_reader:
        ethnicity_types = line[ 'Ethnicity' ].split( ';' )
        for ethnicity_type in ethnicity_types:
            ethnicity_data.setdefault( ethnicity_type, {
                'total': 0,
                'jobsat': Counter()
            })
            languages = line[ 'JobSat' ].split( ';' )
            ethnicity_data[ ethnicity_type ][ 'total' ] += 1
            ethnicity_data[ ethnicity_type ][ 'jobsat' ].update( languages )

    for ethnicity, data in ethnicity_data.items():
        print( ethnicity )
        for language, value in data[ 'jobsat' ].most_common( 5 ):
            language_pct = round( value / data[ 'total' ] * 100, 2 )
            print( f'\t{language}: {language_pct}%' )





if __name__ == '__main__':
    pass
