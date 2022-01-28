from pytest import raises
from Juice_offer_weekend import calculate_discount, percentages, minimum, maximum, bonus


class TestOperations:

    def test_juice_offer_not_member(self):
        m = False
        for key in percentages:
            for i in range(key[0], (key[1] + 1)):
                assert calculate_discount(i, m) == 1 - percentages[key]

    def test_juice_offer_member(self):
        m = True
        for key in percentages:
            for i in range(key[0], (key[1] + 1)):
                assert calculate_discount(i, m) == 1 - (percentages[key] * bonus)

    def test_juice_offer_below_range(self):
        with raises(ValueError):
            calculate_discount((minimum - 5), True)

    def test_juice_offer_over_range(self):
        with raises(ValueError):
            calculate_discount((maximum + 5), False)


#        assert calculate_discount((minimum - 5), True) == \
#               ValueError(f"amount has to be greater than {minimum-1} and less or equal to {maximum}")
#        assert calculate_discount((maximum + 5), False) == \
#               ValueError(f"amount has to be greater than {minimum-1} and less or equal to {maximum}")
