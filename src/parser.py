import shapely as shp
from pathlib import Path

class GerberParser:
    def __init__(self, gerber_file: Path | str) -> None:
        self.gerber_file = Path(gerber_file)
        self._parse()

    def _parse(self) -> None:
        for line in self.gerber_file.open().readlines():
            