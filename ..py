def no_notes(a):
    Q = [5000, 1000, 500, 100, 50, 20, 10, 1]
    X = 0
    for i in range(8):
        q =Q[i]
        x = a//q
        print("Notes of {} = {}".format(q, x))
        a = a%q 

amount = int(input("Enter Amount"))
no_notes(amount)
