##### app.py是基于flask框架搭建的，其余的python文件是基于streamlit框架搭建的。



## 环境配置

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run it locally

```sh
streamlit run Hello！🤠.py
```

## 在服务器端打开外网可访问前端

```sh
streamlit run Hello！🤠.py --server.port 5200 --server.address 0.0.0.0
```

