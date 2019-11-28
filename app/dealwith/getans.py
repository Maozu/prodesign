def JOJO(jsonData):
    import json
    lis = []
    text = json.loads(jsonData)
    print(type(jsonData))
    print(type(text))
    for k in text["Results"][0]["Candidates"]:
        L = text["Results"][0]["Candidates"]
    print(L)
    for k in L:
        en = []
        if (k['Score'] > 10):
            en.append(k['PersonId'])
            en.append(k['Score'])
            lis.append(en)
    return lis
