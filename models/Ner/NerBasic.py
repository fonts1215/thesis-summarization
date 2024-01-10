from dataclasses import dataclass
from spacy.training import Example

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
class ExtractContentResult:
    content: str

@dataclass
class NerBasicResponse:
    items: list[NerItem]

@dataclass
class NerTrainingRequest:
    items: list[NerItem]

@dataclass
class NerBlobRequest:
    id_file: str
