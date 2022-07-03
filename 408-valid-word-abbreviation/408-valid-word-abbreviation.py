class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_char_len = 0
        num = ''
        for x in abbr:
            if x.isnumeric():
                # If it's numeric and not leading zero, save the number.
                if x == '0' and not num:
                    return False
                num += x
                continue
                
            elif num != '':
                # If the numbers sequence ended, calculate the number
                abbr_char_len += int(num)
                num = ''
           
            # Check that the curr char located in the right position in `word`
            if abbr_char_len < len(word) and x != word[abbr_char_len]:
                return False
                
            abbr_char_len +=1
        # Calcaulate num in case arr abbr is ending with numbers
        if num:
            abbr_char_len += int(num)

        return abbr_char_len == len(word)