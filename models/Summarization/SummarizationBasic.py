from dataclasses import dataclass

@dataclass
class SummarizationBasicRequest:
    string_to_summarize: str

@dataclass
class SummarizationItem:
    summarize_text: str


# @dataclass
# class SummarizationBasicResponse:
#     items: list[SummarizationItem]


@dataclass
class SummarizationBlobRequest:
    id_file: str
