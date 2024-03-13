class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        m = {}

        box =set()

        for i in range(len(orders)):

            box.add(orders[i][2])

        for i in range(len(orders)):

            if int(orders[i][1]) not in m:

                m[int(orders[i][1])] = [orders[i][2]]

            else:

                m[int(orders[i][1])].append(orders[i][2])

        dishes = ["Table"]

        arr = list(box)

        arr.sort()

        for i in arr:

            dishes.append(i)
        ans = [dishes]

        nums = list(m.keys())

        nums.sort()

        for i in nums:
            temp = [str(i)]
            for j in range(1,len(dishes)):
                if dishes[j] in m[i]:
                    temp.append(str(m[i].count(dishes[j])))
                else:
                    temp.append(str(0))
            ans.append(temp)
        print(m)
        return ans
