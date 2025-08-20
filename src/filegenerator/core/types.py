from pydantic import BaseModel, EmailStr

class FileTypes(BaseModel):
    name: str
    description: str
    convention: str
    settings: str

class SettingTypes(BaseModel):
    type: str
    settings: str
    command: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

available_file_types = [
    FileTypes(
        name="default", 
        settings="filegen v <Setting Files>", 
        description="Custom File", 
        convention="<Custom>.<FileExtension>"
        ),
    FileTypes(
        name="auto_debit", 
        settings="filegen v <Setting Files>", 
        description="AutoDebit Bulk File", 
        convention="<Unique ID>_<Prefix>_<YYYYMMDD>_<RunningNo>.<FileExtension>"
        ),
    FileTypes(
        name="consent", 
        settings="filegen v <Setting Files>", 
        description="Consent Bulk File", 
        convention="CRB_<Unique ID>_<YYYYMMDD>_<RunningNo>.<FileExtension>"
        ), 
]

available_settings = [
    SettingTypes(
        type="Custom Setting",
        settings="<Number of columns> etc.",
        command="filegen v -d"
    )
]