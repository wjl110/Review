# Review

> 个人技术成长与面试准备的综合知识库，涵盖技术实验项目、面试话术准备、AI 应用实践等内容。

---

## 📋 目录

- [项目简介](#项目简介)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [模块详细说明](#模块详细说明)
- [技术栈](#技术栈)
- [使用指南](#使用指南)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## 项目简介

**Review** 是一个个人综合知识库，主要用于记录和整理：

- **技术实验项目**：包含阿里云通义千问 API 调用示例，支持命令行对话和 Gradio Web UI
- **面试准备资料**：系统化整理面试话术、离职理由、职业规划、薪资谈判等实战内容
- **AI Agent 应用**：基于四范式 OpenClaw 平台的电竞解说 AI 人设设计与实践

本项目旨在帮助开发者系统化地准备技术面试、积累 AI 应用经验，并对相关知识进行持续沉淀。

---

## 项目结构

```
Review/
├── Proj/                          # 技术实验项目
│   ├── Aliyun.py                  # 阿里云通义千问命令行对话示例
│   ├── app_gradio.py              # 基于 Gradio 的 Web UI 对话应用
│   ├── requirements.txt           # Python 依赖包
│   ├── .env.example               # 环境变量配置模板
│   ├── Cursor-Agent-性价比配置.md  # Cursor Agent 配置指南
│   └── 云服务实操说明.md           # 云服务操作说明文档
│
├── rhetoric/                      # 面试话术和准备资料
│   ├── 01-离职与短任期.md          # 离职原因与短任期解释话术
│   ├── 02-职业规划与换工作动机.md  # 职业规划与跳槽动机话术
│   ├── 03-薪资与福利.md            # 薪资谈判与福利话术
│   ├── 04-履历时间线与重叠.md      # 履历时间线梳理与重叠处理
│   ├── 05-项目深挖与STAR.md        # 项目经历深挖与 STAR 法则应用
│   ├── 06-压力面刁钻题补充.md      # 压力面试刁钻问题应对
│   ├── 07-反问与收尾.md            # 面试反问技巧与收尾话术
│   ├── 08-阿里HRBP-HRG面试考察与问答对策.md  # 阿里 HRBP/HRG 面试专项
│   ├── 面试推理文件1.md            # 面试场景推理与分析
│   └── 面试推理文件2.md            # 面试场景推理与分析（续）
│
├── 4Paradigm/                     # 四范式 AI Agent 项目
│   └── OpenClaw-电竞解说-小龙虾/  # 电竞解说 AI 人设与技能定义
│       ├── OpenClaw_话题触发钳钳人格_原理说明.md
│       ├── OpenClaw_钳钳人设与多渠道会话_总结.md
│       ├── 小龙虾跨平台配置与自动化实践指南.md
│       └── 演示.md
│
├── Aliyun/                        # 阿里云相关资料
├── Anker/                         # Anker 面试相关资料
├── Baidu/                         # 百度面试相关资料
├── ByteDance/                     # 字节跳动面试相关资料
├── China_Mobile/                  # 中国移动相关资料
├── DIDI/                          # 滴滴面试相关资料
├── DingTalk/                      # 钉钉面试相关资料
├── Item/                          # 面试题目汇总
├── NIO/                           # 蔚来面试相关资料
├── PDD/                           # 拼多多面试相关资料
├── SKILLS/                        # 技能知识库
└── interview.md                   # 面试综合笔记
```

---

## 快速开始

### 克隆仓库

```bash
git clone https://github.com/wjl110/Review.git
cd Review
```

### Proj 模块 - 通义千问 API 示例

```bash
cd Proj

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的 DASHSCOPE_API_KEY

# 运行命令行对话
python Aliyun.py

# 启动 Gradio Web UI
python app_gradio.py
```

### rhetoric 模块 - 面试话术

直接浏览 `rhetoric/` 目录下的 Markdown 文件，按需阅读对应话题的准备内容：

```bash
# 查看面试话术目录
ls rhetoric/
```

### 4Paradigm 模块 - AI Agent 项目

浏览 `4Paradigm/OpenClaw-电竞解说-小龙虾/` 目录，查看电竞解说 AI 人设配置和 YAML 技能定义。

---

## 模块详细说明

### 🔧 Proj/ - 技术实验项目

基于 OpenAI 兼容模式调用阿里云百炼通义千问大模型（`openai` Python SDK + DashScope compatible-mode），包含两种使用方式：

| 文件 | 说明 |
|------|------|
| `Aliyun.py` | 命令行单轮对话示例，快速验证 API 连通性 |
| `app_gradio.py` | 基于 Gradio 的 Web UI，提供多轮可视化交互界面 |
| `requirements.txt` | 项目依赖：`openai`、`gradio`、`python-dotenv` |
| `.env.example` | 环境变量模板，需配置 `DASHSCOPE_API_KEY` |
| `Cursor-Agent-性价比配置.md` | Cursor AI 编辑器的 Agent 性价比配置方案 |
| `云服务实操说明.md` | 阿里云等云服务的实操配置说明 |

**使用前置条件：**
- Python 3.8+
- 阿里云 DashScope API Key（可在[阿里云控制台](https://dashscope.console.aliyun.com/)申请）

---

### 💬 rhetoric/ - 面试话术和准备资料

系统化整理面试各环节的应对话术，覆盖从自我介绍到薪资谈判的完整流程：

| 文件 | 内容 |
|------|------|
| `01-离职与短任期.md` | 如何解释离职原因、短任期经历，避免触雷 |
| `02-职业规划与换工作动机.md` | 职业发展规划阐述、换工作动机的正向表达 |
| `03-薪资与福利.md` | 薪资期望报价策略、福利谈判技巧 |
| `04-履历时间线与重叠.md` | 简历时间轴梳理、多段经历重叠的处理方法 |
| `05-项目深挖与STAR.md` | STAR 法则（情境-任务-行动-结果）的实战应用 |
| `06-压力面刁钻题补充.md` | 压力面试常见刁钻问题及应对策略 |
| `07-反问与收尾.md` | 面试末尾反问面试官的技巧与话术 |
| `08-阿里HRBP-HRG面试考察与问答对策.md` | 针对阿里巴巴 HRBP/HRG 面试的专项准备 |

---

### 🤖 4Paradigm/ - AI Agent 项目（四范式 OpenClaw）

基于四范式 OpenClaw 平台构建的电竞解说 AI Agent "小龙虾"（钳钳），包含完整的人设设计和技能配置：

| 文件 | 内容 |
|------|------|
| `OpenClaw_话题触发钳钳人格_原理说明.md` | 话题触发机制与 AI 人格设计原理 |
| `OpenClaw_钳钳人设与多渠道会话_总结.md` | 钳钳人设定义与多渠道会话配置总结 |
| `小龙虾跨平台配置与自动化实践指南.md` | 跨平台部署配置与自动化实践 |
| `演示.md` | 项目演示说明 |
| `龙虾人风格提案 - Sheet1.csv` | 风格提案数据表 |

---

### 🏢 企业面试专项目录

| 目录 | 说明 |
|------|------|
| `Aliyun/` | 阿里云相关面试和技术资料 |
| `Anker/` | Anker（安克创新）面试准备资料 |
| `Baidu/` | 百度面试准备资料 |
| `ByteDance/` | 字节跳动面试准备资料 |
| `China_Mobile/` | 中国移动相关资料 |
| `DIDI/` | 滴滴出行面试准备资料 |
| `DingTalk/` | 钉钉面试准备资料 |
| `NIO/` | 蔚来汽车面试准备资料 |
| `PDD/` | 拼多多面试准备资料 |

---

## 技术栈

| 技术/工具 | 用途 |
|-----------|------|
| **Python** | 主要编程语言（Proj 模块） |
| **openai SDK** | 通过 DashScope compatible-mode 调用阿里云通义千问 API |
| **Gradio** | Web UI 框架，构建可视化对话界面 |
| **python-dotenv** | 环境变量管理 |
| **YAML** | OpenClaw AI Agent 技能配置文件格式 |
| **Markdown** | 知识文档格式 |
| **四范式 OpenClaw** | AI Agent 开发平台 |

---

## 使用指南

### 浏览面试资料

1. 进入 `rhetoric/` 目录，按编号顺序阅读各话术文件
2. 根据即将面试的目标公司，查阅对应的企业专项目录（如 `ByteDance/`、`Baidu/` 等）
3. 参考 `interview.md` 查阅综合面试笔记

### 运行 AI 对话示例

1. 参考[快速开始](#快速开始)中的步骤配置环境
2. 命令行方式：运行 `python Proj/Aliyun.py`，直接在终端进行多轮对话
3. Web UI 方式：运行 `python Proj/app_gradio.py`，在浏览器中打开可视化界面（默认端口 7860）

### 使用 AI Agent 配置

1. 进入 `4Paradigm/OpenClaw-电竞解说-小龙虾/` 目录
2. 阅读人设和技能配置文档
3. 参考配置指南在四范式 OpenClaw 平台上部署 AI Agent

---

## 贡献指南

欢迎提交 Pull Request 来完善本知识库！

### 贡献步骤

1. **Fork 仓库**

   点击页面右上角的 `Fork` 按钮，将项目 Fork 到你的账户

2. **克隆到本地**

   ```bash
   git clone https://github.com/<your-username>/Review.git
   cd Review
   ```

3. **创建新分支**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **提交你的改动**

   ```bash
   git add .
   git commit -m "feat: 添加 xxx 内容"
   git push origin feature/your-feature-name
   ```

5. **发起 Pull Request**

   在 GitHub 上发起 Pull Request，描述你所做的改动

### 提交规范

- `feat`: 新增内容或功能
- `fix`: 修复错误或问题
- `docs`: 文档改进
- `refactor`: 结构调整（不改变内容）

---

## 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

---

> 📌 如有问题或建议，欢迎通过 [Issues](https://github.com/wjl110/Review/issues) 反馈。
