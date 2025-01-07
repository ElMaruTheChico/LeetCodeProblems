class Solution:
    def intToRoman(self, num: int) -> str:
        romano = ''
        while num != 0:
            snum = str(num)
            if snum[0] != '4' and snum[0] != '9':
                if num >= 1000:
                    romano = romano + 'M'
                    num = num - 1000
                elif num >= 500:
                    romano = romano + 'D'
                    num = num - 500
                elif num >= 100:
                    romano = romano + 'C'
                    num = num - 100
                elif num >= 50:
                    romano = romano + 'L'
                    num = num - 50
                elif num >= 10:
                    romano = romano + 'X'
                    num = num - 10
                elif num >= 5:
                    romano = romano + 'V'
                    num = num - 5
                elif num >= 1:
                    romano = romano + 'I'
                    num = num - 1
            else:
                if num >= 900:
                    romano = romano + 'CM'
                    num = num - 900
                elif num >= 400:
                    romano = romano + 'CD'
                    num = num - 400
                elif num >= 90:
                    romano = romano + 'XC'
                    num = num - 90
                elif num >= 40:
                    romano = romano + 'XL'
                    num = num - 40
                elif num >= 9:
                    romano = romano + 'IX'
                    num = num - 9
                else:
                    romano = romano + 'IV'
                    num = num - 4   
        return romano

