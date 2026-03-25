# interview-qa-jd-resume · 元信息

本目录封装「根据岗位 JD + 个人简历，生成面试问答全流程」的工作方式，供 Agent 与人类快速对齐输入输出。

## 用途

- 用户只需提供 **JD 路径或 URL**、**简历路径**（PDF/图片/Markdown 均可），即可生成结构化面试准备材料。
- `SKILL.md` 为 Agent 执行规范；本文件为 **人类可读** 的速查卡。

## 推荐调用方式

1. 在对话中写明：`@SKILLS/interview-qa-jd-resume/SKILL.md`（或贴出本目录路径），并附上 JD 与简历路径。
2. 若希望 Cursor **自动发现** Skill：将本目录 **复制或软链** 到个人技能目录，例如
  `~/.cursor/skills/interview-qa-jd-resume/`  
   （勿写入 `~/.cursor/skills-cursor/`，该目录为系统保留。）

## 默认输入


| 项   | 说明                                             |
| --- | ---------------------------------------------- |
| JD  | 本地图片/PDF/文本，或招聘页 URL（Agent 需抓取或让用户粘贴全文）        |
| 简历  | 本地 PDF/图片/Markdown；PDF 优先用 PyMuPDF（`fitz`）提取文本 |


## 默认输出

- 建议在 **与 JD 同级或用户指定目录** 生成：`面试问答全流程-{公司}-{岗位简写}.md`
- 内容结构以 `SKILL.md` 中的模板为准。

## 维护

- 更新流程：只改 `SKILL.md`；本文件仅同步「路径约定与调用方式」变更。
- 人类入口与文件索引见 [README.md](./README.md)；架构与扩展见 [设计方案.md](./设计方案.md)；对话范式见 [对话示例.md](./对话示例.md)。

