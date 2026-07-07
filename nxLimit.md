# NeXus 限制修改器使用说明

这份文档只说明限制修改器（nxLimit）。它用于通过多层限制规则，对粒子的速度、位置、缩放、旋转、速率、半径、质量和用户值做上限、下限或方向约束。

## 限制修改器（nxLimit）

限制修改器（nxLimit）创建后会自动生成一个默认的速度（Velocity）限制层。后续所有限制都是按限制层（Limit Layers）顺序叠加的。

它由一组分层限制操作组成：

- 先用层类型（Layer Type）决定当前层要限制哪一种粒子属性。
- 再用混合模式（Blend Mode）和混合强度（Blend Strength）决定这一层怎样并入前面的结果。
- 然后在该层自己的设置区里决定限制范围、限制方向或固定方式。

### 设置页（Section）

设置页（Section）用于切换当前显示的主设置页。

限制修改器（nxLimit）除了自己的物体属性（Object Properties）页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）

启用（Enabled）控制限制修改器（nxLimit）是否参与当前粒子流程。

关闭后，所有限制层都会暂停生效，但层本身和参数会保留。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制限制修改器（nxLimit）的编辑器辅助显示是否可见。

当前代码没有专门的限制视口图形，这个开关主要属于通用显示控制。

### 物体属性（Object Properties）

物体属性（Object Properties）是限制修改器（nxLimit）的主设置页。这里包含限制层（Limit Layers）列表，以及当前选中层的具体限制参数。

### 限制层（Limit Layers）

限制层（Limit Layers）是限制修改器（nxLimit）的核心列表。每一层都只处理一种粒子属性，并按列表顺序参与结果叠加。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）记录限制层（Limit Layers）列表当前选中的条目。

### 层名称（Layer Name）

层名称（Layer Name）用于标记当前限制层。

它主要帮助你区分不同限制规则，不直接改变限制结果。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制当前限制层是否参与计算。

关闭后，这一层会保留在列表里，但不会继续影响最终限制结果。

### 层类型（Layer Type）

层类型（Layer Type）决定当前层要限制哪一种粒子属性。

当前可选类型包括：

- 速度（Velocity）
- 位置（Position）
- 缩放（Scale）
- 旋转（Rotation）
- 速度（Speed）
- 半径（Radius）
- 质量（Mass）
- 用户值（User Value）

这里的速度（Velocity）和速度（Speed）不是同一个概念。速度（Velocity）是按轴分别限制的向量；速度（Speed）是限制运动速率大小。

### 混合模式（Blend Mode）

混合模式（Blend Mode）决定当前限制层怎样和前面的层结果叠加。

当前可选模式包括：

- 法线方向（Normal）
- 添加（Add）
- 减去（Subtract）
- 相乘（Multiply）
- 差值（Difference）
- 屏幕（Screen）
- 叠加（Overlay）
- 最小（Min）
- 最大（Max）

### 混合强度（Blend Strength）

混合强度（Blend Strength）控制当前限制层混入最终结果的力度。

数值越高，这一层的限制越明显；数值越低，这一层更像轻度修正。

### 坐标（Coordinates）

坐标（Coordinates）只在速度（Velocity）层里出现。

它决定速度限制按哪一种坐标系解释。当前可选发射器（Emitter）和世界（World）。

### 坐标系统（Coordinate System）

坐标系统（Coordinate System）只在位置（Position）层里出现。

它决定位置限制按哪一种空间基准解释。当前可选发射器（Emitter）、世界（World）和粒子（Particle）。

- 发射器（Emitter）：相对于发射器。
- 世界（World）：按世界坐标解释。
- 粒子（Particle）：相对于粒子出生位置。

### 范围最小值（Range Min）

范围最小值（Range Min）表示当前限制层的下限开关或下限入口。

它在不同层里的含义略有区别：

- 速度（Velocity）层里，它对应每个轴的最小限制百分比。
- 缩放（Scale）、速度（Speed）、半径（Radius）、质量（Mass）和用户值（User Value）层里，它表示是否启用下限。

### 范围最大值（Range Max）

范围最大值（Range Max）表示当前限制层的上限开关或上限入口。

它在不同层里的含义也会随层类型变化：

- 速度（Velocity）层里，它对应每个轴的最大限制百分比。
- 缩放（Scale）、速度（Speed）、半径（Radius）、质量（Mass）和用户值（User Value）层里，它表示是否启用上限。

### 值（Value）

值（Value）是当前限制项真正写入的限制数值。

它会随着层类型不同而表示不同内容，例如最小速度、最大半径、上限质量或当前缩放向量。

### 变化（Variation）

变化（Variation）给当前限制值加入随机变化。

它通常跟在某个具体限制值后面读取，例如最低速度的变化、正向旋转限制的变化或最小质量的变化。

### X变化量（Variation X）

X变化量（Variation X）用于三轴向量限制的 X 分量随机变化。

### Y变化量（Variation Y）

Y变化量（Variation Y）用于三轴向量限制的 Y 分量随机变化。

### Z变化量（Variation Z）

Z变化量（Variation Z）用于三轴向量限制的 Z 分量随机变化。

### X轴限制（X-Axis Restriction）

X轴限制（X-Axis Restriction）只在速度（Velocity）层里出现。

它决定 X 轴速度允许限制哪一个方向。当前可选无（None）、+X 和 -X。

### Y轴限制（Y-Axis Restriction）

Y轴限制（Y-Axis Restriction）只在速度（Velocity）层里出现。

它决定 Y 轴速度允许限制哪一个方向。当前可选无（None）、+Y 和 -Y。

### Z轴限制（Z-Axis Restriction）

Z轴限制（Z-Axis Restriction）只在速度（Velocity）层里出现。

它决定 Z 轴速度允许限制哪一个方向。当前可选无（None）、+Z 和 -Z。

### 无倾斜（No Banking）

无倾斜（No Banking）只在速度（Velocity）层里出现。

它用于关闭速度限制里的倾斜处理。当前代码只能确认它作为一个单独布尔开关同步到内部数据。

### X限制（X Restriction）

X限制（X Restriction）只在位置（Position）层里出现。

它决定 X 轴位置怎么限制。当前可选无（None）、X+、X-、范围（Range）和固定（Fixed）。

- 选固定（Fixed）时，显示 X固定（X Fixed）。
- 选范围（Range）时，同时显示 X最小值（X Min）和 X最大值（X Max）。
- 选 X+ 或 X- 时，只显示一侧边界。

### Y限制（Y Restriction）

Y限制（Y Restriction）只在位置（Position）层里出现，规则和 X限制（X Restriction）相同，只是作用在 Y 轴。

### Z限制（Z Restriction）

Z限制（Z Restriction）只在位置（Position）层里出现，规则和 X限制（X Restriction）相同，只是作用在 Z 轴。

### X最小值（X Min）

X最小值（X Min）定义位置（Position）层里 X 轴的最小边界。

### X最大值（X Max）

X最大值（X Max）定义位置（Position）层里 X 轴的最大边界。

### Y最小值（Y Min）

Y最小值（Y Min）定义位置（Position）层里 Y 轴的最小边界。

### Y最大值（Y Max）

Y最大值（Y Max）定义位置（Position）层里 Y 轴的最大边界。

### Z最小值（Z Min）

Z最小值（Z Min）定义位置（Position）层里 Z 轴的最小边界。

### Z最大值（Z Max）

Z最大值（Z Max）定义位置（Position）层里 Z 轴的最大边界。

### X固定（X Fixed）

X固定（X Fixed）在 X限制（X Restriction）设为固定（Fixed）时出现，用来把 X 轴位置固定到指定值。

### Y固定（Y Fixed）

Y固定（Y Fixed）在 Y限制（Y Restriction）设为固定（Fixed）时出现，用来把 Y 轴位置固定到指定值。

### Z固定（Z Fixed）

Z固定（Z Fixed）在 Z限制（Z Restriction）设为固定（Fixed）时出现，用来把 Z 轴位置固定到指定值。

### 链接通道（Link Channels）

链接通道（Link Channels）只在旋转（Rotation）层里出现。

开启后，旋转限制会改成统一控制全部旋转通道；关闭后，改为分别编辑朝向（Heading）、俯仰（Pitch）和倾斜（Banking）。

这时界面里的开关和数值会按“某个通道是否启用正向/负向限制”来显示，不是单独的模式切换。

### 模式（Mode）

模式（Mode）在旋转（Rotation）层里决定旋转限制使用哪一种参考方式。

当前可选世界（World）和相对（Relative）。

### 通道（Channel）

通道（Channel）只在旋转（Rotation）层关闭链接通道（Link Channels）时出现。

它用于切换当前编辑朝向（Heading）、俯仰（Pitch）还是倾斜（Banking）这一组旋转限制。

当前界面的工作顺序是：

- 先选通道（Channel），也就是朝向（Heading）、俯仰（Pitch）或倾斜（Banking）。
- 再决定是否启用这一通道的正向限制或负向限制。
- 最后分别设置正向限制（Positive Limit）和负向限制（Negative Limit）的角度上限。

### 正（Positive）

正（Positive）在旋转（Rotation）层里表示当前通道的正向一侧限制开关。

界面里实际会显示成“启用朝向正向限制”“启用俯仰正向限制”或“启用倾斜正向限制”这类文字。开关关闭时，下面对应的正向限制（Positive Limit）数值不会生效。

### 负向（Negative）

负向（Negative）在旋转（Rotation）层里表示当前通道的负向一侧限制开关。

界面里实际会显示成“启用朝向负向限制”“启用俯仰负向限制”或“启用倾斜负向限制”这类文字。开关关闭时，下面对应的负向限制（Negative Limit）数值不会生效。

### 正向限制（Positive Limit）

正向限制（Positive Limit）定义当前旋转通道允许达到的正向角度上限。

如果当前选中的是朝向（Heading）页签，它表示朝向的正向角度上限；如果当前选中的是俯仰（Pitch）或倾斜（Banking），读法也是同样的。

### 负向限制（Negative Limit）

负向限制（Negative Limit）定义当前旋转通道允许达到的负向角度上限。

它和正向限制（Positive Limit）是分开控制的，所以可以只限制一侧，也可以两侧同时限制。

### 速度（Speed）

速度（Speed）层限制的是粒子的速率大小，而不是方向向量。

它只提供下限和上限，不按轴分别设置。

### 半径（Radius）

半径（Radius）层用于限制粒子半径的最小值和最大值。

### 质量（Mass）

质量（Mass）层用于限制粒子质量的最小值和最大值。

### 用户值（User Value）

用户值（User Value）层用于限制粒子的用户值数据。

如果当前流程里有其他修改器把用户值（User Value）当作辅助通道使用，这一层可以直接约束它的可用范围。

## 通用页签

### 组（Groups Affected）

组（Groups Affected）用于限制限制修改器（nxLimit）影响哪些粒子组。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表当前选中的条目。

### 添加组（Add Group）

添加组（Add Group）把一个 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动限制修改器（nxLimit）的参数。

因为限制修改器（nxLimit）本身是分层修改器，映射时除了映射目标参数（Mapping Parameter），通常还要确认映射图层（Mapping Layer）是否指向了正确的限制层。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的规则列表。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射控制限制修改器（nxLimit）的哪个参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定这条映射使用哪种粒子属性作为输入。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于指定当前映射作用到哪一个限制层。

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

衰减（Falloff）用于按空间范围限制限制修改器（nxLimit）的影响。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的对象列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）把一个 nx 衰减（nxFalloff）加入衰减（Falloff）列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减列表项里实际引用的 nx 衰减（nxFalloff）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）定义多个衰减对象怎样一起调制当前限制结果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。
