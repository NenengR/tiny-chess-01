import json,os,sys,urllib.request
sys.setrecursionlimit(9**4)
A=os.environ["MAKEFUN_ENV_URL"]
V=dict(p=100,n=320,b=330,r=500,q=900,k=0)
D=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
N=((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
F="abcdefgh";DM={"n":N,"b":D[4:],"r":D[:4],"q":D,"k":D}
C=[0];M=12000;MT=10000
def P(s):
 p=s.split();B={}
 for y,z in enumerate(p[0].split("/")):
  x=0
  for q in z:
   if q.isdigit():x+=int(q)
   else:B[7-y,x]=q;x+=1
 return B,p[1],p[2],None if p[3]=="-"else(int(p[3][1])-1,F.index(p[3][0]))
def H(B,r,f,w):
 if any(B.get((r+1-2*w,f+y))=="pP"[w]for y in(-1,1)):return 1
 if any((z:=B.get((r+a,f+b)))and z.isupper()==w and z.lower()==("n"if(a,b)in N else"k")for a,b in N+D):return 1
 for a,b in D:
  x,y=r+a,f+b;t="RQ"if a*b==0 else"BQ"
  while 0<=x<8 and 0<=y<8:
   z=B.get((x,y))
   if z:
    if z.isupper()==w and z.upper()in t:return 1
    break
   x+=a;y+=b
def MV(B,m,c):
 (r,f),(x,y),q=m;p=B[r,f];n=dict(B);z=n.pop((x,y),None)
 if p in"pP"and f!=y and not z:n.pop((r,y),None)
 n[x,y]=("Q"if p=="P" else"q")if q else p;del n[r,f];e=None
 if p in"pP"and abs(x-r)==2:e=(r+x>>1,f)
 if p in"Kk":c=c.replace(p,"").replace("Qq"[p=="k"],"")
 if p in"Kk"and abs(y-f)==2:n[r,5 if y>f else 3]=n.pop((r,7 if y>f else 0))
 for a,b,d in((0,7,"K"),(0,0,"Q"),(7,7,"k"),(7,0,"q")):
  if(a,b)in((r,f),(x,y)):c=c.replace(d,"")
 return n,c,e
def G(B,t,c,e):
 w=t=="w";o=[]
 for(r,f),p in B.items():
  if p.isupper()!=w:continue
  x=p.lower();s=(r,f)
  if x=="p":
   d=2*w-1;k=7*w
   if(r+d,f)not in B:
    o.append((s,(r+d,f),"q"if r+d==k else""))
    if r==6-5*w and(r+2*d,f)not in B:o.append((s,(r+2*d,f),""))
   for y in(f-1,f+1):
    if 0<=y<8 and((z:=B.get((r+d,y)))is None and(r+d,y)==e or z and z.isupper()!=w):
     o.append((s,(r+d,y),"q"if z and r+d==k else""))
  else:
   for a,b in DM[x]:
    rr,ff=r+a,f+b
    while 0<=rr<8 and 0<=ff<8 and not((z:=B.get((rr,ff)))and z.isupper()==w):
     o.append((s,(rr,ff),""))
     if z or x not in"brq":break
     rr+=a;ff+=b
 rk=7-7*w;R="R"if w else"r"
 for z,kt,rf,es,at in(("K"if w else"k",6,7,(5,6),(4,5,6)),("Q"if w else"q",2,0,(1,2,3),(4,3,2))):
  if z in c and B.get((rk,rf))==R and B.get((rk,4))==("K"if w else"k")and not any(B.get((rk,s))for s in es)and not any(H(B,rk,s,not w)for s in at):o.append(((rk,4),(rk,kt),""))
 for m in o[:]:
  n=MV(B,m,c)[0];k=next(s for s,z in n.items()if z==("K"if w else"k"))
  if H(n,*k,not w):o.remove(m)
 return o
def pv(x,r,f,eg):
 c=min(r,7-r)+min(f,7-f)
 return 8*r if x=="p" else 6*c-30 if x=="n" else 5*c-20 if x=="b" else 3*c+8*(r==6)-10 if x=="r" else 4*c-15 if x=="q" else 10*c-45 if eg else -8*c+20
def E(B):
 nm=sum(V[p.lower()]for p in B.values()if p.lower()not in"pk")
 s=0
 for(r,f),p in B.items():
  x=p.lower();g=1 if p.isupper()else-1
  s+=g*(V[x]+pv(x,r if g>0 else 7-r,f,nm<1300))
  if x=="k"and nm>=1300:s+=g*12*bool(B.get((r+g,f))==("P"if g>0 else"p"))
  if x=="b":s+=30*g
 return s
def S(B,t,c,e,d,a,b,ex,pl):
 C[0]+=1
 if C[0]>M:1/0
 w=t=="w"
 k=next(s for s,z in B.items()if z==("K"if w else"k"))
 ch=H(B,*k,not w)
 if ch and ex<2:d+=1;ex+=1
 if d<=0:return E(B)*(1 if w else-1)
 o=G(B,t,c,e)
 if not o:return-(MT+pl)if ch else 0
 o.sort(key=lambda m:-(9**7 if m[2]else 7**7+10*V[z.lower()]-V[B[m[0]].lower()]if(z:=B.get(m[1]))else 0))
 al=a
 for m in o:
  n,cc,ee=MV(B,m,c)
  s=-S(n,"wb"[w],cc,ee,d-1,-b,-al,ex,pl+1)
  if s>al:al=s
  if al>=b:break
 return al
def R(B,t,c,e):
 w=t=="w";o=G(B,t,c,e);b=o[0]if o else((0,0),(0,0),"")
 for d in range(1,9):
  C[0]=0;al=-99999;m2=b
  try:
   for m in o:
    n,cc,ee=MV(B,m,c)
    s=-S(n,"wb"[w],cc,ee,d-1,-99999,-al,0,1)
    if s>al:al=s;m2=m
  except:break
  b=m2;o.remove(m2);o.insert(0,m2)
 return b
def W(m):
 (r,f),(x,y),q=m;return f"{F[f]}{r+1}{F[y]}{x+1}{q}"
def post(p,b):
 q=urllib.request.urlopen(A+p,json.dumps(b).encode());return json.load(q)
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  B,t,c,e=P(g["fen"]);m=W(R(B,t,c,e));g=post("/move",{"game":g["game"],"move":m if m in g["legal_moves"]else g["legal_moves"][0]})
