import collect
from config import CONFIG
import analyze
import visualize

if __name__ == '__main__':

    # 데이터 수집 - CONFIG 적용
    for pagename in CONFIG['pagename']:
        collect.crawling(pagename, **CONFIG['common'])

'''
    items = [{'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-12-31'},
             {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}]

    # 데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile

    

    # 데이터 분석(analyze)
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)

    # 데이터 시각화(visualize)
    for item in items:
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))

        filename = '%s_%s_%s' % (item['pagename'], item['since'], item['until'])
        visualize.wordcloud(filename, count_m50)
        visualize.graph_bar(title='%s 빈도 분석' % (item['pagename']),  xlabel='단어', ylabel='빈도수',
                            values=list(count_m50.values()), ticks=list(count_m50.keys()), showgrid=False,
                            filename=filename, showgraph=False)
'''