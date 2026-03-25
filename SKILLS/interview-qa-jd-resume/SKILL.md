---
name: interview-qa-jd-resume
description: >-
  Builds a full interview Q&A playbook from a job description (JD) and the
  candidate's resume—gap analysis, STAR stories, project deep-dives, role-specific
  cases, behavioral questions, and questions to ask the interviewer. Use when the
  user provides JD path/URL plus resume path, asks for 面试问答/模拟面试/面试准备,
  or references Aliyun/SKILLS/interview-qa-jd-resume.
---

# 面试问答全流程（JD + 简历）

## 目标

基于 **岗位 JD** 与 **候选人简历**，产出一份可直接背诵与模拟的面试全流程文档：匹配度、自我介绍、项目深挖、岗位场景题、行为面、反问环节；答案须 **锚定简历事实**，缺信息处标注「需补充」而非编造。

## 执行步骤

1. **摄取 JD**
   - 本地文件：按类型读取（图片/PDF 用 Read 或 PyMuPDF；文本直接读）。
   - URL：抓取正文；失败则请用户粘贴 JD 全文。
2. **摄取简历**
   - PDF：优先 `import fitz`（PyMuPDF）`page.get_text()`；无则 `pip install pymupdf` 后重试。
   - 图片：视觉 Read；Markdown/Docx：直接读。
3. **对齐岗位关键词**
   - 从 JD 提取：职责动词、硬技能（如搜索/策略/数据/指标/LLM）、软技能（协同/项目管理）、年限与学历。
4. **写匹配度矩阵**
   - 表格三列：**JD 要求 | 简历证据（公司/项目/数据）| 差距与补位话术**。
5. **生成问答全文**（使用下方模板，语言与用户一致；默认中文）
6. **质量自检**
   - 每个关键结论能否在简历中找到对应句；数据是否原样引用；是否覆盖 JD 五条职责与任职资格要点。

## 输出模板（复制填充）

```markdown
# 面试问答全流程 · {公司} · {岗位}

## 0. 岗位快照与考察重点
- 部门/方向一句话
- 面试官最可能追问的 5 个点

## 1. 匹配度矩阵（JD × 简历）
| JD 要点 | 简历锚点 | 风险/补位 |
|--------|----------|-----------|

## 2. 自我介绍（1～2 分钟）
- 结构：我是谁 → 与岗位相关的 2～3 段经历 → 为什么是这个团队 → 收束
- 【背诵版】……

## 3. 项目深挖（STAR）
对每个核心项目：背景-目标-你的动作-结果-复盘；准备 3 个追问层（技术/协作/数据）。

### 项目 A …
**Q** …  
**A（STAR）** …  
**追问** …

## 4. 岗位场景 / 业务题（结合 JD 定制）
- 搜索/推荐/策略类：指标体系、bad case、实验、与 LLM 结合等
- 每题：思考框架 30 秒版 + 2 分钟版回答

## 5. 行为面（宝洁八大问变体）
- 冲突、优先级、失败、影响力、学习速度…（各 1 题，答案挂简历）

## 6. 反问面试官（分角色）
- 业务负责人 / 直属 leader / HR 各 3～5 个

## 7. 模拟节奏（60～90 分钟）
- 时间分配与过关标准
```

## 答题原则

- **STAR**：情境-任务-行动-结果；结果尽量量化（与简历一致）。
- **搜索/AI 产品**：先定义用户任务与成功标准，再谈机制（召回/排序/意图/安全）、指标（CTR、时长、满意度、bad case 率）、实验与迭代。
- **诚实**：简历未写的技术细节不冒充；可答「当时由研发主导，我负责需求边界与验收标准」。

## 可选附属输出

用户若需要：再给出 **单页 Cheatsheet**（半页 A4：指标公式、项目数字、三条故事标题）。
