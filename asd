[1mdiff --git a/darwin.png b/darwin.png[m
[1mindex 85b5b78..ff79298 100644[m
Binary files a/darwin.png and b/darwin.png differ
[1mdiff --git a/darwin.pnggaussblurred-goorain.png b/darwin.pnggaussblurred-goorain.png[m
[1mindex e69de29..5a5b20c 100644[m
Binary files a/darwin.pnggaussblurred-goorain.png and b/darwin.pnggaussblurred-goorain.png differ
[1mdiff --git a/gaussian_blur.py b/gaussian_blur.py[m
[1mindex ed1bda2..f212da8 100644[m
[1m--- a/gaussian_blur.py[m
[1m+++ b/gaussian_blur.py[m
[36m@@ -38,25 +38,40 @@[m [mdef process(filename, r):[m
     coeff = gauss_dist / np.sum(gauss_dist)[m
 [m
     # код сюда ....[m
[32m+[m[32m    print(img.size)[m
[32m+[m[32m    print(np.array(img.getdata()).size)[m
     w, h = img.size[m
[31m-    a = np.array(img.getdata(), dtype = np.uint8).reshape(h, w)[m
[31m-    b = np.zeros((h, w), dtype = np.float)[m
[31m-    startH = 1000[m
[31m-    startW = 1000[m
[31m-    endH = h + r - 1 - 1500[m
[31m-    endW = w + r - 1 - 1400[m
[31m-    total = endH * endW[m
[32m+[m[32m    a = np.array(img.getdata(), dtype = np.uint8).reshape(w, h)[m
[32m+[m[32m    b = np.zeros((w, h), dtype = np.uint8)[m
[32m+[m[32m    startH = r[m
[32m+[m[32m    startW = r[m
[32m+[m[32m    endH = h - r[m
[32m+[m[32m    endW = w - r[m
[32m+[m[32m    total = h * w[m
     iteration = 0[m
[31m-    for i in range(startH + r + 1, endH):[m
[31m-        for j in range(startW + r + 1, endW):[m
[32m+[m[32m    # [ ? ? ? ? ? ? ?]  x = -r, -r + 1, -r + 2, 0, r - 2, r - 1, r = range(-r, r + 1)[m
[32m+[m[32m    # [ ? ? ? ? ? ? ?][m
[32m+[m[32m    # [ ? ? ? ? ? ? ?][m
[32m+[m[32m    # [ ? ? ? ? ? ? ?][m
[32m+[m[32m    # [ ? ? ? X ? ? ?]  X[i, j] = ?[i - x, j - y] * coeff[m
[32m+[m[32m    # [ ? ? ? ? ? ? ?][m
[32m+[m[32m    # [ ? ? ? ? ? ? ?][m
[32m+[m[32m    # [ ? ? ? ? ? ? ?][m
[32m+[m[32m    # [ ? ? ? ? ? ? ?][m[41m  [m
[32m+[m[41m    [m
[32m+[m[32m    for i in range(startW, endW):[m
[32m+[m[32m        for j in range(startH, endH):[m
[32m+[m[32m            iteration += 1[m
             for x in range(-r, r + 1):[m
                 for y in range(-r, r + 1):[m
[31m-                        iteration += 1[m
[31m-                        b[i,j] += coeff[x // 2 + r // 2,y // 2 + r // 2] * a[i + x, j + y][m
[31m-                        printProgressBar(iteration, total, length = 75)[m
[32m+[m[32m                        b[i,j] += a[i + x, j + y] * coeff[r + x, r + y][m
[32m+[m[32m                        # print(b[i,j])[m
[32m+[m[32m                        # printProgressBar(iteration, total, length = 75)[m
[32m+[m[32m        printProgressBar(iteration, total, length = 75)[m
 [m
     newimg = Image.fromarray(b)[m
[31m-    newimg.save(filename + 'gaussblurred-goorain.png')[m
[32m+[m[32m    newimg.save(filename[:-4] + 'gaussblurred-goorain.png')[m
[32m+[m[32m    print("Success!")[m
 [m
 if __name__=='__main__':[m
     # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png[m
