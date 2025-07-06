class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=""
        for num in digits:
            number=number+str(num)
        number=int(number)
        number+=1 
        number=str(number)
        number=list(number)
        g=[]
        for no in number:
            g.append(int(no))
        return g