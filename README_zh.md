# FastF1 可视化脚本

使用 FastF1 库和 Plotly 可视化一级方程式赛车比赛数据的 Python 脚本集合。

## Demo: https://youtu.be/tzwww0bJy3c

## 脚本概览

### 1. 车手风格图

**文件：** [`plot_driver_styling.py`](plot_driver_styling.py)

此脚本创建具有车手特定样式的自定义单圈时间比较图。它允许您：
- 从官方 F1 赛程中选择比赛年份和轮次
- 从参赛车手中选择要比较的特定车手
- 应用交替的自定义线条样式：
  - 主要车手：较粗的线条（5px）和较低的透明度（0.3）
  - 次要车手：较细的线条（1px）和较高的透明度（0.7）
- 仅使用快速单圈（quicklaps）可视化整个比赛的单圈时间进展
- 使用 FastF1 的官方 F1 样式自动分配车队颜色

### 2. 位置变化图

**文件：** [`plot_position_changes.py`](plot_position_changes.py)

此脚本可视化车手在整个比赛中的位置变化。它允许您：
- 从官方 F1 赛程中选择比赛年份和轮次
- 从参赛车手中选择要追踪的特定车手
- 使用官方 F1 车队颜色显示位置变化
- 使用不同的线条样式（实线/虚线）区分同一车队的车手
- 反向 y 轴，位置 1 在顶部，提高可读性
- 交互式垂直布局图例，便于车手识别

## 安装

1. 克隆或下载此仓库

2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

### 车手风格图

```bash
python plot_driver_styling.py
```

按照交互式提示：
1. 输入比赛年份（例如：2024）
2. 从显示的赛程中选择轮次
3. 按索引号选择车手（用逗号分隔，例如："1,3,5"）

### 位置变化图

```bash
python plot_position_changes.py
```

按照交互式提示：
1. 输入比赛年份（例如：2024）
2. 从显示的赛程中选择轮次
3. 按索引号选择车手（用逗号分隔，例如："1,3,5"）

> **注意：** 车队第二车手（偶数编号车手）将用虚线显示以便更好地区分。

## 依赖项

- Python 3.8+
- FastF1 >= 3.1.0
- Plotly >= 5.14.0
- Pandas >= 1.5.0

完整依赖列表请参见 [`requirements.txt`](requirements.txt)。

## 功能特点

- **交互式选择**：友好的用户提示，显示完整赛程用于比赛和车手选择
- **官方 F1 样式**：通过 FastF1 使用官方车队颜色和车手样式
- **Plotly 可视化**：具有缩放、平移和悬停功能的交互式图表
- **智能车手样式**：自动交替样式以获得更好的视觉比较效果
- **位置追踪**：反向 y 轴，位置 1 在顶部（显示领先者）

## 项目结构

```
fastf1/
├── plot_driver_styling.py      # 单圈时间比较与自定义样式
├── plot_position_changes.py    # 比赛中的位置变化
├── speed-visualization.py      # （额外的可视化脚本）
├── requirements.txt            # Python 依赖
├── README.md                   # 英文版本
└── README_zh.md                # 中文版本
```

## 许可证

本项目是开源的，根据 [MIT 许可证](LICENSE) 提供。

## 贡献

欢迎贡献！请随时提交问题或拉取请求。

---

英文版本请查看 [README.md](README.md)
