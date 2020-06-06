"""
调查GitHub中某一编程语言对应最热门的开源项目，并绘制成柱状图（配有链接）
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 要调查的编程语言
language = "python"
# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:" + language + "&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
# 研究有关仓库的信息
repo_dicts = response_dict["items"]
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    if repo_dict["description"]:
        plot_dict = {
            "value": repo_dict["stargazers_count"],  # pygal采用“value”相关联的数字确定条形高度
            "label": repo_dict["description"],  # 使用与”label“相关联的字符串给条形创建工具提示
            "xlink": repo_dict["html_url"], # 与键“xlink”相关联的URL将每个条形都转换为活跃的链接
        }
    else: # 解决有的项目无描述的情况
        plot_dict = {
            "value": repo_dict["stargazers_count"],
            "label": "No description",
            "xlink": repo_dict["html_url"],
        }
    plot_dicts.append(plot_dict)
# 可视化
my_style = LS("#333366", base_style=LCS)
# 样式配置
my_config = pygal.Config() # Config实例，可定制图标外观
my_config.x_label_rotation = 45 # x轴标签旋转45度
my_config.show_legend = False # 隐藏图例
my_config.title_font_size = 24 # 标题尺寸
my_config.label_font_size = 14 # 副标签尺寸
my_config.major_label_font_size = 18 # 主标签尺寸
my_config.truncate_label = 15 # 将较长的标签名截断
my_config.show_y_guides = False # 隐藏图标中的水平线
my_config.width = 1000 # 自定义宽度
# 传参后具体实现图表
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred " + language.title() +" Projects on GitHub"
chart.x_labels = names
chart.add("", plot_dicts)
chart.render_to_file(language + "_repos.svg")