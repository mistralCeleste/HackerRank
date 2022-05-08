from unittest import TestCase
from unittest.mock import patch, mock_open
from .word_counter import \
    (
        CaseInsensitiveOrderedCounter
        , CaseInsensitiveOrderedDict
        , CaseInsensitiveOrderedWordCounter
        , FileMode
        , FileReader
        , ResultsWriter
    )


class TestCaseInsensitiveOrderedDict(TestCase):

    def test_setitem_sets_and_gets_expected_value_from_normalized_key_using_square_brackets(self):
        key = 'TestKey'
        value = 'TestValue'
        expected_key = key.casefold()
        expected_value = value
        items = CaseInsensitiveOrderedDict()
        items[key] = value
        actual_value = items[expected_key]
        self.assertEqual(expected_value, actual_value)

    def test_setitem_sets_and_gets_expected_value_from_normalized_key_using_getter(self):
        key = 'TestKey'
        value = 'TestValue'
        expected_key = key.casefold()
        expected_value = value
        items = CaseInsensitiveOrderedDict()
        items[key] = value
        actual_value = items.get(expected_key)
        self.assertEqual(expected_value, actual_value)


class TestCaseInsensitiveOrderedWordCounter(TestCase):

    def test_count_words_counts_expected_word_count(self):
        text = "If you prick us, do we not bleed? If you tickle us, do we not laugh?" \
               "If you poison us, do we not die? And if you wrong us, shall we not revenge?"
        expected_value = \
            {
                'if': 4
                , 'you': 4
                , 'prick': 1
                , 'us': 4
                , 'do': 3
                , 'we': 4
                , 'not': 4
                , 'bleed': 1
                , 'tickle': 1
                , 'laugh': 1
                , 'poison': 1
                , 'die': 1
                , 'and': 1
                , 'wrong': 1
                , 'shall': 1
                , 'revenge': 1
            }
        actual_value = CaseInsensitiveOrderedWordCounter.count_words(text)
        self.assertDictEqual(expected_value, actual_value)

    def test_update_word_count_adds_words(self):
        text = "If you prick us"
        expected_value = \
            {
                'if': 1
                , 'you': 1
                , 'prick': 1
                , 'us': 1
            }
        actual_value = CaseInsensitiveOrderedWordCounter()
        actual_value.update_word_count(text)
        self.assertDictEqual(expected_value, actual_value)

    def test_update_word_count_updates_words(self):
        text = "If you prick us,"
        values = \
            {
                'if': 2
                , 'you': 2
                , 'prick': 1
                , 'us': 1
            }
        expected_value = CaseInsensitiveOrderedWordCounter(**values)
        test_value = \
            {
                'if': 1
                , 'you': 1
            }
        actual_value = CaseInsensitiveOrderedWordCounter(**test_value)
        actual_value.update_word_count(text)
        self.assertDictEqual(expected_value, actual_value)

    def test_update_word_counts_updates_words(self):
        text = \
            [
                "If you prick us,"
                , "If you tickle us,"
            ]
        values = \
            {
                'if': 2
                , 'you': 2
                , 'prick': 1
                , 'us': 2
                , 'tickle': 1
            }
        expected_value = CaseInsensitiveOrderedWordCounter(**values)
        actual_value = CaseInsensitiveOrderedWordCounter()
        actual_value.update_word_counts(text)
        self.assertDictEqual(expected_value, actual_value)


class TestStrEnum(TestCase):

    def test_read_is_r(self):
        expected_value = 'r'
        actual_value = FileMode.read
        self.assertEqual(expected_value, actual_value)

    def test_read_binary_is_rb(self):
        expected_value = 'rb'
        actual_value = FileMode.read_binary
        self.assertEqual(expected_value, actual_value)

    def test_write_is_w(self):
        expected_value = 'w'
        actual_value = FileMode.write
        self.assertEqual(expected_value, actual_value)


class TestFileReader(TestCase):

    def test_read_lines_yields_two_expected_lines(self):
        path = 'volume:/directory/file.extension'
        test_data = 'one\ntwo\n'
        with patch('builtins.open', mock_open(read_data=test_data)) as mocked_stream:
            lines = FileReader.read_lines(path)
            for line in lines:
                pass
            mocked_stream.return_value.readlines.assert_called()


class TestResultsWriter(TestCase):

    def test_print_index(self):
        data = \
            {
                'if': 4
                , 'you': 4
            }
        test_value = CaseInsensitiveOrderedCounter(data)
        expected_value = "if=4\n"
        with patch('builtins.open', mock_open()) as mocked_stream:
            path = 'volume:/directory/file.extension'
            ResultsWriter.write_to_file(path, test_value)
            mocked_stream.return_value.write.assert_any_call(expected_value)
