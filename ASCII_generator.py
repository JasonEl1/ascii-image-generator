#image selection / multiple image support
#resize image to a specific size / user selects quality


from PIL import Image
import os

with open ("asciiResult.txt", "w") as result_saver:
        
    result_saver.write('\n')

print("v.1.1")

for f in os.listdir('.'):
    
    if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.JPG') or f.endswith('.PNG') or f.endswith('.jpeg'):
        im=Image.open(f).convert('L')
        fn, fext = os.path.splitext(f)
        width, height = im.size
        print(width,height)
        
        if(height > width):
            im.rotate(90)

        i=im.resize((int(width/30),int(height/30)))
try:     
    width, height = i.size
except:
    print("No image found")
    exit()

print(fn)
print(width,height)

px = i.load()

# black -> white.
#  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. "

#current scale (black -> white) is:
#@%#*+=-:.

row_test = []

for j in range(int(height)):
    
    row_test = []
    
    for k in range(int(width)):
        val = (px[k,j]) / (85/3)
        
        
        if(val<=1):
            val = '@@'
        elif(val<=2 and val>1):
            val = '%%'
        elif(val<=3 and val>2):
            val = '##'
        elif(val<=4 and val>3):
            val = '**'
        elif(val<=5 and val>4):
            val = '++'
        elif(val<=6 and val>5):
            val = '=='
        elif(val<=7 and val>6):
            val = '--'
        elif(val<=8 and val>7):
            val = '::'
        elif(val<=9 and val>8):
            val = '..'

            
        row_test.append(val)
        
    print(f"{int((j/i.size[1])*100)}% done")

    with open ("asciiResult.txt", "a") as result_saver:
        
        for x in range(len(row_test)):
            result_saver.write(str(row_test[x]))
            
        result_saver.write('\n')
        
os.system(r"asciiResult.txt")
exit()