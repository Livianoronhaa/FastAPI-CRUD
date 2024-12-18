# models.py
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Mova essa linha para cá

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

    tarefas = relationship("Tarefa", back_populates="usuario", cascade="all, delete-orphan")

class Projeto(Base):
    __tablename__ = "projetos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text)

    tarefas = relationship("Tarefa", back_populates="projeto", cascade="all, delete-orphan")

class Tarefa(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(String(50), default="pendente")
    projeto_id = Column(Integer, ForeignKey("projetos.id", ondelete="CASCADE"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))

    projeto = relationship("Projeto", back_populates="tarefas")
    usuario = relationship("Usuario", back_populates="tarefas")
