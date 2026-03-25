# 阿里云 GenAI SA（大模型解决方案架构师）面试准备指南

> 岗位：阿里云智能 - 大模型解决方案架构 - GenAI SA | 海外 AI MaaS 业务 | 北京/杭州/广州/上海

---

## 一、岗位核心拆解（JD → 你要证明的能力）

| JD 要求 | 面试要证明的点 | 你的抓手（可结合现有经历） |
|----------|----------------|----------------------------|
| 支持海外 AI MaaS 销售，提升 Token 调用量 | 懂客户场景、能讲清价值、能设计可落地方案 | 百炼/Qwen 产品理解 + 方案设计话术 |
| 与全球客户深入沟通业务与技术架构 | 英语沟通、需求澄清、技术翻译能力 | 准备英文技术介绍与 Q&A |
| 基于百炼设计 AI 大模型与云上方案 | 百炼/Qwen/Wan/云 IaaS·PaaS 组合方案 | 用 Aliyun 项目讲「云+模型」落地 |
| 模型选型、架构设计、Prompt、RAG、Agent 咨询 | 能讲原理、能选型、能给建议 | 准备 RAG/Agent/Prompt 标准话术 + Demo 经验 |
| 设计并开发 Demo，Prompt/工作流/Agent 演示 | 动手做 Demo、能现场/远程演示 | Gradio+百炼 Demo、可扩展为 RAG/Agent Demo |
| 协同内部产品与算法，需求反哺、专项支持 | 跨团队协作、需求抽象、问题升级 | 准备 1～2 个「需求推动产品/算法」的例子 |
| 大模型微调（LoRA/QLoRA/PEFT）、PAI/Hugging Face | 能评估可行性、能和算法协作、有实验经验更佳 | 概念清晰 + 若有实验可讲，没有就讲学习与协作思路 |
| 云服务、AI 模型调用、云上 DevOps | 能讲清云架构、调用方式、CI/CD/配置管理 | 用 Aliyun 项目串讲云搭建·调用·DevOps |
| 英语流利、跨时区跨文化、可出差 | 英文技术表达、会议与邮件 | 准备英文自我介绍 + 2～3 个场景英文回答 |

---

## 二、阿里云产品与方案（必须能讲清楚）

### 2.1 百炼（Model Studio）— 你的主战场

- **是什么**：一站式大模型开发与应用平台，提供模型推理、应用开发、模型调优、部署与监控。
- **和 DashScope 关系**：DashScope API（如 `dashscope-intl.aliyuncs.com`）是百炼的推理服务入口；Model Studio 控制台是管理、应用、调优的统一入口。
- **地域**：国际（新加坡）、美国（弗吉尼亚）、中国（北京），不同地域 Base URL、Key、模型列表、价格可能不同。
- **核心能力**：模型服务（Qwen/Wan/第三方）、Prompt 工程、智能体、工作流、知识库 RAG、插件、模型调优（含 LoRA 等）、部署与用量监控。

**面试话术示例**：  
「我理解百炼是阿里云 AI MaaS 的旗舰平台，客户可以通过 API 直接调用 Qwen、Wan 等模型，也可以在控制台做 Prompt 调试、RAG 知识库、Agent 和工作流，快速从 PoC 做到生产。我在本地用 DashScope 兼容 OpenAI 的接口做过调用和 Gradio Demo，对从开通到上线的链路比较清楚。」

### 2.2 Qwen 与 Wan — 模型选型

- **Qwen**：通义千问系列。Qwen3-Max（最强）、Qwen3.5-Plus（均衡）、Qwen3.5-Flash（低成本低延迟）、Qwen-Coder（代码场景）。支持文本、多轮、代码、多模态（VL）、长文本等。
- **Wan**：通义万相。文生图、图生图、视频生成（如 Wan 2.x），面向创意与媒体场景。
- **选型逻辑**：对话/通用 → Plus；成本敏感/高并发 → Flash；代码/工具调用 → Coder；图像视频 → Wan；需最强推理 → Max。

**面试话术示例**：  
「客户若是对话/客服类，我会优先推荐 Qwen3.5-Plus 或 Flash 看预算；若是代码助手或 Agent，会结合 Coder 或 Plus；若是 UGC 内容、短视频，会看 Wan 系列的能力和计费方式。」

### 2.3 云 IaaS基础设施即服务/PaaS平台即服务 与 AI 的组合

- **只调 API**：客户仅用百炼 API，不买 ECS(阿里云服务器)/GPU，快速验证、降低运维成本。
- **自建推理/微调**：需要 GPU、容器时，用阿里云 ECS、容器服务（如 ACK阿里云容器服务——Alibaba Cloud Container Service for Kubernetes）、PAI阿里云的 AI 训练 & 部署平台（Platform of Artificial Intelligence） 做训练与推理，百炼做托管模型或混合方案。
- **DevOps**：CI/CD、镜像、环境变量与密钥管理（如 .env + .gitignore）、监控与日志，便于客户从 Demo 到生产。

**面试话术示例**：  
「我会先判断客户是‘纯 API 调用’还是‘需要自建推理/微调’。前者以百炼为主、配合用量与成本规划；后者会设计云上 GPU、PAI 或容器方案，并考虑密钥、环境与发布流程，保证可落地、可运维。」

---

## 三、技术能力题（按 JD 顺序准备）

### 3.1 Prompt 工程（Prompt Engineering）

- **考察点**：是否理解 system/user/assistant 角色、few-shot小样本学习/少样本提示、思维链、输出格式约束、长度与成本权衡。
- **回答要点**：  
  - 明确任务与角色（system prompt 定边界）。  
  - 少样本示例提升准确率（给大模型看「几个例子」，让它照着格式 / 逻辑做任务）。  
  - 对复杂任务可引导分步推理。  
  - 用结构化指令控制输出（JSON、列表等），便于下游集成。  
- **结合经历**：在百炼或本地 Demo 里如何设计 prompt、迭代效果（可举一个简单例子）。

**示例问题**：如何为一家海外客服客户设计基于 Qwen 的客服 Bot 的 Prompt 策略？  
**参考回答**：先通过 system prompt 限定身份、语言、禁止内容；用 few-shot 示例规范回答风格与兜底话术；对多轮对话设计上下文摘要或关键信息抽取，控制 token；再根据实际效果做 A/B 与迭代。

### 3.2 RAG（检索增强生成）

- **考察点**：RAG 是什么、为什么用、基本架构（文档切分、向量化、检索、拼 prompt、生成）、评估维度。
- **回答要点**：  
  - RAG = 检索（向量库/关键词） + 把检索结果注入 prompt + 大模型生成，用于知识库问答、减少幻觉。  
  - 切分策略：把长文档切成一段段小文本，给大模型看（chunk size每一段多大/overlap段与段之间重叠多少内容）、Embedding 模型、检索 Top-K、重排序（可选）会影响效果与成本。  
  - 百炼提供知识库能力，可上传文档、做检索增强对话，适合企业知识库、帮助文档等场景。
- **结合经历**：若做过知识库或“检索+生成”的 Demo，可简要说明数据、检索方式、模型选型。

**示例问题**：客户有一批内部文档，想做成“问文档”的问答系统，你会怎么设计？  
**参考回答**：采用 RAG：文档切块、用百炼或自建 Embedding 建向量库，查询时检索相关块、拼进 prompt 让 Qwen 生成答案；在百炼上可直接用知识库功能快速搭 Demo，再根据延迟与准确率考虑 chunk 大小、Top-K、是否加 rerank。

### 3.3 Agent 开发

- **考察点**：Agent 概念（规划、工具调用、多步执行）、与单轮对话的区别、常见框架与落地方式。
- **回答要点**：  
  - Agent 能拆任务、选工具、多轮执行（如查 API、读文件、执行命令），适合复杂工作流与自动化。  
  - 百炼支持 Agent/工具调用；LangChain、Dify、MCP、Skills 等可和百炼或 Qwen 结合做编排。  
  - 设计时需考虑：工具定义、权限与安全、失败重试、成本与延迟。
- **结合经历**：若用过 Cursor Agent、或任何“工具调用+大模型”的 Demo，可概括为「任务分解 + 工具调用 + 结果汇总」。

**示例问题**：客户想做“自动查数据并生成报告”的 Agent，你会推荐什么架构？  
**参考回答**：用 Qwen 做规划与生成，工具侧对接数据源 API 或数据库；在百炼上可搭工作流或 Agent，把“查询—汇总—生成报告”串起来；海外客户若已有 AWS/GCP，可说明阿里云百炼的 API 兼容性便于集成。

### 3.4 模型选型与架构设计

- **考察点**：能否根据场景、成本、延迟、合规选模型与部署方式。
- **回答要点**：  
  - 对话/通用：Qwen3.5-Plus/Flash。  
  - 代码/Agent：Qwen-Coder 或 Plus。  
  - 多模态：Qwen-VL、Wan。  
  - 成本敏感：Flash、按量计费与缓存策略。  
  - 架构要写清：调用方式（API/私有化）、地域、高可用与降级、密钥与合规。

**示例问题**：客户在新加坡，要低延迟且控制成本，你会怎么推荐？  
**参考回答**：优先用百炼国际（新加坡）地域，选 Qwen3.5-Flash 或 Auto 类能力，减少跨区延迟；从用量与缓存策略上控制 token 成本，并给出大致用量预估与预算区间。

### 3.5 大模型微调（LoRA / QLoRA / PEFT）

- **考察点**：概念理解 + 能否评估客户是否适合微调、与算法协作。
- **回答要点**：  
  - 全参数微调：效果最好，成本高，适合数据多、预算足的客户。  
  - LoRA：低秩适配，参数少、显存低，工业常用。  
  - QLoRA：量化 + LoRA，进一步省显存，适合单卡或小规模。  
  - PEFT：参数高效微调统称，少改原权重、多训小模块。  
  - 评估：数据质量与规模、任务是否适合微调（vs 提示词/RAG）、合规与数据安全；可先在百炼做小规模实验，再考虑 PAI 或 Hugging Face 做正式训练。
- **结合经历**：若有 PAI/Hugging Face 实验经历可讲；没有则强调「能评估需求、能和算法同事一起定方案、愿意快速上手」。

**示例问题**：客户想用自己数据微调 Qwen 做行业客服，你会怎么评估？  
**参考回答**：先看数据量、标注质量与合规；若数据足够且场景确实需要专属话术，再考虑 LoRA/QLoRA；建议先在百炼用通用模型+Prompt 验证效果，再上 PAI 或 HF 做小规模微调实验，和算法团队一起定数据格式与评估指标。

### 3.6 云服务与 DevOps

- **考察点**：云上搭建、AI 模型调用、CI/CD、配置与密钥管理。
- **回答要点**：  
  - 云搭建：选地域、开通服务、鉴权（API Key）、端点（Base URL）、网络与安全。  
  - AI 调用：HTTP/OpenAI 兼容 API，鉴权、限流、监控与日志。  
  - DevOps：依赖管理（requirements.txt）、环境变量与密钥（.env + .gitignore）、CI 中注入 Key、容器化与发布。
- **结合经历**：直接用你的 Aliyun 项目：从开通百炼、配置 Key、选 base_url，到写调用代码、用 .env 管理密钥、requirements.txt 与 README，说明「云服务搭建 + AI 模型调用 + 云上 DevOps 基础」你都做过。

**示例问题**：如何在一个新客户环境中快速搭一个可演示的 Qwen 对话 Demo？  
**参考回答**：在百炼开通账号、创建 API Key、选地域；本地或云上写一个最小调用（如 OpenAI SDK + base_url + api_key），用环境变量存 Key；用 Gradio 或简单 Web 做界面，用 requirements.txt 和 README 让客户或同事能一键复现；强调密钥不进代码、不进仓库，符合生产习惯。

---

## 四、行为与场景题（SA 常见）

### 4.1 客户需求不清晰时你怎么做？

- **要点**：主动澄清业务目标、成功标准、约束（预算、时区、合规）；用原型或 Demo 快速验证理解；书面总结需求与方案要点，对齐后再深入设计。

### 4.2 客户技术栈与阿里云不一致（如主要用 AWS）

- **要点**：强调百炼提供标准 API（含 OpenAI 兼容），便于集成；可做混合架构（业务在 AWS，AI 调用阿里云）；从 PoC 小范围验证，再谈迁移或长期合作。

### 4.3 如何推动内部产品/算法支持客户需求？

- **要点**：把客户需求抽象成通用场景与功能点；整理用例、数据样本（脱敏）与价值说明；通过工单、需求池或项目通道反馈；对重点客户可申请专项支持或定制评估。

### 4.4 做过的最复杂的 AI 方案或 Demo？

- **建议**：用「阿里云百炼 + Qwen API + Gradio（或 RAG/Agent）」串成一个完整故事：需求 → 选型（模型、地域）→ 设计（调用方式、Prompt/知识库/工具）→ 实现（代码、配置、DevOps）→ 演示与迭代。若有微调或跨团队协作，可一并讲。

---

## 五、英文准备（海外客户沟通）

### 5.1 英文自我介绍（1～2 分钟）

- 教育背景 + 几年相关经验。  
- 做过什么：AI/云/解决方案或售前，是否涉及大模型、RAG、Agent、Demo。  
- 为什么对 Gen AI SA 感兴趣：喜欢把技术与业务结合、支持客户落地、对阿里云 AI MaaS 和海外市场感兴趣。

### 5.2 英文技术简述（可背 2～3 段）

- **Bailian / Model Studio**：  
  "Bailian is Alibaba Cloud’s end-to-end platform for building and running LLM applications. Customers can call Qwen and Wan via API, or use the console for prompt engineering, RAG knowledge bases, agents, and workflows. I’ve used the DashScope API and built demos on top of it."
- **Qwen**：  
  "Qwen is our flagship LLM family. We have Max for the hardest tasks, Plus for balance of quality and cost, Flash for high throughput and low latency, and Coder for code and agent use cases. I help customers choose the right model based on their use case and budget."
- **Your project**：  
  "I built a small demo that calls Qwen via the OpenAI-compatible API, with environment-based config and a simple web UI. That gave me a clear picture of how to go from zero to a working AI demo on Alibaba Cloud."

### 5.3 常见英文 Q&A

- What’s the difference between Bailian and DashScope?  
  — DashScope is the API layer for model inference; Bailian (Model Studio) is the console and platform that includes the API, apps, RAG, agents, and tuning. Same backend, different entry points.
- How do you help a customer choose between Qwen Plus and Flash?  
  — Plus for better quality and harder tasks; Flash for cost-sensitive or high-QPS scenarios. I’d suggest starting with Flash for PoC and moving to Plus where quality matters.
- How do you handle data security for overseas customers?  
  — We use region-specific endpoints (e.g. Singapore), support VPC and private link, and don’t use customer data for training. I’d align with their compliance requirements and document the architecture.

---

## 六、你的优势与故事线（建议反复打磨）

1. **产品理解**：百炼、Qwen、Wan、DashScope、地域与计费，能讲清并能做选型。  
2. **动手能力**：真实用百炼 API 做过调用与 Gradio Demo，具备从 0 到 1 的落地经验。  
3. **云与 DevOps**：能用「云服务搭建 + AI 模型调用 + 配置与依赖管理」讲清楚一个小而完整的链路。  
4. **可扩展性**：同一套经验可延伸到 RAG 知识库、Agent 工作流、微调评估与 PAI/Hugging Face 协作。  
5. **SA 思维**：能翻译业务需求为技术方案、能考虑成本与可落地、能写清架构与演示路径。

**面试中反复传递**：  
「我理解海外 AI MaaS 的核心是让客户快速、安全、可控地用上大模型。我既有百炼和 Qwen 的实操经验，也能从架构和成本角度设计方案，并愿意通过 Demo 和客户一起验证价值。」

---

## 七、面试前检查清单

- [ ] 能口头讲清：百炼是什么、和 DashScope 关系、Qwen/Wan 选型逻辑。  
- [ ] 能用 Aliyun 项目 3 分钟内讲完：云搭建 → 模型调用 → DevOps。  
- [ ] 能简述 Prompt / RAG / Agent 原理并各举一个客户场景。  
- [ ] 能说明 LoRA/QLoRA/PEFT 概念及何时建议客户做微调。  
- [ ] 准备 1 个「复杂方案或 Demo」故事、1 个「推动内部支持客户」的例子。  
- [ ] 英文自我介绍 + 2～3 个英文技术段落熟到能脱稿。  
- [ ] 看过百炼控制台与文档，能说出主要功能入口（模型、知识库、工作流、Agent、调优）。  

---

*可根据每次面试反馈，把新题和更好回答补充进本文档，形成你的专属 GenAI SA 面试库。*
