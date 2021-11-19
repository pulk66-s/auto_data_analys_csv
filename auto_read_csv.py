import pandas as pd

def read_csv():
    csv_path = csv_content = ""
    csv_ok = False
    while csv_path == "" or not csv_ok:
        csv_path = input("csv path : ")
        csv_sep = input("csv sep : ")
        try:
            csv_content = pd.read_csv(csv_path, sep=csv_sep)
            csv_ok = True
        except:
            pass
    return pd.DataFrame(csv_content)

def get_column_list(df):
    input_col = ""
    col_list = []
    while input_col != "end":
        input_col = input("column to read : ")
        if not input_col in df.columns.values:
            print(f"column : {input_col} not in csv")
        else:
            col_list.append(input_col)
            print(f"column : {input_col} added")
    return col_list

def check_sub_cond(row, conditions):
    for key in conditions:
        if row[key] != conditions[key]:
            return False
    return True

def fill_dict(df, res, col_list, conditions):
    rows = df.iloc
    col = col_list[0]
    gsize = 0
    if res != {}:
        res[col] = {}
        res = res[col]
    for row in rows:
        if check_sub_cond(row, conditions):
            gsize += 1
            if not row[col] in res.keys():
                res[row[col]] = {
                    "nb": 0,
                    "percentage": 0
                }
            res[row[col]]["nb"] += 1
    for key in res:
        res[key]["percentage"] = round(res[key]["nb"] / gsize * 100, 2)
    for key in res.copy():
        conditions[col] = key
        if len(col_list) > 1:
            fill_dict(df, res[key], col_list[1:], conditions)
        del conditions[col]

def get_res_dict(df, col_list):
    res_dict = {}
    conditions = {}
    fill_dict(df, res_dict, col_list, conditions)
    return res_dict

def main():
    df = read_csv()
    column_list = get_column_list
    res_dic = get_res_dict(df, column_list)
    print("res :")
    print(res_dic)

main()