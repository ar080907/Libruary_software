a=["Enter or remove books/borrowers",'Classification']
z=['remove books','add books','remove borrowers','add borrowers']
b=str(input("Enter or remove books/borrowers or Classification: "))
d=["Fiction","Nonfiction"]
v=['Books','Borrowers']

if(b not in a):
    print("Invalid Entry")
elif(b=="Enter or remove books/borrowers"):
      
      print(z)
      y=str(input('Choose one of the options: '))
      if y not in z:
        raise IndexError("invalid appraoch")
      else:
          if y==z[1] :
                x=str(input("Fiction or Nonfiction: "))
                if x==d[0]:
                 import pickle
                 try:
                   with open("libruary software/fiction.pkl", "rb") as fr:
                    f=pickle.load(fr)
                    f.append(input("book: "))
                 except:
                   f=[]
                   f.append(input("book: "))


                 with open("libruary software/fiction.pkl", "wb") as fr:
                  pickle.dump(f, fr)
                elif x==d[1]:
                 import pickle
                 try:
                  with open("libruary software/nonfiction.pkl", "rb") as fr:
                   n=pickle.load(fr)
                   n.append(input("book: "))
                 except:
                  n=[]
                  n.append(input("book: "))
                 with open("libruary software/nonfiction.pkl", "wb") as fr:
                  pickle.dump(n, fr)
                else:
                  raise IndexError('Invaid Approach')
          elif y==z[0]:
             x=str(input("Fiction or Nonfiction: "))
             if x==d[0]:
                 import pickle
                 try:
                   with open("libruary software/fiction.pkl", "rb") as fr:
                    f=pickle.load(fr)
                    f.remove(input("book: "))
                 except:
                   f=[]
                 with open("libruary software/fiction.pkl", "wb") as fr:
                  pickle.dump(f, fr)
             elif x==d[1]:
                 import pickle
                 try:
                  with open("libruary software/nonfiction.pkl", "rb") as fr:
                   n=pickle.load(fr)
                   n.remove(input("book: "))
                 except:
                  n=[]
                  
                 with open("libruary software/nonfiction.pkl", "wb") as fr:
                  pickle.dump(n, fr)
             else:
                  raise IndexError('Invaid Approach')
          elif y==z[3]:
             x=str(input("Fiction or Nonfiction: "))
             bk=str(input('book'))
             br=str(input("borrower"))
             if x==d[0]:
                 import pickle
                 try:
                   with open("libruary software/fiction borrower.pkl", "rb") as fr:
                    f=pickle.load(fr)
                   f.append(f'{bk} is borrowed by {br}')
                 except:
                   f=[]
                   f.append(f'{bk} is borrowed by {br}')
                   with open("libruary software/fiction borrower.pkl", "wb") as fr:
                      pickle.dump(f, fr)
             elif x==d[1]:
                 import pickle
                 try:
                  with open("libruary software/nonfiction borrower.pkl", "rb") as fr:
                   n=pickle.load(fr)
                   n.append(f'{bk} is borrowed by {br}')
                 except:
                  n=[]
                  n.append(f'{bk} is borrowed by {br}')
                 with open("libruary software/nonfiction borrower.pkl", "wb") as fr:
                  pickle.dump(n, fr)
             else:
                  raise IndexError('Invaid Approach')
          elif y==z[2]:
                x=str(input("Fiction or Nonfiction: "))
                bk=str(input('book: '))
                br=str(input("borrower: "))

                if x==d[0]:
                 import pickle
                 try:
                   with open("libruary software/fiction borrower.pkl", "rb") as fr:
                    f=pickle.load(fr)
                    f.remove(f'{bk} is borrowed by {br}')
                 except:
                   f=[]
                   


                 with open("libruary software/fiction borrower.pkl", "wb") as fr:
                  pickle.dump(f, fr)
                elif x==d[1]:
                 import pickle
                 try:
                  with open("libruary software/nonfiction borrower.pkl", "rb") as fr:
                   n=pickle.load(fr)
                   n.remove(f'{bk} is borrowed by {br}')
                 except:
                  n=[]
                  
                 with open("libruary software/nonfiction borrower.pkl", "wb") as fr:
                  pickle.dump(n, fr)
                else:
                  raise IndexError('Invaid Approach')
else:
    cl=str(input('Books or Borrowers: '))
    if cl not in v:
      raise IndexError('Invalid Appraoch')
    elif cl=='Books':
     g=input("Fiction or Nonfiction: ")
     if(g not in d):
        print("Invalid input")
     elif(g=="Fiction"):
        import pickle
        try:
         with open("libruary software/fiction.pkl", "rb") as fr:
          f=pickle.load(fr)
        except:
           f=[]
        

        print(f)

     else:
      import pickle
     try:
      with open("libruary software/nonfiction.pkl", "rb") as fr:
       n=pickle.load(fr)
     except:
      n=[]
     print(n)
    else:
      g=input("Fiction or Nonfiction: ")
      if(g not in d):
        print("Invalid input")
      elif(g=="Fiction"):
        import pickle
        try:
         with open("libruary software/fiction borrower.pkl", "rb") as fr:
          f=pickle.load(fr)
        except:
           f=[]
        print(f)

      else:
       import pickle
       try:
          with open("libruary software/nonfiction borrower.pkl", "rb") as fr:
           n=pickle.load(fr)
       except:
          n=[]
       print(n)




