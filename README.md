# Structural Change & Regime Modeling

**From structural breaks to change points and recurring latent regimes.**

一份连接计量经济学、统计学与机器学习的中文选择性综述。核心问题是：**什么时候应该寻找新的分段，什么时候应该识别曾经出现过的状态？**

状态：文献综述初稿；已整理核心来源与实验方案，尚未实施实验。检索日期：2026-09-16。不是穷尽式或系统性综述，也不主张首次统一这些领域。

## 内容

- [中文综述](survey.zh-CN.md)：概念、统一表示、方法比较、局限与研究问题。
- [参考文献](references.bib)：10 篇核心来源的 BibTeX。
- [实验设计](benchmark-plan.md)：用于后续复现的协议，不含未经运行的结果。

## 从这五篇综述读起

| 文献 | 适合回答的问题 | 本项目中的位置 |
|---|---|---|
| Casini & Perron (2018), [Structural Breaks in Time Series](https://arxiv.org/abs/1805.03807) | 回归关系是否改变？如何估计断点并做推断？ | 计量经济学主线；引用的是 2018 年预印本版本 |
| Truong, Oudre & Vayatis (2020), [Selective review of offline change point detection methods](https://doi.org/10.1016/j.sigpro.2019.107299) | 怎样选择离线分段算法？ | 用代价函数、搜索方法、断点数量约束组织方法 |
| Hamilton (2016), [Macroeconomic Regimes and Regime Shifts](https://www.nber.org/papers/w21863) | 如何对潜在经济状态与转换建模？ | 状态切换与经济解释；此处引用 NBER 版本 |
| Xie et al. (2021), [Sequential (Quickest) Change Detection: Classical Results and New Directions](https://arxiv.org/abs/2104.04186) | 如何兼顾检测延迟和误报？ | 在线检测主线 |
| Gama et al. (2014), [A survey on concept drift adaptation](https://doi.org/10.1145/2523813) | 数据关系改变后，预测模型如何适应？ | 连接检测与模型更新 |

建议顺序：Truong → Casini & Perron → Hamilton → Xie → Gama。先建立分类，再按研究问题阅读原始方法论文。

## 本项目的观点

结构突变、变点检测与状态切换有重叠，但目标不同。分段模型通常给每一段单独估计参数；状态模型则可以让相隔很远的时间段共享同一组参数。比较时必须区分**断点定位、状态恢复、实时报警和样本外预测**，不能用单一分数宣称一种方法全面优胜。

## 范围与来源

本版本聚焦时间序列中的突变、重复状态和预测适应。生态临界转变、因果机制识别、高维网络与深度序列模型仅作为后续扩展，不在本次覆盖范围内。

检索使用 structural breaks review、offline change point detection review、regime switching survey、quickest change detection、concept drift adaptation 等词，并从综述追溯代表性方法。优先引用作者预印本、出版商页面和机构版本。当前核验以题录、摘要及可访问的方法说明为主；不是逐篇全文精读记录。经典方法与综述分开标注。

另检索到 Tan & Wu (2025), *On Regime Switching Models*（[出版商入口](https://www.mdpi.com/2227-7390/13/7/1128)）；本次出版商页面未能读取，暂列待核验扩展阅读，不作为正文论证依据。本版本不沿用“已覆盖 2025–2026 最新综述”的说法。

## 维护方式

每篇新增论文记录：研究问题、假设、目标量、在线/离线信息集、推断与复杂度条件、评价协议、局限、原文链接。将实证结果与待检验想法分开记录；仅分享自写笔记和论文链接。
