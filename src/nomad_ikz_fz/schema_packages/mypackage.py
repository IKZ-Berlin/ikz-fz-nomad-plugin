from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

import numpy as np
from nomad.config import config
from nomad.datamodel.data import ArchiveSection, EntryData, EntryDataCategory, Schema
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    ELNComponentEnum,
    SectionProperties,
)
from nomad.datamodel.metainfo.basesections import (
    CompositeSystem,
    CompositeSystemReference,
    Process,
    System,
)
from nomad.metainfo import Datetime, MEnum, Quantity, SchemaPackage, Section, SubSection
from nomad.metainfo.metainfo import Category
from structlog.stdlib import BoundLogger

configuration = config.get_plugin_entry_point('nomad_ikz_fz.schema_packages:mypackage')

m_package = SchemaPackage()


class IKZFZCategory(EntryDataCategory):
    m_def = Category(label='IKZ Fz', categories=[EntryDataCategory])


class MySchema(Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        logger.info('MySchema.normalize', parameter=configuration.parameter)
        self.message = f'Hello {self.name}!'


class FzMaterial(System, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FzMaterial` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Feed_rod(CompositeSystem, FzMaterial, EntryData, ArchiveSection):  # FzMaterial
    """
    Class autogenerated from yaml schema.
    """

    # m_def = Section(
    #     a_display={
    #         'order': [
    #             'name',
    #             'lab_id',
    #             'datetime',
    #             'diameter',
    #             'length',
    #             'weight',
    #             'rod_surface',
    #             'rod_pretreatment',
    #             'rod_angle',
    #             'chemical_formula',
    #             'storage_location',
    #             'sharpened',
    #             'etched',
    #             'status',
    #             'description',
    #         ]
    #     },
    # )

    m_def = Section(
        categories=[IKZFZCategory],
        label='Fz Feed Rod',
        # links=[],
        a_eln=ELNAnnotation(
            properties=SectionProperties(
                order=[
                    'name',
                    'lab_id',
                    'datetime',
                    'supplier',
                    'furnace_type_compatibility',
                    'feed_rod_resistivity',
                    'diameter',
                    'length',
                    #'weight',
                    'rod_surface',
                    'rod_pretreatment',
                    'rod_angle',
                    # 'chemical_formula', not needed or default value = Si
                    'storage_location',
                    'sharpened',
                    'etched',
                    'etching_location',
                    'etch_date',
                    'status',
                    'description',
                ],
            ),
            lane_width='800px',
        ),
    )

    supplier = Quantity(
        type=MEnum(['Wacker', 'ASIMI', 'REC', 'other']),
        description='feed rod material options',
        a_eln={'component': 'EnumEditQuantity'},
    )
    diameter = Quantity(
        type=MEnum(['100 mm', '126 - 130 mm', 'other']),
        description='diameter of feed rod',
        a_eln={
            'component': 'EnumEditQuantity',
        },
        # unit='mm',
    )
    length = Quantity(
        type=np.float64,
        description='length of feed rod',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='mm',
    )
    # weight = Quantity(
    #     type=np.float64,
    #     description='weight of feed rod',
    #     a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'kg'},
    #     unit='kg',
    # )
    rod_surface = Quantity(
        type=MEnum(['round grinded', 'raw']),
        description='rod surface condition',
        a_eln={'component': 'EnumEditQuantity'},
    )
    # rod_pretreatment = Quantity(
    #     type=MEnum(['etched', 'raw', 'US cleaned']),
    #     description='rod pretreatment',
    #     a_eln={'component': 'EnumEditQuantity'},
    # )
    rod_angle = Quantity(
        type=np.float64,
        description='angle of feed rod',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'deg'},
        unit='deg',
    )
    # chemical_formula = Quantity(
    #     type=str,
    #     description='chemical formula of feed rod',
    #     a_eln={'component': 'StringEditQuantity'},
    # )
    status = Quantity(
        type=MEnum(
            [
                'needs to be etched',
                'ready to use',
                'sent to etching',
                'needs to be sharpened',
            ]
        ),
        description='rod pretreatment',
        a_eln={},
    )
    sharpened = Quantity(
        type=bool,
        description='tick if rod is sharpened',
        default=False,
        a_eln={'component': 'BoolEditQuantity'},
    )
    etched = Quantity(
        type=bool,
        default=False,
        description='tick if rod is etched',
        a_eln={'component': 'BoolEditQuantity'},
    )
    etch_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    etching_location = Quantity(
        type=MEnum(
            [
                'in house',
                'company',
            ]
        ),
        description='tick if rod was etched at IKZ',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    # add a quantity to choose
    furnace_type_compatibility = Quantity(
        type=MEnum(
            [
                'PVA TePla',
                'Steremat',
            ]
        ),
        description='Furnace rod holder compatibility',
        a_eln={'component': 'EnumEditQuantity'},
    )
    feed_rod_resistivity = Quantity(
        type=MEnum(
            [
                'standard resistivity',
                'high resistivity',
            ]
        ),
        description='resistivity of the feed rod',
        a_eln={'component': 'EnumEditQuantity'},
    )
    # ready_to_use = Quantity(
    #    type=bool,
    #    description='tick if rod is ready to use',
    #    a_eln={'component': 'BoolEditQuantity'},
    # )
    storage_location = Quantity(
        type=str,
        description='location of feed rod',
        a_eln={
            'component': 'EnumEditQuantity',
            'props': {
                'suggestions': [
                    'Wagen FZ-Halle',
                    'Keller',
                    'FZ Halle Regal',
                    'Kiste Keller',
                    'Kiste Glaspasage',
                    'Sent to Etching',
                    'other - add in comment where!',
                ],
            },
        },
    )
    description = Quantity(
        type=str,
        description='description of feed rod',
        a_eln={'component': 'RichTextEditQuantity', 'label': 'comment'},
        # a_eln=ELNAnnotation(label='comment',
        # ,
    )
    lab_id = Quantity(
        type=str,
        description='lab id of feed rod, it takes the ID from the name of the feed rod entry',
        # a_eln={'component': 'StringEditQuantity'},
        a_eln=ELNAnnotation(
            label='ID',
        ),
    )
    name = Quantity(
        type=str,
        description='name of feed rod which also represents its ID ',
        a_eln={'component': 'StringEditQuantity'},
    )

    def normalize(self, archive, logger: BoundLogger) -> None:
        """
        The normalizer for the `Feed_rod` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super(Feed_rod, self).normalize(archive, logger)
        if self.name is not None:
            self.lab_id = self.name
        # if self.length and self.diameter:
        #     density = (2.33 * ureg('kilogram')) / (1000000 * ureg('millimeter**3'))
        #     self.weight = (np.pi * ((self.diameter / 2) ** 2) * self.length) * (density)
        if self.etched == True:
            self.sharpened = True
        if self.storage_location == 'Sent to Etching':
            self.sharpened = True
            self.etched = False

        if self.sharpened == False and self.etched == False:
            self.status = 'needs to be sharpened'
            self.ready_to_use = False
        elif (
            self.sharpened == True
            and self.etched == False
            and self.storage_location != 'Sent to Etching'
        ):
            self.status = 'needs to be etched'
            self.ready_to_use = False
        elif (
            self.sharpened == True
            and self.etched == False
            and self.storage_location == 'Sent to Etching'
        ):
            self.status = 'sent to etching'
            self.ready_to_use = False
        elif self.sharpened == True and self.etched == True:
            self.status = 'ready to use'
            self.ready_to_use = True
        # else:
        #    self.status = 'wurde zum Ätzen geschickt'
        #    self.ready_to_use = False
        # self.figures.append(
        #     PlotlyFigure(
        #         figure=(
        #             go.Figure(
        #                 data=[
        #                     go.Table(
        #                         header=dict(values=['length', 'diameter']),
        #                         cells=dict(values=[[self.length], [self.diameter]]),
        #                     )
        #                 ]
        #             )
        #         ).to_plotly_json()
        #     )
        # )


class Seed(CompositeSystem, FzMaterial, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        categories=[IKZFZCategory],
        label='Fz Seed',
    )
    orientation = Quantity(
        type=MEnum(['100', '111', 'Other']),
        description='seed orientation',
        a_eln={'component': 'EnumEditQuantity'},
    )
    # chemical_formula = Quantity(
    #     type=str,
    #     description='chemical formula of feed rod',
    #     a_eln={'component': 'StringEditQuantity'},
    # )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Seed` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FzCrystal(CompositeSystem, FzMaterial, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        categories=[IKZFZCategory],
        label='Fz Crystal',
        a_eln=ELNAnnotation(
            properties=SectionProperties(
                order=[
                    'name',
                    #'lab_id',
                    'datetime',
                    'fz_furnace',
                    'orientation',
                    'diameter',
                    'length',
                    'weight',
                    'resistivity',
                    'doping_type',
                    'location',
                    # 'chemical_formula', not needed or default value = Si
                    'status',
                    'description',
                ],
            ),
            lane_width='800px',
        ),
    )
    name = Quantity(
        type=str,
        description='name of crystal',
        a_eln={'component': 'StringEditQuantity'},
    )
    lab_id = Quantity(
        type=str,
        description='lab id of crystal',  # it takes the ID from the name of the crystal entry
        # a_eln={'component': 'StringEditQuantity'},
    )
    # description_crystal = Quantity(
    #     type=str,
    #     description='description of crystal',
    #     a_eln={'component': 'StringEditQuantity'},
    # )
    status = Quantity(
        type=str,
        description='status of crystal',
        a_eln={'component': 'StringEditQuantity'},
    )
    fz_furnace = Quantity(
        type=str,
        description='fz furnace used to grow this crystal',
        a_eln={'component': 'StringEditQuantity'},
    )
    # fz_furnace = (
    #     Quantity(
    #         type=str,
    #         description='fz furnace used to grow this crystal',
    #         a_eln={
    #             'component': 'EnumEditQuantity',
    #             'props': {
    #                 'suggestions': [
    #                     '1505/1',
    #                     '1505/2',
    #                     '1520',
    #                     'FZ30',
    #                 ]
    #             },
    #         },
    #     ),
    # )

    diameter = Quantity(
        type=np.float64,
        description='diameter of crystal',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='mm',
    )
    length = Quantity(
        type=np.float64,
        description='length of crystal',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='mm',
    )
    orientation = Quantity(
        type=str,
        description='orientation of crystal',
        a_eln={
            'component': 'EnumEditQuantity',
            'props': {'suggestions': ['<100>', '<111>', 'other']},
        },
    )
    resistivity = Quantity(
        type=np.float64,
        description='resistance of crystal',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm cm'},
        unit='ohm cm',
    )
    doping_type = Quantity(
        type=MEnum(['p', 'n', 'other']),
        description='doping type of the crystal',
        a_eln={'component': 'EnumEditQuantity'},
    )
    location = Quantity(
        type=str,
        description='location of crystal',
        a_eln={
            'component': 'EnumEditQuantity',
            'props': {
                'suggestions': [
                    'Schrank Büro R. 124',
                    'Schrank zw. FZ 20 und CZ',
                    'Schrank zw. FZ 20 und CZ, weiße Plastikkiste',
                    'Schrank hinter FZ 30',
                    'Schrank hinter FZ 30, weiße Pappkiste',
                    'Schrank hinter FZ 30, weiße Plastikkiste',
                    'Schrank hinter FZ 30, Rote Kiste',
                    'Rollwagen (Siltronic 4V), Züchtungshalle',
                    'Rollwagen FZ 1520',
                    'Rollwagen mitte, Züchtungshalle',
                    'Schrank hinter EKZ 200',
                    'Kristallregal Züchtungshalle',
                    'other - add in comment where!',
                ]
            },
        },
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FzCrystal` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)
        if self.name is not None:
            self.lab_id = self.name


class Gas(CompositeSystem, FzMaterial, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln=None,
        categories=[IKZFZCategory],
        label='Fz Gas',
    )
    substance = Quantity(
        type=str,
        description='name of gas',
        a_eln={'component': 'StringEditQuantity'},
    )
    gas_source = Quantity(
        type=MEnum(['from bottle', 'from pipeline', 'Other']),
        description='source type of gas',
        a_eln={'component': 'EnumEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Gas` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Dopant(CompositeSystem, FzMaterial, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln=None,
        categories=[IKZFZCategory],
        label='Fz Dopant',
    )
    doping_substance = Quantity(
        type=MEnum(['PH3', 'B2H6', 'CH4', 'Other']),
        description='name/type of dopant',
        a_eln={'component': 'EnumEditQuantity'},
    )
    doping_source_type = Quantity(
        type=MEnum(['from bottle', 'from pipeline', 'Other']),
        description='source type of dopant',
        a_eln={'component': 'EnumEditQuantity'},
    )


class Fz_Materials(CompositeSystemReference, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    reference = Quantity(
        type=FzMaterial,
        a_eln={'component': 'ReferenceEditQuantity'},
        a_label='Fz Material Reference',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Fz_Materials` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FzGrowthProcess(Process, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        categories=[IKZFZCategory],
        label='Fz Growth Process',
    )
    # instruments = SubSection(
    #     section_def=Instruments,
    # )
    FzMaterials = SubSection(
        section_def=Fz_Materials,
        repeats=True,
    )
    # steps = SubSection(
    #     section_def=FzGrowthStep,
    #     repeats=True,
    # )
    # samples = SubSection(
    #     section_def=FzCrystal,
    #     repeats=True,
    # )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FzGrowthProcess` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


m_package.__init_metainfo__()
