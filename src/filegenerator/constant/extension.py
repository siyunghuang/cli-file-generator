from enum import Enum

class FileFormat(str, Enum):
    FILE_FORMAT_CSV = "csv"
    FILE_FORMAT_XLS = "xls"
    FILE_FORMAT_TXT = "txt"
    FILE_FORMAT_XLSX = "xlsx"