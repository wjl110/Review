# Contributing to Review

首先，感谢您考虑为本项目做出贡献！

## 行为准则

参与本项目即表示您同意遵守我们的行为准则：
- 尊重所有贡献者
- 保持专业和友好的交流
- 接受建设性的批评

## 如何贡献

### 报告 Bug

在提交 Bug 报告前：
1. 检查 [Issues](https://github.com/wjl110/Review/issues) 确认问题未被报告
2. 收集以下信息：
   - 操作系统和版本
   - Python 版本
   - 相关依赖版本
   - 重现步骤
   - 错误信息和日志

提交 Issue 时请使用清晰的标题和详细的描述。

### 功能建议

欢迎提出新功能建议！请：
1. 描述功能的用例和价值
2. 说明期望的行为
3. 提供示例或草图（如适用）

### Pull Request 流程

1. **Fork 仓库**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Review.git
   cd Review
   ```

2. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

3. **进行更改**
   - 遵循代码风格指南（见下文）
   - 添加测试（如适用）
   - 更新文档

4. **运行测试**
   ```bash
   cd Proj
   # 安装开发依赖
   pip install -r requirements-dev.txt

   # 运行测试
   pytest tests/

   # 运行代码质量检查
   black --check *.py
   flake8 *.py
   pylint *.py
   ```

5. **提交更改**
   ```bash
   git add .
   git commit -m "类型(范围): 简短描述"
   ```

   提交消息格式：
   - `feat(proj)`: 新功能
   - `fix(proj)`: Bug 修复
   - `docs`: 文档更新
   - `test`: 测试相关
   - `chore`: 构建/工具更改
   - `refactor`: 代码重构

6. **推送并创建 PR**
   ```bash
   git push origin feature/your-feature-name
   ```

   在 GitHub 上创建 Pull Request，填写：
   - 清晰的标题
   - 详细的描述
   - 相关 Issue 编号（如有）

## 代码风格指南

### Python 代码

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范
- 使用 Black 格式化代码（行长度 100）
- 为所有函数编写 docstrings
- 使用类型注解（Type Hints）

示例：
```python
def example_function(name: str, age: int) -> str:
    """
    示例函数的简短描述。

    Args:
        name: 用户名称
        age: 用户年龄

    Returns:
        格式化的问候语
    """
    return f"Hello, {name}! You are {age} years old."
```

### 测试

- 为新功能编写单元测试
- 测试应该独立且可重复
- 使用描述性的测试函数名
- 测试覆盖率目标：80%+

示例：
```python
def test_example_function_returns_greeting():
    """
    测试函数是否返回正确的问候语
    """
    result = example_function("Alice", 30)
    assert result == "Hello, Alice! You are 30 years old."
```

### 文档

- 使用 Markdown 格式
- 中文为主，必要时提供英文
- 保持文档与代码同步
- 包含代码示例

## 开发环境设置

1. **克隆仓库**
   ```bash
   git clone https://github.com/wjl110/Review.git
   cd Review
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate  # Windows
   ```

3. **安装依赖**
   ```bash
   cd Proj
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **配置环境变量**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件，填入你的 API Key
   ```

5. **运行测试**
   ```bash
   pytest tests/ -v
   ```

## 项目结构

```
Review/
├── Proj/               # 主要代码
│   ├── tests/         # 测试文件
│   ├── *.py           # 源代码
│   └── requirements.txt
├── rhetoric/          # 面试资料
├── docs/              # 文档
└── .github/           # GitHub 配置
```

## 分支策略

- `main`: 稳定的生产分支
- `develop`: 开发分支
- `feature/*`: 功能分支
- `fix/*`: Bug 修复分支

## Review 流程

PR 提交后：
1. 自动化 CI 检查（代码质量、测试、安全）
2. 代码审查
3. 必要的修改
4. 合并到目标分支

## 发布流程

1. 更新 CHANGELOG.md
2. 更新版本号
3. 创建 Git tag
4. 发布 GitHub Release

## 需要帮助？

- 查看 [README.md](./README.md)
- 查看 [PROJECT_HEALTH_AUDIT.md](./PROJECT_HEALTH_AUDIT.md)
- 提交 [Issue](https://github.com/wjl110/Review/issues)
- 查看现有的 [Pull Requests](https://github.com/wjl110/Review/pulls)

## 认可

所有贡献者将在 README.md 中得到认可。

感谢您的贡献！ 🎉
