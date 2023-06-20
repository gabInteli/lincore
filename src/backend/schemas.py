# Schemas são usados pelo sqlalchemy para o entendimento dos tipos de dados manuseados pelo python e tradução para os diferentes bancos de dados
from datetime import datetime
from typing import List
from pydantic import BaseModel


class ReportBaseSchema(BaseModel):
    id: int | None = None
    projectName: str
    typePlace: int
    operator: str | None = None
    date: datetime | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None
    avg:float

    class Config:
        # mapea os models como objetos relacionais
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class ListReportResponse(BaseModel):
    status: str
    results: int
    report: List[ReportBaseSchema]

