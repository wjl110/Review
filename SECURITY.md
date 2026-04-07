# Security Policy

## Supported Versions

我们目前支持以下版本的安全更新：

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

如果您发现了安全漏洞，请**不要**通过公开的 Issue 报告。

### 报告流程

1. **发送邮件至项目维护者**（或通过 GitHub 私信）
2. 提供以下信息：
   - 漏洞的详细描述
   - 重现步骤
   - 潜在影响
   - 建议的修复方案（如有）

### 响应时间

- **初步响应**: 48 小时内
- **漏洞确认**: 7 天内
- **修复发布**: 根据严重程度，14-30 天内

### 安全更新通知

安全更新将通过以下渠道发布：
- GitHub Security Advisories
- CHANGELOG.md
- GitHub Releases

## Security Best Practices

在使用本项目时，请遵循以下最佳实践：

### API Key 管理

1. **永远不要**将 API Key 硬编码到代码中
2. 使用 `.env` 文件存储敏感信息
3. 确保 `.env` 文件在 `.gitignore` 中
4. 定期轮换 API Key
5. 使用环境变量或密钥管理服务

### 依赖项安全

1. 定期运行 `pip-audit` 检查依赖漏洞
2. 及时更新依赖项到最新稳定版本
3. 查看 Dependabot 的自动更新 PR

### 代码安全

1. 不要在日志中记录敏感信息
2. 对用户输入进行验证和清理
3. 使用 HTTPS 进行所有 API 调用
4. 限制 API 请求频率以防止滥用

### 部署安全

1. 在生产环境中使用受限的 API Key
2. 配置适当的网络安全规则
3. 启用日志记录和监控
4. 定期备份配置文件

## Known Security Considerations

### API Key 暴露风险

- **风险**: API Key 可能在环境变量中暴露
- **缓解**: 使用 `.env.example` 模板，确保 `.env` 被 gitignore

### 输入验证

- **风险**: 未验证的用户输入可能导致问题
- **缓解**: 已实现消息长度限制（10000 字符）

### 依赖项漏洞

- **风险**: 第三方库可能存在安全漏洞
- **缓解**:
  - 启用 Dependabot 自动更新
  - GitHub Actions 中集成安全扫描
  - 定期运行 `bandit` 和 `pip-audit`

## Security Updates History

| Date | Version | Description |
|------|---------|-------------|
| 2026-04-07 | 0.1.0 | 初始安全审查 - 无已知严重漏洞 |

## Contact

如有安全相关问题，请联系：
- GitHub: [@wjl110](https://github.com/wjl110)
- Issues: [GitHub Issues](https://github.com/wjl110/Review/issues) (仅用于非敏感问题)

感谢您帮助保持项目安全！
