from dataclasses import dataclass

@dataclass
class NerBasicRequest:
    string_to_ner: str

@dataclass
class NerItem:
    text: str
    label: str
    start: int
    end: int


@dataclass
class NerBasicResponse:
    items: list[NerItem]


@dataclass
class NerBlobRequest:
    id_file: str
