# 阿里云 GenAI SA 三面 · 口述版话术 + 全流程模拟面试

> 基于你的简历定制。面试官视角：业务专业负责人，问题会更深、更贴业务和项目。

---

# 第一部分：你的核心故事（口述版，背熟可 1～2 分钟讲完）

## 1. 自我介绍（中/英各一版，约 45 秒）

**中文口述版：**

> 您好，我是王健霖。硕士毕业于香港岭南大学计算机科学，本科是电气工程自动化。过去近一年在微博 AI 创新产品部做产品管培生，主要负责三块：一是微博内部 RAG 智能体项目——用 LangChain 搭了多模态输入、规划、决策、执行的 Agent 架构，接入了 RAG 和博主数据库的 function call，上线后内部 1500 多人次使用，并持续做 A/B 和反馈迭代；二是 iOS 26 与微博的系统级合作，从 PRD 到排期、联调、上线，端侧大模型和 App Intents 相关，上线后日活约 3 万；三是 AIGC 视频实验室，做文生图、文生视频、LoRA 微调、ComfyUI 工作流，以及多模态模型如 Qwen、Wan、Sora 的评估和工业化方案。更早之前在微博 AIGC 产品部实习，做过千问知识库、Prompt、Dify 工作流和 AIFlow 自动发博。读研期间还做过 BERT 情绪检测专利和 MCP-A2A 具身智能协议专利，用过 Hugging Face 和微调。我更喜欢把技术和业务连起来做方案和落地，所以更倾向 SA 方向，也希望在阿里云 GenAI SA 岗位上继续深耕。

**英文口述版（简短）：**

> Hi, I'm Jianlin Wang. I have a master's in Computer Science from Lingnan University and nearly one year at Weibo's AI team. I led an internal RAG-based agent project with LangChain—multi-modal input, planning, RAG, and function calls to internal databases—reaching 1,500+ internal users. I also drove the Weibo–iOS 26 integration with on-device LLM and App Intents. I have hands-on experience with Qwen, Wan, LoRA, ComfyUI, and Dify. I prefer solution architecture and delivery over pure BD, so I'm focused on the GenAI SA role here.

---

## 2. 最能体现 SA 价值的项目（口述版，2 分钟内）

**项目：微博内部 RAG 智能体**

- **背景**：微博希望用 AI 赋能内部提效，且信息要可控，所以立项做基于内部 Wiki 的 RAG 智能体。
- **需求**：我负责收集、拆解业务场景需求，对标 Google AI Studio、Gemini Enterprise 等，给研发做需求梳理、工具和 UI 选型。
- **方案**：协助研发同事，用 LangChain 搭原型，以 Ghost、Big Model、Shell 为底座，设计多模态输入 → 感知 → 规划 → 决策 → 执行的全流程，适配微博博主等场景。RAG 侧：对博主文本切块、Embedding 进向量库、检索控幻觉，并接博主等数据库；Agent 侧用 function call 调内部库，并做了长短时记忆，实现 CoT、ReAct、RAG 和 Multi-Agent 协作。
- **结果**：周期内 1500+ 人次使用，收集约 58 条反馈，通过 A/B 和数据分析驱动迭代，并开源到 GitHub。
- **复盘**：需求从“要一个智能体”到“要可检索、可执行、可协作”的收敛，以及 RAG 切块和检索策略对效果影响很大，这部分我会在后续项目里更早做消歧和实验。

**口述时注意**：先一句话说清「做的是什么、解决什么问题」，再讲你的角色（需求+方案+落地），最后用数字收尾。

---

## 3. RAG / Agent 技术口述（被问到“怎么做的”时用）

- **RAG**：业务侧有博主文本和 Wiki；我们对文本做切块、Embedding 写入向量库，查询时先检索再喂给 LLM，用检索结果约束生成、控制幻觉；中间调过 chunk 大小和检索条数。
- **Agent**：规划+决策用 CoT、ReAct，执行层用 function call 调微博博主等数据库；多个子任务用 Multi-Agent 协作；还做了长短时记忆保证上下文连贯。
- **和 SA 的关联**：从业务需求到“要 RAG 还是纯 Agent、数据从哪来、接口怎么设计”，都是 SA 要回答的，我在这个项目里实际做了这部分。

---

## 4. 对阿里云百炼 / Qwen / Wan 的口述（如实说 + 选型逻辑）

> 我目前对百炼的实操主要来自文档和了解，生产环境还没直接用过百炼。但我用过千问、Wan 在多模态和视频评估里，也用过 OpenAI、Gemini 等。选型时我会看：场景是通用对话、长文本还是多模态；时延和成本；数据合规和是否要私有化。Qwen 更偏通用与长文本，Wan 更偏多模态和特定场景；和海外模型比，会强调成本、合规和与云产品的整合。入职后会尽快在百炼上做几个 Demo 把链路跑通。

---

# 第二部分：高概率问答（基于 JD + 你的简历）

## 一、项目与角色深挖

**Q1：你在这个 RAG 智能体项目里，具体是怎么从业务需求落到技术方案的？**

**参考回答：**

> 业务最初提的是“用 AI 整合内部知识、提高效率”。我先和用研、业务方聊，区分出几类场景：查规范、查博主信息、跨部门协作。再对标 Google AI Studio、Gemini Enterprise，看别人怎么做知识检索和工具调用。然后归纳出技术诉求：一是要有 RAG 把 Wiki 和博主文本用起来；二是要能调内部系统（博主库等），所以需要 Agent + function call；三是多步任务需要规划和记忆，所以上了 CoT、ReAct 和长短时记忆。我把这些整理成需求文档和架构要点，和研发一起定技术选型（比如 LangChain、向量库、模型），再参与原型和迭代。所以是从“业务场景 → 能力拆解 → 技术方案”一步步收敛的。

---

**Q2：RAG 这块你们切块、检索策略是怎么定的？遇到过什么坑？**

**参考回答：**

> 切块我们按段落和语义试过不同 size，太大容易带噪声，太小容易丢上下文，最后取了一个折中，并且对关键字段做了保留。检索用的是向量检索，条数也调过，太多会拉长上下文、影响时延和幻觉。遇到的坑主要是：有些长文档切完检索不准，我们通过加元数据、关键句抽取做了补充；还有少数场景幻觉明显，用“检索结果 + 明确引用”的 Prompt 约束生成，好很多。后续如果做企业级方案，我会更早做 chunk 和检索的评估实验。

---

**Q3：你提到 1500+ 人次、58 条反馈，这些反馈你是怎么用的？有没有推动产品或方案改动的例子？**

**参考回答：**

> 反馈我们按类型归过类：有的是“查不到”，对应检索和数据覆盖；有的是“答得不对”，对应 Prompt 和模型；有的是“想批量用、想对接系统”，对应接口和权限。我们做了简单的 A/B 和数据分析，看哪些路径用得最多、哪里断点最多。具体改动比如：检索条数从 5 调到 8 后，部分场景的准确率有提升；还有把高频问题做成快捷入口，减少多轮对话。部分需求我们也同步给研发，作为后续迭代的输入，和 SA 把客户需求转成产品改进的逻辑是类似的。

---

**Q4：iOS 26 这个项目里，SA 或方案架构相关的工作你具体做了哪些？**

**参考回答：**

> 我负责从能力梳理到落地的整体方案。先梳理端侧 3B 大模型、App Intents 和微博可结合的点，用 Shortcut、Spotlight、Widget、App Intents 等入口增加“系统级打开微博”的能力，把热搜、智搜等能力接到系统层。输出的是 PRD“iOS 26 × 微博”，里面包括底层能力、适配边界、产品定位和功能拆解。然后带 UI/UE 和开发排期、联调、测试、灰度和上线，并设计 Spotlight 的 schema 和埋点。所以更多是“能力拆解 + 方案设计 + 跨团队推进”，和 SA 做客户方案时的拆需求、定架构、推动落地是同一类工作。

---

**Q5：AIGC 视频实验室里你评估过 Qwen、Wan、Sora 等，从解决方案角度你会怎么给客户选型？**

**参考回答：**

> 会先看客户场景：是文生图、文生视频、数字人还是剪辑流水线；再看质量、成本、时延和是否要私有化。比如 Sora 质量好但成本高、API 限制多；即梦、可灵国内可用、集成快；Qwen、Wan 在阿里云生态里和百炼、GPU 整合好，适合要合规、要一条龙云上方案的客户。我会按“场景 → 质量/成本/合规 → 推荐 1～2 个方案并说明取舍”，必要时用 Demo 做对比，让客户能决策。

---

## 二、技术深度（RAG / Agent / 微调）

**Q6：如果客户要做“企业知识库问答”，你会怎么设计整体方案？**

**参考回答：**

> 先界定场景：谁用、问什么、成功标准（准确率、时延、成本）。数据侧：知识来源、格式、量级、更新频率，再定接入和清洗方式。架构上：数据 → 清洗/分块 → 向量化与检索（RAG）→ 调用大模型 → Prompt（强调引用、控幻觉）→ 前端或 API。模型选型看是否要长文本、多语言，以及是否要微调。我会建议先用 RAG 验证效果，再考虑微调。风险和优化：幻觉用检索+引用约束；检索不准调 chunk 和检索策略；时延从检索条数、模型选型、缓存几头优化。我在微博的 RAG 项目就是按类似思路做的，可以复用这套框架。

---

**Q7：Agent 的 function call 你们是怎么设计和对接的？**

**参考回答：**

> 我们把微博内部博主等数据库封装成可被 Agent 调用的工具，定义好输入输出和鉴权。在 LangChain 里用 function call 让 LLM 在合适的步骤选择工具、填参数，执行后把结果塞回上下文再继续推理。设计时要注意：工具描述要清晰，否则 LLM 会选错；错误处理和限流要写好；敏感操作要加权限。这样 Agent 既能回答“是什么”，也能执行“查一下、导出一份”这类动作，和 SA 给客户做“检索+执行”方案是同一套思路。

---

**Q8：你做过 LoRA、ComfyUI，那大模型微调你了解多少？客户要定制化模型你会怎么配合？**

**参考回答：**

> 我做过的微调主要是视觉侧 LoRA、ComfyUI 工作流；NLP 侧在专利里做过 BERT 的微调和 Hugging Face。大模型微调我了解全参、LoRA、QLoRA 和 PEFT 的大致思路：全参成本高，LoRA/QLoRA 省显存、迭代快。客户要定制时，我会先和算法同事一起看：数据量、质量、场景目标，再判断是提示词/RAG 能解决，还是真要微调；若微调，再估数据规模、算力和周期，选全参还是 LoRA。我可以在需求、场景和数据层面配合，具体训练和实验由算法主导，我配合做效果验证和客户沟通。

---

## 三、协作与软技能

**Q9：SA 和销售、产品、算法一般怎么配合？你有过类似经历吗？**

**参考回答：**

> 销售带商机和客户关系，SA 负责把需求讲清、出方案、做 Demo、支撑标书技术部分。产品负责路线图，SA 把客户需求归纳成“场景+价值+建议”，推动是否进需求池。算法负责模型和实验，SA 提供场景、数据理解和效果标准，配合做选型和验收。在微博我虽然没有挂 SA  title，但 RAG 项目里我做了需求收集、方案梳理、和研发的对接；iOS 项目里带了多团队排期和上线；AIGC 里也做过需求到方案到文档的沉淀，和 SA 的协作方式是一致的。

---

**Q10：客户提了一个我们产品目前没有的能力，你会怎么处理？**

**参考回答：**

> 先判断是“单客户定制”还是“通用能力缺失”。若是单客户，看能否用现有能力组合或小定制满足，能做的在方案里写清楚范围和边界。若是通用能力，我会把场景、客户价值、频率和竞品情况整理成简短需求说明，和产品/研发同步，看能否排期；同时给客户一个预期，比如“已反馈给产品，有进展再同步”，避免过度承诺。在微博我们收反馈后也是先归类，再决定是当前迭代改还是进 backlog，逻辑一样。

---

## 四、动机与岗位匹配

**Q11：为什么想做 GenAI SA、为什么选阿里云？**

**参考回答：**

> 一二面下来，我和面试官都认为我更适合 SA：我喜欢把技术和业务连起来，做方案、做 Demo、推动落地，而不是纯商务拓展。GenAI 正在改各行各业，SA 离客户和场景最近，我想在这个窗口期专注做这件事。阿里云有百炼、Qwen、Wan 和完整云产品线，海外 AI MaaS 也在拓展，和我之前做的 RAG、Agent、多模态评估和产品落地比较契合，所以希望能在阿里云 GenAI SA 岗位上深耕。

---

**Q12：你之前更多是产品/研究，为什么转 SA？**

**参考回答：**

> 我在微博的岗位虽是产品管培生，但大量工作本质是“需求理解 + 方案设计 + 技术选型 + 推动落地”：RAG 项目里做需求梳理和架构设计，iOS 项目里做 PRD 和跨团队推进，AIGC 里做技术方案和选型。我更喜欢这种“用技术解决业务问题、并亲手把方案做出来”的角色，而不是纯产品规划或纯算法。SA 正是这样的定位，所以是顺势转，而不是从零转。

---

## 五、英文（若三面有英文环节）

**Q13 (EN): Walk me through your most relevant project for a solution architect role.**

**参考回答：**

> The most relevant one is our internal RAG-based agent at Weibo. We had internal Wiki and blogger data; the business wanted AI to help with retrieval and execution while keeping control. I gathered requirements, benchmarked products like Google AI Studio, and then designed the architecture: multi-modal input, planning, RAG for retrieval with chunking and vector DB, and function calls to internal databases. We used LangChain, CoT, ReAct, and multi-agent where needed. It reached 1,500+ users; we collected feedback and iterated with A/B tests. So it was full-cycle: requirements, solution design, and delivery—exactly what an SA does.

---

**Q14 (EN): How would you explain to a customer when to use RAG vs. fine-tuning?**

**参考回答：**

> I’d say: start with the use case. If the knowledge changes often or is large and you need to control sources, RAG is better—faster to implement and easier to update. If you need a specific style, tone, or task that’s stable and you have enough quality data, fine-tuning can help. Often we do RAG first to validate value and collect data, then consider fine-tuning for refinement. I’ve done both in projects and would recommend this order to customers.

---

# 第三部分：全流程模拟面试（约 40～50 分钟）

## 阶段 0：开场（1～2 分钟）

**面试官：** 你好，我是 xx，负责海外 AI MaaS 解决方案架构这块。今天我们会聊得偏业务和技术一些，先简单介绍一下你自己吧。

**你：** （用 **第一部分·1** 中文自我介绍，约 45 秒～1 分钟。）

**面试官：** 好的，那我们开始。

---

## 阶段 1：项目深挖（约 15～20 分钟）

**面试官：** 你简历里微博这个 RAG 智能体项目，你具体负责哪几块？从需求到上线完整讲一讲。

**你：** （用 **第一部分·2** “最能体现 SA 价值的项目”口述版，约 2 分钟；可顺带提 **第一部分·3** 的 RAG/Agent 技术点。）

**面试官：** 需求是怎么从业务方那里拿到的？有没有客户一开始说不清、你帮他理清楚的例子？

**你：** （用 **Q1** 参考回答，强调“几类场景”“对标”“归纳出 RAG + function call + 规划记忆”。）

**面试官：** RAG 的切块和检索你们怎么做的？踩过什么坑？

**你：** （用 **Q2** 参考回答。）

**面试官：** 58 条反馈之后，有没有推动产品或方案改动的具体例子？

**你：** （用 **Q3** 参考回答。）

**面试官：** iOS 26 这个项目里，和“解决方案架构”最相关的工作是什么？

**你：** （用 **Q4** 参考回答。）

---

## 阶段 2：技术方案与阿里云（约 10～15 分钟）

**面试官：** 如果客户要做企业知识库问答，你会怎么设计整体方案？

**你：** （用 **Q6** 参考回答，可加一句“和我在微博做的 RAG 项目思路一致”。）

**面试官：** 你对阿里云百炼、Qwen、Wan 了解多少？和 OpenAI 比你会怎么给客户选型？

**你：** （用 **第一部分·4** 百炼/Qwen/Wan 口述 + **Q5** 的选型逻辑。）

**面试官：** 客户要定制化模型，要微调，你会怎么配合？

**你：** （用 **Q8** 参考回答。）

---

## 阶段 3：协作与软技能（约 5～8 分钟）

**面试官：** SA 要和销售、产品、算法配合，你有过类似经历吗？

**你：** （用 **Q9** 参考回答。）

**面试官：** 如果客户提了一个我们产品没有的能力，你怎么处理？

**你：** （用 **Q10** 参考回答。）

---

## 阶段 4：动机与英文（约 5 分钟，英文看面试官是否要求）

**面试官：** 为什么想做 GenAI SA、为什么选阿里云？

**你：** （用 **Q11** 参考回答。）

**面试官（可选）：** In one or two minutes, tell me about your most relevant project for this SA role. / When would you recommend RAG vs. fine-tuning to a customer?

**你：** （用 **Q13** 或 **Q14** 英文回答。）

---

## 阶段 5：你的反问（2～3 分钟）

**你：** 想请教两件事：一是这个岗位目前主要 support 哪几个行业或区域？二是团队里 SA 和销售、产品的协作节奏大概是怎样的，比如从线索到 POC 的流程？

AI native前线汇报，poc很深，项目会找到我们中台，模型相关需求。客户名单调研团队，触达成功率低BD，中台推荐场景，策略，1，成熟降本增效，替换，切换等。2，新业务+场景，有无最佳实践和测试，poc做，交互；模型表现+商务+折扣+签单+起量+别的场景。；售后问题我们解决，Plan。

**面试官：** （对方答。）

**你：** 谢谢，没有其他问题了。

---

## 阶段 6：结束

**面试官：** 今天先到这里，后续 HR 会跟你联系。

**你：** 好的，谢谢您的时间，期待后续消息。

---

# 第四部分：口述练习清单（今天可做）


| 序号  | 内容               | 建议                         |
| --- | ---------------- | -------------------------- |
| 1   | 中文自我介绍           | 掐表 45 秒～1 分钟，练 2～3 遍       |
| 2   | 英文自我介绍 + Q13/Q14 | 各练 1～2 遍，保证不断句             |
| 3   | “RAG 智能体项目”完整口述  | 2 分钟内讲完，练 2 遍              |
| 4   | 企业知识库方案（Q6）      | 按场景→数据→架构→风险讲 2～3 分钟，练 1 遍 |
| 5   | 百炼/Qwen/Wan 选型话术 | 背熟“如实说 + 选型逻辑”那一段          |
| 6   | 反问两句             | 记牢，自然问出                    |


---

**最后提醒：** 回答时先听清问题，可重复一句确认（“您是想了解 xxx 这部分对吗？”）；不会的就说“这块我目前了解有限，我的理解是……”，再接到你熟悉的部分；数字和项目名要准（1500+、58、iOS 26、LangChain、RAG、function call）。祝你三面顺利。