from PIL import Image
import numpy as np

L_path='1.png'
L_image=Image.open(L_path)
out = L_image.convert("RGB")
img=np.array(out)

m , n = out.size
cnt = 0


with open('2.txt') as f:
    with open('3.txt','w') as z:
        for i in range(n):
            for j in range(m):
                a = f.readline().split(" ")
                if len(a)<3:
                    z.write('??')
                    continue
                if ((int(a[0]) > 150 or int(a[1]) > 150 or int(a[2]) > 150) and not(int(a[0]) > 100 and int(a[1]) > 100 and int(a[2]) > 100)):
                    z.write('  ')
                else:
                    z.write('██')
                    #z.write(str(a))
            z.write('\n')
        z.close()
    f.close()
"""
h = ""
with open('2.txt') as f:
    with open('sample3.txt','w') as z:
        for i in range(n):
            for j in range(m):
                a = f.readline().split(" ")
                if len(str(a))<5:
                    #z.write('--')
                    continue
                if (int(a[0]) != 255 and int(a[1])>200 and int(a[2]) != 255):
                    #z.write('1')
                    h = h + "1"
                else:
                    #z.write('0')
                    #z.write(str(a))
                    h = h + "0"
            #z.write('\n')
            h = h + "\n"
        for j in range(m):
            for i in range(n):
                if( h[i][j] == "1" ):
                    z.write('1')
                if( h[i][j] == "0" ):
                    z.write('0')
                if( h[i][j] == "\n" ):
                    z.write('\n')
        z.close()
    f.close()
"""
