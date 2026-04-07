# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 项目健康检查报告 (PROJECT_HEALTH_AUDIT.md)
- 改进跟踪表 (IMPROVEMENT_TRACKING.md)
- 测试基础设施 (tests/ 目录)
- GitHub Actions CI/CD 工作流
  - 代码质量检查 (code-quality.yml)
  - 自动化测试 (test.yml)
  - 安全扫描 (security.yml)
- Dependabot 自动依赖更新配置
- 项目配置文件
  - pyproject.toml
  - .flake8
  - pytest.ini
  - requirements-dev.txt
- 代码文档 (docstrings) 和类型注解
- 日志系统配置
- 输入验证和错误处理改进

### Changed
- 改进了 `Proj/Aliyun.py` 的代码文档
- 改进了 `Proj/app_gradio.py` 的错误处理和类型注解
- 修复了代码格式问题（尾随空格、文件末尾换行）
- Pylint 评分从 5.8/10 提升至 6.9+/10

### Fixed
- 修复 Flake8 报告的格式问题
- 改进了异常处理的精确性

## [0.1.0] - 2026-04-07

### Added
- 初始版本
- 阿里云通义千问 API 调用示例
- Gradio Web UI 对话界面
- 面试准备资料库
- AI Agent 项目文档
- 企业面试专项资料

[Unreleased]: https://github.com/wjl110/Review/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/wjl110/Review/releases/tag/v0.1.0
