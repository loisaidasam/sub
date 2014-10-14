sub
===

Python helper library for accessing NYC MTA subway data

### Usage

To output all Subway routes and a list of all stops for each route from the command line, simply invoke:

    $ ./parser.py
    
The results of this data (collected 14 October 2014) are stored in [stops_per_subway_line.txt](https://github.com/loisaidasam/sub/blob/5369ebc22ef57b932d57066a357fd4cd5a41a402/stops_per_subway_line.txt).

Parser library usage:

    >>> from parser import get_routes
    >>> routes = get_routes()
    >>> routes['F']
    {'agency_id': 'MTA NYCT',
     'route_color': 'FF6319',
     'route_desc': 'Trains operate at all times between Jamaica, Queens, and Stillwell Av, Brooklyn via the 63 St Connector (serving 21 St-Queensbridge, Roosevelt Island, Lexington Av-63 St, and 57 St-6 Av). F trains operate express along Queens Blvd at all times. Trains do not serve Queens Plaza, 23 St-Ely Av, Lexington Av-53 St and 5 Av-53 St.',
     'route_id': 'F',
     'route_long_name': 'Queens Blvd Express/ 6 Av Local',
     'route_short_name': 'F',
     'route_text_color': '',
     'route_type': '1',
     'route_url': 'http://web.mta.info/nyct/service/pdf/tfcur.pdf'}
    >>> routes.keys()
    ['FS',
     '5X',
     'GS',
     '1',
     '3',
     '2',
     '5',
     '4',
     '7',
     '6',
     '7X',
     'A',
     'C',
     'B',
     'E',
     'D',
     'G',
     'F',
     'H',
     'J',
     'M',
     'L',
     'N',
     'Q',
     'R',
     'Z',
     'SI',
     '6X']

### About

This library was written in accordance with the [Agreement for Access to Metropolitan Transportation Authority ("MTA") Data Feeds](http://web.mta.info/developers/developer-data-terms.html) and anyone who wishes to modify this library should do so within the terms of the agreement.

Sample data in the [google_transit](https://github.com/loisaidasam/sub/tree/master/google_transit) directory was downloaded from [http://web.mta.info/developers/data/nyct/subway/google_transit.zip](http://web.mta.info/developers/data/nyct/subway/google_transit.zip) via [http://web.mta.info/developers/developer-data-terms.html](http://web.mta.info/developers/developer-data-terms.html) on 14 October 2014.

### Motivation

The original motivation was to get a list of subway stations per line, essentially answering this post:

[http://stackoverflow.com/questions/25634764/scrape-mta-subway-data](http://stackoverflow.com/questions/25634764/scrape-mta-subway-data)
