def introduce(GuestA,GuestB):
    print(GuestA,"I'd like to introduce you to", GuestB)
    print(GuestB, "meet", GuestA)
    

def dinnerParty(listofGuests):
    for guestx in listofGuests:
        for guesty in listofGuests:
            introduce(guestx, guesty)

print(dinnerParty([0,1,2,3]))


