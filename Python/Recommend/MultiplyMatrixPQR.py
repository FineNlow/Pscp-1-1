"""MultiplyMatrixPQR"""
def main(p, q, r):
    """MultiplyMatrixPQR"""
    # matrixA (p x q)
    matA = [[int(input()) for _ in range(q)] for _ in range(p)]
    # matrixB (q x r)
    matB = [[int(input()) for _ in range(r)] for _ in range(q)]
    # result (p * r)
    result = [[0 for _ in range(r)] for _ in range(p)]
    # loop rows
    for i in range(p):
        # loop cols
        for j in range(r):
            # loop matrix บวกกัน
            for k in range(q):
                # แถว*หลัก = A แถวตัว i ตำแหน่ง k * B หลักตัว j ตำแหน่ง k
                result[i][j] += matA[i][k] * matB[k][j]
    for row in result:
        print(*row)
main(int(input()), int(input()), int(input()))
# มึนๆตอนเขียนลูป งงจัด
