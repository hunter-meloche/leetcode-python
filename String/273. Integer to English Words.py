class Solution:
    def numberToWords(self, num: int) -> str:

        def handle_singles(digit):
            if  digit == '0':
                return False
            elif  digit == '1':
                return 'One '
            elif  digit == '2':
                return 'Two '
            elif  digit == '3':
                return 'Three '
            elif  digit == '4':
                return 'Four '
            elif  digit == '5':
                return 'Five '
            elif  digit == '6':
                return 'Six '
            elif  digit == '7':
                return 'Seven '
            elif  digit == '8':
                return 'Eight '
            elif  digit == '9':
                return 'Nine '

        def handle_teens(digit):
            if  digit == '0':
                return 'Ten '
            elif  digit == '1':
                return 'Eleven '
            elif  digit == '2':
                return 'Twelve '
            elif  digit == '3':
                return 'Thirteen '
            elif  digit == '4':
                return 'Fourteen '
            elif  digit == '5':
                return 'Fifteen '
            elif  digit == '6':
                return 'Sixteen '
            elif  digit == '7':
                return 'Seventeen '
            elif  digit == '8':
                return 'Eighteen '
            elif  digit == '9':
                return 'Nineteen '

        def handle_decades(digit):
            if  digit == '0':
                return False
            elif  digit == '2':
                return 'Twenty '
            elif  digit == '3':
                return 'Thirty '
            elif  digit == '4':
                return 'Forty '
            elif  digit == '5':
                return 'Fifty '
            elif  digit == '6':
                return 'Sixty '
            elif  digit == '7':
                return 'Seventy '
            elif  digit == '8':
                return 'Eighty '
            elif  digit == '9':
                return 'Ninety '

        snum = ''.join(reversed(str(num)))  # Turns num into a string and reverses it to make it easier to iterate through
        length = len(snum)
        english = ''
        temp = ''

        # Handle Zero by itself
        if length == 1 and snum[0] == '0':
            return 'Zero'

        # Takes the reversed string form of the integer and iterates though it in reverse
        i = length - 1
        while i >= 0:

            # Billions
            if i == 9:
                temp = handle_singles(snum[i])
                if temp:
                    english += temp
                    english += 'Billion '
            
            # Hundred Milllions
            if i == 8:
                temp = handle_singles(snum[i])
                if temp:
                    english += temp
                    english += 'Hundred '

            # Ten Millions
            if i == 7:
                if snum[i] == '1':
                    english +=  handle_teens(snum[i-1])
                    english += 'Million '
                    i -= 2
                    continue
                else:
                    temp =  handle_decades(snum[i])
                    if temp:
                        english += temp
            
            # Millions
            if i == 6:
                temp = handle_singles(snum[i])
                if temp:
                    english += temp
                    english += 'Million '
                elif snum[i+1] != '0' or snum[i+2] != '0':
                    english += 'Million '

            # Hundred Thousands
            if i == 5:
                temp = handle_singles(snum[i])
                if temp:
                    english += temp
                    english += 'Hundred '

            # Ten Thousands
            if i == 4:
                if snum[i] == '1':
                    english +=  handle_teens(snum[i-1])
                    english += 'Thousand '
                    i -= 2
                    continue
                else:
                    temp =  handle_decades(snum[i])
                    if temp:
                        english += temp

            # One Thousands
            if i == 3:
                temp = handle_singles(snum[i])
                if temp:
                    english += temp
                    english += 'Thousand '
                elif snum[i+1] != '0' or snum[i+2] != '0':
                    english += 'Thousand '

            # Hundreds
            if i == 2:
                temp = handle_singles(snum[i])
                if temp:
                    english += temp
                    english += 'Hundred '

            # Tens
            if i == 1:
                if snum[i] == '1':
                    english +=  handle_teens(snum[i-1])
                    break
                else:
                    temp =  handle_decades(snum[i])
                    if temp:
                        english += temp

            # Singles
            if i == 0:
                temp = handle_singles(snum[i])
                if temp:
                    english += temp

            # Decrement the iterator by one to move to the next digit
            i -= 1
                    
        return english[:-1]
