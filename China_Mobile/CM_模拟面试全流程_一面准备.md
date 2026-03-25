# 中国移动香港创新研究院 · 模拟面试全流程（一面标准）

> 依据：`CM_JD.md`（AI Research Engineer / AI Frontier Technology Researcher）与候选人简历（王健霖）整理。  
> 用途：岗位拆解、自我介绍、高频问答、业务匹配、离职/动机、反问清单。**请把括号内数字与表述替换为你的真实口径。**

---

## 一、岗位拆解（面试官真正在筛什么）

JD 实际包含两条线，一面通常**合并考察**，但侧重点不同：

| 维度 | AI Research Engineer（广） | AI Frontier Technology Researcher（深） |
|------|---------------------------|----------------------------------------|
| 核心画像 | 算法 + 工程 + 垂直场景端到端 | **大模型 + Agent 全链路**（数据/训练/优化/部署） |
| 硬技能 | CNN/RNN/Transformer/GAN、PyTorch/TF、分布式/压缩/边缘（加分） | **Prompt / RAG / SFT**、Agent 框架、**memory/plan/action/tools** |
| 软技能 | 跨团队、产学研、论文专利开源 | 复杂问题拆解、产品化热情、多学科协作 |
| 语言 | **英文可开展日常科研** | 同上 |

**一面常见通过标准（归纳）**

1. **真实性**：项目能讲清输入输出、指标、取舍，经得起追问。  
2. **深度**：至少 1～2 个项目能下到「数据—模型/Agent—评测—上线/灰度」一层。  
3. **匹配**：简历里的 RAG/Agent、多模态、专利与论文，能映射到 JD 的「平台工具链 + 垂直落地 + 论文专利」。  
4. **沟通**：结构化表达；英文能自我介绍与技术段落（不少团队一面会穿插英文）。

---

## 二、自我介绍（中文 90～120 秒版）

面试官好，我是王健霖。香港岭南大学计算机科学硕士，本科电气背景，所以我对**系统与工程落地**也比较敏感。

我最近在**新浪微博 AI 创新产品部**做集团产品管培，工作重心是 **LLM 应用与 Agent**：主导过内部 **RAG 智能体**项目，把 Wiki、博主知识等接入向量检索与 **function call**，配合 **LangChain** 做多模态解析、规划与执行，用 **A/B 和反馈闭环**推动迭代，累计约 **（1500+）** 人次使用。另一条线是 **iOS 系统级合作**，把 Spotlight、App Intents 等入口与微博能力打通，我负责 PRD、埋点与灰度策略，上线后日均使用约 **（3 万+）** 量级并持续优化。此外还有 **AIGC 管线**（ComfyUI、工作流、成本与质量评估）支撑运营生产。

研究侧我在岭大做过 **BERT 情绪检测**与 **MCP-A2A 混合具身智能协议**相关专利工作，还有 **强化学习**方向的会议论文汇报经历，和 **Kaggle** 回归类竞赛实践。

我希望加入贵院，把**大模型与 Agent 的端到端能力**和**科研产出（论文/专利）**结合起来，在 **5G/6G、垂直行业**等场景里做可验证的落地。以上是我的简要介绍。

---

## 三、英文自我介绍（60～90 秒，一面常考）

Good morning / afternoon. I’m Jianlin Wang. I recently completed my MSc in Computer Science at Lingnan University in Hong Kong.

Professionally, I worked at Weibo’s AI Innovation team as a **product management trainee**, focusing on **LLM applications and agents**. I led an internal **RAG agent** project: chunking and embedding blogger/Wiki content, retrieval to reduce hallucinations, and **tool/function calling** against internal databases, with **A/B tests** and user feedback loops. I also drove an **iOS system-level integration** (Spotlight, App Intents, widgets), owning PRD, analytics, and rollout.

On the research side, I worked on **Transformer-based emotion detection** and **embodied-AI protocol** topics with patent contributions, plus **reinforcement learning** paper experience and **Kaggle** practice.

I’m excited about this role because it combines **frontier LLM/Agent R&D** with **end-to-end delivery**—exactly where I want to grow next. Thank you.

---

## 四、模拟问答（一面高频 + 建议答法）

### 4.1 动机与岗位理解

**Q：为什么投我们 / 香港创新研究院？**  
**A 框架**：香港区位 + 运营商场景（5G/6G、B2B/B2C）+ JD 里「平台 + 论文专利 + 产学研」与个人经历对齐；避免空泛夸公司。

**Q：你更偏研究还是工程？**  
**A**：**双栈**。产品侧训练了需求拆解、评测与迭代；研究侧有专利与论文训练。**愿意按团队阶段调整**：前期偏原型与验证，稳定后偏平台化与论文/专利沉淀。

**Q：两个 JD 你更匹配哪一个？**  
**A**：**Agents 岗与近期工作重合度最高**（RAG、工具调用、记忆与工作流）；**Research Engineer 岗**可用硕士阶段 **BERT/蒸馏/TensorRT**、**RL 论文**、**Kaggle** 与 **AIGC 管线**补足「训练与推理链路」叙事。

---

### 4.2 RAG / Agent（必深挖）

**Q：你们的 RAG 架构是怎样的？如何控幻觉？**  
**A 要点**：  
- 数据：切块策略、清洗、权限（内部 Wiki/博主数据）。  
- 检索：embedding、向量库、**重排/阈值**（如有）。  
- 生成：prompt 约束、**引用片段**、拒答策略。  
- 评测：离线 hit rate + 线上反馈 + **A/B**。  
（按你真实实现说，不要夸大自研向量库若实际是托管服务。）

**Q：Agent 的 memory / plan / tools 你怎么设计？**  
**A 要点**：  
- **Memory**：短期对话上下文 vs 长期知识（向量库/结构化库）边界。  
- **Plan**：任务拆解是否用固定 workflow 还是模型规划；人审节点（如有）。  
- **Tools**：function schema、鉴权、超时与失败回退；日志与可观测性。

**Q：Multi-Agent 协作在你们项目里解决什么问题？**  
**A**：按简历口径：**分工**（检索/生成/校验）或 **流水线**；说明**协调成本**与**何时不值得上多 Agent**（体现工程判断）。

---

### 4.3 训练与优化（Research Engineer 线会追问）

**Q：你有微调经验吗？SFT 怎么做？**  
**A**：实习期有 **BadCase 收集、提示词与工作流迭代**；AIGC 侧有 **LoRA、ComfyUI 管线**。若实际未主导大规模 SFT：**诚实说明**，补充「数据构造思路 + 评测维度 + 希望入职后深入分布式训练」。

**Q：BERT 情绪检测项目，数据与指标？**  
**A**：按专利/简历：**数据清洗与增强（同义替换、回译、SMOTE）**、**对抗训练 FGM/PGD**、**蒸馏/剪枝**、**TensorRT 推理**；指标说 **准确率/召回/F1** 及**跨域**验证（数字若记不清，说「以当时实验记录为准」并准备截图或一页纸）。

**Q：强化学习论文做了什么？**  
**A**：准备 **问题设定、算法选型、实验结论、与电网/场景的关系** 三句话 + 一个细节（状态/动作/奖励），避免泛泛。

---

### 4.4 系统、协作与影响力

**Q：iOS 项目里你怎么和研发协作？**  
**A**：PRD **边界清晰**（系统能力 vs 微博能力）、**埋点 schema**、**灰度与回滚**、**数据复盘会议**；用 **日均 3 万+** 等结果收束。

**Q：和「研究院」相比，你在微博的差异是什么？**  
**A**：微博偏 **产品迭代速度与业务 KPI**；研究院更偏 **方法创新、可发表成果、平台复用**。你希望 **把产品化经验带到可复用平台与论文专利**。

---

### 4.5 行为面

**Q：最大失败或踩坑？**  
**STAR**：场景（例如检索噪声/工具误触发）→ 你如何发现（日志/用户反馈）→ 改动（阈值、prompt、路由）→ 结果（指标或工单下降）。

**Q：和算法/工程意见不一致怎么办？**  
**A**：对齐 **评测标准与成本约束**；用 **小规模实验** 说话；**向上同步风险**而不是僵持。

---

## 五、业务匹配细节（简历 ↔ JD 映射表）

| JD 关键词 | 你简历中的锚点 | 面试一句话 |
|-----------|----------------|------------|
| LLM 训练与优化（Prompt/RAG/SFT） | RAG 智能体、AIFlow、BadCase 与知识库 | 「RAG 上线闭环 + 提示词/工作流迭代，SFT 以实习与 AIGC 侧为延伸」 |
| Agent memory/plan/action/tools | 长短期记忆、CoT/ReAct、Multi-Agent、function call | 「工具 schema + 记忆分层 + 工作流编排，有灰度与反馈」 |
| 多模态 / 大模型 | 多模态输入解析、AIGC 管线、Flux/Qwen 等跟踪 | 「多模态在 Agent 输入与 AIGC 管线两侧都有实践」 |
| 推理加速 / 边缘 | TensorRT、BERT 工程化 | 「端侧推理优化有完整一段，可与 5G 边缘场景衔接」 |
| 垂直领域 | 电网 RL 口头报告、金融实践项目 | 「有行业交叉项目，可迁移到运营商垂直场景」 |
| 论文 / 专利 / 开源 | 专利两项、论文 oral、GitHub | 「成果习惯沉淀；开源按团队合规策略贡献」 |
| 英文科研 | 硕士全英文环境 + 国际会议口径 | 「可读写论文与邮件；口语持续练技术 Q&A」 |

---

## 六、离职原因（多版本，请选真实且一致的一种）

**原则**：不贬低前司、不抱怨个人；**一句原因 + 一句正向目标**。

1. **职业规划**：「前段经历验证了 LLM Agent 产品化路径，希望下一阶段在**研究院平台**做更深的方法研究与**可发表成果**。」  
2. **地域/家庭**（若属实）：「长期发展重心在**香港**，希望岗位与地域一致。」  
3. **合同/实习性质**（若属实）：「管培/项目阶段结束，寻求**全职研发/研究员**长期岗位。」  
4. **避免**：薪资细节纠纷、人身攻击、过度透露竞品机密。

---

## 七、反问环节（一面推荐问法）

选 2～3 个即可，体现你**在选团队**：

1. **团队分工**：Agent 方向当前是偏 **平台** 还是偏 **业务课题**？入职前半年最可能落地的里程碑是什么？  
2. **数据与算力**：训练与推理资源大致如何申请？是否有 **on-prem / 合作云** 的约束？  
3. **成果预期**：论文/专利/KPI 的大致比例？是否鼓励 **开源**（合规边界）？  
4. **协作模式**：与内地研究院、高校、业务单元的 **联合项目** 通常怎样组织？  
5. **英文工作场景**：日常是 **文档+会议英文** 还是部分中文？是否有 **mentor** 机制？

---

## 八、一面前 24 小时 Checklist

- [ ] 准备 **1 页纸**：RAG Agent 架构图 + 3 个数字（用户量、A/B 结论、上线时间）。  
- [ ] BERT / RL / 专利各准备 **「30 秒 + 3 分钟」** 两档讲解。  
- [ ] 英文：**自我介绍 + 任意一个项目** 各练 3 遍。  
- [ ] 核对简历日期与项目名（如 **iOS 26** 等）与口述一致。  
- [ ] GitHub/作品集：确保主页与简历链接可打开。

---

## 九、风险提示（诚实区）

- JD 强调 **C++、分布式训练、大规模 SFT**：若你主力在 **Python 与 Agent 应用层**，一面应 **主动定位**「强项在 LLM 应用与 Agent 全链路 + 传统 DL 工程化经历」，并表达 **补齐分布式与 C++ 侧** 的意愿。  
- **产品 title** 可能被挑战「是否够 research」：用 **专利、论文、模型训练细节、评测与复现** 对冲，强调 **可转 full-time researcher/engineer**。

---

*文档生成说明：基于提供的 JD 文本与 PDF 简历结构化整理；具体数字与日期请以你最终核对后的简历为准。*
