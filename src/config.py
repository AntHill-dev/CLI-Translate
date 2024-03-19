from pathlib import Path

from pydantic import BaseModel


class _MetaInfo(BaseModel):
    author: str = "Ivan Kovach"
    copyright: str = "Copyright 2024 (c) Ivan Kovach aka Qu1nel"
    license: str = Path(__file__).parent.with_name("LICENSE").read_text(encoding="UTF-8")
    version: str = "1.1.1"

    maintainer: str = "Ivan Kovach"
    email: str = "covach.qn@gmail.com"
    status: str = "Production"

    prog_name: str = "CLI-Translate"


class _RotationSettings(BaseModel):
    size: str = "2.5 MB"
    type: str = "zip"
    folder: str = "log"


class _CLISetting(BaseModel):
    CONTEXT_SETTINGS: dict[str, list[str]] = {"help_option_names": ["-h", "--help"]}

    class Docs:
        Dest: str = "Forcibly translate into the selected language."

    class Colors:
        Translated: str = "green"
        Original: str = "blue"


MetaInfo = _MetaInfo()
RotationSettings = _RotationSettings()
CLISetting = _CLISetting()
