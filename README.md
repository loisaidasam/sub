sub
===

Python helper library for accessing MTA subway data

This library was written in accordance with the [Agreement for Access to Metropolitan Transportation Authority ("MTA") Data Feeds](http://web.mta.info/developers/developer-data-terms.html) and anyone who wishes to modify this library should do so within the terms of the agreement.

Sample data in the [google_transit](https://github.com/loisaidasam/sub/tree/master/google_transit) directory was downloaded from [http://web.mta.info/developers/data/nyct/subway/google_transit.zip](http://web.mta.info/developers/data/nyct/subway/google_transit.zip) via [http://web.mta.info/developers/developer-data-terms.html](http://web.mta.info/developers/developer-data-terms.html) on 14 October 2014.

The original motivation was to get a list of subway stations per line, essentially answering this post: [http://stackoverflow.com/questions/25634764/scrape-mta-subway-data](http://stackoverflow.com/questions/25634764/scrape-mta-subway-data)

The parser script was run:

    $ ./parser.py
    
and the results of this data (collected 14 October 2014) are stored in [stops_per_subway_line.txt](https://github.com/loisaidasam/sub/blob/5369ebc22ef57b932d57066a357fd4cd5a41a402/stops_per_subway_line.txt).
