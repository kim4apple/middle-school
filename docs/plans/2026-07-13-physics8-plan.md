# 八年级物理自学教材 实施计划

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement.

**Goal:** 创建八年级物理自学教材（12 章 + 附录），单 HTML/章，共享 CSS，SVG 示意图

**架构:** `physics8/` 目录下，每章独立 HTML，共享 `css/physics.css`，复用 `katex/`

**工具链:** 纯 HTML/CSS/JS + KaTeX 渲染（本地离线）+ 内联 SVG 示意图

---

### Task 1: 创建目录结构与共享 CSS

**文件:**
- 创建: `physics8/css/physics.css`
- 创建: `physics8/` 子目录结构

**输入:** 数学教材 `math7.html` 的 CSS 为模板（第9-382行），增加物理专用样式：
- `.experiment-card`、`.experiment-step`、`.experiment-tip`
- SVG 图通用样式（force-arrow、light-ray、lens 等）
- 保持与 math 系列一致的配色变量

### Task 2: 创建导航页 index.html

**文件:**
- 创建: `physics8/index.html`

**内容:**
- 侧边栏导航（12 章 + 附录）
- 学习路径建议
- 各章一句话简介
- 暗色模式切换
- IntersectionObserver 滚动高亮

### Task 3: 第1章 机械运动

**文件:** `physics8/ch01.html`
**SVG:** 刻度尺读数、s-t 图像、v-t 图像（3幅）
**实验探究:** 测量平均速度

### Task 4: 第2章 声现象

**文件:** `physics8/ch02.html`
**SVG:** 音调/响度波形对比（2幅）
**实验探究:** 声音在空气中的传播

### Task 5: 第3章 物态变化

**文件:** `physics8/ch03.html`
**SVG:** 晶体熔化凝固曲线、温度计读数（2幅）
**实验探究:** 探究固体熔化时温度的变化规律

### Task 6: 第4章 光现象

**文件:** `physics8/ch04.html`
**SVG:** 光的反射定律、平面镜成像、光的折射（3幅）
**实验探究:** 探究光的反射定律

### Task 7: 第5章 透镜及其应用

**文件:** `physics8/ch05.html`
**SVG:** 凸透镜三条特殊光线、成像光路图、成像规律图（3幅）
**实验探究:** 凸透镜成像规律

### Task 8: 第6章 质量与密度

**文件:** `physics8/ch06.html`
**SVG:** 量筒读数、托盘天平（2幅）
**实验探究:** 测量物质的密度

### Task 9: 第7章 力

**文件:** `physics8/ch07.html`
**SVG:** 力的示意图、重力三要素（G=mg）、弹力（弹簧测力计）（3幅）
**实验探究:** 弹簧测力计的使用

### Task 10: 第8章 运动和力

**文件:** `physics8/ch08.html`
**SVG:** 二力平衡、摩擦力方向判定、牛顿第一定律（理想实验）（2幅）
**实验探究:** 探究二力平衡的条件 / 探究滑动摩擦力的影响因素

### Task 11: 第9章 压强

**文件:** `physics8/ch09.html`
**SVG:** 液体压强分布、连通器、大气压实验（3幅）
**实验探究:** 探究液体内部压强的特点

### Task 12: 第10章 浮力

**文件:** `physics8/ch10.html`
**SVG:** 浮力示意图、阿基米德实验、浮沉条件（3幅）
**实验探究:** 探究浮力的大小跟哪些因素有关

### Task 13: 第11章 功和机械能

**文件:** `physics8/ch11.html`
**SVG:** 滑轮、斜面、做功示意图（2幅）
**实验探究:** 探究动能与哪些因素有关

### Task 14: 第12章 简单机械

**文件:** `physics8/ch12.html`
**SVG:** 杠杆五要素、滑轮组绕法（2幅）
**实验探究:** 探究杠杆的平衡条件

### Task 15: 附录 appendix.html

**文件:** `physics8/appendix.html`
**内容:**
- 全年级知识体系思维导图
- 核心公式速查表
- 物理实验方法汇总
- 高频易错陷阱总览
- 科学教学法·零基础到精通
- 快速自学与提升技巧
