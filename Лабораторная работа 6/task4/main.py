import json
INPUT_FILE = "input.csv"

def csv_to_list_dict(path_to_file,delimiter=None) -> list[dict]:
    if delimiter==None:
        delimiter=','
    list_=[]
    with open(path_to_file) as f:
        headers=f.readline()
        headers=headers.split(delimiter)
        headers[-1]=headers[-1][0:-1] #удаление "\n"
        for row in f:
            row=row.split(delimiter)
            row[-1]=row[-1][0:-1]
            dict_={}
            count=0
            for word in headers:
                dict_[word]=row[count]
                count+=1
            list_.append(dict_)
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
