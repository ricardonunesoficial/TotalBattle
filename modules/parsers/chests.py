import re
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class TBChest:
    id: str
    name: str
    source: str
    level: int
    player: str
    timestamp: datetime
    raw_text: str

def parse_tb_chests(ocr_text: str) -> List[TBChest]:
    chests = []
    
    # Padrões específicos do Total Battle
    chest_patterns = {
        'crypt': r'(Crypt|Cripta?)\s*L?ev?l?\s*(\d+)',
        'dungeon': r'(Dungeon|Masmorra)\s*L?ev?l?\s*(\d+)',
        'barbarian': r'(Barbarian|Barbárico?)\s*(Chest|Baú)',
        'triumphal': r'(Triumphal|Triunfal)\s*(Chest|Baú)'
    }
    
    lines = [line.strip() for line in ocr_text.split('\n') if line.strip()]
    
    for i, line in enumerate(lines):
        chest = _extract_chest_from_line(line, lines, i)
        if chest:
            chests.append(chest)
    
    return chests

def _extract_chest_from_line(line: str, all_lines: List[str], index: int) -> TBChest | None:
    """Extrai baú de uma linha + contexto das linhas vizinhas"""
    now = datetime.utcnow()
    
    # Detectar nome do jogador (padrão TB)
    player_match = re.search(r'From:\s*(.+?)(?:\n|$)', ' '.join(all_lines[index:index+3]))
    player = player_match.group(1).strip() if player_match else "Unknown"
    
    # Detectar tipo/nível
    source = "unknown"
    level = None
    
    for source_type, pattern in chest_patterns.items():
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            source = source_type
            if len(match.groups()) > 1 and match.group(2):
                level = int(match.group(2))
            break
    
    chest_name = line.split()[0] if line.split() else "Unknown Chest"
    chest_id = f"{now.strftime('%Y%m%d%H%M%S')}_{hash(line) % 10000}"
    
    return TBChest(
        id=chest_id,
        name=chest_name,
        source=source,
        level=level,
        player=player,
        timestamp=now,
        raw_text=line
    )
