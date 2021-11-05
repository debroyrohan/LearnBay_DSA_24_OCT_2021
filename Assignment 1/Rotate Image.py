class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp_list = []
        for i in range(len(matrix)):
            internal_list = []
            for j in range(len(matrix)-1, -1, -1):
                internal_list.append(matrix[j][i])
            temp_list.append(internal_list)
        #print(temp_list)
        for k in range(len(temp_list)):
            matrix.pop(k)
            matrix.insert(k, temp_list[k])
