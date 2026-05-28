class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLet = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
            }
        if not digits:
            return []
        
        res = []
        stack = []

        def bt(idx):
            if idx == len(digits):
                res.append("".join(stack))
                return
            
            dig = int(digits[idx])
            for let in (numToLet[dig]):
                stack.append(let)
                bt(idx+1)
                stack.pop()
        bt(0)
        return res
        