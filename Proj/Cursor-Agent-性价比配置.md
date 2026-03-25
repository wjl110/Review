# Cursor 终端 Agent 模式 · 性价比最高配置指南

---

## 一、核心结论（怎么配最省钱又够用）

**Agent 模式默认用「Auto」或「Composer 1.5」** → 走 **Auto + Composer 用量池**，单价低、包月额度大，性价比最高。

- **Auto**：Cursor 自动在「智能 / 成本 / 稳定性」之间选模型，适合日常大部分任务。
- **Composer 1.5**：Cursor 自研 Agent 模型，专为写代码、改文件、跑命令优化，效果接近 Claude Sonnet 4.5，同样走 Auto + Composer 池。

选「具体模型」（如 Claude Opus、GPT-5.4）会走 **API 池**，按该模型 API 价计费，Agent 多轮+多工具调用会很快烧完 Pro 的 $20 额度。

---

## 二、在 Cursor 里怎么配置（操作步骤）

### 1. 选对模型（最重要）

1. 打开 **Agent / Composer**（终端旁或 Cmd+Shift+I 等）。
2. 在输入框上方或侧边找到 **模型选择器**（Model / 模型下拉）。
3. 选 **「Auto」** 或 **「Composer 1.5」**，不要默认选 Premium 或某个具体贵模型。

之后在同一会话里都会用这个选择，下次新开 Agent 再选一次即可（Cursor 会记住上次选择）。

### 2. 可选：在设置里找「默认模型」

- 打开 **Cursor Settings**（Cmd+, 或 File → Preferences → Cursor Settings）。
- 搜索 **model**、**Agent**、**Composer**。
- 若有「Default model for Agent」或「Composer default model」类选项，设为 **Auto** 或 **Composer 1.5**。

（不同版本入口可能略有差异，以你当前 Cursor 界面为准。）

### 3. 控制 Agent 行为（少烧 token）

- **任务尽量说清楚**：一次说明目标、文件范围，减少来回多轮。
- **能不用 Max Mode 就不开**：超长上下文会明显增加 token，只在真需要全库理解时再开。
- **简单小改优先用 Chat/Ask**：只读不执行、小范围改代码时用普通对话或 Edit，把 Agent 留给「需要执行命令、多文件改动」的任务。

---

## 三、用量池与价格（为什么这样配省钱）

| 用量池 | 何时扣费 | 单价（量级） | 适合 Agent？ |
|--------|----------|--------------|--------------|
| **Auto + Composer** | 选 Auto 或 Composer 1.5 时 | 输入约 $1.25/百万 token，输出约 $6/百万 token | ✅ 推荐，包月额度大 |
| **API 池** | 选具体模型（如 Claude、GPT-5.4）或 Premium 时 | 按该模型 API 价（往往高很多） | ❌ 容易很快用完 $20 |

Pro 套餐每月含 **$20 API 额度** + **较充足的 Auto + Composer 额度**。Agent 用 Auto/Composer 1.5，主要消耗后者，$20 留给偶尔切到强模型用，这样整体最划算。

---

## 四、按任务类型选（进一步省）

| 任务类型 | 建议选择 | 说明 |
|----------|----------|------|
| 日常 Agent（改代码、跑命令、小重构） | **Auto** 或 **Composer 1.5** | 走 Auto+Composer 池，性价比最高 |
| 极简单（查文档、小问答） | 可切 **Ask 模式** 或 Chat，模型选 Auto | 少用 Agent，省 token |
| 特别难（大架构、复杂推理） | 临时切 **Claude 4.5 Sonnet** 或 **GPT-5.4** | 用 API 池，用完再改回 Auto |

---

## 五、小结：终端 Agent 性价比配置清单

1. **模型**：Agent/Composer 里选 **Auto** 或 **Composer 1.5**，不要默认 Premium 或贵模型。
2. **设置**：若有「默认模型」选项，设为 Auto 或 Composer 1.5。
3. **习惯**：任务说清楚、少开 Max Mode、简单事用 Chat/Ask。
4. **查看用量**：**[cursor.com/dashboard](https://cursor.com/dashboard?tab=usage)** → 看 API 池与 Auto+Composer 池使用情况，便于调整。

按以上配置，终端 Agent 模式在「便宜」和「性能」之间能达到较高性价比。
