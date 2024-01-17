from zipfile import ZipFile
import polars as pl


FILE_PATH = 'student-demographics-online-education-dataoulad.zip'
DATA_FILES = [
    'assessments',
    'courses',
    'studentAssessment',
    'studentInfo',
    'studentRegistration',
    'studentVle',
    'vle'
]


def get_data():
    data = {}
    for file in DATA_FILES:
        data[file] = pl.read_csv(ZipFile(FILE_PATH).open(f'{file}.csv'))
    return data
