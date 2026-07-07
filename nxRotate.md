# NeXus 旋转修改器使用说明

这份文档只说明旋转修改器（nxRotate）。它用于围绕修改器轴线给粒子施加旋转影响，可以做旋转力场，也可以直接写入旋转速度。

## 旋转修改器（nxRotate）

旋转修改器（nxRotate）不生成粒子。它处理的是已经存在的粒子，让粒子围绕修改器的旋转轴做环绕运动，或者直接得到指定的旋转速度。

它的工作方式比较集中：

- 先用类型（Type）决定当前是力模式还是速度模式。
- 再用旋转速度（Rotate Speed）和速度乘数（Speed Multiplier）决定基础旋转量。
- 如果需要把粒子往旋转轴拉近，再调吸引力（Attraction）。
- 如果需要让旋转逐步加快或限制角速度，再展开角加速度（Angular Acceleration）设置。

### 设置页（Section）

设置页（Section）用于切换当前显示的主设置页。

旋转修改器（nxRotate）除了自己的物体属性（Object Properties）页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）

启用（Enabled）控制旋转修改器（nxRotate）是否参与当前粒子流程。

关闭后，粒子不会再受到这个旋转场的影响。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制旋转修改器（nxRotate）的视口辅助图形是否显示。

它只影响编辑器里的圈线和方向指示，不改变实际旋转结果。

### 物体属性（Object Properties）

物体属性（Object Properties）是旋转修改器（nxRotate）的主设置页。这里集中设置类型（Type）、旋转速度（Rotate Speed）、速度乘数（Speed Multiplier）、吸引力（Attraction）、角加速（Angular Accel）和逃逸速度（Escape Velocity）。

### 类型（Type）

类型（Type）决定旋转修改器（nxRotate）怎样把旋转作用到粒子上。

当前有两种模式：

- 力（Force）：把旋转当作一种持续施加的旋转力。
- 速度（Velocity）：直接设置旋转速度。

如果你想要更像力场那样持续牵引粒子，通常用力（Force）。如果想更直接地指定旋转速度，用速度（Velocity）。

### 旋转速度（Rotate Speed）

旋转速度（Rotate Speed）定义当前旋转的基础角速度。

数值越高，粒子围绕旋转轴转动得越快。负值会反转旋转方向。

### 速度乘数（Speed Multiplier）

速度乘数（Speed Multiplier）用于对旋转速度（Rotate Speed）再乘一个倍率。

它适合在不改基础角速度的前提下，快速整体放大或减弱旋转效果。

### 吸引力（Attraction）

吸引力（Attraction）控制粒子被拉向旋转轴的力度。

它只在类型（Type）为力（Force）时可编辑。数值越高，粒子越容易被拉向旋转中心，再沿着旋转轨迹运动。

### 角加速度（Angular Acceleration）

角加速度（Angular Acceleration）是一个展开开关，用于显示或隐藏角加速（Angular Accel）和旋转速度钳制相关设置。

展开后，界面会继续显示钳制（Clamp）、最小旋转速度（Min Rotation Speed）和最大旋转速度（Max Rotation Speed）。

### 角加速（Angular Accel）

角加速（Angular Accel）用于让旋转速度随时间继续增加或减少。

它适合做逐渐加速的旋转，而不是从头到尾都保持固定角速度。

### 钳制（Clamp）

钳制（Clamp）决定是否把旋转速度限制在最小旋转速度（Min Rotation Speed）和最大旋转速度（Max Rotation Speed）之间。

当前可选方式包括：

- 都不（Neither）：不做钳制。
- 两者（Both）：同时启用最小值和最大值。
- 最小（Min）：只启用最小旋转速度。
- 最大（Max）：只启用最大旋转速度。

### 最小旋转速度（Min Rotation Speed）

最小旋转速度（Min Rotation Speed）定义旋转速度允许降低到的下限。

它只有在钳制（Clamp）启用了最小值限制时才会生效。

### 最大旋转速度（Max Rotation Speed）

最大旋转速度（Max Rotation Speed）定义旋转速度允许提高到的上限。

它只有在钳制（Clamp）启用了最大值限制时才会生效。

### 逃逸速度（Escape Velocity）

逃逸速度（Escape Velocity）定义粒子多快时会脱离当前旋转场的有效控制。

这个值越低，粒子越容易“甩出去”；这个值越高，粒子更容易继续被旋转场束缚。

## 通用页签

### 组（Groups Affected）

组（Groups Affected）用于限制旋转修改器（nxRotate）影响哪些粒子组。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表当前选中的条目。

### 添加组（Add Group）

添加组（Add Group）把一个 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动旋转修改器（nxRotate）的参数。

对于旋转修改器（nxRotate），更适合被映射的通常是旋转速度（Rotate Speed）、速度乘数（Speed Multiplier）、吸引力（Attraction）或逃逸速度（Escape Velocity）。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的规则列表。每一层代表一条“用某种粒子数据驱动某个目标参数”的规则。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射具体控制旋转修改器（nxRotate）的哪个参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定这条映射使用哪种粒子属性作为输入。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定当前映射要作用到哪一层。

旋转修改器（nxRotate）本身不是分层修改器，所以这个字段通常没有实际作用。

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

衰减（Falloff）用于按空间范围限制旋转修改器（nxRotate）的影响。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的对象列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）把一个 nx 衰减（nxFalloff）加入衰减（Falloff）列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减列表项里实际引用的 nx 衰减（nxFalloff）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）定义多个衰减对象怎样一起调制当前旋转效果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。
