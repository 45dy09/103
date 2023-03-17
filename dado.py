import random
response="x"
while response=="x":
    n=random.randint (1,6)
    if n==1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    if n==2:
        print("[0    ]")
        print("[     ]")
        print("[    0]")
    if n==3:
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
    if n==4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    if n==5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    if n==6:
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
    response=input("presiona x para girar ")
    print("\n")
