class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # start from the end and replace elements
        max_elt = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            elt = arr[i]
            arr[i] = max_elt

            if elt > max_elt:
                max_elt = elt

        return arr