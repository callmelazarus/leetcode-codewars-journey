import codewars_test as test
from solution import digital_root

@test.describe("Sum of Digits / Digital Root")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        test.assert_equals(digital_root(942), 6)
        test.assert_equals(digital_root(132189), 6)
        test.assert_equals(digital_root(493193), 2)