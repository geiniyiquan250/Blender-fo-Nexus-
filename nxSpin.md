# NeXus 自旋修改器使用说明

这份文档只说明自旋修改器（nxSpin）。它用于按层（Layers）控制粒子的旋转、自旋、朝向和时间插值结果。

## 自旋修改器（nxSpin）

自旋修改器（nxSpin）创建时会自动生成一个默认的范围（Range）层。后续所有旋转结果，都会按自旋层（Spin Layers）列表顺序叠加。

当前开发代码里，它本质上是一个“旋转层栈”：

- 先用层类型（Layer Type）决定这一层属于哪种旋转逻辑。
- 再用混合（Blend）和强度（Strength）决定这一层如何并入前面的结果。
- 然后在该层自己的参数区里设置时间、旋转量、变化或目标朝向。

### 设置页（Section）

设置页（Section）用于切换当前显示的主设置页。

自旋修改器（nxSpin）除了自己的物体属性（Object Properties）页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）

启用（Enabled）控制自旋修改器（nxSpin）是否参与当前粒子流程。

关闭后，所有自旋层（Spin Layers）都会暂停生效，但层本身和参数会保留。

### 物体属性（Object Properties）

物体属性（Object Properties）是自旋修改器（nxSpin）的主设置页。这里包含自旋层（Spin Layers）列表，以及当前选中层的具体参数。

### 自旋层（Spin Layers）

自旋层（Spin Layers）是自旋修改器（nxSpin）的核心列表。每一层都代表一套独立的旋转处理规则，并按列表顺序叠加。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）记录自旋层（Spin Layers）列表当前选中的条目。

### 层名称（Layer Name）

层名称（Layer Name）用于标记当前自旋层。

它主要帮助区分不同旋转规则，不直接改变旋转结果。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制当前自旋层是否参与计算。

关闭后，这一层会保留在列表里，但不会继续影响最终旋转结果。

### 层类型（Layer Type）

层类型（Layer Type）决定当前层采用哪一种旋转算法。

当前开发代码提供这些类型：

- 范围（Range）
- 自旋（Spin）
- 增量自旋（Incremental Spin）
- 旋转（Rotate）
- 切向（Tangential）
- 朝向（Facing）
- 滚动（Roll）

但要注意两点实际代码情况：

- 滚动（Roll）层当前只有通用层头，没有独立参数区。
- 当前同步代码里没有单独的滚动（Roll）同步器，所以它不适合被当成已经完整可控的滚动模式。

### 混合（Blend）

混合（Blend）决定当前自旋层怎样和前面的层结果叠加。

可选模式包括法线方向（Normal）、添加（Add）、减去（Subtract）、相乘（Multiply）、差值（Difference）、屏幕（Screen）、叠加（Overlay）、最小（Min）和最大（Max）。

### 强度（Strength）

强度（Strength）控制当前自旋层混入最终结果的力度。

数值越高，这一层的旋转影响越明显；数值越低，这一层更像轻度修正。

### 时间模式（Time Mode）

时间模式（Time Mode）用于自旋（Spin）层和增量自旋（Incremental Spin）层。

当前可选：

- 每帧（Per Frame）
- 每秒（Per Second）
- 出生时（On Birth）仅出现在自旋（Spin）层

它决定这一层的旋转量按帧累加、按秒换算，还是只在粒子出生时应用一次。

### 相对于（Relative To）

相对于（Relative To）用于决定旋转量在世界（World）还是粒子（Particle）空间下解释。

如果你希望旋转始终跟世界轴一致，用世界（World）。如果你希望旋转更贴近粒子自身局部朝向，用粒子（Particle）。

### 自旋量（Spin Amount）

自旋量（Spin Amount）用于自旋（Spin）、增量自旋（Incremental Spin）和切向（Tangential）层。

在不同层里的含义分别是：

- 自旋（Spin）：每一步施加多少旋转。
- 增量自旋（Incremental Spin）：每一步增加多少自旋增量。
- 切向（Tangential）里配合轴自旋（Axis Spin）使用时：表示沿切线轴继续自转的速度。

### 变化（Variation）

变化（Variation）给当前旋转量加入随机浮动。

它会跟在具体数值后面读取，比如自旋量（Spin Amount）、旋转量（Rotation Amount）、旋转偏移（Rotation Offset）或起始/结束自旋的变化。

### 钳制（Clamp）

钳制（Clamp）在自旋（Spin）层和增量自旋（Incremental Spin）层里用于限制累计旋转。

自旋（Spin）层提供钳制（Clamp），增量自旋（Incremental Spin）层还额外提供钳制变化量（Clamp Variation）。

### 钳制变化量（Clamp Variation）

钳制变化量（Clamp Variation）只在增量自旋（Incremental Spin）层显示。

它给钳制（Clamp）值加入随机差异，让不同粒子的累计自旋上限不完全一样。

### 旋转模式（Rotation Mode）

旋转模式（Rotation Mode）只在旋转（Rotate）层显示。

当前可选：

- 绝对（Absolute）：直接把旋转设为指定值。
- 相对（Relative）：在当前旋转基础上再叠加指定值。

### 旋转量（Rotation Amount）

旋转量（Rotation Amount）只在旋转（Rotate）层显示。

它定义要直接写入或叠加的旋转值。

### 使用时间（Use Time）

使用时间（Use Time）只在旋转（Rotate）层显示。

开启后，界面会继续显示时间（Time），让旋转结果按时间逐步到达目标，而不是立即写入。

### 时间（Time）

时间（Time）只在旋转（Rotate）层且使用时间（Use Time）开启时显示。

它定义达到目标旋转量（Rotation Amount）要花多久。

### 切线轴（Tangential Axis）

切线轴（Tangential Axis）只在切向（Tangential）层显示。

它决定粒子的哪一个本地轴去对齐速度方向。

按当前开发代码检查，Y 和 Z 的底层枚举映射是互换的。如果切向结果和界面选择不一致，优先以现版插件实测结果为准。

### 旋转偏移（Rotation Offset）

旋转偏移（Rotation Offset）只在切向（Tangential）层显示。

它用于在“轴向对齐到速度”之后，再额外补一段旋转偏移。

### 轴自旋（Axis Spin）

轴自旋（Axis Spin）只在切向（Tangential）层显示。

开启后，界面会显示一组额外的自旋量（Spin Amount）和变化（Variation），让粒子在已经对齐切线方向后，再沿该轴继续自转。

### 模式（Mode）

模式（Mode）只在朝向（Facing）层显示。

当前可选：

- 面向相机（Face Camera）
- 面向对象（Face Object）
- 面向屏幕（Face Screen）

### 目标（Target）

目标（Target）只在朝向（Facing）层且模式（Mode）为面向对象（Face Object）时显示。

它用于指定要朝向的对象。  
但按当前开发代码检查，目标对象选择界面虽然存在，对象引用本身尚未看到实际同步写入，所以这个模式更适合先按现版插件实际结果确认。

### 自旋时间（Spin Time）

自旋时间（Spin Time）只在范围（Range）层显示。

它决定范围插值按哪一种时间基准计算。当前可选：

- 出生时（On Birth）
- 粒子寿命（Particle Age）
- 帧时间（Frame Time）

### 朝向（Orientation）

朝向（Orientation）只在范围（Range）层显示。

它决定范围（Range）层的旋转值在世界（World）还是粒子（Particle）空间下解释。

### 起始自旋（Spin Start）

起始自旋（Spin Start）只在范围（Range）层显示。

它定义插值起点的旋转值。

### 结束自旋（Spin End）

结束自旋（Spin End）只在范围（Range）层显示。

它定义插值终点的旋转值。

### 开始时间（Start Time）

开始时间（Start Time）只在范围（Range）层且自旋时间（Spin Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它定义主要插值区间从什么时候开始。

### 结束时间（End Time）

结束时间（End Time）只在范围（Range）层且自旋时间（Spin Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它和开始时间（Start Time）一起定义主要插值区间。

### 时间变化量（Time Variation）

时间变化量（Time Variation）只在范围（Range）层且自旋时间（Spin Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它给开始时间（Start Time）和结束时间（End Time）加入随机差异，让不同粒子的旋转变化不要完全同步。

### 钳制模式（Clamp Mode）

钳制模式（Clamp Mode）只在范围（Range）层且自旋时间（Spin Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

当前可选：

- 钳制（Clamp）
- 在范围内钳制（Clamp In Range）
- 重复（Repeat）
- 继续（Continue）

它决定缓动曲线超出时间边界后如何处理。

### 缓动（Ease）

缓动（Ease）只在范围（Range）层且自旋时间（Spin Time）为粒子寿命（Particle Age）或帧时间（Frame Time）时显示。

它是一条缓动曲线，用来定义起始自旋（Spin Start）到结束自旋（Spin End）之间怎样过渡。

## 通用页签

### 组（Groups Affected）

组（Groups Affected）用于限制自旋修改器（nxSpin）影响哪些粒子组。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表当前选中的条目。

### 添加组（Add Group）

添加组（Add Group）把一个 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动自旋修改器（nxSpin）的参数。

对于自旋修改器（nxSpin），更适合被映射的通常是强度（Strength）、自旋量（Spin Amount）、旋转量（Rotation Amount）、时间（Time）或时间变化量（Time Variation）这一类参数。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的规则列表。每一层代表一条“用某种粒子数据驱动某个目标参数”的规则。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射具体控制自旋修改器（nxSpin）的哪个参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定这条映射使用哪种粒子属性作为输入。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定当前映射要作用到哪一层。

对于自旋修改器（nxSpin），它通常用于指定要影响哪一个自旋层（Spin Layer）。

### 范围最小值（Range Min）

范围最小值（Range Min）定义映射输入范围的下限。

### 范围最大值（Range Max）

范围最大值（Range Max）定义映射输入范围的上限。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

### 钳制（Clamp）

钳制（Clamp）决定输入值超出范围最小值（Range Min）和范围最大值（Range Max）后怎样处理。

### 映射启用（Mapping Enabled）

映射启用（Mapping Enabled）控制当前映射层是否参与计算。

### 衰减（Falloff）

衰减（Falloff）用于按空间范围限制自旋修改器（nxSpin）的影响。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的对象列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）把一个 nx 衰减（nxFalloff）加入衰减（Falloff）列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减列表项里实际引用的 nx 衰减（nxFalloff）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）定义多个衰减对象怎样一起调制当前旋转结果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。
