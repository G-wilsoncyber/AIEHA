from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class NodeType(StrEnum):
    """Controlled types for nodes in the AIEHA economic graph."""

    WORKLOAD = "workload"
    MODEL = "model"
    PROVIDER = "provider"
    COMPUTE = "compute"
    ENERGY = "energy"
    TOKEN = "token"
    TOOL = "tool"
    API = "api"
    OUTPUT = "output"
    OUTCOME = "outcome"
    KPI = "kpi"
    VALUE = "value"



class Node(BaseModel):
    """Canonical node in the AIEHA economic graph."""

    id: UUID = Field(default_factory=uuid4)
    type: str
    attributes: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )
