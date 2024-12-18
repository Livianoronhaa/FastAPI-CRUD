from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Modelo Pydantic para representar usuários
class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str

# Simulando um banco de dados em memória
usuarios = []

@router.post("/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    """Cria um novo usuário."""
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": usuario.nome,
        "email": usuario.email,
    }
    usuarios.append(novo_usuario)
    return novo_usuario

@router.get("/", response_model=List[Usuario])
def listar_usuarios():
    """Lista todos os usuários."""
    return usuarios

@router.get("/{usuario_id}", response_model=Usuario)
def consultar_usuario(usuario_id: int):
    """Consulta um usuário pelo ID."""
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=Usuario)
def editar_usuario(usuario_id: int, usuario: Usuario):
    """Edita um usuário existente."""
    usuario_existente = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    # Atualizando as informações do usuário
    usuario_existente["nome"] = usuario.nome
    usuario_existente["email"] = usuario.email
    return usuario_existente

@router.delete("/{usuario_id}")
def excluir_usuario(usuario_id: int):
    """Exclui um usuário pelo ID."""
    usuario_existente = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    usuarios.remove(usuario_existente)  # Exclui o usuário da lista
    return {"message": f"Usuário com ID {usuario_id} excluído com sucesso"}

