# 流场修改器使用说明（NeXus）

这份文档只说明流场修改器（nxFlowField）。它用于创建分层流场，通过多个生成层、修饰层和空间算子共同驱动粒子速度。

## 流场修改器（nxFlowField）

流场修改器（nxFlowField）会在一个三维域内烘焙出矢量场，然后把这个场应用到粒子上。你可以把它理解为一个可叠加、可混合、可导入导出的速度场系统。

创建流程：创建流场修改器（nxFlowField）后，插件会自动添加一个默认图层。之后你可以继续添加更多图层，把多个流场来源叠在一起，最后用全局参数决定这个结果如何作用到粒子。

### 设置页（Section）

设置页（Section）切换流场修改器（nxFlowField）的主界面和附加页签。当前界面包含主设置区，以及一个单独的显示页签（Display）。

### 启用（Enabled）

启用（Enabled）控制流场修改器（nxFlowField）是否继续参与系统（NeXus）计算。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制流场修改器（nxFlowField）在编辑器里的辅助显示状态。

## 主设置区

主设置区由图层列表、全局作用方式、流场域（Domain）、放置（Placement）和导入导出（Import / Export）组成。

### 图层（Layers）

图层（Layers）是流场修改器（nxFlowField）的核心。每一层都代表一个流场来源或一次场处理操作，图层按顺序叠加。

图层列表支持：

- 添加新层
- 删除层
- 选择当前编辑层
- 独显（Solo）某一层，只烘焙被独显（Solo）的层

### 图层类型（Layer Type）

图层类型（Layer Type）决定当前层生成什么样的场，或对已有场做什么处理。

当前大类包括：

- 力场类（Fields）：直接生成速度场
- 目标与表面类（Targets & Surfaces）：根据目标、曲线、表面或贴图生成流向
- 来源类（Sources）：从现有模拟或素材读取速度
- 修饰层（Modifiers）：对已有结果做强度、范围或响应修饰
- 空间算子（Operators）：在体素域里对流场做空间运算

### 全局作用方式（Apply）

全局作用方式（Apply）决定烘焙完成后的流场怎样作用到粒子。

可选值：

- 加速度（Acceleration）：把流场当作力来累加
- 设定速度（Set Velocity）：直接把粒子速度设为场值
- 拖拽逼近（Drag）：让粒子速度逐步逼近流场
- 转向（Steer）：让粒子朝流场方向转向，同时尽量保持原速度

### 加速度（Acceleration）

加速度（Acceleration）只在拖拽逼近（Drag）和转向（Steer）模式下出现。

它控制粒子逼近目标流向的速度。

### 场强（Field Strength）

场强（Field Strength）控制整个组合流场的总强度倍增。

### 场权重（Field Weight）

场权重（Field Weight）控制流场施加到粒子上的权重。

它适合配合映射或粒子属性做逐粒子控制。

### 最大力（Max Force）

最大力（Max Force）限制流场施加的最大推动强度。

### 最大速度（Max Speed）

最大速度（Max Speed）限制流场最终可推动出的粒子速度上限。

### 平滑（Smoothing）

平滑（Smoothing）控制流场跨帧更新时的缓动程度。

提高后，场变化会更柔和，也会带来一点延迟感。

### 逃逸标记（Flag on Escape）

逃逸标记（Flag on Escape）用于给离开流场域的粒子打上逃逸标记（Escaped）。

这个标记可以交给别的系统节点（NeXus）继续判断和处理。

## 流场域（Domain）

流场域（Domain）控制流场烘焙域本身。

### 域尺寸（Domain Size）

域尺寸（Domain Size）控制流场盒子的三维范围。

粒子在这个盒子里读取流场，域外通常不会获得当前流场结果。

### 体素尺寸（Voxel Size）

体素尺寸（Voxel Size）控制烘焙网格的单元大小。

数值越小，细节越多，内存和计算量也会提高。

### 精度（Precision）

精度（Precision）控制流场网格使用十六位（16-bit）还是三十二位（32-bit）存储。

十六位（16-bit）更省内存，三十二位（32-bit）更适合细节密集或多次叠加运算的场。

## 放置（Placement）

放置（Placement）控制当前图层在流场域中的放置方式。

### 中心偏移（Centre Offset）

中心偏移（Centre Offset）控制当前层相对修改器原点的位置偏移。

大多数图层都会用到它。方向场（Directional）层没有这个参数。

## 混合（Blend）

混合（Blend）用来控制当前层怎样与下方图层混合。

### 混合模式（Blend Mode）

混合模式（Blend Mode）常见选项包括：

- 覆盖（Over）
- 相加（Add）
- 相减（Subtract）
- 平均（Average）
- 最大幅值（Max Magnitude）

生成层通常会用到混合模式。修饰层和算子层更偏向在已有结果上继续处理。

### 字段模式（Field Mode）

字段模式（Field Mode）决定当前层输出矢量的解释方式。

常见选项包括：

- 方向（Direction）
- 单位速度（Unit Speed）
- 衰减（Attenuate）

### 不透明度（Opacity）

不透明度（Opacity）控制当前层参与最终结果的强度比例。

## 常用图层参数

很多图层会共享下面这些参数：

- 强度（Strength）
- 反转（Invert）
- 旋转（Rotation）
- 距离衰减（Falloff）
- 衰减反转（Invert Falloff）
- 衰减距离（Distance）

启用距离衰减（Falloff）后，当前层的作用会按距离逐步减弱，并且会出现一条可编辑曲线。

## 图层类型速览

### 力场类（Fields）

径向（Radial）

- 从原点向外推或向内吸
- 常用参数有强度（Strength）、反转（Invert）、径向轮廓（Profile）

方向场（Directional）

- 沿局部方向提供均匀推动
- 常用参数有方向（Direction）

涡旋（Vortex）

- 围绕局部轴旋转
- 常用参数有核心半径（Core Radius）、轴向推动（Axial Lift）、径向推拉（Radial）、旋转（Rotation）

涡环（Vortex Ring）

- 创建类似烟圈的环形旋涡
- 常用参数有环半径（Ring Radius）和旋转（Rotation）

轨道（Orbit）

- 围绕中心做刚性旋转
- 重点参数是角速度（Angular Speed）和旋转（Rotation）

卷曲噪声（Curl Noise）和湍流（Turbulence）

- 生成连续噪声流场
- 常用参数有噪声尺度（Noise Scale）、倍频层数（Octaves）、频率倍率（Lacunarity）、粗糙度（Roughness）、动画速度（Animation Speed）、旋转（Rotation）

随机场（Random）

- 给每个体素单元分配随机方向
- 主要参数是随机种子（Seed）

结构流（ABC Flow）

- 生成结构化的闭合湍流
- 常用参数有单元尺寸（Cell Size）、动画（Animate）、旋转（Rotation）

### 目标与表面类（Targets & Surfaces）

目标（Target）

- 朝目标物体吸引或远离
- 支持目标列表和径向轮廓（Profile）

朝向物体（To Object）

- 从修改器原点流向对象列表中的物体
- 支持管道半径（Tube Radius）、旋流（Swirl）和径向推拉（Radial）

沿样条线（Along Spline）和朝向样条线（To Spline）

- 沿曲线流动，或者朝曲线最近点流动
- 需要在对象列表里指定曲线

表面法线（Surface Normal）

- 按网格法线方向生成流场

朝向表面（To Surface）

- 朝网格表面最近点流动

表面切线（Surface Tangent）

- 沿表面切线方向流动
- 会额外用到方向（Direction）

贴图（Texture）

- 从图片读取方向或亮度
- 常用参数有图像（Image）、读取方式（Read As）、方向（Direction）

流动（Flow）

- 类似风洞流，主流方向绕开碰撞网格
- 常用参数有碰撞体（Colliders）、流入方向（Inflow Direction）、质量（Quality）

### 来源类（Sources）

爆炸流体（ExplosiaFX）

- 读取爆炸流体（ExplosiaFX）速度

液体（Liquid）

- 读取翻转粒子流体（FLIP）或仿射粒子流体（APIC）速度

粒子（Particles）

- 读取附近粒子的平均速度，适合做跟随群体流动
- 支持来源列表（Sources）和影响力（Influence）

光流（Optical Flow）

- 从视频或序列帧运动中生成流场
- 还会用到流动平滑（Flow Smoothing）

快照（Snapshot）

- 由快照按钮（Snapshot）冻结当前组合流场得到
- 适合把某一时刻的场保存下来继续使用

## 修饰层（Modifiers）

修饰层针对下方已经存在的流场结果继续加工。

常见类型：

- 增益（Gain）：整体放大或缩小
- 钳制（Clamp）：限制最大场强
- 反转（Invert）：反转场方向
- 归一化（Normalize）：统一速度大小
- 阈值（Threshold）：低于阈值的区域清掉
- 范围映射（Rangemap）：把输入速度范围映射到输出范围
- 量化（Quantize）：把速度分成阶梯段
- 曲线（Curve）：用曲线重塑速度响应

## 空间算子（Operators）

空间算子会直接在体素域里处理组合结果。

常见类型：

- 平滑（Smooth）：柔化场
- 锐化（Sharpen）：增强细节
- 膨胀（Dilate）：向外扩张影响
- 腐蚀（Erode）：向内收缩影响
- 无散投影（Divergence Free）：把场重新投影成更像流体的无散场
- 涡量补偿（Vorticity）：补回旋涡细节
- 外推（Extrapolate）：把已有流动扩散到空白区域
- 平流（Advect）：让流场沿自身继续流动

这类层经常会用到迭代（Iterations）或质量（Quality）。

## 导入导出（Import / Export）

导入导出（Import / Export）用来导入外部流场，或者把当前流场导出保存。

当前界面提供：

- 导入流场（Import Field）
- 导出流场（Export Field）
- 流场快照（Snapshot Field）

流场快照（Snapshot Field）会把当前组合结果冻结成一个快照图层（Snapshot），方便后续继续叠加和编辑。

## 显示页签（Display）

显示页签（Display）负责视口里的流场预览。

### 预览样式（Preview Glyph）

预览样式（Preview Glyph）控制流场用什么方式显示。

常见样式包括线段、箭头、轨迹或关闭预览。

### 字段分辨率（Field Resolution）

字段分辨率（Field Resolution）控制视口预览采样密度。

### 轨迹步数（Trail Steps）

轨迹步数（Trail Steps）只在轨迹预览模式下出现，用来控制每条轨迹的长度。

### 预览长度（Preview Length）

预览长度（Preview Length）只在线段或箭头模式下出现，用来控制显示长度。

### 颜色渐变（Color）

颜色渐变（Color）按流速为预览上色，方便观察快慢分布和场的结构。
