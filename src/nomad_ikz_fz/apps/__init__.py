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
                #'entry_id',
                'data.name#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.length#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.status#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.storage_location#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.resistivity#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                'data.description#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
            ],
            options={
                #'entry_id': Column(),
                'data.name#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
                'data.length#nomad_ikz_fz.schema_packages.mypackage.Feed_rod': Column(),
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
            'widgets': [
                {
                    'type': 'terms',
                    'scale': 'linear',
                    'quantity': 'data.status#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 4, 'w': 5, 'y': 0, 'x': 0},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                    },
                },
                {
                    'type': 'histogram',
                    'autorange': False,
                    'nbins': 30,
                    'scale': 'linear',
                    'quantity': 'data.length#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 4, 'w': 5, 'y': 0, 'x': 5},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                    },
                },
                {
                    'type': 'histogram',
                    'autorange': False,
                    'nbins': 30,
                    'scale': 'linear',
                    'quantity': 'data.diameter#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 4, 'w': 8, 'y': 0, 'x': 10},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 3,
                            'w': 8,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                    },
                },
                {
                    'type': 'terms',
                    'scale': 'linear',
                    'quantity': 'data.storage_location#nomad_ikz_fz.schema_packages.mypackage.Feed_rod',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 4, 'w': 5, 'y': 0, 'x': 18},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 9,
                            'w': 6,
                            'y': 0,
                            'x': 10,  #'.inf',
                        },
                    },
                },
            ]
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
        columns=Columns(
            selected=[
                #'entry_id',
                'data.name#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.length#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.status#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.location#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.resistivity#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.description#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.datetime#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'fz_furnace#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'data.orientation#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
                'doping_type#nomad_ikz_fz.schema_packages.mypackage.FzCrystal',
            ],
            options={
                #'entry_id': Column(),
                'data.name#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.length#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.diameter#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.status#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.location#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.resistivity#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.description#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.datetime#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'fz_furnace#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'data.orientation#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
                'doping_type#nomad_ikz_fz.schema_packages.mypackage.FzCrystal': Column(),
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
    ),
)
