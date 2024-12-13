from DrissionPage import SessionPage
import argparse

# 创建参数解析器
parser = argparse.ArgumentParser(description='批量下载 Steam 截图')
parser.add_argument('-u', '--username', type=str, required=True, help="用户名")
parser.add_argument('-s', '--save', type=str, help="图片保存路径")
args = parser.parse_args()

# 获取用户名
if args.username:
    url = f'https://steamcommunity.com/id/{args.username}/screenshots/?view=grid&p='
else:
    print('请输入用户名')
    exit()

# 获取保存路径
if args.save:
    savePath = args.save
else:
    print('请输入保存路径')
    exit()

# 创建页面对象
page = SessionPage()

# 查看爬取
pageNo = 1;
while True:
    print(f'———— 开始下载第 {pageNo} 页 ————')

    # 获取所有截图页面连接
    page.get(f'{url}{pageNo}')
    tagA = page.eles('@@class=profile_media_item modalContentLink   ugc')
    for a in tagA:
        link = a.attr('href')
        page.get(link)
        tagImg = page.ele('@@class=actualmediactn').ele('tag:a')
        img_src = tagImg.attr('href')
        # 下载图片
        title = link.split('=')[-1]
        game = page.ele('.screenshotAppName').ele('tag:a').text
        suffix = 'jpeg'
        print(f'下载 {savePath}/screenshot/{game}/{title}.{suffix}')
        page.download.add(img_src, f'{savePath}/screenshot/{game}', title, suffix)

    # 翻页
    if len(tagA) < 50:
        print('没有更多截图了')
        break
    else:
        pageNo += 1
