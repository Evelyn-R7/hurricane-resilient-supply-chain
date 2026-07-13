# 中文快速开始

本仓库研究不同飓风风险表示如何影响两阶段 CVaR 供应链网络设计。建议先阅读英文 [README](README.md)，了解研究问题、主要发现和限制。

## 快速验证

在仓库根目录创建 Python 环境并安装依赖：

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

运行轻量级仓库验证和单元测试：

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests
```

上述验证不会重新运行需要 Gurobi 的优化实验，也不会覆盖公开结果。

## 数据与完整复现

- 原始 `ibtracs_NA.csv` 未在仓库中分发；数据版本、下载地址、校验值和引用见 [DATA_SOURCES.md](DATA_SOURCES.md)。
- 完整与免求解器复现路线见 [REPRODUCIBILITY.md](REPRODUCIBILITY.md)。
- 重新运行完整优化流程需要有效的 Gurobi 安装和许可证。
- 请按 `01 → 04 → 02 → 03` 的顺序阅读或运行 `notebooks/` 中的笔记本。

## 解释边界

- 预测目标是飓风危险暴露代理，而非真实企业停产标签。
- 网络是一个 14 节点的风格化测试平台，不代表特定企业网络。
- 结果体现成本与尾部风险之间的权衡，不支持“复杂机器学习模型无条件更优”的结论。

原创代码与文档使用 [MIT License](LICENSE)。NOAA/NCEI IBTrACS、Gurobi 及其他第三方材料仍遵循原始来源的许可与使用条款，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
