# NeXus 缩放修改器使用说明
这份文档说明缩放修改器（nxScale）。它用于通过分层方式修改粒子的几何缩放、半径或质量，并可以按范围、噪波、时间、速度、加速度、衰减或贴图距离来驱动这些变化。

## 缩放修改器（nxScale）
缩放修改器（nxScale）本身不生成粒子，而是对当前流程中的粒子缩放相关数据做分层处理。你可以在同一个修改器里叠加多个图层，让粒子的尺寸、半径或质量随时间、速度、加速度、空间距离或噪波逐步变化。

它的工作方式更像一个“缩放层列表”。每一层都可以选择作用目标、混合方式和具体算法，最终把多层结果叠加到粒子缩放类数据上。

### 设置页（Section）
设置页（Section）用于切换当前显示的主设置页。缩放修改器（nxScale）除了自己的物体属性页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）
启用（Enabled）控制缩放修改器（nxScale）是否参与当前 NeXus 计算。关闭后，这个修改器中的缩放图层不会继续影响粒子缩放、半径或质量。

### 物体属性（Object Properties）
物体属性（Object Properties）是缩放修改器（nxScale）的主设置页。这里包含缩放图层列表，以及当前选中图层的具体参数。

### 缩放层（Scale Layers）
缩放层（Scale Layers）是缩放修改器（nxScale）的核心列表。每一个图层都代表一套独立的缩放规则，最终会按顺序混合成粒子的缩放结果。

### 活动层索引（Active Layer Index）
活动层索引（Active Layer Index）记录缩放层（Scale Layers）列表中当前选中的条目。它主要服务于界面编辑，不需要单独手动修改。

### 图层名称（Layer Name）
图层名称（Layer Name）是列表中显示的名称。默认名称通常会跟随图层类型和目标参数自动变化，手动改名后更适合整理复杂的缩放结构。

### 图层启用（Layer Enabled）
图层启用（Layer Enabled）控制当前缩放图层是否参与计算。关闭后，这一层会保留在列表里，但不会继续影响最终结果。

### 层类型（Layer Type）
图层类型（Layer Type）决定当前图层采用哪一种缩放方式。当前可选类型包括：

- 范围（Range）：在一个起止范围内改变数值。
- 噪波（Noise）：使用噪波来驱动数值变化。
- 随时间改变数值，绝对方式（Change Value Over Time (Absolute)）：按绝对变化量随时间推进。
- 随时间改变数值，相对方式（Change Value Over Time (Relative)）：按百分比随时间推进。
- 设置数值（Set Value）：直接设置绝对值。
- 随衰减设置（Set by Falloff (TODO)）：根据衰减值来控制结果，代码中仍标记为 TODO。
- 按速度缩放（Scale by Speed）：根据粒子速度驱动变化。
- 按加速度缩放（Scale by Acceleration）：根据粒子加速度驱动变化。
- 按映射缩放（Scale by Map）：根据对象距离与顶点组权重映射变化。

### 混合模式（Blend Mode）
混合模式（Blend Mode）决定当前图层如何与前面图层的结果叠加。它定义的是“这一层怎么混进去”，而不是“这一层混多少”。

当前可选模式包括：

- 法线方向（Normal）
- 最小（Min）
- 减去（Subtract）
- 相乘（Multiply）
- 叠加（Overlay）
- 最大（Max）
- 添加（Add）
- 屏幕（Screen）
- 差值（Difference）

### 图层强度（Layer Strength）
图层强度（Layer Strength）控制当前图层对最终缩放结果的影响程度。数值越高，这一层的效果越明显；数值越低，这一层更像轻微修饰。

### 目标参数（Target Parameter）
目标参数（Target Parameter）决定当前图层要作用于哪一种粒子数据。当前可选粒子缩放（Particle Scale）、粒子半径（Particle Radius）和粒子质量（Particle Mass）。

### 时序（Timing）
时序（Timing）模式决定某些图层按什么时间逻辑生效。当前可选出生时（On Birth）、粒子寿命（Particle Age）、帧时间（Frame Time）和衰减（Falloff）。

### 重映射衰减值（Remap Falloff Value）
重映射衰减值（Remap Falloff Value）用于衰减型图层，控制当前图层是否先对衰减值做重映射，再把结果用于缩放计算。

### 绝对值（Absolute Value）
绝对值（Absolute Value）用于直接指定当前图层要写入的目标值。对于粒子缩放，它是三轴缩放值；对于半径和质量，它是单一数值。

### 数值变化（Value Change）
数值变化（Value Change）定义当前图层每一步要增加或减少多少。它适合做随时间、速度或加速度逐步推进的变化。

### 数值变化变异（Value Change Variation）
数值变化变异（Value Change Variation）为数值变化（Value Change）加入随机浮动。它适合让同类粒子之间的变化不要完全一致。

### 百分比变化（Percentage Change）
百分比变化（Percentage Change）按百分比方式改变当前目标值。它适合做相对放大或相对缩小，而不是写死一个绝对变化量。

### 使用限制（Use Limits）
使用限制（Use Limits）控制当前图层是否把结果限制在上下边界内。启用后，数值不会继续无限增大或减小。

### 下限（Lower Limit）
下限（Lower Limit）定义当前图层允许达到的最小值。它适合防止粒子缩放、半径或质量被压得过低。

### 上限（Upper Limit）
上限（Upper Limit）定义当前图层允许达到的最大值。它适合防止粒子缩放、半径或质量被推得过大。

### 在范围内限制（Clamp Within Range）
在范围内限制（Clamp Within Range）控制随机值是否也被限制在当前上下范围内。启用后，随机变化不会轻易跑出设定区间。

### 范围起点（Range Start）
范围起点（Range Start）定义范围型或噪波型图层使用的起始值。它表示渐变或映射的较低一端。

### 范围起点变异（Range Start Variation）
范围起点变异（Range Start Variation）为范围起点（Range Start）加入随机浮动。它适合让起始区间在不同粒子之间略有变化。

### 范围终点（Range End）
范围终点（Range End）定义范围型、噪波型或贴图型图层使用的结束值。它表示映射的较高一端。

### 范围终点变异（Range End Variation）
范围终点变异（Range End Variation）为范围终点（Range End）加入随机浮动。它适合让结束区间不要固定不变。

### 噪波类型（Noise Type）
噪波类型（Noise Type）决定当前噪波图层使用哪一种噪波算法。不同算法会带来不同的纹理感、平滑度和细节分布。

### 种子（Seed）
种子（Seed）控制噪波分布结果。修改它可以在不改变整体参数范围的前提下，得到不同的噪波图案。

### 噪波缩放（Noise Scale）
噪波缩放（Noise Scale）控制噪波图案的整体尺度。数值越大，噪波变化通常越密或越频繁；数值越低，图案通常更舒展。

### 持续度（Persistence）
持续度（Persistence）控制多层噪波叠加时后续层保留多少影响。它会影响细节衰减速度和整体层次感。

### 间隙度（Lacunarity）
间隙度（Lacunarity）控制噪波不同频段之间的间隔关系。它通常会影响细节层次被拉开的程度。

### 频率（Frequency）
频率（Frequency）控制噪波变化有多快。频率越高，数值图案通常越细碎；频率越低，变化更平缓。

### 倍频层数（Octaves）
倍频层数（Octaves）控制噪波叠加的层数。层数越多，细节通常越丰富，但结果也更复杂。

### 开始时间（Start Time）
开始时间（Start Time）定义当前时间型图层从什么时候开始生效。它适合控制变化启动的时间点。

### 结束时间（End Time）
结束时间（End Time）定义当前时间型图层到什么时候结束主要变化。它和开始时间（Start Time）一起决定作用区间。

### 时间变化量（Time Variation）
时间变化量（Time Variation）为时间区间加入随机浮动。它适合让不同粒子的缩放变化不要完全同步。

### 钳制模式（Clamp Mode）
钳制模式（Clamp Mode）决定曲线超过边界后如何处理。当前可选钳制（Clamp）、重复（Repeat）和继续（Continue）。

### 顶点组对象（Vertex Group Object）
顶点组对象（Vertex Group Object）用于贴图型图层，指定从哪个网格或曲线对象读取顶点组数据。当前映射会参考这个对象的几何和权重。

### 顶点组（Vertex Group）
顶点组（Vertex Group）用于贴图型图层，指定具体使用哪个顶点组。当前图层会用这个顶点组的权重分布来驱动缩放结果。

### 最大距离（Max Distance）
最大距离（Max Distance）用于贴图型图层，定义粒子与参考对象之间参与映射的最大距离。距离越近，越容易受到当前贴图层影响。

## 通用页签

### 组（Groups Affected）
组（Groups Affected）用于限制缩放修改器（nxScale）只影响哪些粒子组。列表为空时，表示不额外按组过滤。

### 活动组索引（Active Group Index）
活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的条目。它主要服务于界面选择。

### 添加组（Add Group）
添加组（Add Group）把一个 nx 组（nxGroup）对象加入组（Groups Affected）列表。加入后，缩放修改器只会对这些组里的粒子生效。

### 组对象（Group Object）
组对象（Group Object）是组列表条目里实际引用的 nx 组（nxGroup）对象。只有属于这些组的粒子会进入当前缩放流程。

### 组启用（Group Enabled）
组启用（Group Enabled）控制当前组条目是否参与过滤。关闭后，这个条目会保留在列表中，但暂时不生效。

### 映射（Mapping）
映射（Mapping）用于让粒子数据动态驱动缩放修改器（nxScale）的参数。它适合让某些缩放阈值或层强度随粒子状态变化。

### 映射层（Mapping Layers）
映射层（Mapping Layers）是映射（Mapping）页里的规则列表。每一层都表示“用某种粒子数据去驱动某个参数”的一条映射关系。

### 活动映射索引（Active Mapping Index）
活动映射索引（Active Mapping Index）记录当前正在编辑哪一层映射。通常通过点击映射层列表切换。

### 映射参数（Mapping Parameter）
映射参数（Mapping Parameter）决定当前映射层要驱动哪个目标参数。只有被映射到的参数，才会随粒子数据变化。

### 粒子数据（Particle Data）
粒子数据（Particle Data）决定当前映射层读取哪种粒子属性作为输入。你可以用年龄、速度、半径、颜色等数据来驱动缩放参数。

### 映射图层（Mapping Layer）
映射图层（Mapping Layer）是通用映射系统里的层标识字段。它用于组织多层映射关系。

### 范围最小值（Range Min）
范围最小值（Range Min）定义映射输入范围的下限。低于这个范围时，结果会按映射规则处理。

### 范围最大值（Range Max）
范围最大值（Range Max）定义映射输入范围的上限。它与范围最小值（Range Min）一起决定映射区间。

### 映射权重（Mapping Weight）
映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。数值越高，这一层映射越明显。

### 钳制（Clamp）
钳制（Clamp）决定输入值超出范围后如何处理。启用后，超出区间的值不会继续无限延伸。

### 映射启用（Mapping Enabled）
映射启用（Mapping Enabled）控制当前映射层是否参与计算。关闭后，这一层会保留在列表里，但不再驱动参数。

### 衰减（Falloff）
衰减（Falloff）用于按空间范围限制缩放修改器（nxScale）的影响。它适合让缩放效果只出现在特定位置附近。

### 衰减对象（Falloff Objects）
衰减对象（Falloff Objects）是当前修改器使用的衰减对象列表。只有这些衰减对象定义的范围会参与当前缩放效果。

### 活动衰减索引（Active Falloff Index）
活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。它主要用于界面选择。

### 添加衰减（Add Falloff）
添加衰减（Add Falloff）把一个 NeXus nx 衰减（nxFalloff）加入当前列表。加入后，这个衰减对象就可以参与限制缩放影响范围。

### 衰减对象（Falloff Object）
衰减对象（Falloff Object）是衰减列表条目里实际引用的对象。当前修改器会根据它的空间范围调节缩放效果。

### 衰减启用（Falloff Enabled）
衰减启用（Falloff Enabled）控制当前衰减条目是否参与计算。关闭后，它会留在列表里，但不参与当前影响范围的计算。

### 衰减混合（Falloff Blend）
衰减混合（Falloff Blend）定义多个衰减结果如何与当前缩放修改器效果混合。它决定不同衰减对象叠加时的合成方式。

### 衰减混合强度（Falloff Blend Strength）
衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。数值越高，这个衰减对象对缩放效果的调制越明显。

## 列表操作按钮

这些按钮通常出现在图层、组、映射或衰减列表旁边，用于管理列表内容，不直接参与粒子计算。

### 添加项（Add Item）
添加项（Add Item）在当前列表里新增一个条目。对于缩放修改器（nxScale），具体新建哪种缩放层通常还要结合添加菜单（Add Menu）里的选择。

### 添加菜单（Add Menu）
添加菜单（Add Menu）打开一个类型菜单，用于选择要加入哪一种缩放层。它适合在同一个图层列表里混合多种缩放方式。

### 创建并添加（Create and Add）
创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。缩放修改器（nxScale）的图层列表通常不会直接用到这个按钮，但通用列表系统可能会显示它。

### 连续拾取（Continuous Pick）
连续拾取（Continuous Pick）用于在视口中连续选择多个对象并加入当前列表。缩放修改器（nxScale）的图层列表通常不会直接使用它，但组或衰减类列表可能会用到。

### 移除项（Remove Item）
移除项（Remove Item）从当前列表中删除选中的条目。删除图层后，这一层的缩放规则将不再参与最终结果。

### 上移项（Move Item Up）
上移项（Move Item Up）把当前选中的列表项向上移动一位。对缩放图层来说，这会改变图层叠加顺序。

### 下移项（Move Item Down）
下移项（Move Item Down）把当前选中的列表项向下移动一位。它同样会影响缩放图层的叠加先后顺序。

### 切换启用（Toggle Enabled）
切换启用（Toggle Enabled）切换当前列表条目是否参与作用。它只影响这一条目，不等于关闭整个缩放修改器。

### 增加缩进（Indent Item）
增加缩进（Indent Item）用于层级列表，把当前条目向更深一层移动。缩放修改器（nxScale）的图层列表通常是平级结构，一般不会使用这个按钮。

### 减少缩进（Outdent Item）
减少缩进（Outdent Item）用于层级列表，把当前条目向外提升一层。缩放修改器（nxScale）的图层列表通常是平级结构，一般不会使用这个按钮。
