from pydantic import BaseModel, RootModel
from typing import Dict, Literal, Optional

class ColumnConfig(BaseModel):
    data_type: Literal["str", "int", "float"]
    data_size: Optional[str] = ""
    randomize: bool
    
class ProfileConfig(BaseModel):
    output_filename: str
    format: Literal["csv", "excel", "json"]
    columns: list[Dict[str, ColumnConfig]]

class ConfigModel(BaseModel):
    profiles: list[Dict[str, ProfileConfig]]