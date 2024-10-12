from classifier import Classifier


class TestClassifierWorks:

    def test_do_clean_input_func(self):
        input_str = "  2 + 2  "
        expected = "2 + 2"
        cls = Classifier()
        result = cls.do_clean_input(input_str)
        assert expected == result

    # def test_do_clean_input_error(self):
    #     input_str = 2 + 2
    #     expected = "2 + 2"
    #     cls = Classifier()
    #     result = cls.do_clean_input(input_str)
    #     assert expected == result
