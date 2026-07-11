# 从这里开始：交给 Codex 发布到 GitHub

这个文件夹已经是清理后的公开版本，不需要再从原始压缩包中挑文件。

## 目标

Codex 需要完成两件事：

1. 在 GitHub 账号 `Evelyn-R7` 下创建并发布公开仓库 `hurricane-resilient-supply-chain`；
2. 在个人主页仓库 `Evelyn-R7/Evelyn-R7` 的 README 中加入这个项目，但保留主页原有内容。

## 使用步骤

1. 把整个文件夹解压到本地，例如：

   ```text
   GitHub/hurricane-resilient-supply-chain
   ```

2. 在 Codex 中打开这个文件夹。
3. 将 `CODEX_PROMPT_CN.txt` 的全部内容发送给 Codex。
4. Codex 应先阅读 `CODEX_INSTRUCTIONS.md` 并运行：

   ```bash
   python scripts/validate_repository.py
   ```

5. 确认 Codex 当前连接的 GitHub 账号是 `Evelyn-R7`，再让它创建仓库、commit 和 push。
6. 发布完成后，检查 README 主图、Mermaid 流程图、数据来源链接和表格是否正常显示。

## 重要说明

- 不要上传原始文件 `ibtracs_NA.csv`；公开仓库已包含处理后的数据和结果。
- 不要把旧稿、`before/`、checkpoint 或废弃结果重新放回来。
- 不要让 Codex改写研究数值或声称机器学习模型“无条件更优”。
- 不要在未征得你同意的情况下添加开源许可证。
- NOAA/NCEI IBTrACS 的来源、DOI、引用和原始文件校验值已经写在 `DATA_SOURCES.md`。
