class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {
            '2': 'abc', '3':'def', '4':'ghi','5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9': 'wxyz'
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append(''.join(path))
                return

            current_dig = digits[index]
            for l in digit_map[current_dig]:
                path.append(l)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations
# digits = ''.join(filter(str.isdigit, digits))
# print(letterCombinations(digits))