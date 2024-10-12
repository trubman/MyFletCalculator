

class TestClassifierWorks:

    def test_do_clean_input_func(self):
        input_str = "  2 + 2  "
        expected = "2 + 2"
        result = Classifier.do_clean_input(input_str)
        assert expected == result
