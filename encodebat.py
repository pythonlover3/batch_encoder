import re
import sys

if len(sys.argv)<3:
    print("Usage:",sys.argv[0],"Sourcefile Encodefile")
else:
    key = '号功GN败制tA面uEMJRq激错ceH找s脑mbI电成WSdiD误KQ此hflz失F控kV活O在密yxPX码g到板BTULnCv存未w暗pYajroZ'
    replacestr = 'Blah'
    #encode
    fin = open(sys.argv[1],"r")
    alllines = fin.readlines();
    fin.close()
    fout = open(sys.argv[2],"a")
    fout.write("@echo off"+'\n'+"set"+" "+replacestr+"="+key+'\n')
 
    for line in alllines:
        if line[0]==':':
            fout.write(line)
            continue
        strout = ''
        strlen = len(line)
        flag =True
        ##1 == %xx% 2 == %~ 3 == %%i 
        mode = 0
        for i in range(0,strlen):
            if line[i]=='%' and  line[i+1]=='%' and mode==0:         
                flag = False
                mode =3
                strout = strout+line[i]
                continue
            elif line[i]=='%' and  line[i+1]=='~' and mode==0:
                flag = False
                mode =2
                strout = strout+line[i]
                continue
            elif line[i]=='%' and key.find(line[i+1])>=0 and mode==0:
                flag = False
                mode =1
                strout = strout+line[i]
                continue
            elif mode ==3 and line[i]=='%':
                strout = strout+line[i]
                continue
         
            if line[i]=='%' and mode ==1:
                mode =0
                flag = True
                strout = strout+line[i]
                continue
            elif line[i]=='"' and mode ==2 or mode ==3:
                mode =0
                flag = True
                strout = strout+line[i]
                continue
            elif line[i]==' ' and mode ==3:
                mode =0
                flag = True
                strout = strout+line[i]
                continue
             
            nPos = key.find(line[i])
            if nPos>=0 and flag == True:
                temp = '%'+replacestr+':~'+str(nPos)+',1%'
                strout = strout + temp
            else:
                strout = strout+line[i]
        fout.write(strout)
    fout.close()
