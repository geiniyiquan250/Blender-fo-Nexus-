# NeXus 速度修改器使用说明

这份文档只说明速度修改器（nxSpeed）。它用于通过速度层（Speed Layers）按分层方式控制粒子的速率，可以做递增、绝对设置、指数变化、样条驱动或按时间范围插值。

## 速度修改器（nxSpeed）

速度修改器（nxSpeed）创建后会自动生成一个默认的递增（Incremental）速度层。后续所有速度变化都是按速度层（Speed Layers）顺序叠加的。

它更像一个“速度层列表”：

- 先用层类型（Layer Type）决定当前层采用哪一种速度算法。
- 再用混合（Blend）和强度（Strength）决定这一层怎样并入前面的结果。
- 然后在该层自己的设置区里定义速度值、时间、样条或上下限。

### 设置页（Section）

设置页（Section）用于切换当前显示的主设置页。

速度修改器（nxSpeed）除了自己的物体属性（Object Properties）页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）

启用（Enabled）控制速度修改器（nxSpeed）是否参与当前粒子流程。

关闭后，所有速度层都会暂停生效，但层本身和参数会保留。

### 物体属性（Object Properties）

物体属性（Object Properties）是速度修改器（nxSpeed）的主设置页。这里包含速度层（Speed Layers）列表，以及当前选中层的具体速度参数。

### 速度层（Speed Layers）

速度层（Speed Layers）是速度修改器（nxSpeed）的核心列表。每一层都代表一套独立的速度处理规则，并按列表顺序叠加。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）记录速度层（Speed Layers）列表当前选中的条目。

### 层名称（Layer Name）

层名称（Layer Name）用于标记当前速度层。

它主要帮助你区分不同速度规则，不直接改变速度结果。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制当前速度层是否参与计算。

关闭后，这一层会保留在列表里，但不会继续影响最终速度结果。

### 层类型（Layer Type）

层类型（Layer Type）决定当前层采用哪一种速度算法。

当前可选类型包括：

- 范围（Range）：在一段时间范围内把速度从起点插值到终点。
- 递增（Incremental）：在当前速度基础上继续增减一个速度量。
- 绝对（Absolute）：把速度直接设为指定值。
- 指数（Exponential）：按指数式加速变化速度。
- 使用样条（Use Spline）：按样条曲线输出速度。

### 混合（Blend）

混合（Blend）决定当前速度层怎样和前面的层结果叠加。

当前可选模式包括法线方向（Normal）、添加（Add）、减去（Subtract）、相乘（Multiply）、差值（Difference）、屏幕（Screen）、叠加（Overlay）、最小（Min）和最大（Max）。

### 强度（Strength）

强度（Strength）控制当前速度层混入最终结果的力度。

数值越高，这一层的速度影响越明显；数值越低，这一层更像轻度修正。

### 速度值（Speed Value）

速度值（Speed Value）用于递增（Incremental）和绝对（Absolute）层。

在递增（Incremental）层里，它表示要额外增加或减少多少速度；在绝对（Absolute）层里，它表示直接设定的速度值。

### 变化（Variation）

变化（Variation）给当前速度值加入随机浮动。

它会跟在具体数值后面读取，比如速度值（Speed Value）、起始速度（Speed Start）、结束速度（Speed End）或最大速度（Speed Max）的变化。

### 加速度（Acceleration）

加速度（Acceleration）只在层类型（Layer Type）为指数（Exponential）时显示。

它控制速度按指数方式变化的强弱。数值越高，速度增长或衰减越明显。

### 限制最小值（Clamp Min）

限制最小值（Clamp Min）控制当前速度层是否启用最小速度限制。

开启后，界面会继续显示粒子速度最小值（Particle Speed Min）和它的变化（Variation）。

### 粒子速度最小值（Particle Speed Min）

粒子速度最小值（Particle Speed Min）定义当前层允许的最低速度。

它只有在限制最小值（Clamp Min）开启时才会生效。

### 限制最大值（Clamp Max）

限制最大值（Clamp Max）控制当前速度层是否启用最大速度限制。

开启后，界面会继续显示粒子速度最大值（Particle Speed Max）和它的变化（Variation）。

### 粒子速度最大值（Particle Speed Max）

粒子速度最大值（Particle Speed Max）定义当前层允许的最高速度。

它只有在限制最大值（Clamp Max）开启时才会生效。

### 速度样条（Speed Spline）

速度样条（Speed Spline）只在层类型（Layer Type）为使用样条（Use Spline）时显示。

它定义一个样条曲线，用来输出当前层的速度变化形状。

### 最大速度（Speed Max）

最大速度（Speed Max）只在层类型（Layer Type）为使用样条（Use Spline）时显示。

它定义速度样条（Speed Spline）输出的整体倍率上限。样条曲线本身给出的是变化形状，最大速度（Speed Max）决定这个形状最终放大到多大。

### 速度时间（Speed Time）

速度时间（Speed Time）只在层类型（Layer Type）为范围（Range）时显示。

它决定范围插值按哪一种时间基准计算。当前可选出生时（On Birth）、粒子寿命（Particle Age）和帧时间（Frame Time）。

### 出生时（On Birth）

出生时（On Birth）是速度时间（Speed Time）的一种模式。

它表示速度层只参考粒子出生时刻的插值结果。这个模式下，界面只需要结束速度（Speed End）和它的变化（Variation），不会显示完整的时间区间设置。

### 粒子寿命（Particle Age）

粒子寿命（Particle Age）是速度时间（Speed Time）的一种模式。

它表示按每个粒子的年龄来推进速度插值。不同粒子会根据各自的年龄落在不同插值位置。

### 帧时间（Frame Time）

帧时间（Frame Time）是速度时间（Speed Time）的一种模式。

它表示按场景时间线的帧时间来推进速度插值。所有粒子会共同跟随时间线变化。

### 起始速度（Speed Start）

起始速度（Speed Start）只在范围（Range）层且速度时间（Speed Time）不是出生时（On Birth）时显示。

它定义插值开始时的速度值。

### 结束速度（Speed End）

结束速度（Speed End）定义范围（Range）层插值结束时的速度值。

它在所有范围（Range）模式里都会使用，只是出生时（On Birth）模式下通常只直接使用这个终点值。

### 开始时间（Start Time）

开始时间（Start Time）只在范围（Range）层且速度时间（Speed Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它定义速度插值从什么时候开始进入主要变化区间。

### 结束时间（End Time）

结束时间（End Time）只在范围（Range）层且速度时间（Speed Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它和开始时间（Start Time）一起定义速度插值的主要时间区间。

### 时间变化量（Time Variation）

时间变化量（Time Variation）只在范围（Range）层且速度时间（Speed Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它为开始时间（Start Time）和结束时间（End Time）加入随机浮动，让不同粒子的速度变化不要完全同步。

### 钳制模式（Clamp Mode）

钳制模式（Clamp Mode）只在范围（Range）层且速度时间（Speed Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它决定缓动曲线超过边界后如何处理。当前可选：

- 钳制（Clamp）
- 在范围内钳制（Clamp In Range）
- 重复（Repeat）
- 继续（Continue）

### 缓动（Ease）

缓动（Ease）只在范围（Range）层且速度时间（Speed Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它是一条缓动曲线，用来定义起始速度（Speed Start）到结束速度（Speed End）之间如何过渡。它控制的是变化节奏，不是最终速度上限。

## 通用页签

### 组（Groups Affected）

组（Groups Affected）用于限制速度修改器（nxSpeed）影响哪些粒子组。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表当前选中的条目。

### 添加组（Add Group）

添加组（Add Group）把一个 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动速度修改器（nxSpeed）的参数。

因为速度修改器（nxSpeed）本身是分层修改器，映射时除了映射目标参数（Mapping Parameter），通常还要确认映射图层（Mapping Layer）是否指向了正确的速度层。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的规则列表。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射控制速度修改器（nxSpeed）的哪个参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定这条映射使用哪种粒子属性作为输入。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于指定当前映射作用到哪一个速度层。

### 范围最小值（Range Min）

范围最小值（Range Min）定义映射输入范围的下限。

### 范围最大值（Range Max）

范围最大值（Range Max）定义映射输入范围的上限。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

### 钳制（Clamp）

钳制（Clamp）决定映射输入超出范围后怎样处理。

### 映射启用（Mapping Enabled）

映射启用（Mapping Enabled）控制当前映射层是否参与计算。

### 衰减（Falloff）

衰减（Falloff）用于按空间范围限制速度修改器（nxSpeed）的影响。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的对象列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）把一个 nx 衰减（nxFalloff）加入衰减（Falloff）列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减列表项里实际引用的 nx 衰减（nxFalloff）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）定义多个衰减对象怎样一起调制当前速度结果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。

## 列表操作按钮

这些按钮通常出现在速度层、组、映射或衰减列表旁边，用于管理列表内容，不直接参与粒子计算。

### 添加项（Add Item）

添加项（Add Item）在当前列表里新增一个条目。

### 添加菜单（Add Menu）

添加菜单（Add Menu）打开一个类型菜单，用于选择要加入哪一种速度层。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口中连续选择多个对象并加入当前列表。

### 移除项（Remove Item）

移除项（Remove Item）从当前列表中删除选中的条目。

### 上移项（Move Item Up）

上移项（Move Item Up）把当前选中的列表项向上移动一位。对速度层来说，这会改变层叠加顺序。

### 下移项（Move Item Down）

下移项（Move Item Down）把当前选中的列表项向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）用于快速打开或关闭当前列表项。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于层级列表里的层级调整。普通速度层列表通常不需要使用它。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于层级列表里的层级调整。普通速度层列表通常不需要使用它。
