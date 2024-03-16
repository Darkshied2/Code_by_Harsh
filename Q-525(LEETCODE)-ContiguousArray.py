prefix = {0:-1}
ret = 0
diff = 0
for idx, num in enumerate(nums):
    diff = diff + 1 if num else diff - 1
    if diff in prefix:
        ret = max(ret, idx - prefix.get(diff))
    else:
        prefix[diff] = idx
return ret
