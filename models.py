from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    is_done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
