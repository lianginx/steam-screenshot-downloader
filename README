# Steam Screenshot Downloader

**Steam Screenshot Downloader** 是一个用于批量下载 Steam 截图的工具。通过输入 Steam 用户名和保存路径，程序会自动爬取指定用户的公开截图并下载到本地。

## 功能特点

- 自动爬取 Steam 用户公开截图。
- 支持自定义保存路径。
- 基于 [DrissionPage](https://github.com/g1879/DrissionPage) 的轻量级爬虫工具，易于使用。

---

## 安装依赖

在使用该工具之前，请确保已安装必要的依赖项。

1. 安装 Python（建议使用 3.8 或更高版本）。
2. 安装必要的依赖库：

   ```bash
   pip install -r requirements.txt
   ```

## 使用说明

### 获取 Steam 用户名

浏览器打开想要爬取 Steam 用户截图库，复制 `https://steamcommunity.com/id/<username>/screenshots` 中的用户名部分。

### 运行脚本

运行以下命令以启动工具：

```bash
python main.py -u <用户名> -s <保存路径>
```

参数说明

- `-u` 或 `--username`：Steam 用户名（必填）。
- `-s` 或 `--save`：图片保存路径（必填）。

示例

```bash
python main.py -u njl1 -s /Users/liang/Downloads
```

上述命令将爬取 Steam 用户 `njl1` 的公开截图，并将其保存到 `/Users/liang/Downloads/screenshot` 目录下。

### 输出说明

程序运行后，图片将按照游戏分类保存到指定路径，目录结构如下：

```bash
<保存路径>/screenshot/<游戏名称>/<截图名称>.jpeg
```

例如：

```bash
/Users/liang/Downloads/screenshot/Counter-Strike/123456.jpeg
```

注意事项

1. 请确保目标 Steam 用户的截图是公开的，否则无法获取。
2. 对于较大的用户截图库，下载时间可能较长。

## 贡献

欢迎提交 Issue 或 Pull Request 来改进该工具！

## 许可

本项目基于 MIT License 开源。

---

如果你希望添加更多细节（如运行示例截图、环境配置方法等），可以告诉我，我可以帮助完善！
