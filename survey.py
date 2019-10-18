
import csv
from collections import defaultdict, Counter

def survey( file ):
    with open( file ) as f:
        csv_reader = csv.DictReader( f )
        dev_type_info = {}
        for line in csv_reader:
            dev_types = line[ 'DevType' ].split( ';' )
            for dev_type in dev_types:
                dev_type_info.setdefault( dev_type, {
                    'total': 0,
                    'language_counter': Counter()
                })
                languages = line[ 'LanguageWorkedWith' ].split( ';' )
                dev_type_info[ dev_type ][ 'language_counter' ].update( languages )
                dev_type_info[ dev_type ][ 'total' ] += 1
        for dev_type, info in dev_type_info.items():
            print( dev_type + ':' )
            for language, value in info[ 'language_counter' ].most_common( 5 ):
                language_pct = round( value / info[ 'total' ] * 100, 2 )
                print( f'\t{language}: {language_pct}%' )


if __name__ == '__main__':
    survey( 'survey_results_public.csv' )
