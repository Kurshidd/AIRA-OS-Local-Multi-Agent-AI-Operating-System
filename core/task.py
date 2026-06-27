from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Task:

    user_input: str

    agent: str = "chat"

    tool: str = "none"

    confidence: float = 1.0

    reason: str = ""

    metadata: Dict[str, Any] = field(default_factory=dict)