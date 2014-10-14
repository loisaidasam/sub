#!/usr/bin/env python

"""Python helper library for using MTA data
"""

import csv
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'google_transit')


def _get_filename(name_short):
    """Filename builder helper
    Pass in something like 'routes' and get back 'google_transit/routes.txt'
    """
    return os.path.join(BASE_DIR, '%s.txt' % name_short)


def _get_file_data(filename):
    """Helper for getting data from .csv file as a list of dicts
    """
    with open(filename, 'r') as fp:
        reader = csv.reader(fp)
        headers = reader.next()
        results = []
        for row in reader:
            results.append(dict(zip(headers, row)))
    return results


def get_routes():
    """
    agency_id,route_id,route_short_name,route_long_name,route_type,route_desc,route_url,route_color,route_text_color
    MTA NYCT,1,1,Broadway - 7 Avenue Local,1,"Trains operate between 242 St in the Bronx and South Ferry in Manhattan, most times",http://web.mta.info/nyct/service/pdf/t1cur.pdf,EE352E,
    MTA NYCT,2,2,7 Avenue Express,1,"Trains operate between Wakefield-241 St, Bronx, and Flatbush Av-Brooklyn College, Brooklyn, at all times. Trains operate local in Bronx and Brooklyn. Trains operate express in Manhattan except late night when it operates local.",http://web.mta.info/nyct/service/pdf/t2cur.pdf,EE352E,
    MTA NYCT,3,3,7 Avenue Express,1,"Trains operate between 148 St, 7 Av, Manhattan, and New Lots Av, Brooklyn, at all times except late nights. During late nights, trains operate only in Manhattan between 148 St, 7 Av and Times Square-42 St.",http://web.mta.info/nyct/service/pdf/t3cur.pdf,EE352E,
    MTA NYCT,4,4,Lexington Avenue Express,1,"Trains operate daily between Woodlawn/Jerome Av, Bronx, and Utica Av/Eastern Pkwy, Brooklyn, running express in Manhattan and Brooklyn. During late night and early morning hours, trains runs local in Manhattan and Brooklyn, and extends beyond Utica Av to New Lots/Livonia Avs, Brooklyn.",http://web.mta.info/nyct/service/pdf/t4cur.pdf,00933C,
    """
    filename = _get_filename('routes')
    route_data = _get_file_data(filename)
    return {row['route_id']: row for row in route_data}


def get_trips():
    """
    route_id,trip_id,service_id,trip_headsign,direction_id,shape_id
    2,A20140608SAT_000250_2..S08R,A20140608SAT,FLATBUSH AV - BROOKLYN COLLEGE,1,2..S08R
    3,A20140608SAT_000300_3..S42R,A20140608SAT,TIMES SQ - 42 ST,1,3..S42R
    4,A20140608SAT_000400_4..S01R,A20140608SAT,NEW LOTS AV,1,4..S01R
    1,A20140608SAT_000650_1..S02R,A20140608SAT,SOUTH FERRY LOOP,1,
    6,A20140608SAT_000700_6..S01R,A20140608SAT,BROOKLYN BRIDGE - CITY HALL,1,6..S01R
    """
    filename = _get_filename('trips')
    trip_data = _get_file_data(filename)
    return {row['trip_id']: row for row in trip_data}


def get_stops():
    """
    stop_id,stop_name,stop_lat,stop_lon,location_type,parent_station
    101,Van Cortlandt Park - 242 St,40.889248,-73.898583,1,
    101N,Van Cortlandt Park - 242 St,40.889248,-73.898583,,101
    101S,Van Cortlandt Park - 242 St,40.889248,-73.898583,,101
    103,238 St,40.884667,-73.900870,1,
    103N,238 St,40.884667,-73.900870,,103
    103S,238 St,40.884667,-73.900870,,103
    104,231 St,40.878856,-73.904834,1,
    """
    filename = _get_filename('stops')
    stop_data = _get_file_data(filename)
    return {row['stop_id']: row for row in stop_data}


def get_stop_times():
    """
    trip_id,stop_id,arrival_time,departure_time,stop_sequence,pickup_type,drop_off_type
    A20140608SAT_000250_2..S08R,201S,00:02:30,00:02:30,1,,
    A20140608SAT_000250_2..S08R,204S,00:04:00,00:04:00,2,,
    A20140608SAT_000250_2..S08R,205S,00:05:30,00:05:30,3,,
    A20140608SAT_000250_2..S08R,206S,00:06:30,00:06:30,4,,
    A20140608SAT_000250_2..S08R,207S,00:07:30,00:07:30,5,,
    A20140608SAT_000250_2..S08R,208S,00:09:00,00:09:00,6,,
    A20140608SAT_000250_2..S08R,209S,00:10:30,00:10:30,7,,
    A20140608SAT_000250_2..S08R,210S,00:11:30,00:11:30,8,,
    """
    filename = _get_filename('stop_times')
    return _get_file_data(filename)


def main():
    """Getting all stops for each subway line

    Example from: http://stackoverflow.com/questions/25634764/scrape-mta-subway-data

    Solved by connecting:
    routes -> trips, by route_id -> stop times, by trip_id -> stops, by stop_id
    """
    routes = get_routes()
    trips = get_trips()
    stop_times = get_stop_times()
    stops = get_stops()
    for route_id, route in routes.iteritems():
        print "%s / %s" % (route_id, route['route_long_name'])
        route_trips = filter(lambda trip: trip['route_id'] == route_id, trips.itervalues())
        route_trip_ids = set([trip['trip_id'] for trip in route_trips])

        # To get a list of names per stop:
        stop_names = set()
        for row in stop_times:
            if row['trip_id'] not in route_trip_ids:
                continue
            stop = stops[row['stop_id']]
            if stop['stop_name'] not in stop_names:
                print "\t%s" % stop['stop_name']
                stop_names.add(stop['stop_name'])

        # To get unique stop ids and counts per stop_id:
        # stop_counts = {}
        # for row in stop_times:
        #     if row['trip_id'] not in route_trip_ids:
        #         continue
        #     if row['stop_id'] not in stop_counts:
        #         stop_counts[row['stop_id']] = 0
        #     stop_counts[row['stop_id']] += 1
        # for stop_id, count in stop_counts.iteritems():
        #     print "\t%s / %s (%s stops)" % (stop_id,
        #                                     stops[stop_id]['stop_name'],
        #                                     count)

        print ""


if __name__ == '__main__':
    main()
