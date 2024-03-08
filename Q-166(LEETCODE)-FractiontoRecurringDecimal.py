sol = ""
        if n == 0:
            return "0"
        negative = (n < 0) ^ (d < 0)
        n = abs(n)
        d = abs(d)
        sol += str(n // d)
        dec = ""
        if n % d:
            nums = {}
            sol += "."
            n = n % d
            while n:
                if n in nums:
                    dec += ")"
                    pos = nums[n]
                    dec = dec[:pos] + "(" + dec[pos:]
                    break
                nums[n] = len(dec)
                n *= 10
                dec += str(n // d)
                n = n % d
        sign = "-" if negative else ""
        return sign + sol + dec
