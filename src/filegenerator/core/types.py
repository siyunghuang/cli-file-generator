from pydantic import BaseModel, EmailStr

class FileTypes(BaseModel):
    name: str
    description: str
    extension: str

available_file_types = [
    FileTypes(name="auto_debit", description="AutoDebit Bulk File", extension="adb.csv"),
    FileTypes(name="consent", description="Consent Bulk File", extension="consent.csv"),
    FileTypes(name="invoice", description="Invoice Template", extension="invoice.xlsx"),
    FileTypes(name="report", description="Monthly Report", extension="report.pdf"),    
]

class User(BaseModel):
    id: int
    name: str
    email: EmailStr