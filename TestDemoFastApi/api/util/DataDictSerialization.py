import pandas as pd


def dict_serialization(description,data):
    df = pd.DataFrame(list(data), columns=[x[0] for x in description])
    try:
        decimal_columns=df.columns[df.dtypes == 'datetime64[ns]']
        df[decimal_columns[0]] = df[decimal_columns[0]].apply(lambda x: str(x))
        for i in range(len(df.columns)):
            decimal_columns = df.columns[df.dtypes == 'object']
            # print(decimal_columns)
            try:
                df[decimal_columns[i]] = df[decimal_columns[i]].apply(lambda x: float(x))
            except:
                continue
    except:
        pass
    data_dicts = df.to_dict('records')

    return data_dicts