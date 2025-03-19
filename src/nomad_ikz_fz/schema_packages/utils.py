def get_reference(upload_id, entry_id):
    return f'../uploads/{upload_id}/archive/{entry_id}#/data'


def get_entry_id_from_file_name(file_name, archive):
    from nomad.utils import hash

    return hash(archive.metadata.upload_id, file_name)


def create_archive(entity, archive, file_name) -> str:
    import json

    from nomad.datamodel.context import ClientContext

    if isinstance(archive.m_context, ClientContext):
        return None
    if not archive.m_context.raw_path_exists(file_name):
        entity_entry = entity.m_to_dict(with_root_def=True)
        with archive.m_context.raw_file(file_name, 'w') as outfile:
            json.dump({'data': entity_entry}, outfile)
        archive.m_context.process_updated_raw_file(file_name)
    return get_reference(
        archive.metadata.upload_id, get_entry_id_from_file_name(file_name, archive)
    )
from datetime import timedelta

def time_str_to_seconds(time_str):
    """
    Converts a string like "0 days 00:01:00" into total seconds.

    Parameters:
        time_str (str): Input string in format "X days HH:MM:SS"

    Returns:
        float: total seconds
    """
    days_part, time_part = time_str.strip().split(' days ')
    hours, minutes, seconds = map(int, time_part.split(':'))
    days = int(days_part)

    td = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

    return td.total_seconds()

from datetime import timedelta
import pandas as pd

def time_to_seconds(time_input):
    """
    Converts a time string ("0 days 00:01:00") or Timedelta object into total seconds.

    Parameters:
        time_input (str, timedelta, pd.Timedelta): Time input.

    Returns:
        float: total seconds
    """
    if isinstance(time_input, (timedelta, pd.Timedelta)):
        return time_input.total_seconds()

    days_part, time_part = time_input.strip().split(' days ')
    hours, minutes, seconds = map(int, time_part.split(':'))
    days = int(days_part)

    td = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

    return td.total_seconds()