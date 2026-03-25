# 阿里云通义千问 API 调用示例

基于 DashScope（灵积）调用 Qwen3.5 模型。

## 环境准备

```bash
pip install -r requirements.txt
cp .env.example .env   # 填入 DASHSCOPE_API_KEY
```

## 运行

**命令行对话：**
```bash
python Aliyun.py
```

**本地 Web UI（Gradio）：**
```bash
python app_gradio.py
```
启动后浏览器访问 http://127.0.0.1:7860 即可使用多轮对话。

## 配置说明

- `DASHSCOPE_API_KEY`: 在 [DashScope 控制台](https://dashscope.console.aliyun.com/) 获取。
- 地域与 `base_url` 见 `Aliyun.py` 内注释。
