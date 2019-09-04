from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from .models import Product, Box , invoice
from django.views.decorators.csrf import csrf_protect
# from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.
def after_login(request):
    product = Product.objects.all()
    return render(request,'production.html',{'product':product})

def new_project(request):
    return render(request,'newproject.html')

def add_project(request):
    if request.method=='POST':
        code = request.POST.get('code')
        name = request.POST.get('pname')
        box_t_n = request.POST.get('type_name')
        box_n = request.POST.get('no.')
        one_pc = request.POST.get('single_wt')
        carton = request.POST.get('carton_wt')
        dim1 = request.POST.get('dimension1')
        dim2 = request.POST.get('dimension2')
        x = Product(p_id = code, p_name = name, box_type_name = box_t_n, box_type = box_n, one_pc_weight = one_pc, box_weight = carton, box_size_1 = dim1,box_size_2=dim2)
        x.save()
        product = Product.objects.all()
        return render(request, 'production.html', {'product':product})


@csrf_protect
def data_test(request):
    if (request.method=='POST'):
        code = request.POST.getlist('code')
        qty = request.POST.getlist('quantity')
        # checks = request.POST.getlist('checks')
        bx = request.POST.getlist('box_type')
        print(bx, type(bx[0]))
        # print(checks)
        print(code)
        print(qty)
        # invoice = request.POST.get('invoice')
        # date = request.POST.get('date')
        rem1, pkg1, rem2, pkg2_6, pkg2_7, rem3, pkg3_6, pkg3_7 = ([] for i in range(8))
        rem4, pkg4_3, pkg4_4, rem5, pkg5_6, pkg5_7, rem6, pkg6_12, pkg6_14 = ([] for j in range(9))
        rem7, pkg7, rem8, pkg8, rem9, pkg9_6, pkg9_7, rem10, pkg10_3, pkg10_4 = ([] for k in range(10))
        rem11, pkg11_3, pkg11_4 = ([] for l in range(3))
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 = ([] for m11 in range(11))
        det1, det2, det3, det4, det5, det6, det7, det8, det9, det10, det11 = ([] for i in range(11))
        print('yo')


        def box_two(x):
            cartons = [6,7]
            n = x
            if n<80:
                def find_changes(n, cartons):
                    if n < 0:
                        return []
                    if n == 0:
                         return [[]]
                    all_changes = []

                    for last_used_carton in cartons:
                        combos = find_changes(n - last_used_carton, cartons)
                        for combo in combos:
                            combo.append(last_used_carton)
                            all_changes.append(combo)

                    return all_changes

                k = find_changes(n,cartons)
                if not k:
                    if n>=15:
                        x=0
                        y = n//7
                        z =n%7
                        return x,y,z
                    else:
                        potty = n//7
                        susu = n%7
                        print('p = ', potty , 's = ', susu)
                        if n%7==6:
                            return potty,1,0
                        else:
                            return 0,potty,susu
                else:
                    p = k[-1].count(6)
                    q = k[-1].count(7)
                    r = 0
                    return p,q,r
            else:
                if n%7==0:
                    return 0,n//7,0
                if n%7==6:
                    return 1,n//7,0
                    print('6pc = 1, 7pc =',n//7)
                if n%7==5:
                    return 2,n//7,0
                    print('6pc = 2, 7pc =',(n-12)//7)
                if n%7==4:
                    return 3,n//7,0
                    print('6pc = 3, 7pc =',(n-18)//7)
                if n%7==3:
                    return 4,n//7,0
                    print('6pc = 4, 7pc =',(n-24)//7)
                if n%7==2:
                    return 5,n//7,0
                    print('6pc = 5, 7pc =',(n-30)//7)
                if n%7==1:
                    return 6,n//7,0
                    print('6pc = 6, 7pc =',(n-36)//7)

        def box_four(a):
            n = a
            if n==5:
                return 0,1,1
            if n<3:
                if n==1:
                    return 0,0,1
                else:
                    return 0,0,2
            dedo = a//4
            y = a%4
            if y==0:
                return 0,dedo,0
            if y==1:
                z = (n-9)//4
                return 3,z,0
            if y==2:
                z = (n-6)//4
                return 2,z,0
            if y==3:
                z = (n-3)//4
                return 1,z,0

        def box_six(i):
            if i<=120:
                cartons = [12,13]
                n=i
                def find_changes(n, cartons):
                    if n < 0:
                        return []
                    if n == 0:
                         return [[]]
                    all_changes = []
                    for last_used_carton in cartons:
                        combos = find_changes(n - last_used_carton, cartons)
                        for combo in combos:
                            combo.append(last_used_carton)
                            all_changes.append(combo)
                    return all_changes
                k = find_changes(n,cartons)
                if not k:
                    x = n//13

                    print(n)
                    return 0,x,n%13
                else:
                    m=k[-1].count(12)
                    q=k[-1].count(13)
                    return m,q,0
            else:
                if n%13==0:
                    return 0,n//13,0
                else:
                    z = n//13
                    p = (z+1)*13
                    x = p-n
                    y = z+1-x
                    return x,y,0

        def only_six(j):
            print(j//6,0,j%6)
            return j//6,0,j%6

        def only_seven(k):
            print(0,k//7,k%7)
            return 0,k//7,k%7

        def only_three(l):
            return l//3,0,l%3

        def only_four(m):
            return 0,m//4,m%4

        def only_twelve(n):
            return n//12,0,n%12

        def only_thirteen(o):
            return 0,o//13,o%13


        s1=s2=s3=s4=s5=s6=s7=s8=s9=s10=s11=0
        for i in range(len(code)):
            xx = Product.objects.filter(p_id=code[i]).values_list('box_type','p_id', 'one_pc_weight', 'box_weight', 'box_size_1','box_size_2')
            print(xx)
            qty[i] = int(qty[i])
            # box type 1 has only 10pc space
            if xx[0][0]==1:
                x1.append(xx[0][1])
                det1.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x1)
                rem1.append((xx[0][1],qty[i]%15))
                pkg1.append(qty[i]//15)
                s1+=qty[i]%15

            # box type 2 has 6,7 pc space

            if xx[0][0]==2:
                x2.append(xx[0][1])
                det2.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x2)
                if bx[i]=='6':
                    print('1 me')
                    p1,p2,p3 = only_six(qty[i])
                    pkg2_6.append(p1)
                    pkg2_7.append(p2)
                    rem2.append((xx[0][1],p3))
                    s2+=p3
                elif bx[i]=='7':
                    print('2 me')
                    p1,p2,p3 = only_seven(qty[i])
                    pkg2_6.append(p1)
                    pkg2_7.append(p2)
                    rem2.append((xx[0][1],p3))
                    s2+=p3
                else:
                    print('yaha')
                    p1,p2,p3 = box_two(qty[i])
                    pkg2_6.append(p1)
                    pkg2_7.append(p2)
                    rem2.append((xx[0][1],p3))
                    s2+=p3
                    print(s2)
                print(rem2)

            # box type 3 has 6,7 pc space
            if xx[0][0]==3:
                x3.append(xx[0][1])
                det3.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x3)
                if bx[i]=='6':
                    q1,q2,q3 = only_six(qty[i])
                    pkg3_6.append(q1)
                    pkg3_7.append(q2)
                    rem3.append((xx[0][1],q3))
                    s3+=q3
                elif bx[i]=='7':
                    q1,q2,q3 = only_seven(qty[i])
                    pkg3_6.append(q1)
                    pkg3_7.append(q2)
                    rem3.append((xx[0][1],q3))
                    s3+=q3
                else:
                    q1,q2,q3 = box_two(qty[i])
                    pkg3_6.append(q1)
                    pkg3_7.append(q2)
                    rem3.append((xx[0][1],q3))
                    s3+=q3

            # box type 4 has 3,4 pc space
            if xx[0][0]==4:
                x4.append(xx[0][1])
                det4.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x4)
                if bx[i]=='3':
                    r1,r2,r3 = only_three(qty[i])
                    pkg4_3.append(r1)
                    pkg4_4.append(r2)
                    rem4.append((xx[0][1],r3))
                    s4+=r3
                elif bx[i]=='4':
                    r1,r2,r3 = only_four(qty[i])
                    pkg4_3.append(r1)
                    pkg4_4.append(r2)
                    rem4.append((xx[0][1],r3))
                    s4+=r3
                else:
                    r1,r2,r3 = box_four(qty[i])
                    pkg4_3.append(r1)
                    pkg4_4.append(r2)
                    rem4.append((xx[0][1],r3))
                    s4+=r3


            # box type 5 has 6,7 pc space
            if xx[0][0]==5:
                x5.append(xx[0][1])
                det5.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x5)
                if bx[i]=='6':
                    ss1,ss2,ss3 = only_six(qty[i])
                    pkg5_6.append(ss1)
                    pkg5_7.append(ss2)
                    rem5.append((xx[0][1],ss3))
                    s5+=ss3
                elif bx[i]=='7':
                    ss1,ss2,ss3 = only_seven(qty[i])
                    pkg5_6.append(ss1)
                    pkg5_7.append(ss2)
                    rem5.append((xx[0][1],ss3))
                    s5+=ss3
                else:
                    ss1,ss2,ss3 = box_two(qty[i])
                    pkg5_6.append(ss1)
                    pkg5_7.append(ss2)
                    rem5.append((xx[0][1],ss3))
                    s5+=ss3


            # box type 6 has 12,13 pc space
            if xx[0][0]==6:
                x6.append(xx[0][1])
                det6.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x6)
                if bx[i]=='12':
                    t1,t2,t3 = only_twelve(qty[i])
                    pkg6_12.append(t1)
                    pkg6_14.append(t2)
                    rem6.append((xx[0][1],t3))
                    s6+=t3
                elif bx[i]=='13':
                    t1,t2,t3 = only_thirteen(qty[i])
                    pkg6_12.append(t1)
                    pkg6_14.append(t2)
                    rem6.append((xx[0][1],t3))
                    s6+=t3
                else:
                    t1,t2,t3 = box_six(qty[i])
                    pkg6_12.append(t1)
                    pkg6_14.append(t2)
                    rem6.append((xx[0][1],t3))
                    s6+=t3

            # box type 7 has 10pc space
            if xx[0][0]==7:
                print('idhar')
                x7.append(xx[0][1])
                det7.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x7)
                rem7.append(qty[i]%10)
                pkg7.append(qty[i]//10)
                s7+=qty[i]%10

            # box type 8 has 8pc space
            if xx[0][0]==8:
                x8.append(xx[0][1])
                det8.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x8)
                pkg8.append(qty[i]//8)
                rem8.append(qty[i]%8)
                s8+=qty[i]%8

            # box type 9 has 6,7 pc space
            if xx[0][0]==9:
                x9.append(xx[0][1])
                det9.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x9)
                if bx[i]=='6':
                    u1,u2,u3 = only_six(qty[i])
                    pkg9_6.append(u1)
                    pkg9_7.append(u2)
                    rem9.append((xx[0][1],u3))
                    s9+=u3
                elif bx[i]=='7':
                    u1,u2,u3 = only_seven(qty[i])
                    pkg9_6.append(u1)
                    pkg9_7.append(u2)
                    rem9.append((xx[0][1],u3))
                    s9+=u3
                else:
                    u1,u2,u3 = box_two(qty[i])
                    pkg9_6.append(u1)
                    pkg9_7.append(u2)
                    rem9.append((xx[0][1],u3))
                    s9+=u3

            # box type 10 has 3,4 pc space
            if xx[0][0]==10:
                x10.append(xx[0][1])
                det10.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x10)
                if bx[i]=='3':
                    v1,v2,v3 = only_three(qty[i])
                    pkg10_3.append(v1)
                    pkg10_4.append(v2)
                    rem10.append((xx[0][1],v3))
                    s10+=v3
                elif bx[i]=='4':
                    v1,v2,v3 = only_four(qty[i])
                    pkg10_3.append(v1)
                    pkg10_4.append(v2)
                    rem10.append((xx[0][1],v3))
                    s10+=v3
                else:
                    v1,v2,v3 = box_four(qty[i])
                    pkg10_3.append(v1)
                    pkg10_4.append(v2)
                    rem10.append((xx[0][1],v3))
                    s10+=v3

            # box type 11 has 3,4 pc space
            if xx[0][0]==11:
                x11.append(xx[0][1])
                det11.append((xx[0][2],xx[0][3],xx[0][4],xx[0][5]))
                print(x11)
                if bx[i]=='3':
                    w1,w2,w3 = only_three(qty[i])
                    pkg11_3.append(w1)
                    pkg11_4.append(w2)
                    rem11.append((xx[0][1],w3))
                    s11+=w3
                elif bx[i]=='4':
                    w1,w2,w3 = only_four(qty[i])
                    pkg11_3.append(w1)
                    pkg11_4.append(w2)
                    rem11.append((xx[0][1],w3))
                    s11+=w3
                else:
                    w1,w2,w3 = box_four(qty[i])
                    pkg11_3.append(w1)
                    pkg11_4.append(w2)
                    rem11.append((xx[0][1],w3))
                    s11+=w3

        if s1!=0:
            for i1 in range(len(rem1)):
                print(rem1[i1][0],rem1[i1][1])
        if s2!=0:
            a2,b2,c2 = box_two(s2)

            for i2 in range(len(rem2)):
                print(rem2[i2][0],rem2[i2][1])

        if s3!=0:
            a3,b3,c3 = box_two(s3)
            for i2 in range(len(rem3)):
                print(rem3[i2][0],rem3[i2][1])

        if s4!=0:
            a4,b4,c4 = box_four(s4)
            for i2 in range(len(rem4)):
                print(rem4[i2][0],rem4[i2][1])

        if s5!=0:
            a5,b5,c5 = box_two(s5)
            for i2 in range(len(rem5)):
                print(rem5[i2][0],rem5[i2][1])

        if s6!=0:
            a6,b6,c6 = box_six(s6)
            for i2 in range(len(rem6)):
                print(rem6[i2][0],rem6[i2][1])

        if s9!=0:
            a9,b9,c9 = box_two(s9)
            for i2 in range(len(rem9)):
                print(rem9[i2][0],rem9[i2][1])

        if s10!=0:
            a10,b10,c10 = box_four(s10)
            for i2 in range(len(rem10)):
                print(rem10[i2][0],rem10[i2][1])

        if s11!=0:
            a11,b11,c11 = box_four(s11)
            for i2 in range(len(rem11)):
                print(rem11[i2][0],rem11[i2][1])


        print('here now')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="packaging.csv"'
        writer = csv.writer(response)
        count = 0
        writer.writerow(['', '', '', '', '', ''])
        writer.writerow(['', '', '', '', '', ''])
        writer.writerow(['', '', '', '', '', ''])
        writer.writerow(['Box number', 'SKU', 'Wt/pc', 'Wt/box', 'Size','Act/Wt'])
        writer.writerow(['', '', '', '', '', ''])
        if x2 or x3 or x5 or x9:
            if x2:
                # writer.writerow(['STEM 2'])

                for a in range(len(x2)):
                    if pkg2_6[a]!=0:
                        for aa in range(pkg2_6[a]):
                            count+=1
                            writer.writerow([count,x2[a]+'x6', det2[a][0], det2[a][0]*6+det2[a][1], det2[a][2]])
                    if pkg2_7[a]!=0:
                        for bb in range(pkg2_7[a]):
                            count+=1
                            writer.writerow([count,x2[a]+'x7', det2[a][0], det2[a][0]*7+det2[a][1], det2[a][3]])
                # writer.writerow(['',''])
            if x3:
                for a in range(len(x3)):
                    if pkg3_6[a]!=0:
                        for aa in range(pkg3_6[a]):
                            count+=1
                            writer.writerow([count,x3[a]+'x6', det3[a][0], det3[a][0]*6+det3[a][1], det3[a][2]])
                    if pkg3_7[a]!=0:
                        for bb in range(pkg3_7[a]):
                            count+=1
                            writer.writerow([count,x3[a]+'x7', det3[a][0], det3[a][0]*7+det3[a][1], det3[a][3]])
                # writer.writerow(['',''])
            if x5:
                # writer.writerow(['STEM small'])
                # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
                for a in range(len(x5)):
                    if pkg5_6[a]!=0:
                        for aa in range(pkg5_6[a]):
                            count+=1
                            writer.writerow([count,x5[a]+'x6', det5[a][0], det5[a][0]*6+det5[a][1], det5[a][2]])
                    if pkg5_7[a]!=0:
                        for bb in range(pkg5_7[a]):
                            count+=1
                            writer.writerow([count,x5[a]+'x7', det5[a][0], det5[a][0]*7+det5[a][1], det5[a][3]])
                # writer.writerow(['',''])
            if x9:
                # writer.writerow(['STEM other Propulsion Car'])
                # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
                for a in range(len(x9)):
                    if pkg9_6[a]!=0:
                        for aa in range(pkg9_6[a]):
                            count+=1
                            writer.writerow([count,x9[a]+'x6', det9[a][0], det9[a][0]*6+det9[a][1], det9[a][2]])
                    if pkg9_7[a]!=0:
                        for bb in range(pkg9_7[a]):
                            count+=1
                            writer.writerow([count,x9[a]+'x7', det9[a][0], det9[a][0]*7+det9[a][1], det9[a][3]])
                # writer.writerow(['',''])
        if x4 or x10 or x11:
            if x4:
                # writer.writerow(['STEM Big'])
                # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
                for a in range(len(x4)):
                    if pkg4_3[a]!=0:
                        for aa in range(pkg4_3[a]):
                            count+=1
                            writer.writerow([count,x4[a]+'x3', det4[a][0], det4[a][0]*3+det4[a][1], det4[a][2]])
                    if pkg4_4[a]!=0:
                        for bb in range(pkg4_4[a]):
                            count+=1
                            writer.writerow([count,x4[a]+'x4', det4[a][0], det4[a][0]*4+det4[a][1], det4[a][3]])
                # writer.writerow(['',''])
            if x10:
                # writer.writerow(['STEM Other Princess Castle'])
                # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
                for a in range(len(x10)):
                    if pkg10_3[a]!=0:
                        for aa in range(pkg10_3[a]):
                            count+=1
                            writer.writerow([count,x10[a]+'x3', det10[a][0], det10[a][0]*3+det10[a][1], det10[a][2]])
                    if pkg10_4[a]!=0:
                        for bb in range(pkg10_4[a]):
                            count+=1
                            writer.writerow([count,x10[a]+'x4', det10[a][0], det10[a][0]*4+det10[a][1], det10[a][3]])
                # writer.writerow(['',''])
            if x11:
                # writer.writerow(['STEM Other Dragon Coaster'])
                # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
                for a in range(len(x11)):
                    if pkg11_3[a]!=0:
                        for aa in range(pkg11_3[a]):
                            count+=1
                            writer.writerow([count,x11[a]+'x3', det11[a][0], det11[a][0]*3+det11[a][1], det11[a][2]])
                    if pkg11_4[a]!=0:
                        for bb in range(pkg11_4[a]):
                            count+=1
                            writer.writerow([count,x11[a]+'x4', det11[a][0], det11[a][0]*4+det11[a][1], det11[a][3]])
                # writer.writerow(['',''])
        if x6:
            # writer.writerow(['STEM mini'])
            # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
            for a in range(len(x6)):
                if pkg6_12[a]!=0:
                    for aa in range(pkg6_12[a]):
                        count+=1
                        writer.writerow([count,x6[a]+'x12', det6[a][0], det6[a][0]*12+det6[a][1], det6[a][2]])
                if pkg6_14[a]!=0:
                    for bb in range(pkg6_14[a]):
                        count+=1
                        writer.writerow([count,x6[a]+'x13', det6[a][0], det6[a][0]*13+det6[a][1], det6[a][3]])
            # writer.writerow(['',''])

        # if x1 or x7:
        if x1:
            # writer.writerow(['Edge'])
            # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
            for a in range(len(x1)):
                if pkg1[a]!=0:
                    for aa in range(pkg1[a]):
                        count+=1
                        writer.writerow([count,x1[a]+'x15', det1[a][0], det1[a][0]*15+det1[a][1], det1[a][2]])
            # writer.writerow(['',''])


        if x7:
            # writer.writerow(['Kidzee 1'])
            # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
            for a in range(len(x7)):
                if pkg7[a]!=0:
                    for aa in range(pkg7[a]):
                        count+=1
                        writer.writerow([count,x7[a]+'x10', det7[a][0], det7[a][0]*10+det7[a][1], det7[a][2]])
            # writer.writerow(['',''])

        if x8:
            # writer.writerow(['Kidzee 2'])
            # writer.writerow(['Box number', 'Box content', 'One pc Weight', 'Carton Weight', 'Dimension', 'Actual Carton Weight', 'Actual Dimensions'])
            for a in range(len(x8)):
                if pkg8[a]!=0:
                    for aa in range(pkg8[a]):
                        count+=1
                        writer.writerow([count,x8[a]+'x8', det8[a][0], det8[a][0]*8+det8[a][1], det8[a][2]])

        #  Remaining starts from here


        writer.writerow(['',''])
        writer.writerow(['',''])
        writer.writerow(['',''])
        writer.writerow(['',''])
        writer.writerow(['',''])
        writer.writerow(['Remaining'])
        writer.writerow(['',''])
        print('remaining not working')
        if s1!=0:
            # writer.writerow(['Edge'])
            for i in range(len(rem1)):
                if rem1[i][1]!=0:
                    writer.writerow([str(rem1[i][0])+'X'+str(rem1[i][1]),'Edge'])
            # writer.writerow(['Remaining = '+str(s1)])
            # writer.writerow(['',''])
        print(s2)
        if s2!=0:
            print(rem2)
            print('remaining working')
            # writer.writerow(['STEM 2'])
            for i in range(len(rem2)):
                print(rem2[i])
                if rem2[i][1]!=0:
                    writer.writerow([str(rem2[i][0])+'X'+str(rem2[i][1]),'STEM 2'])
            # writer.writerow(['6pc reqd = '+str(a2),'7pc reqd = '+str(b2),'remaining = '+str(c2)])
            # writer.writerow(['',''])
        if s3!=0:
            # writer.writerow(['STEM other Tinkerer'])
            for i in range(len(rem3)):
                if rem3[i][1]!=0:
                    writer.writerow([str(rem3[i][0])+'X'+str(rem3[i][1]),'STEM other Tinkerer'])
            # writer.writerow(['6pc reqd = '+str(a3),'7pc reqd = '+str(b3),'remaining = '+str(c3)])
            # writer.writerow(['',''])
        if s4!=0:
            writer.writerow(['STEM Big'])
            for i in range(len(rem4)):
                if rem4[i][1]!=0:
                    writer.writerow([str(rem4[i][0])+'X'+str(rem4[i][1]),'STEM Big'])
            # writer.writerow(['3pc reqd = '+str(a4),'4pc reqd = '+str(b4),'remaining = '+str(c4)])
            # writer.writerow(['',''])
        if s5!=0:
            writer.writerow(['STEM Small'])
            for i in range(len(rem5)):
                if rem5[i][1]!=0:
                    writer.writerow([str(rem5[i][0])+'X'+str(rem5[i][1]),'STEM Small'])
            # writer.writerow(['6pc reqd = '+str(a5),'7pc reqd = '+str(b5),'remaining = '+str(c5)])
            # writer.writerow(['',''])
        if s6!=0:
            writer.writerow(['STEM Mini'])
            for i in range(len(rem6)):
                if rem6[i][1]!=0:
                    writer.writerow([str(rem6[i][0])+'X'+str(rem6[i][1]),'STEM Mini'])
            # writer.writerow(['12pc reqd = '+str(a6),'13pc reqd = '+str(b6),'remaining = '+str(c6)])
            # writer.writerow(['',''])

        if s7!=0:
            for i in range(len(rem7)):
                if rem7[i]!=0:
                    writer.writerow([str(x7[i])+'X'+str(s7),'Kidzee 1'])
            # writer.writerow(['Kidzee 1'])
            # writer.writerow([x7+str(s7)])
            # writer.writerow(['',''])

        if s8!=0:
            for i in range(len(rem8)):
                if rem8[i]!=0:
                    writer.writerow([str(x8[i])+'X'+str(s8),'Kidzee 2'])
            # writer.writerow(['Kidzee 2'])
            # writer.writerow(['Remaining = '+str(s8)])
            # writer.writerow(['',''])

        if s9!=0:
            writer.writerow(['STEM other Propulsion Car'])
            for i in range(len(rem9)):
                if rem9[i][1]!=0:
                    writer.writerow([str(rem9[i][0])+'X'+str(rem9[i][1]),'STEM other Propulsion Car'])
            # writer.writerow(['6pc reqd = '+str(a9),'7pc reqd = '+str(b9),'remaining = '+str(c9)])
            # writer.writerow(['',''])
        if s10!=0:
            writer.writerow(['STEM other Princess Castle'])
            for i in range(len(rem10)):
                if rem10[i][1]!=0:
                    writer.writerow([str(rem10[i][0])+'X'+str(rem10[i][1]),'STEM other Princess Castle'])
            # writer.writerow(['3pc reqd = '+str(a10),'4pc reqd = '+str(b10),'remaining = '+str(c10)])
            # writer.writerow(['',''])
        if s11!=0:
            writer.writerow(['STEM other Dragon Coaster'])
            for i in range(len(rem11)):
                if rem11[i][1]!=0:
                    writer.writerow([str(rem11[i][0])+'X'+str(rem11[i][1]),'STEM other Dragon Coaster'])
            # writer.writerow(['3pc reqd = '+str(a11),'4pc reqd = '+str(b11),'remaining = '+str(c11)])
            # writer.writerow(['',''])

        return response
    return render(request, 'production.html')
