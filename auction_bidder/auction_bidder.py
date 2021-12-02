def auction_bidder(initial_price,instant_buy_price, list_of_bids):
    winner_price = initial_price
    bidder_history = []
    highest_bidder_name = "-"
    bidder_history.append(highest_bidder_name + "," +  str(winner_price))
    current_maximum_bid = initial_price
    for bid in list_of_bids:
        if highest_bidder_name == "-":
            current_maximum_bid = bid[1]
            highest_bidder_name = bid[0]
            bidder_history.append(bid[0] + "," + str(winner_price))
            if instant_buy_price !=0 and winner_price >= instant_buy_price:
                print("sajt  " + ",".join(bidder_history))
                return ",".join(bidder_history)
        elif bid[1] > current_maximum_bid:
            if highest_bidder_name != bid[0]:
                if instant_buy_price !=0 and current_maximum_bid >= instant_buy_price:
                    bidder_history.append(highest_bidder_name + "," + str(instant_buy_price))
                    print("instant buyout: " + ",".join(bidder_history))
                    return ",".join(bidder_history)
                winner_price = current_maximum_bid +1
                bidder_history.append(bid[0] + "," + str(winner_price))
            current_maximum_bid = bid[1]
            highest_bidder_name = bid[0]
        elif bid[1] == current_maximum_bid:
            if len(bidder_history) == 1:
                highest_bidder_name = bid[0]
            if instant_buy_price !=0 and current_maximum_bid >= instant_buy_price:
                bidder_history.append(highest_bidder_name + "," + str(instant_buy_price))
                print("instant buyout: " + ",".join(bidder_history))
                return ",".join(bidder_history)
            winner_price = current_maximum_bid
            bidder_history.append(highest_bidder_name + "," + str(winner_price))
        elif bid[1] < current_maximum_bid:
            winner_price = bid[1] + 1
            if instant_buy_price !=0 and winner_price >= instant_buy_price:
                bidder_history.append(highest_bidder_name + "," + str(instant_buy_price))
                print("instant buyout: " + ",".join(bidder_history))
                return ",".join(bidder_history)
            bidder_history.append(highest_bidder_name + "," + str(winner_price))
    print(",".join(bidder_history))
    return ",".join(bidder_history)

#1,15,A,5,B,10,A,8,A,14,A,17,B,17
auction_bidder(1,15, [["A",5],["B",10],["A",8],["A", 14],["A",17],["B",17]])


#1,nepper,15,hamster,24,philipp,30,mmautne,31,hamster,49,hamster,55,thebenil,57,fliegimandi,59,ev,61,philipp,64,philipp,65,ev,74,philipp,69,philipp,71,fliegimandi,78,hamster,78,mio,95,hamster,103,macquereauxpl,135
auction_bidder(1,0,[["nepper",15],["hamster",24],["philipp",30],["mmautne",31],["hamster",49],["hamster", 55],["thebenil",57],["fliegimandi",59],["ev",61],["philipp",64],["philipp",65],["ev",74],["philipp",69],["philipp",71],["fliegimandi",78],["hamster",78],["mio",95],["hamster",103],["macquereauxpl",135]])

#auction_bidder(1,[["cable",5],["ente",10],["karl",19],["moehe",14],["moehe",23],["michbex",24],["melloy",25],["achi",26]])

#auction_bidder(1,[["cable",5],["ente",10],["karl",19],["moehe",23],["michbex",24],["melloy",29],["achi",26]])

#auction_bidder(15, [["urtyp",17],["neuli",16],["schlurchi",25],["tokay",75],["horni",35],["sue",60],["sue",65],["gap",70]])

#100,A,100,A,115,A,119,A,144,A,145,A,157,A,158,A,171,A,179,A,194,A,206,A,207,A,227,A,229,A,231,A,234
#auction_bidder(100,[["A",100],["A",115],["A",119],["A",144],["A",145],["A",157],["A",158],["A",171],["A",179],["A",194],["A",206],["A",207],["A",227],["A",229],["A",231],["A",234]])

#100,0, C,100,C,115,C,119,C,121,C,144,C,154,C,157,G,158,C,171,C,179,C,194,C,206,C,214,C,227,C,229,C,231,C,298
auction_bidder(100,0,[["C",100],["C",115],["C",119],["C",121],["C",144],["C",154],["C",157],["G",158],["C",171],["C",179],["C",194],["C",206],["C",214],["C",227],["C",229],["C",231],["C",298]])


#100,C,100,C,115,C,119,C,121,C,144,C,154,C,157,G,158,C,171,C,179,C,194,C,206,C,214,C,227,C,229,C,231,C,298
auction_bidder(100,325,[["C",100],["C",115],["C",119],["C",121],["C",144],["C",154],["C",157],["G",158],["C",171],["C",179],["C",194],["C",206],["C",214],["C",227],["C",229],["C",231],["C",298]])

#100,160,C,100,C,115,C,119,C,121,C,144,C,154,C,157,G,158,C,171,C,179,C,194,C,206,C,214,C,227,C,229,C,231,C,298
auction_bidder(100,160,[["C",100],["C",115],["C",119],["C",121],["C",144],["C",154],["C",157],["G",158],["C",171],["C",179],["C",194],["C",206],["C",214],["C",227],["C",229],["C",231],["C",298]])


#1,120,6a,17,kl,5,kl,10,kl,15,cs,28,kl,20,kl,25,hr,35,hr,40,hr,41,hl,42,hr,43,hr,44,hl,44,hl,49,hr,47
auction_bidder(1,120,[["6a", 17], ["kl", 5], ["kl", 10], ["kl", 15], ["cs",28], ["kl",20],["kl", 25],["hr", 35],["hr",40],["hr",41],["hl",42],["hr",43],["hr",44],["hl",44],["hl",49],["hr",47]])

#1,47,6a,17,kl,5,kl,10,kl,15,cs,28,kl,20,kl,25,hr,35,hr,40,hr,41,hl,42,hr,43,hr,44,hl,44,hl,49,hr,47
auction_bidder(1,47,[["6a", 17], ["kl", 5], ["kl", 10], ["kl", 15], ["cs",28], ["kl",20],["kl", 25],["hr", 35],["hr",40],["hr",41],["hl",42],["hr",43],["hr",44],["hl",44],["hl",49],["hr",47]])

#15,urtyp,15
#auction_bidder(15,[["urtyp",15]])

#1,rx,50,aa,2000,de,3558,einseins,3999,ek,4999,yd,8332,lb,5000,lb,6000,lb,7000,lb,8000,lb,8999,yd,9999,zn,11000,ir,11110,nr,12999,kt,12567,kt,12667,kt,13000,go,14000,ym,14999,hm,15400,nr,15690,nr,17000,td,18500,kt,18750,uy,18850,hr,18999,td,19049,st,19200
#auction_bidder(1, [["rx", 50], ["aa", 2000], ["de", 3558], ["einseins", 3999], ["ek", 4999], ["yd", 8332], ["lb", 5000],["lb", 6000],["lb", 7000], ["lb", 8000], ["lb", 8999], ["yd",9999],["zn",11000], ["ir",11110],["nr",12999],["kt",12567],["kt",12667],["kt",13000],["go",14000],["ym",14999],["hm",15400],["nr",15690],["nr",17000],["td",18500],["kt",18750],["uy",18850],["hr",18999],["td",19049],["st",19200]])