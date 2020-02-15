import asyncio

import aiohttp
from pygti.auth import Auth
from pygti.const import *
from pygti.gti import *

print("To run the examples, enter your credentials for the GTI API.")
gti_user = input("GTI Username: ")
gti_pass = input("GTI Password: ")


async def main():
    async with aiohttp.ClientSession() as session:

        auth = Auth(session, gti_user, gti_pass)
        gti = GTI(auth)

        print("Example 1: init()")
        ir = await gti.init()
        print(ir)

        print()
        print("Example 2: checkName()")
        cn = await gti.checkName({"theName": {"name": "Wartenau"}})
        print(cn)

        print()
        print("Example 3: getRoute()")
        payload = {
            "version": 37,
            "language": "de",
            "start": {
                "name": "Ritterstraße",
                "city": "Hamburg",
                "combinedName": "Ritterstraße",
                "id": "Master:60904",
                "type": "STATION",
                "coordinate": {"x": 10.046196, "y": 53.567617},
            },
            "dest": {
                "name": "Wartenau",
                "city": "Hamburg",
                "combinedName": "Wartenau",
                "id": "Master:10901",
                "type": "STATION",
                "coordinate": {"x": 10.035515, "y": 53.56478},
            },
            "time": {"date": "heute", "time": "jetzt"},
            "timeIsDeparture": True,
            "realtime": "REALTIME",
        }
        gr = await gti.getRoute(payload)
        print(gr)

        print()
        print("Example 3.1: departureList()")
        dl = await gti.departureList(
            {
                "station": {
                    "name": "Wartenau",
                    "id": "Master:10901",
                    "type": "STATION",
                },
                "time": {"date": "heute", "time": "jetzt"},
                "maxList": 5,
                "maxTimeOffset": 200,
                "useRealtime": True,
            }
        )

        print(dl)

        print()
        print("Example 3.2: departureList(), return filters")
        dl = await gti.departureList(
            {
                "station": {
                    "name": "Wartenau",
                    "id": "Master:10901",
                    "type": "STATION",
                },
                "time": {"date": "heute", "time": "jetzt"},
                "maxList": 5,
                "maxTimeOffset": 200,
                "useRealtime": True,
                "returnFilters": True,
            }
        )
        print(dl)

        print()
        print("Example 10: getIndividualRoute()")
        payload = {
            "starts": [
                {"type": "ADDRESS", "coordinate": {"x": 9.92496, "y": 53.563494}}
            ],
            "dests": [
                {"type": "ADDRESS", "coordinate": {"x": 9.924269, "y": 53.562925}}
            ],
            "maxLength": 10000,
            "serviceType": "BICYCLE",
            "profile": "BICYCLE_NORMAL",
            "speed": "NORMAL",
        }
        indRoute = await gti.getIndividualRoute(payload)
        print(indRoute)

        print()
        print("Example 4: stationInformation()")
        si = await gti.stationInformation(
            {"station": {"name": "Wartenau", "id": "Master:10901", "type": "STATION"}}
        )
        print(si)


asyncio.run(main())
