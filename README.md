# psdash\_HTTPBasicAuth

簡介：在 psdash 的基礎上添加 HTTP 基本身份驗證（即打開頁面會彈出提示框，需要輸入用戶名和密碼），界面翻譯為中文，並增加展示所有節點基本狀態的主界面，可以理解為 psdash 的中文版分支。

功能：psdash 是基於 psutil 和 zerorpc 的 Python 語言開發的主機監控面板，本分支包含 psdash 的所有功能，支持多節點/集群部署，所有數據每 3 秒自動更新，無需手動刷新頁面。

* **總覽頁**：支持查看 CPU、磁碟、網絡、用戶、內存、交換區（swap）、網絡
* **進程**：進程列表，展示每個進程的詳細信息，包括打開的文件數、打開的連接數、內存佔用、子進程、資源限制
* **硬碟**：顯示所有硬碟和分區
* **網絡**：顯示所有網絡接口和使用的流量，以及當前的網絡連接
* **日誌**：展示自定義的日誌文件詳細信息，支持搜索文件內容

# 安裝

**1\. 主節點和 agent 節點都執行下面的命令（安裝 psdash）**

Debian/Ubuntu:

```bash
apt-get install build-essential python-dev -y
apt-get install python-setuptools  -y
pip install psdash --allow-external argparse
```

如果上面的命令安裝不成功，則執行以下命令：

```bash
git clone https://github.com/Jahaja/psdash.git
cd psdash
pip install -U setuptools
python setup.py install
```

RHEL (Fedora, CentOS):

```bash
yum groupinstall "Development Tools" -y
yum install python-devel -y
yum install python-setuptools -y
pip install psdash --allow-external argparse
```

如果上面的命令安裝不成功，則執行以下命令：

```bash
git clone https://github.com/Jahaja/psdash.git
cd psdash
pip install -U setuptools
python setup.py install
```

**2\. 主節點執行**

```bash
pip install flask-httpauth
git clone https://github.com/wenguonideshou/psdash_HTTPBasicAuth.git
cd psdash_HTTPBasicAuth
python run.py -l '/var/log/**/*.log'
```

**3\. Agent 節點執行**

```bash
psdash -a --register-as xxx -l '/var/log/**/*.log' --register-to http://主節點IP:5000
```

## 如何修改參數？

在 `run.py` 中 `app = Flask(__name__)` 下面添加如下語句：

```bash
app.config.xxx = yyy
```

例如：

```bash
app.config.PSDASH_ALLOWED_REMOTE_ADDRESSES = "10.0.0.2, 192.29.20.2"
app.config.PSDASH_URL_PREFIX = "/psdash"
app.config.PSDASH_LOG_LEVEL = logging.INFO
app.config.PSDASH_LOG_LEVEL = "%(levelname)s"
app.config.PSDASH_NODES = [{'name': 'mywebnode', 'host': '10.0.0.2', 'port': 5000}]
app.config.PSDASH_NET_IO_COUNTER_INTERVAL = 3
app.config.PSDASH_LOGS_INTERVAL = 60
app.config.PSDASH_REGISTER_INTERVAL = 60
app.config.PSDASH_LOGS = ['/var/log/*.log']
app.config.PSDASH_REGISTER_TO = 'http://10.0.20.2:5000'
app.config.PSDASH_REGISTER_AS = 'myvps'
app.config.PSDASH_HTTPS_KEYFILE = '/home/user/private.key'
app.config.PSDASH_HTTPS_CERTFILE = '/home/user/certificate.crt'
app.config.PSDASH_ENVIRON_WHITELIST = ['HOME']
```

詳細參數說明請參考：[https://github.com/Jahaja/psdash#configuration](https://github.com/Jahaja/psdash#configuration)

**修改用戶名密碼**

修改 `web.py` 中的 `users = {"admin": "admin"}`，前面是用戶名，後面是密碼，可以添加多個用戶。

**修改刷新時間間隔**

修改 `static/js/psdash.js` 中的 3000 數字。

修改 `templates/all.html` 中的 3000 數字。

**卸載**

```bash
pip uninstall psdash
rm -r /root/psdash_HTTPBasicAuth
```

![面板](https://s1.ax1x.com/2017/12/18/OYE60.jpg) ![面板](https://s1.ax1x.com/2017/12/15/LmM4O.png) ![面板](https://s1.ax1x.com/2017/12/15/LmuE6.png) ![面板](https://s1.ax1x.com/2017/12/15/LmeD1.png) ![面板](https://s1.ax1x.com/2017/12/15/LmZuR.png) ![面板](https://s1.ax1x.com/2017/12/15/LmKUK.png) ![面板](https://s1.ax1x.com/2017/12/15/LmM4O.png) ![面板](https://s1.ax1x.com/2017/12/15/LmlCD.png)

