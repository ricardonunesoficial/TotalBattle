# parser.py
import re
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Chest:
    chest_name: str
    source: str
    level: int | None
    from_player: str | None
    captured_at: datetime

@dataclass
class Report:
    report_type: str
    description: str
    player: str | None
    created_at: datetime

def parse_chest_block(text: str) -> list[Chest]:
    """
    Recebe texto OCR de uma secção de baús, devolve lista de Chest.
    Exemplo esperado de linhas:
    'Barbarian Chest'
    'From: Godfather'
    'Source: Level 15 Crypt'
    """
    chests: list[Chest] = []

    blocks = text.split("\n\n")  # separar por blocos em branco
    now = datetime.utcnow()

    for block in blocks:
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines:
            continue

        chest_name = lines[0]
        from_player = None
        source = ""
        level = None

        for line in lines[1:]:
            if line.lower().startswith("from"):
                # From: Godfather
                _, _, name = line.partition(":")
                from_player = name.strip()
            elif "crypt" in line.lower() or "chest" in line.lower() or "source" in line.lower():
                # Source: Level 15 Crypt
                m_level = re.search(r"[Ll]evel\s+(\d+)", line)
                if m_level:
                    level = int(m_level.group(1))
                source = line.strip()

        chests.append(
            Chest(
                chest_name=chest_name,
                source=source,
                level=level,
                from_player=from_player,
                captured_at=now,
            )
        )

    return chests

def parse_reports_block(text: str) -> list[Report]:
    # Por agora, parse mais simples; podes sofisticar depois.
    reports: list[Report] = []
    now = datetime.utcnow()
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    for line in lines:
        # heurística: tipo entre [] no começo
        m = re.match(r"\[(.+?)\]\s*(.+)", line)
        if m:
            r_type = m.group(1)
            desc = m.group(2)
        else:
            r_type = "generic"
            desc = line
        reports.append(
            Report(
                report_type=r_type,
                description=desc,
                player=None,
                created_at=now,
            )
        )
    return reports
