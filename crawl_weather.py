import requests
import pandas as pd

url = "https://tianqi.2345.com/Pc/GetHistory"

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"""
}


def crawl_table(year, month):
    # 年份和月份作为参数，查询天气信息
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }

    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()["data"]
    # df = date frame
    df = pd.read_html(data)[0]
    return df


df_list = []
for year in range(2011, 2022):
    for month in range(1, 13):
        print("爬取: ", year, month)
        df = crawl_table(year, month)
        df_list.append(df)

pd.concat(df_list).to_excel("北京10年天气数据.xlsx", index=False)
