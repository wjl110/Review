# GenAI SA 面试 · 一页纸速记（≈3 分钟口述提纲）

---

## 1. 百炼 vs DashScope（30 秒）

| | 百炼 Bailian (Model Studio) | DashScope |
|---|----------------------------|-----------|
| **是什么** | 一站式大模型**平台**（控制台入口） | **API 推理层**（你调用的接口） |
| **能做什么** | 模型体验、应用开发、RAG 知识库、工作流、Agent、模型调优、用量监控 | 发 HTTP 请求 → 拿模型回复 |
| **关系** | 同一套服务的**管理/应用入口** | 同一套服务的**调用入口**（如 `dashscope-intl.aliyuncs.com`） |

**一句话**：DashScope 是 API，百炼是「API + 控制台 + 应用/调优」的总平台；你写代码调的是 DashScope，在网页上管 Key、做 Demo、看用量用的是百炼。

---

## 2. Qwen 系列选型（30 秒）

| 模型 | 场景 | 记法 |
|------|------|------|
| **Qwen3-Max** | 最难任务、最强推理 | 要最好效果 |
| **Qwen3.5-Plus** | 对话/通用、质量与成本平衡 | 日常主力 |
| **Qwen3.5-Flash** | 高 QPS 每秒查询率 Queries Per Second、成本敏感、低延迟 | 省钱/高并发 |
| **Qwen-Coder** | 代码、Agent、工具调用 | 写代码/调工具 |

**一句话**：对话客服 → Plus 或 Flash 看预算；代码/Agent → Coder 或 Plus；要顶配 → Max；省钱/试跑 → Flash。

---

## 3. Prompt / RAG / Agent 各一个场景（各 20 秒）

- **Prompt**：海外客服 Bot → system 定身份/语言/红线，few-shot 定话风，多轮做摘要控 token，再 A/B 迭代。
- **RAG**：「问文档」问答 → 文档切块 → Embedding 建向量库 → 检索 Top-K 召回(从一堆数据里，找出最相关的前 K 个结果，并按相似度 / 分数排序返回)拼进 prompt → Qwen 生成；百炼控制台可直接用知识库搭 Demo。
- **Agent**：「查数据生成报告」→ Qwen 做规划与生成，工具接数据源 API/DB，百炼上工作流把「查—汇总—生成」串起来；API 兼容性好，海外客户已有 AWS 也能接。

---

## 4. 微调概念（20 秒）

- **全参数**：效果最好，成本高，数据多、预算足再用。
- **LoRA**：只训少量低秩矩阵，省显存、工业常用。
- **QLoRA**：量化 + LoRA，更省显存，单卡可训 7B/13B。
- **PEFT**：参数高效微调统称（LoRA/Adapter/Prefix 等都算）。
- **何时建议客户微调**：先看数据质量与规模；能 Prompt/RAG 解决就先上；确实要专属话术/领域再评估 LoRA/QLoRA，和算法一起定格式与指标，百炼小规模试再上 PAI/HF。

---

## 5. 英文 2～3 段技术简述（背下来 ≈1 分钟）

**Bailian / Model Studio**  
"Bailian is Alibaba Cloud's end-to-end platform for building and running LLM applications. Customers can call Qwen and Wan via API, or use the console for prompt engineering, RAG knowledge bases, agents, and workflows. I've used the DashScope API and built demos on top of it."

**Qwen 选型**  
"Qwen is our flagship LLM family. We have Max for the hardest tasks, Plus for balance of quality and cost, Flash for high throughput and low latency, and Coder for code and agent use cases. I help customers choose the right model based on their use case and budget."

**你的项目**  
"I built a small demo that calls Qwen via the OpenAI-compatible API, with environment-based config and a simple web UI. That gave me a clear picture of how to go from zero to a working AI demo on Alibaba Cloud."

---

## 6. 收尾金句（中/英各一句）

- **中文**：海外 AI MaaS 的核心是让客户快速、安全、可控地用上大模型；我既有百炼和 Qwen 的实操，也能从架构和成本设计方案，并愿意用 Demo 和客户一起验证价值。
- **English**：I combine hands-on experience with Bailian and Qwen with solution design from an architecture and cost perspective, and I'm ready to validate value with customers through demos.

---

*口述时：先产品（百炼 vs DashScope + Qwen 选型）→ 再技术（Prompt/RAG/Agent 各一场景 + 微调）→ 最后英文 2～3 段 + 金句，控制在 3 分钟内。*
