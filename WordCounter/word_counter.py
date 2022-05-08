from enum import Enum
from collections import Counter, OrderedDict
from typing import AnyStr, Dict, Iterable


class CaseInsensitiveOrderedDict(
    OrderedDict
):

    def __setitem__(
            self
            , key: AnyStr
            , value: AnyStr
    ) -> None:
        normalized_key = self._normalize_key(key)
        super().__setitem__(normalized_key, value)

    def __getitem__(
            self
            , key: AnyStr
    ) -> AnyStr:
        normalized_key = self._normalize_key(key)
        return super().__getitem__(normalized_key)

    def get(
            self
            , key: AnyStr
            , default=None
    ) -> AnyStr:
        normalized_key = self._normalize_key(key)
        return super().get(normalized_key, default)

    @staticmethod
    def _normalize_key(
            key: AnyStr
    ) -> AnyStr:
        return key.casefold()


class CaseInsensitiveOrderedCounter(
    Counter
    , CaseInsensitiveOrderedDict
):  # pragma no cover
    pass


class CaseInsensitiveOrderedWordCounter(
    CaseInsensitiveOrderedCounter
):

    @classmethod
    def count_words(
            cls
            , text: str
    ) -> Dict[str, int]:
        import re as regex
        pattern = r"(?:\b\w*[-']\w*\b){1,}|\w+|\b'\w*(?<=[^'])\b"
        parsed_text = regex.findall(pattern, text, flags=regex.ASCII)
        table = cls(parsed_text)
        return table

    def update_word_count(
            self
            , text: str
    ) -> None:
        counts = self.count_words(text)
        self.update(counts)

    def update_word_counts(
            self
            , iterable_text: Iterable[str]
    ) -> None:
        for text in iterable_text:
            self.update_word_count(text)


class StrEnum(
    str
    , Enum
):  # pragma no cover
    pass


class FileMode(StrEnum):
    read = 'r'
    read_binary = 'rb'
    write = 'w'


class FileReader:

    @staticmethod
    def read_lines(
            path: str
    ) -> Iterable[str]:
        with open(path, FileMode.read) as file_stream:
            for line in file_stream.readlines():
                yield line


class ResultsWriter:

    new_line = '\n'

    @classmethod
    def write_to_file(
            cls
            , path: str
            , results: Dict[str, int]
    ) -> None:
        with open(path, FileMode.write) as file_stream:
            for word, count in results.items():
                file_stream.write(f"{word}={count}{cls.new_line}")


class WordCounter:

    @classmethod
    def count_words(
            cls
            , input_file_path: str
            , output_file_path: str
    ) -> None:
        word_counter = CaseInsensitiveOrderedWordCounter()
        lines = FileReader.read_lines(input_file_path)
        word_counter.update_word_counts(lines)
        ResultsWriter.write_to_file(output_file_path, word_counter)
