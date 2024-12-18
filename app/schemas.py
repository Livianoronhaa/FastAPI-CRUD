from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nome: str
    email: str

class UsuarioResponse(UsuarioBase):
    id: int

        class Config: 
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ProjetoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class ProjetoCreate(ProjetoBase):
    pass

class ProjetoResponse(ProjetoBase):
    id: int

        class Config: 
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class TarefaBase(BaseModel):
    nome: str
    descricao: str
    projeto_id: int
    usuario_id: Optional[int] = None
    status: Optional[str] = "pendente"

class TarefaCreate(TarefaBase):
    pass

class TarefaResponse(TarefaBase):
    id: int

        class Config: 
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True