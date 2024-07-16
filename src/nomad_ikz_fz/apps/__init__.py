import yaml
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Columns,
    FilterMenu,
    FilterMenus,
    Filters,
)

myapp = AppEntryPoint(
    name='FzFeedRodApp',
    description='Explore Fz data.',
    app=App(
        label='FzFeedRodApp',
        path='fzapp',
        category='Fz Crystal Growth',
        columns=Columns(
            selected=[
                #'entry_id', name, diamater, length, status resistivity, location
                'data.name#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.length#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.status#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.resistivity#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.storage_location#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.description#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
            ],
            options={
                #'entry_id': Column(),
                'data.name#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.length#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(
                    unit='mm'
                ),
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.status#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.storage_location#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.feed_rod_resistivity#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.description#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
                'eln': FilterMenu(label='Electronic Lab Notebook'),
                'custom_quantities': FilterMenu(label='User Defined Quantities'),
                'author': FilterMenu(label='Author / Origin / Dataset'),
                'metadata': FilterMenu(label='Visibility / IDs / Schema'),
            }
        ),
        filters=Filters(
            include=['*#nomad_ikz_fz.schema_packages.mypackage.Feed_rod'],
        ),
        filters_locked={
            'section_defs.definition_qualified_name': [
                'nomad_ikz_fz.schema_packages.mypackage.Feed_rod'
            ],
        },
        dashboard={
            'widgets': yaml.safe_load(
                """
- type: terms
  showinput: false
  scale: linear
  quantity: data.status#nomad_ikz_fz.schema_packages.mypackage.Feed_rod
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 3
      w: 7
      y: 3
      x: 11
    xl:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 0
      x: 8
    lg:
      minH: 3
      minW: 3
      h: 3
      w: 5
      y: 4
      x: 11
    md:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 0
      x: 6
    sm:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 0
      x: 0
- type: histogram
  showinput: true
  autorange: false
  nbins: 30
  scale: linear
  x:
    quantity: data.length#nomad_ikz_fz.schema_packages.mypackage.Feed_rod
    unit: mm
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 9
      w: 11
      y: 0
      x: 0
    xl:
      minH: 3
      minW: 3
      h: 6
      w: 8
      y: 0
      x: 0
    lg:
      minH: 3
      minW: 3
      h: 4
      w: 16
      y: 0
      x: 0
    md:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 3
      x: 6
    sm:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 6
      x: 0
- type: terms
  showinput: false
  scale: linear
  quantity: data.diameter#nomad_ikz_fz.schema_packages.mypackage.Feed_rod
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 3
      w: 7
      y: 0
      x: 11
    xl:
      minH: 3
      minW: 3
      h: 3
      w: 5
      y: 0
      x: 14
    lg:
      minH: 3
      minW: 3
      h: 3
      w: 5
      y: 4
      x: 0
    md:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 3
      x: 0
    sm:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 3
      x: 0
- type: terms
  showinput: false
  scale: linear
  quantity: data.storage_location#nomad_ikz_fz.schema_packages.mypackage.Feed_rod
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 9
      w: 5
      y: 0
      x: 18
    xl:
      minH: 3
      minW: 3
      h: 6
      w: 6
      y: 0
      x: 19
    lg:
      minH: 3
      minW: 3
      h: 7
      w: 5
      y: 0
      x: 16
    md:
      minH: 3
      minW: 3
      h: 6
      w: 6
      y: 0
      x: 12
    sm:
      minH: 3
      minW: 3
      h: 6
      w: 6
      y: 3
      x: 6
- type: terms
  showinput: false
  scale: linear
  quantity: data.feed_rod_resistivity#nomad_ikz_fz.schema_packages.mypackage.Feed_rod
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 3
      w: 7
      y: 6
      x: 11
    xl:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 3
      x: 8
    lg:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 4
      x: 5
    md:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 0
      x: 0
    sm:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 0
      x: 6


                """
            )
        },
    ),
)


fzcrysapp = AppEntryPoint(
    name='FzCrystalApp',
    description='Explore Fz crystals.',
    app=App(
        label='FzCrystalApp',
        path='fzcrysapp',
        category='Fz Crystal Growth',
        pagination={'page_size': 100},
        columns=Columns(
            selected=[
                #'entry_id', crystals: name, furnace, diameter, length, status, orientation, resistivity, doping type,  location, datetime, description
                'data.name#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.fz_furnace#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.length#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.status#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.orientation#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.resistivity_measurement.resistivity#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.doping_type#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.location#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.process_date#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.description#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
            ],
            options={
                #'entry_id': Column(),
                'data.name#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.length#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(
                    unit='mm',
                ),
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(
                    unit='mm',
                ),
                'data.status#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.location#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.resistivity_measurement.resistivity#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(
                    unit='kohm cm', format={'decimals': 2, 'mode': 'scientific'}
                ),
                'data.description#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.process_date#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.fz_furnace#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.orientation#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.doping_type#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
                'eln': FilterMenu(label='Electronic Lab Notebook'),
                'custom_quantities': FilterMenu(label='User Defined Quantities'),
                'author': FilterMenu(label='Author / Origin / Dataset'),
                'metadata': FilterMenu(label='Visibility / IDs / Schema'),
            }
        ),
        filters=Filters(
            include=['*#nomad_ikz_fz.schema_packages.mypackage.FzCrystal'],
        ),
        filters_locked={
            'section_defs.definition_qualified_name': [
                'nomad_ikz_fz.schema_packages.mypackage.FzCrystal'
            ],
        },
        dashboard={
            'widgets': yaml.safe_load(
                """
- type: terms
  showinput: false
  scale: linear
  quantity: data.fz_furnace#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 7
      w: 6
      y: 0
      x: 0
    xl:
      minH: 3
      minW: 3
      h: 7
      w: 4
      y: 0
      x: 0
    lg:
      minH: 3
      minW: 3
      h: 7
      w: 4
      y: 0
      x: 0
    md:
      minH: 3
      minW: 3
      h: 6
      w: 4
      y: 0
      x: 0
    sm:
      minH: 3
      minW: 3
      h: 7
      w: 6
      y: 0
      x: 0
- type: terms
  showinput: false
  scale: linear
  quantity: data.doping_type#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 4
      w: 6
      y: 3
      x: 12
    xl:
      minH: 3
      minW: 3
      h: 4
      w: 4
      y: 3
      x: 8
    lg:
      minH: 3
      minW: 3
      h: 4
      w: 4
      y: 0
      x: 8
    md:
      minH: 3
      minW: 3
      h: 3
      w: 4
      y: 6
      x: 0
    sm:
      minH: 3
      minW: 3
      h: 4
      w: 6
      y: 7
      x: 0
- type: terms
  showinput: false
  scale: linear
  quantity: data.orientation#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  title: ""
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 7
      w: 6
      y: 0
      x: 6
    xl:
      minH: 3
      minW: 3
      h: 7
      w: 4
      y: 0
      x: 4
    lg:
      minH: 3
      minW: 3
      h: 7
      w: 4
      y: 0
      x: 4
    md:
      minH: 3
      minW: 3
      h: 6
      w: 4
      y: 0
      x: 4
    sm:
      minH: 3
      minW: 3
      h: 7
      w: 6
      y: 0
      x: 6
- type: histogram
  showinput: true
  autorange: false
  nbins: 30
  scale: linear
  x:
    unit: mm
    quantity: data.length#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 4
      w: 9
      y: 7
      x: 9
    xl:
      minH: 3
      minW: 3
      h: 5
      w: 7
      y: 7
      x: 8
    lg:
      minH: 3
      minW: 3
      h: 4
      w: 5
      y: 7
      x: 7
    md:
      minH: 3
      minW: 3
      h: 3
      w: 5
      y: 3
      x: 8
    sm:
      minH: 3
      minW: 3
      h: 4
      w: 6
      y: 15
      x: 0
- type: histogram
  showinput: true
  autorange: false
  nbins: 30
  scale: linear
  x:
    unit: mm
    quantity: data.diameter#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 4
      w: 9
      y: 7
      x: 18
    xl:
      minH: 3
      minW: 3
      h: 5
      w: 7
      y: 7
      x: 15
    lg:
      minH: 3
      minW: 3
      h: 4
      w: 6
      y: 7
      x: 12
    md:
      minH: 3
      minW: 3
      h: 3
      w: 5
      y: 3
      x: 13
    sm:
      minH: 3
      minW: 3
      h: 4
      w: 6
      y: 15
      x: 6
- type: histogram
  showinput: true
  autorange: false
  nbins: 30
  scale: 1/2
  x:
    unit: kohm cm
    quantity: data.resistivity_measurement.resistivity#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 4
      w: 9
      y: 7
      x: 27
    xl:
      minH: 3
      minW: 3
      h: 5
      w: 8
      y: 7
      x: 22
    lg:
      minH: 3
      minW: 3
      h: 4
      w: 6
      y: 7
      x: 18
    md:
      minH: 3
      minW: 3
      h: 3
      w: 5
      y: 0
      x: 13
    sm:
      minH: 3
      minW: 3
      h: 4
      w: 12
      y: 11
      x: 0
- type: scatterplot
  autorange: true
  size: 1000
  markers:
    color:
      quantity: data.fz_furnace#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  y:
    unit: mm
    quantity: data.length#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  x:
    unit: mm
    quantity: data.diameter#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 7
      w: 18
      y: 0
      x: 18
    xl:
      minH: 3
      minW: 3
      h: 7
      w: 18
      y: 0
      x: 12
    lg:
      minH: 3
      minW: 3
      h: 7
      w: 12
      y: 0
      x: 12
    md:
      minH: 3
      minW: 3
      h: 6
      w: 10
      y: 6
      x: 8
    sm:
      minH: 3
      minW: 3
      h: 7
      w: 12
      y: 19
      x: 0
- type: terms
  showinput: false
  scale: linear
  quantity: data.status#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 3
      w: 6
      y: 0
      x: 12
    xl:
      minH: 3
      minW: 3
      h: 3
      w: 4
      y: 0
      x: 8
    lg:
      minH: 3
      minW: 3
      h: 3
      w: 4
      y: 4
      x: 8
    md:
      minH: 3
      minW: 3
      h: 3
      w: 4
      y: 6
      x: 4
    sm:
      minH: 3
      minW: 3
      h: 4
      w: 6
      y: 7
      x: 6
- type: histogram
  showinput: true
  autorange: false
  nbins: 30
  scale: linear
  x:
    quantity: data.process_date#nomad_ikz_fz.schema_packages.mypackage.FzCrystal
  layout:
    xxl:
      minH: 3
      minW: 3
      h: 4
      w: 9
      y: 7
      x: 0
    xl:
      minH: 3
      minW: 3
      h: 5
      w: 8
      y: 7
      x: 0
    lg:
      minH: 3
      minW: 3
      h: 4
      w: 7
      y: 7
      x: 0
    md:
      minH: 3
      minW: 3
      h: 3
      w: 5
      y: 0
      x: 8
    sm:
      minH: 3
      minW: 3
      h: 3
      w: 8
      y: 26
      x: 0

"""
            )
        },
    ),
)
