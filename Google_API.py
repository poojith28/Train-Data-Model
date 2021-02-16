import populartimes


def Get_GoogleData(Place_key,
                   API_KEY,
                   Normailze=True,
                   day=0):
    a = populartimes.get_id(API_KEY, Place_key)

    monday = pd.DataFrame(a["populartimes"][day]["data"]).astype(float)

    if not Normailze:

        print(monday)

        return monday

    else:

        pd.set_option("display.precision", 8)

        total = sum(monday[0])

        j = 0

        for i in monday[0]:
            j = j + 1

            monday[0][j - 1] = i / total

        return monday
