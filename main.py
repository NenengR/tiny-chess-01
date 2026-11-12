import json,os,urllib.request
A=os.environ["MAKEFUN_ENV_URL"]
V={"p":100,"n":320,"b":330,"r":500,"q":900,"k":0}
D=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
N=((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
F="abcdefgh"
def P(s):
 p=s.split();B={}
 for y,z in enumerate(p[0].split("/")):
  x=0
  for q in z:
   if q.isdigit():x+=int(q)
   else:B[(7-y,x)]=q;x+=1
 return B,p[1],p[2],None if p[3]=="-"else(int(p[3][1])-1,F.index(p[3][0]))
def H(B,r,f,w):
 for y in(-1,1):
  if B.get((r-1 if w else r+1,f+y))==("P" if w else"p"):return 1
 for a,b in N+D:
  if B.get((r+a,f+b))==(("N" if w else"n")if(a,b)in N else("K" if w else"k")):return 1
 for a,b in D:
  x,y=r+a,f+b
  while 0<=x<8 and 0<=y<8:
   z=B.get((x,y))
   if z:
    if(a*b==0 and z in("R" if w else"r","Q" if w else"q"))or(a*b and z in("B" if w else"b","Q" if w else"q")):return 1
    break
   x+=a;y+=b
 return 0
def MV(B,m,c):
 (r,f),(x,y),q=m;p=B[(r,f)];n=dict(B);z=n.pop((x,y),None)
 if p in"pP"and f!=y and z is None:n.pop((r,y))
 n[(x,y)]=("Q" if p=="P" else"q")if q else p;del n[(r,f)];e=None
 if p in"pP"and abs(x-r)==2:e=((r+x)//2,f)
 if p in"Kk":c=c.replace(p,"").replace("Q" if p=="K" else"q","")
 if p in"Kk"and abs(y-f)==2:n[(r,5 if y>f else 3)]=n.pop((r,7 if y>f else 0))
 for s,d in(((0,7),"K"),((0,0),"Q"),((7,7),"k"),((7,0),"q")):
  if s in((r,f),(x,y)):c=c.replace(d,"")
 return n,c,e
def G(B,t,c,e):
 w=t=="w";o=[]
 for s,p in B.items():
  if p.isupper()!=w:continue
  r,f=s;x=p.lower()
  if x=="p":
   d=1 if w else-1;k=7 if w else 0
   if(r+d,f)not in B:
    o.append((s,(r+d,f),"q" if r+d==k else""))
    if r==(1 if w else 6)and(r+2*d,f)not in B:o.append((s,(r+2*d,f),""))
   for y in(f-1,f+1):
    if 0<=y<8:
     z=B.get((r+d,y))
     if z is None:
      if(r+d,y)==e:o.append((s,(r+d,y),""))
     elif z.isupper()!=w:o.append((s,(r+d,y),"q" if r+d==k else""))
  elif x=="n"or x=="k":
   for a,b in(N if x=="n" else D):
    rr,ff=r+a,f+b
    if 0<=rr<8 and 0<=ff<8 and(B.get((rr,ff))is None or B[rr,ff].isupper()!=w):o.append((s,(rr,ff),""))
  else:
   for a,b in(D if x=="q" else D[:4]if x=="r" else D[4:]):
    rr,ff=r+a,f+b
    while 0<=rr<8 and 0<=ff<8:
     z=B.get((rr,ff))
     if z is None:o.append((s,(rr,ff),""))
     else:
      if z.isupper()!=w:o.append((s,(rr,ff),""))
      break
     rr+=a;ff+=b
 rk=0 if w else 7;R="R" if w else"r"
 for z,kt,rf,es,at in((("K" if w else"k"),6,7,(5,6),(4,5,6)),(("Q" if w else"q"),2,0,(1,2,3),(4,3,2))):
  if z in c and B.get((rk,rf))==R and all(B.get((rk,s))is None for s in es)and not any(H(B,rk,s,not w)for s in at):o.append(((rk,4),(rk,kt),""))
 for m in o[:]:
  B2,c2,e2=MV(B,m,c);k=[s for s,z in B2.items() if z==("K" if w else"k")][0]
  if H(B2,k[0],k[1],not w):o.remove(m)
 return o
def E(B):
 s=0
 for (r,f),p in B.items():
  x=p.lower();v=V[x];g=1 if p.isupper() else-1
  if x=="p":v+=6*(r-1 if p=="P" else 6-r)
  s+=g*v
 return s
C=[0]
def T(o,B):o.sort(key=lambda m:-V[(B.get(m[1])or"p").lower()])
def S(B,t,c,e,d,a,b):
 C[0]+=1
 if C[0]>10000:raise Exception
 w=t=="w";o=G(B,t,c,e)
 if not o:
  k=[s for s,z in B.items() if z==("K" if w else"k")][0]
  return-9999-d if H(B,k[0],k[1],not w)else 0
 if d<=0:
  s=E(B)*(1 if w else-1)
  if s>=b:return b
  if s>a:a=s
 T(o,B)
 for m in o:
  if d<=0 and B.get(m[1])is None and not m[2]:continue
  B2,c2,e2=MV(B,m,c);s=-S(B2,"b" if w else"w",c2,e2,d-1,-b,-a)
  if s>a:a=s
  if a>=b:break
 return a
def R(B,t,c,e):
 w=t=="w";o=G(B,t,c,e)
 T(o,B)
 b=o[0]if o else((0,0),(0,0),"")
 for d in(1,2,3,4,5):
  C[0]=0;v=-99999;m2=b
  try:
   for m in o:
    B2,c2,e2=MV(B,m,c);s=-S(B2,"b" if w else"w",c2,e2,d-1,-99999,99999)
    if s>v:v=s;m2=m
  except Exception:break
  b=m2
  if C[0]>9000:break
 return b
def W(m):
 (r,f),(x,y),q=m;return F[f]+str(r+1)+F[y]+str(x+1)+q
def post(p,b):
 q=urllib.request.urlopen(A+p,json.dumps(b).encode());return json.load(q)
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  B,t,c,e=P(g["fen"]);m=W(R(B,t,c,e));g=post("/move",{"game":g["game"],"move":m if m in g["legal_moves"]else g["legal_moves"][0]})
