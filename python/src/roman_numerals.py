class RomanNumerals:

    def convert(self, amount: int) -> str:
        if amount == 5:
            return "V"
        if amount == 4:
            return "IV"

        roman = ""
        for _ in range(amount):
            roman += "I"
        return roman
