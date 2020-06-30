from typing import List

import pandas as pd

from tide_query import YouDaoQuery, TideQuery as Tq

if __name__ == "__main__":
    source_excel_name = '/home/jover/Documents/english.xlsx'  # 源excel路径

    result_list: List[YouDaoQuery.Result] = Tq(
        target=YouDaoQuery(  # 使用有道词典作为搜索目标
            lang=YouDaoQuery.Language.cn,  # 选择中英文翻译
            silent=False,  # 不关闭提示
        ),
        query_list=pd.read_excel(source_excel_name)['单词'].tolist(),  # 将源excel的"单词"列作为搜索源
        interval=(1, 2)  # 请求间隔 1-2秒
    ).start()  # 开始查询

    target_excel_name = '/home/jover/Documents/english.xlsx'  # 目标excel路径 (建议不要与源excel为同一个文件)
    writer = pd.ExcelWriter(target_excel_name)  # 打开目标excel
    pd.DataFrame(data={
        '单词': [i['source'] for i in result_list],  # 生成单词列
        '音标1': [i['symbol_us'] for i in result_list],  # 生成美式音标列
        '音标2': [i['symbol_en'] for i in result_list],  # 生成英式音标
        '结果': [i['target'] for i in result_list],  # 生成翻译结果列
    }).to_excel(writer, index=None)
    writer.save()  # 保存目标excel文件
