import yaml
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Columns,
    FilterMenu,
    FilterMenus,
    Filters,
    #SearchQuantities
)

schema = 'nomad_ikz_fz.schema_packages.mypackage.Feedstock'

feedstockapp = AppEntryPoint(
    name='FzFeedstockApp',
    description='App for searching feedstock material.',
    app=App(
        label='FzFeedstockApp',
        path='fzfeedstockapp',
        category='Fz Crystal Growth',
        description="""
        Explore feedstock material.
        """,
        # search_quantities=SearchQuantities(
        #     include=[
        #         f'*#{schema}',
        #     ],
        # ),
        columns=[
            Column(
                search_quantity=f'data.name#{schema}',
                selected=True,
                #label='Sputtering ID',
            ),
            Column(
                search_quantity=f'data.grain_size#{schema}',
                selected=True,
                label='Grain size',
                unit='nm',
            ),
            Column(
                search_quantity=f'data.description#{schema}',
                selected=True,
                label='Description',
            ),
            Column(
                search_quantity=f'data.storage_location#{schema}',
                selected=True,
                label='Storage location',
            ),
            Column(
                search_quantity='upload_create_time',
                selected=False,
            ),
            Column(
                search_quantity='last_processing_time',
                selected=True,
            ),
        ],
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
            include=['*#nomad_ikz_fz.schema_packages.mypackage.Feedstock'],
        ),
        filters_locked={
            'entry_type': 'Feedstock',
        },
    )
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
                'last_processing_time',
            ],
            options={
                #'entry_id': Column(),
                'data.name#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.length#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(
                    unit='cm'
                ),
                'data.diameter_category#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(
                ),
                'data.status#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.storage_location#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(  # noqa: E501
                ),
                'data.feed_rod_resistivity#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),  # noqa: E501
                'data.description#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),  # noqa: E501
                'upload_create_time': Column(),
                'last_processing_time': Column(),
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
    unit: cm
  title: Feed Length
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
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(  # noqa: E501
                    unit='mm',
                ),
                'data.status#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),  # noqa: E501
                'data.location#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),  # noqa: E501
                'data.resistivity_measurement.resistivity#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(  # noqa: E501
                    unit='kohm cm', format={'decimals': 2, 'mode': 'scientific'}
                ),
                'data.description#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),  # noqa: E501
                'data.process_date#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),  # noqa: E501
                'data.fz_furnace#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),  # noqa: E501
                'data.orientation#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),  # noqa: E501
                'data.doping_type#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),  # noqa: E501
                'upload_create_time': Column(),
                'last_processing_time': Column(),
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
  title: Crystal Length
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
  title: Feed Diameter
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
  title: Resistivity
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
  title: Crystal Length vs. Diameter
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
  title: Process Date
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

"""  # noqa: E501
            )
        },
    ),
)

fzinstrumentapp = AppEntryPoint(
    name='FzInstrumentApp',
    description='Explore Fz instruments and parts.',
    app=App(
        label='FzInstrumentApp',
        path='fzinstrumentapp',
        category='Fz Crystal Growth',
        columns=Columns(
            selected=[
               
                'data.name#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart',
                'data.category#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart',
                'data.instrument_type#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart',
                'data.cabinet#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart',
                'data.shelf#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart',
            ],
            options={
                #'entry_id': Column(),
                'data.name#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart': Column(),  # noqa: E501
                'data.category#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart': Column(),  # noqa: E501
                'data.instrument_type#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart': Column(),  # noqa: E501
                'data.cabinet#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart': Column(),  # noqa: E501
                'data.shelf#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart': Column(),  # noqa: E501
                'upload_create_time': Column(),
                'last_processing_time': Column(),
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
            include=['*#nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart'],
        ),
        filters_locked={
            'section_defs.definition_qualified_name': [
                'nomad_ikz_fz.schema_packages.mypackage.FzInstrumentPart',
                #'nomad_ikz_fz.schema_packages.mypackage.Coil',
            ],
        },
    ),
)
