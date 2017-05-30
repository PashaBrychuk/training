def find_message(text):
    if len(text)>0:
        res = ""
        for i in text:
            if i.isupper() == True:
                res = res +i
        return res
    return ""


s = "Poimali Okunya Darom Oknom"
print find_message(s)