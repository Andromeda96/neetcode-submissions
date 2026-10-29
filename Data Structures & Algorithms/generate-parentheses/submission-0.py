class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        n_open = 0
        n_close = 0        
        seq = ''
        def gen_paren(seq, n_open, n_close):
            if len(seq) > 2*n or n_open > n:
                return None
            if n_open < n_close:
                return None
            if n_open == n_close:
                if len(seq) == 2*n:
                    results.append(seq)
                    return None
                else:
                    seq += '('
                    n_open += 1
                    gen_paren(seq, n_open, n_close)
            else:
                gen_paren(seq + '(', n_open+1 , n_close)
                gen_paren(seq + ')', n_open, n_close+1)

        gen_paren(seq, n_open, n_close)
            
        return results









