# NeXus 方向修改器使用说明

这份文档只说明方向修改器（nxDirection）。重点说明方向层（Layers）怎样叠加、不同层类型怎样改变粒子方向，以及哪些参数只在对应层类型下有意义。

## 方向修改器（nxDirection）

方向修改器（nxDirection）用于用一组方向层控制粒子运动方向。创建方向修改器（nxDirection）时，插件会自动创建一个默认的方向力（Direction Force）层。

方向修改器（nxDirection）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建方向修改器（nxDirection）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认方向修改器（nxDirection）已包含在该列表里。

常见使用流程：

- 创建发射器（nxEmitter），让场景里先有粒子来源。
- 创建方向修改器（nxDirection）。
- 在方向层（Layers）里选择或添加层。
- 用层类型（Layer Type）决定当前层的方向算法。
- 调整混合模式（Blend Mode）、混合强度（Blend Strength）和该层自己的方向参数。

### 启用（Enabled）

启用（Enabled）控制整个方向修改器（nxDirection）是否参与粒子流程。

关闭后，方向修改器（nxDirection）的方向层不会继续影响粒子。调试多个运动修改器时，可以临时关闭它来判断当前运动变化是否来自方向修改器（nxDirection）。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制方向修改器（nxDirection）的编辑器辅助显示是否可见。

方向修改器（nxDirection）的实际视口绘制还会受到当前活动层的层启用（Layer Enabled）和层视口可见（Layer Visible in Editor）影响。

### 方向层（Direction Layers）

方向层（Direction Layers）是方向修改器（nxDirection）的核心列表。每一层代表一条方向控制规则。

创建方向修改器（nxDirection）时，插件会自动添加一个方向力（Direction Force）层。你可以继续添加相对（Relative）、绝对（Absolute）、圆形（Circular）、圆环（Ring）或使用修改器旋转（Use Modifier Rotation）层。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）记录当前正在编辑方向层（Direction Layers）里的哪一项。

普通用户通常不需要直接修改它。你在方向层（Direction Layers）列表中选中哪一层，活动层索引（Active Layer Index）就对应哪一层。

### 层名称（Layer Name）

层名称（Layer Name）用于标记当前方向层。

它主要帮助你在多层方向设置里区分每一层，不直接决定粒子运动。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制当前方向层是否参与计算。

关闭某一层后，该层不会继续影响粒子。它适合临时比较不同方向层的叠加效果。

### 层类型（Layer Type）

层类型（Layer Type）决定当前方向层使用哪种方向算法。

插件提供这些类型：

- 方向力（Direction Force）：使用方向、扭转和吸引强度控制粒子。
- 相对（Relative）：使用相对方向的朝向（Heading）和俯仰（Pitch）。
- 绝对（Absolute）：使用绝对方向的朝向（Heading）和俯仰（Pitch）。
- 圆形（Circular）：使用朝向、方向强度和 Y 轴踢动形成环绕运动。
- 圆环（Ring）：使用每帧步进、角度限制和环限制形成圆盘或圆环路径。
- 使用修改器旋转（Use Modifier Rotation）：使用方向修改器对象自身旋转作为方向。

### 混合模式（Blend Mode）

混合模式（Blend Mode）决定当前方向层怎样和前面的方向层叠加。

常见模式包括法线方向（Normal）、添加（Add）、减去（Subtract）、相乘（Multiply）、差值（Difference）、屏幕（Screen）、叠加（Overlay）、最小（Min）和最大（Max）。

### 混合强度（Blend Strength）

混合强度（Blend Strength）控制当前方向层混入最终方向结果的比例。

数值越高，这一层影响越明显；数值越低，这一层影响越弱。

### 力模式（Force Mode）

力模式（Force Mode）决定当前方向层怎样作用到粒子运动上。

插件提供两种模式：

- 速度（Velocity）：直接修改粒子速度方向。
- 加速度（Acceleration）：以加速度方式影响粒子。

### 随机种子（Random Seed）

随机种子（Random Seed）用于控制当前方向层里的随机变化结果。

当朝向变化量（Heading Variation）、俯仰变化量（Pitch Variation）或 Y推力变化量（Y Kick Variation）大于 0 时，调整随机种子可以改变粒子之间的随机分布。

### 力设置（Force Settings）

方向力设置（Force Settings）只在层类型（Layer Type）为方向力（Direction Force）时显示。

这一组设置包含方向（Direction）、扭曲（Twist）、吸引（Attract）和力衰减类型（Falloff Type）。

### 方向（Direction）

方向（Direction）只在层类型（Layer Type）为方向力（Direction Force）时显示。

它控制方向力中沿修改器方向推动粒子的强度。正负值会改变作用方向。

### 扭曲（Twist）

扭曲（Twist）只在层类型（Layer Type）为方向力（Direction Force）时显示。

它控制方向力中的旋转或扭转成分。需要让粒子围绕方向产生转动趋势时使用它。

### 吸引（Attract）

吸引（Attract）只在层类型（Layer Type）为方向力（Direction Force）时显示。

它控制方向力中的吸引成分。数值越高，粒子越明显地受该吸引成分影响。

### 衰减类型（Falloff Type）

力衰减类型（Falloff Type）只在层类型（Layer Type）为方向力（Direction Force）时显示。

插件提供平直（Flat）、线性（Linear）、二次（Quadratic）和立方（Cubic）衰减。它决定方向力随距离变化的方式。

### 方向设置（Direction Settings）

方向设置（Direction Settings）是相对（Relative）、绝对（Absolute）和圆形（Circular）层里的方向参数设置区。

相对（Relative）和绝对（Absolute）层会显示朝向（Heading）、朝向变化量（Heading Variation）、俯仰（Pitch）、俯仰变化量（Pitch Variation）和方向强度（Direction Strength）。圆形（Circular）层会显示朝向、朝向变化、方向强度、Y 轴踢动和 Y 踢动变化。

### 朝向（Heading）

朝向（Heading）控制当前层绕垂直轴的方向角度。

它出现在相对（Relative）、绝对（Absolute）和圆形（Circular）层里。调整它可以改变粒子在水平面上的运动方向或环绕弯曲方向。

### 朝向变化量（Heading Variation）

朝向变化量（Heading Variation）给朝向（Heading）增加随机角度变化。

数值越高，不同粒子的水平方向差异越明显。随机结果会受随机种子（Random Seed）影响。

### 俯仰（Pitch）

俯仰（Pitch）控制当前层绕水平轴的方向角度。

它出现在相对（Relative）和绝对（Absolute）层里。调整它可以让粒子方向向上或向下偏转。

### 俯仰变化量（Pitch Variation）

俯仰变化量（Pitch Variation）给俯仰（Pitch）增加随机角度变化。

数值越高，不同粒子的上下方向差异越明显。随机结果会受随机种子（Random Seed）影响。

### 方向强度（Direction Strength）

方向强度（Direction Strength）控制当前方向层的方向影响强度。

它出现在相对（Relative）、绝对（Absolute）、圆形（Circular）和使用修改器旋转（Use Modifier Rotation）层里。数值越高，该层对粒子方向的影响越明显。

### Y轴推力（Y-Axis Kick）

Y轴推力（Y-Axis Kick）只在层类型（Layer Type）为圆形（Circular）时显示。

它给环绕运动增加沿 Y 轴的偏移，让环绕轨迹带有额外的推进或抬升趋势。

### Y推力变化量（Y Kick Variation）

Y推力变化量（Y Kick Variation）只在层类型（Layer Type）为圆形（Circular）时显示。

它给 Y轴推力（Y-Axis Kick）增加随机变化。随机结果会受随机种子（Random Seed）影响。

### 环形运动（Ring Motion）

环形运动（Ring Motion）只在层类型（Layer Type）为圆环（Ring）时显示。

这一组设置包含每帧步数（Step Per Frame）、角度限制（Angle Limit）、限制在圆环内（Limit To Ring）和循环（Loop）。

### 每帧步数（Step Per Frame）

每帧步数（Step Per Frame）只在层类型（Layer Type）为圆环（Ring）时显示。

它设置粒子沿圆环路径每帧前进的角度。

### 角度限制（Angle Limit）

角度限制（Angle Limit）只在层类型（Layer Type）为圆环（Ring）时显示。

它设置圆环运动允许达到的最大角度。只有当角度限制接近 360 度时，循环（Loop）才可编辑。

### 限制在圆环内（Limit To Ring）

限制在圆环内（Limit To Ring）只在层类型（Layer Type）为圆环（Ring）时显示。

它控制粒子被限制到圆环路径的强度。数值越高，粒子越明显地被约束到圆环形态。

### 循环（Loop）

循环（Loop）只在层类型（Layer Type）为圆环（Ring）时显示，并且只有当角度限制（Angle Limit）接近 360 度时可编辑。

开启后，粒子到达角度限制后可以循环回到起点。

### 显示（Display）

显示（Display）是方向层里的视口显示设置区。

它包含层视口可见（Layer Visible in Editor）。只有当前层启用并且层视口可见时，方向修改器才会绘制该活动层的辅助图形。

### 层视口可见（Layer Visible in Editor）

层视口可见（Layer Visible in Editor）控制当前方向层的视口辅助图形是否显示。

它只影响编辑器显示，不直接改变粒子方向结果。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是方向修改器（nxDirection）的主设置页。这里主要编辑方向层（Direction Layers）以及当前层的类型、混合和方向参数。

如果你要调整粒子朝哪里走、多个方向效果怎样叠加，通常先回到物体属性（Object Properties）页。

### 设置页（Section）

设置页（Section）是方向修改器（nxDirection）面板顶部的页签切换。它只切换当前正在编辑的设置页。

方向修改器（nxDirection）常见页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 组（Groups Affected）

组（Groups Affected）用于限制方向修改器（nxDirection）影响哪些粒子组。

如果这里不添加任何组，方向通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，方向效果会根据组列表来限制影响对象。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要直接修改它。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

关闭后，这一条组引用会暂时失效，但不会从列表中删除。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动方向参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用年龄（Age）驱动方向强度（Direction Strength），让方向影响随粒子年龄变化。
- 用速度（Speed）驱动朝向（Heading）或俯仰（Pitch），让高速粒子偏转更多。
- 用 ID（ID）或组（Group）驱动随机相关参数，制造稳定的逐粒子差异。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个方向参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制方向修改器（nxDirection）的哪个参数。

对于方向修改器（nxDirection），常见目标包括朝向（Heading）、俯仰（Pitch）、方向强度（Direction Strength）、Y轴推力（Y-Axis Kick）、圆环和方向力相关参数。可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）、距离（Distance）、文档时间（Document Time）、组（Group）和 ID（ID）。选择粒子数据（Particle Data）后，要配合范围最小值（Range Min）和范围最大值（Range Max）设定输入区间。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于指定要映射方向层（Direction Layers）里的哪一层。

方向修改器（nxDirection）是分层修改器。使用映射时，要确认映射图层（Mapping Layer）指向需要控制的方向层。

### 映射启用（Mapping Enabled）

映射启用（Mapping Enabled）控制这一条映射层是否参与计算。

关闭后，这一条映射规则会保留在列表里，但不会继续驱动目标参数。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

它和范围最大值（Range Max）一起决定输入数据如何映射到目标参数。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

如果映射没有变化，先检查粒子数据实际值是否落在范围最小值（Range Min）和范围最大值（Range Max）之间。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

值越高，这条映射越明显；值越低，这条映射越弱。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围最小值（Range Min）和范围最大值（Range Max）后如何处理。

插件提供钳制（Clamp）、循环（Cycle）和继续（Continue）三种模式。

### 衰减（Falloff）

衰减（Falloff）用于用空间衰减对象控制方向修改器（nxDirection）的影响范围。

如果你想控制“哪里受方向影响”，用衰减（Falloff）；如果想控制“哪些组受方向影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前方向修改器（nxDirection）。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。

关闭后，这一条衰减引用会暂时失效，但仍保留在衰减对象（Falloff Objects）列表中。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

---

## 列表操作按钮

这些小按钮通常出现在方向层、组列表、映射列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择层类型或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表支持的可添加类型。方向层（Direction Layers）使用这个入口添加不同层类型。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。例如创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff）。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。方向层列表通常不使用这个按钮，但组和衰减列表可能会使用。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

方向层（Direction Layers）的顺序会影响层叠加结果。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）用于快速打开或关闭当前列表项。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于树状列表里的层级调整。普通方向层列表通常不需要使用它。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于树状列表里的层级调整。普通方向层列表通常不需要使用它。
