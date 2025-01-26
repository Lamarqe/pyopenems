# Installation

    $ pip install pyopenems

# CLI
## get list of all edges, connected to the UI/backend

    $ python -m openems get-edge-list 
    0
    1
    3
    4
    5
    6

## get list of all components for one edge

    $ python -m openems get-component-list 0
    _sum
    evcs0
    scheduler0
    battery0
    ess0
    ....
    
### get all edge config parameters and values for one component (of one edge)

    $ python -m openems get-component-config 0 _sum
    {'alias': 'Core.Sum', 'factoryId': 'Core.Sum', 'properties': {'_lastChangeAt': '2025-01-13T00:23', '_lastChangeBy': 'Internal: ExtremeEverValues', 'consumptionMaxActivePower': 15860, 'essMaxDischargePower': 4515, 'essMinDischargePower': -4842, 'gridMaxActivePower': 12727, 'gridMinActivePower': -8045, 'ignoreStateComponents': [''], 'productionMaxActivePower': 10685}}
