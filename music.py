handlookupSB = {"2.5x/cont" : ["aa","aks","aqs","ajs","ats","a9s", "kk", "kqs", "qq" , "ajo",
                              "ato", "99", "88", "77", "66"],
               "2.5x/fold"  : ["k7s","k6s","k5s","k4s","k3s","k2s","q6s","q5s","q4s","q3s",
                              "q2s","j6s","t6s","96s","86s","76s","75s","65s","64s","54s",
                              "53s","43s","87o","76o","65o","a6o","a5o","a4o","a3o", "a2o",],
               "limp/shove" : ["a5s","a4s","a3s","a2s","ako","aqo","jj","tt","55","44",
                               "33","22"],
               "limp/call"  : ["a8s","a7s","a6s","kjs","kts","k9s","k8s","kqo","qjs","qts",
                               "q9s","q8s","q7s","kjo","qjo","jts","j9s","j8s","j7s","kto","qto","jto","t9s","t8s",
                               "t7s","a9o","k9o","q9o","j9o","t9o","98s","97s","a8o","98o","87s","a7o",],
               "limp/fold"  : ["j5s","j4s","j3s","j2s","t5s","t4s","95s","94s","k8o","q8o","j8o","t8o","85s","84s","k7o",
                               "q7o","j7o","t7o","97o","74s","k6o","86o","63s","k5o","52s","42s","32s"]
               }
handlookupBU = {"min-raise/call" : ["aa","aks","aqs","ajs","ats","a9s","ako","kk","kqs","aqo","qq","ajo","jj","ato","tt",
                                    "99","88","77","66","55"],
                "min-raise/fold" : ["a8s","a7s","a6s","a5s","a4s","a3s","a2s","kjs","kts","k9s","k8s","k7s","k6s","k5s",
                                    "k4s","kqo","qjs","qts","q9s","q8s","q7s","q6s","q5s","kjo","qjo","jts","j9s",
                                    "j8s","j7s","j6s","kto","qto","jto","t9s","t8s","t7s","t6s","a9o","k9o","q9o","j9o",
                                    "t9o","98s","97s","96s","a8o","98o","87s","86s","a7o","76s","75s","a6o","65s","a5o",
                                    "54s","a4o","44","33","22",]
                }
handlookupBB = {"2.5x 3bet/call" : ["aa","kk","qq"],
                "2.5x 3bet/fold" : ["k6o","k5o"],
                "all-in 3bet"    : ["aks","aqs","ajs","ats","a9s","a8s","a7s","a6s","a5s","ako","kqs","aqo","qjs","qts",
                                    "ajo","jj","jts","j9s","ato","tt","t9s","a9o","99","98s","a8o","88","87s","a7o",
                                    "77","76s","a6o","66","55","44","33","22"],
                "fold"           : ["q6o","j6o","t6o","96o","q5o","j5o","t5o","95o","85o","k4o","q4o","j4o","t4o","94o",
                                    "84o","k4o","q4o","j4o","t4o","94o","84o","74o","k3o","q3o","j3o","t3o","93o","83o",
                                    "73o","63o","53o","43o","k2o","q2o","j2o","t2o","92o","82o","72o","62o","52o","42o",
                                    "32o",]
                }

nashpush =     {"aa":"20+","aks":"20+","aqs":"20+","ajs":"20+","ats":"20+","a9s":"20+","a8s":"20+","a7s":"20+","a6s":"20+","a5s":"20+","a4s":"20+","a3s":"20+",
                "a2s":"20+","ako":"20+","kk":"20+","kqs":"20+","kjs":"20+","kts":"20+","k9s":"20+","k8s":"20+","k7s":"20+","k6s":"20+","k5s":"20+","k4s":"20+",
                "k3s":"19.9","k2s":"19.3","aqo":"20+","kqo":"20+","qq":"20+","qjs":"20+","qts":"20+","q9s":"20+","q8s":"20+","q7s":"20+","q6s":"20+","q5s":"20+",
                "q4s":"16.3","q3s":"13.5","q2s":"12.7","ajo":"20+","kjo":"20+","qjo":"20+","jj":"20+","jts":"20+","j9s":"20+","j8s":"20+","j7s":"20+","j6s":"18.6",
                "j5s":"14.7","j4s":"13.5","j3s":"10.6","j2s":"8.5","ato":"20+","kto":"20+","qto":"20+","jto":"20+","tt":"20+","t9s":"20+","t8s":"20+","t7s":"20+",
                "t6s":"20+","t5s":"11.9","t4s":"10.5","t3s":"7.7","t2s":"6.5","a9o":"20+","k9o":"20+","q9o":"20+","j9o":"20+","t9o":"20+","99":"20+","98s":"20+",
                "97s":"20+","96s":"20+","95s":"14.4","94s":"6.9","93s":"4.9","92s":"3.7","a8o":"20+","k8o":"18.0","q8o":"13.0","j8o":"13.3","t8o":"17.5","98o":"20+",
                "88":"20+","87s":"20+","86s":"20+","85s":"18.8","84s":"10.1","83s":"2.7","82s":"2.5","a7o":"20+","k7o":"16.1","q7o":"10.3","j7o":"8.5","t7o":"9.0",
                "97o":"10.8","87o":"14.7","77":"20+","76s":"20+","75s":"20+","74s":"13.9","73s":"2.5","72s":"2.1","a6o":"20+","k6o":"15.1","q6o":"9.6","j6o":"6.5",
                "t6o":"5.7","96o":"5.2","86o":"7.0","76o":"10.7","66":"20+","65s":"20+","64s":"16.3","63s":"*","62s":"2.0","a5o":"20+","k5o":"14.2","q5o":"8.9",
                "j5o":"6.0","t5o":"4.1","95o":"3.5","85o":"3.0","75o":"2.6","65o":"2.4","55":"20+","54s":"20+","53s":"**","52s":"2.0","a4o":"20+","k4o":"13.1",
                "q4o":"7.9","j4o":"5.4","t4o":"3.8","94o":"2.7","84o":"2.3","74o":"2.1","64o":"2.0","54o":"2.1","44":"20+","43s":"***","42s":"1.8","a3o":"20+",
                "k3o":"12.2","q3o":"7.5","j3o":"5.0","t3o":"3.4","93o":"2.5","83o":"1.9","73o":"1.","63o":"1.7","53o":"1.8","43o":"1.6","33":"20+","32s":"1.7",
                "a2o":"20+","k2o":"11.6","q2o":"7.0","j2o":"4.6","t2o":"2.9","92o":"2.2","82o":"1.8","72o":"1.6","62o":"1.5","52o":"1.5","42o":"1.4","32o":"1.4",
                "22": "20+"}

nashcall =     {"aa":"20+","aks":"20+","aqs":"20+","ajs":"20+","ats":"20+","a9s":"20+","a8s":"20+","a7s":"20+","a6s":"20+","a5s":"20+","a4s":"20+","a3s":"20+",
                "a2s":"20+","ako":"20+","kk":"20+","kqs":"20+","kjs":"20+","kts":"20+","k9s":"20+","k8s":"17.6","k7s":"15.2","k6s":"14.3","k5s":"13.2","k4s":"12.4",
                "k3s":"11.4","k2s":"10.7","aqo":"20+","kqo":"20+","qq":"20+","qjs":"20+","qts":"20+","q9s":"16.1","q8s":"13.0","q7s":"10.5","q6s":"9.9","q5s":"8.9",
                "q4s":"8.4","q3s":"7.8","q2s":"7.2","ajo":"20+","kjo":"20+","qjo":"19.5","jj":"20+","jts":"18.0","j9s":"13.4","j8s":"10.6","j7s":"8.8","j6s":"7.0",
                "j5s":"6.9","j4s":"6.1","j3s":"5.8","j2s":"5.6","ato":"20+","kto":"20+","qto":"15.3","jto":"12.7","tt":"20+","t9s":"11.5","t8s":"9.3","t7s":"7.4",
                "t6s":"6.3","t5s":"5.2","t4s":"5.2","t3s":"4.8","t2s":"4.5","a9o":"20+","k9o":"17.1","q9o":"11.7","j9o":"9.5","t9o":"8.4","99":"20+","98s":"8.2",
                "97s":"7.0","96s":"5.8","95s":"5.0","94s":"4.3","93s":"4.1","92s":"3.9","a8o":"20+","k8o":"13.8","q8o":"9.7","j8o":"7.6","t8o":"6.6","98o":"6.0",
                "88":"20+","87s":"6.5","86s":"5.6","85s":"4.8","84s":"4.1","83s":"3.6","82s":"3.5","a7o":"20+","k7o":"12.4","q7o":"8.0","j7o":"6.4","t7o":"5.5",
                "97o":"5.0","87o":"4.7","77":"20+","76s":"5.4","75s":"4.8","74s":"4.1","73s":"3.6","72s":"3.3","a6o":"20+","k6o":"11.0","q6o":"7.3","j6o":"5.4",
                "t6o":"4.6","96o":"4.2","86o":"4.1","76o":"4.0","66":"20+","65s":"4.9","64s":"4.3","63s":"3.8","62s":"3.3","a5o":"20+","k5o":"10.2","q5o":"6.8",
                "j5o":"5.1","t5o":"4.0","95o":"3.7","85o":"3.6","75o":"3.6","65o":"3.7","55":"20+","54s":"4.6","53s":"4.0","52s":"3.6","a4o":"18.3","k4o":"9.1",
                "q4o":"6.2","j4o":"4.7","t4o":"3.8","94o":"3.3","84o":"3.2","74o":"3.2","64o":"3.3","54o":"3.5","44":"20+","43s":"3.8","42s":"3.4","a3o":"16.6",
                "k3o":"8.7","q3o":"5.9","j3o":"4.5","t3o":"3.6","93o":"3.1","83o":"2.9","73o":"2.9","63o":"2.9","53o":"3.1","43o":"3.0","33":"20+","32s":"3.3",
                "a2o":"15.8","k2o":"8.1","q2o":"5.6","j2o":"4.2","t2o":"3.5","92o":"3.0","82o":"2.8","72o":"2.6","62o":"2.7","52o":"2.8","42o":"2.7","32o":"2.6",
                "22": "15.0"}
while True:
    s = 0
    hand = input(">> ")
    if hand[0:2] == "sb":
        for i in handlookupSB:
            if hand[3:] in handlookupSB[i]:
                print(i)
                s = 1

        if s == 0:
            print("fold")

    if hand[0:2] == "bu":
        for i in handlookupSB:
            if hand[3:] in handlookupSB[i]:
                print(i)
                s = 1

        if s == 0:
            print("fold")

    if hand[0:2] == "bb":
        for i in handlookupSB:
            if hand[3:] in handlookupSB[i]:
                print(i)
                s = 1

        if s == 0:
            print("call")

    if hand[0:2] == "np":

        print(nashpush[hand[3:]])

    if hand[0:2] == "nc":

        print(nashcall[hand[3:]])
