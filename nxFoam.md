# 泡沫修改器使用说明（NeXus）

这份文档只说明泡沫修改器（nxFoam）。它用于从流体模拟里生成二级粒子，覆盖表面泡沫、喷雾和气泡三类结果。

## 泡沫修改器（nxFoam）

泡沫修改器（nxFoam）会读取已有的流体粒子运动状态，根据速度、卷气量、波峰曲率和涡量等条件生成二级粒子。它适合做海浪白沫、拍岸喷雾、水下气泡、瀑布泡沫和高速流体附带的细节层。

创建流程：先准备会产出流体粒子的模拟，再添加泡沫修改器（nxFoam）。创建后，它会提供一个主设置页和三个类型页签：泡沫（Foam）、喷雾（Spray）、气泡（Bubble）。

### 设置页（Section）

设置页（Section）切换泡沫修改器（nxFoam）当前显示的主设置页。当前界面由主设置页加泡沫（Foam）、喷雾（Spray）、气泡（Bubble）三个页签组成。

### 启用（Enabled）

启用（Enabled）控制泡沫修改器（nxFoam）是否继续生成二级粒子。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制修改器在编辑器里的辅助显示状态。

## 主设置页

主设置页负责二级粒子的全局解算、边界和数量限制。

### 源求解器（Source Solver）

源求解器（Source Solver）选择泡沫修改器（nxFoam）当前要匹配哪种流体求解器。

可选值包括位置动力学（PBD）、平滑粒子流体（SPH）、翻转粒子流体（FLIP）和仿射粒子流体（APIC）。它决定插件按哪种流体特征来解释源粒子。

### 输出发射器（Output Emitter）

输出发射器（Output Emitter）指定所有泡沫、喷雾和气泡默认创建到哪个发射器里。

留空时，修改器会回退到源流体的发射器。

### 重力（Gravity）

重力（Gravity）指定泡沫修改器（nxFoam）参考的重力对象。

它会影响喷雾下落和气泡上浮方向。

### 生成（Spawn）

生成（Spawn）这一组参数控制所有二级粒子刚出生时的基础行为。

### 生成速度（Spawn Velocity）

生成速度（Spawn Velocity）控制新粒子继承多少源流体速度。

### 生成散布（Spawn Scatter）

生成散布（Spawn Scatter）控制新粒子相对出生位置的随机偏移范围。

### 深层生成速度（Deep Spawn Speed）

深层生成速度（Deep Spawn Speed）控制水面下形成泡沫所需的最低流体速度。

它很适合调节冲击入水、深层翻卷和气泡卷入水体的强度。

### 基于能量的寿命（Lifetime from Energy）

基于能量的寿命（Lifetime from Energy）控制高速出生的二级粒子是否更快消散。

提高后，猛烈飞溅产生的喷雾和泡沫会更短命。

### 类型转换（Type Transition）

类型转换（Type Transition）控制泡沫、喷雾和气泡在生命周期中如何互相转换。

常见模式：

- 自动（Auto）：按所处区域自动转为更合适的类型
- 不转换（None）：出生后一直保持原来的类型
- 清除（Kill）：离开当前类型适合区域后按设定时间移除

### 转换时间（Transition Time）

转换时间（Transition Time）控制粒子出生多久后，才允许开始发生类型转换或被移除。

### 混合时间（Blend Time）

混合时间（Blend Time）控制类型切换后的颜色过渡时长。

### 模拟边界（Simulation Bounds）

模拟边界（Simulation Bounds）是一个对象列表，用来定义二级粒子的活动边界。

每个边界对象都可以决定把粒子限制在体积内部，或者把它当成障碍物使用。

### 限制到流体域（Contain to Fluid Domain）

限制到流体域（Contain to Fluid Domain）控制是否自动把二级粒子约束在源流体域内。

开启后，二级粒子离开流体域时会按边界行为处理。

### 边界行为（Boundary Behaviour）

边界行为（Boundary Behaviour）分别为泡沫（Foam）、喷雾（Spray）、气泡（Bubble）三类粒子定义触碰模拟边界后的处理方式。

常见结果包括移除和碰撞反弹。

### 回弹（Bounce）

回弹（Bounce）控制边界行为设为碰撞时的反弹强度。

### 最大粒子数（Max Particles）

最大粒子数（Max Particles）控制整个模拟允许生成的二级粒子总量上限。

数值设为 0 时表示不设上限。

### 阻力变化（Drag Variance）

阻力变化（Drag Variance）给二级粒子的跟随、下落和上浮行为加入随机差异。

适当提高后，喷雾和气泡运动会更散、更自然。

## 泡沫页签（Foam）

泡沫页签（Foam）控制表面泡沫，也就是贴着液面漂浮和堆积的白沫层。

### 启用（Enable）

启用（Enable）控制是否生成表面泡沫。

### 创建（Creation）

创建（Creation）参数决定什么时候开始生成泡沫，以及生成强度有多大。

这一组主要包括：

- 发射量（Emission）
- 最小能量（Energy Min）
- 最大能量（Energy Max）
- 最小卷气量（Trapped Air Min）
- 最大卷气量（Trapped Air Max）
- 波峰曲率强度（Wave Curvature Strength）
- 最小波峰曲率（Wave Curvature Min）
- 最大波峰曲率（Wave Curvature Max）
- 涡量强度（Vorticity Strength）
- 最小涡量（Vorticity Min）
- 最大涡量（Vorticity Max）
- 生成前粒子年龄（Spawn After Age）
- 最大生成深度（Max Spawn Depth）

这些参数共同决定平静水面、翻卷波峰、旋涡和深层搅动各自会贡献多少泡沫。

### 外观（Appearance）

外观（Appearance）控制泡沫粒子的尺寸、寿命和显示方式。

这一组主要包括：

- 半径（Radius）
- 半径变化（Radius Variation）
- 寿命（Lifetime）
- 寿命变化（Lifetime Variation）
- 自定义显示（Custom Display）
- 颜色（Color）
- 显示（Display）

### 行为（Behaviour）

行为（Behaviour）控制泡沫贴着水面的跟随方式。

### 表面阻力（Surface Drag）

表面阻力（Surface Drag）控制泡沫跟随液面的紧密程度。

### 旋转到表面（Rotate to Surface）

旋转到表面（Rotate to Surface）控制泡沫显示方向是否贴合液面。

### 泡沫持续性（Foam Persistence）

泡沫持续性（Foam Persistence）会让密实的泡沫层活得更久。

### 聚合（Cohesion）

聚合（Cohesion）这一组控制泡沫彼此靠拢或互相推开的趋势。

### 泡沫吸引（Foam Attraction）

泡沫吸引（Foam Attraction）让相邻泡沫更容易聚成条带、团块或泡沫带。

### 泡沫推开（Foam Push）

泡沫推开（Foam Push）让相邻泡沫更均匀地摊开。

### 侵蚀（Erosion）

侵蚀（Erosion）用于清理孤立泡沫。

### 侵蚀速率（Erosion Rate）

侵蚀速率（Erosion Rate）控制孤立泡沫消散得有多快。

### 侵蚀阈值（Erosion Threshold）

侵蚀阈值（Erosion Threshold）控制局部至少要有多少泡沫邻居，才会被视为稳定泡沫层。

### 输出（Output）

输出（Output）里的输出组（Output Group）可以把表面泡沫分到指定粒子组（nxGroup）中。

## 喷雾页签（Spray）

喷雾页签（Spray）控制喷雾，也就是从液面高速抛出的细小粒子。

### 启用（Enable）

启用（Enable）控制是否生成喷雾。

### 创建（Creation）

喷雾的创建参数和泡沫页签（Foam）结构一致，同样由发射量、能量、卷气量、波峰、涡量、生成前粒子年龄和最大生成深度共同决定。

喷雾通常更依赖高速、剧烈翻卷和强抛射区域。

### 外观（Appearance）

喷雾的外观参数同样包括半径、寿命、颜色和显示方式。

### 行为（Behaviour）

喷雾页当前主要提供旋转到表面（Rotate to Surface）。

它决定喷雾粒子的显示方向是否参考液面朝向。

### 输出（Output）

输出（Output）里的输出组（Output Group）可以把喷雾分配到指定粒子组（nxGroup）。

## 气泡页签（Bubble）

气泡页签（Bubble）控制水下气泡，也就是被卷入液体内部并向上浮动的二级粒子。

### 启用（Enable）

启用（Enable）控制是否生成气泡。

### 创建（Creation）

气泡的创建参数和另外两类一致，同样受发射量、能量、卷气量、波峰、涡量、生成前粒子年龄和最大生成深度影响。

其中最大生成深度（Max Spawn Depth）对气泡很重要，因为它常常决定气泡能否在更深的区域生成。

### 外观（Appearance）

气泡的外观参数同样包括半径、寿命、颜色和显示方式。

### 行为（Behaviour）

气泡行为主要由以下参数控制：

- 浮力（Bubble Buoyancy）
- 气泡阻力（Bubble Drag）
- 气泡推开（Bubble Push）
- 旋转到表面（Rotate to Surface）

### 浮力（Bubble Buoyancy）

浮力（Bubble Buoyancy）控制气泡向液面上升的速度。

### 气泡阻力（Bubble Drag）

气泡阻力（Bubble Drag）控制周围流体对气泡运动的拖带强度。

### 气泡推开（Bubble Push）

气泡推开（Bubble Push）控制气泡之间的分散程度。

### 输出（Output）

输出（Output）里的输出组（Output Group）可以把气泡分配到指定粒子组（nxGroup）。
