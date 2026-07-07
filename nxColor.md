# NeXus 颜色修改器使用说明
这份文档说明颜色修改器（nxColor）。它用于通过分层方式修改粒子颜色，你可以按参数、时间、距离或噪波来给粒子着色，也可以直接设置颜色或增减 RGB 通道。

## 颜色修改器（nxColor）
颜色修改器（nxColor）本身不生成粒子，而是对当前流程中的粒子颜色做分层处理。你可以在同一个修改器里叠加多个颜色层，让粒子颜色随条件、时间和空间关系逐步变化。

它的工作方式更像一个“颜色层列表”。每一层都可以定义自己的混合方式、作用强度和颜色来源，最终把多层结果叠加到粒子颜色上。

### 设置页（Section）
设置页（Section）用于切换当前显示的主设置页。颜色修改器（nxColor）除了自己的物体属性页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）
启用（Enabled）控制颜色修改器（nxColor）是否参与当前 NeXus 计算。关闭后，这个修改器中的颜色层不会继续影响粒子颜色。

### 视口可见（Visible in Editor）
视口可见（Visible in Editor）控制颜色修改器（nxColor）在编辑器中的辅助显示是否可见。它不直接改变颜色结果，只影响编辑时的可见性。

### 物体属性（Object Properties）
物体属性（Object Properties）是颜色修改器（nxColor）的主设置页。这里包含出生时着色开关、颜色层列表，以及当前选中颜色层的具体参数。

### 仅在出生时改变（Change On Birth Only）
仅在出生时改变（Change On Birth Only）控制颜色是否只在粒子刚出生时写入一次。启用后，颜色层更适合做初始着色，而不是在粒子生命周期中持续变化。

### 层（Layers）
图层（Layers）是颜色修改器（nxColor）的核心列表。每一个图层都代表一套独立的着色规则，最终会按顺序混合成粒子的颜色结果。

### 活动层索引（Active Layer Index）
活动层索引（Active Layer Index）记录图层（Layers）列表中当前选中的条目。它主要服务于界面编辑，不需要单独手动修改。

### 图层名称（Layer Name）
图层名称（Layer Name）是列表中显示的名称。默认名称通常会跟随图层类型自动变化，手动改名后更适合整理复杂的着色结构。

### 图层启用（Layer Enabled）
图层启用（Layer Enabled）控制当前颜色图层是否参与计算。关闭后，这一层会保留在列表里，但不会继续影响最终颜色结果。

### 层类型（Layer Type）
图层类型（Layer Type）决定当前图层采用哪一种着色方式。当前可选类型包括：

- 参数梯度（Gradient by Parameter）：根据模拟参数用渐变给粒子着色。
- 噪波（Noise）：使用噪波生成颜色变化。
- 设置颜色（Set Color）：直接把粒子设为指定颜色。
- 递增/递减（Increment/Decrement）：逐步增减红、绿、蓝通道。
- 时间相关（Time-Dependent）：让颜色随时间推进变化。
- 到物体的距离（Distance from Object）：根据粒子与对象的距离着色。
- 到摄像机的距离（Distance from Camera）：根据粒子与相机的距离着色。

### 混合模式（Blend Mode）
混合模式（Blend Mode）决定当前图层如何与前面图层的结果叠加。它定义的是“这一层怎么混进去”，而不是“这一层混多少”。

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

### 强度（Strength）
强度（Strength）控制当前图层对最终颜色结果的影响程度。数值越高，这一层的效果越明显；数值越低，这一层更像轻微修饰。

### 变化速率模式（Rate Mode）
变化速率模式（Rate Mode）决定当前图层的颜色变化是立刻生效、按帧时间推进，还是按自定义速率推进。它影响颜色变化随时间发生的节奏。

### 变化速率倍率（Rate Multiplier）
变化速率倍率（Rate Multiplier）在自定义速率模式下控制颜色变化推进得有多快。数值越高，当前图层的变化节奏通常越明显。

### 阈值（Threshold）
阈值（Threshold）用于限制当前颜色图层开始明显生效的门槛。它适合在部分图层里压低较弱影响，只保留更明显的颜色变化。

### 颜色类型（Color Type）
颜色类型（Color Type）决定设置颜色图层使用什么着色来源。当前界面里可选纯颜色（Color）和着色器（Shader），但代码已标明 Shader 在 Blender 中不可用。

### 颜色（Color）
颜色（Color）用于直接指定当前图层写入或混合的基础颜色。它最适合设置颜色图层，也适合做明确的目标色。

### 红色变化率（Red Rate of Change）
红色变化率（Red Rate of Change）控制当前图层对红色通道逐步增加或减少多少。正值会提高红色成分，负值会降低红色成分。

### 绿色变化率（Green Rate of Change）
绿色变化率（Green Rate of Change）控制当前图层对绿色通道逐步增加或减少多少。它和红、蓝通道一起决定增减色图层的整体偏色方向。

### 蓝色变化率（Blue Rate of Change）
蓝色变化率（Blue Rate of Change）控制当前图层对蓝色通道逐步增加或减少多少。调高或调低它，可以让颜色往更冷或更暖的方向偏移。

### 梯度（Gradient）
梯度（Gradient）用于给渐变型颜色图层定义颜色带。它适合把参数、时间、距离或噪波结果映射到一段连续颜色过渡上。

### 参数（Parameter）
参数（Parameter）决定参数梯度图层当前读取哪一种模拟数据来驱动颜色。可选来源包括年龄、方向、移动距离、密度、寿命、质量、邻居、半径、速度、衰减、随机，以及 EFX 体积数据（EFX）里的烟雾（Smoke）、温度（Temperature）和燃料（Fuel）。

### 参数最小值（Parameter Min）
参数最小值（Parameter Min）定义普通数值型参数输入范围的下限。它和参数最大值（Parameter Max）一起决定渐变映射使用的区间。

### 参数最大值（Parameter Max）
参数最大值（Parameter Max）定义普通数值型参数输入范围的上限。输入值在这个区间内时，会沿着当前梯度做颜色过渡。

### 邻居半径（Neighbor Radius）
邻居半径（Neighbor Radius）只在参数为邻点（Neighbor）时使用。它定义当前粒子向周围搜索邻居时的范围，用来决定邻居相关着色的参考范围。

### 距离最小值（Distance Min）
距离最小值（Distance Min）用于按移动距离参数映射颜色时的下限。粒子走过的距离越接近这个值，就越接近梯度起点。

### 距离最大值（Distance Max）
距离最大值（Distance Max）用于按移动距离参数映射颜色时的上限。它和距离最小值（Distance Min）一起限定距离渐变区间。

### 最小速度（Speed Min）
最小速度（Speed Min）用于按速度参数映射颜色时的下限。它决定较慢粒子落在梯度的哪个起始位置。

### 最大速度（Speed Max）
最大速度（Speed Max）用于按速度参数映射颜色时的上限。速度越接近这个值，颜色越接近梯度终点。

### 半径最小值（Radius Min）
半径最小值（Radius Min）用于按粒子半径映射颜色时的下限。它适合区分较小粒子和较大粒子的颜色分布。

### 半径最大值（Radius Max）
半径最大值（Radius Max）用于按粒子半径映射颜色时的上限。和半径最小值（Radius Min）一起决定尺寸驱动的颜色过渡范围。

### 衰减最小值（Falloff Min）
衰减最小值（Falloff Min）用于按衰减数据映射颜色时的下限。它通常表示较弱衰减区域开始进入颜色渐变的位置。

### 衰减最大值（Falloff Max）
衰减最大值（Falloff Max）用于按衰减数据映射颜色时的上限。它通常表示较强衰减区域对应的颜色终点。

### 随机最小值（Random Min）
随机最小值（Random Min）用于参数为随机（Random）时的下限。它与随机最大值（Random Max）一起决定随机着色使用的取值范围。

### 随机最大值（Random Max）
随机最大值（Random Max）用于参数为随机（Random）时的上限。范围越大，可产生的随机颜色变化通常越分散。

### 使用固定点（Use Fixed Point）
使用固定点（Use Fixed Point）控制随机参数是否尽量基于固定参考点来取样。启用后，随机结果更适合保持稳定；关闭后，结果更容易出现变化感。

### 轴（Axis）
方向轴（Axis）只在参数为方向（Direction）时使用。它决定当前图层读取方向数据的哪个轴分量来驱动颜色。

### 完成时间（Time to Completion）
完成时间（Time to Completion）用于时间相关图层，控制一轮颜色渐变完成需要多久。数值越大，颜色变化越慢。

### 完成时（On Complete）
完成时（On Complete）决定时间渐变走到终点后接下来怎么处理。当前可选无操作（Do Nothing）、循环至开始（Wrap to Start）或反转（Reverse）。

### 目标对象（Gradient Object）
目标对象（Gradient Object）只在到物体的距离图层中使用。它指定当前距离着色要参考哪个对象。

### 最近距离（Nearest Distance）
最近距离（Nearest Distance）定义距离类图层中较近一端的阈值。粒子越接近这个距离，颜色越接近梯度起点。

### 最远距离（Furthest Distance）
最远距离（Furthest Distance）定义距离类图层中较远一端的阈值。它和最近距离（Nearest Distance）一起限定距离到颜色的映射范围。

### 目标相机（Gradient Camera）
目标相机（Gradient Camera）只在到摄像机的距离图层中使用。它指定当前距离着色要参考哪个相机对象。

### 视场（FOV）
视场（FOV）决定到摄像机的距离图层是否把相机视场因素一起纳入判断。启用后，颜色变化更适合配合镜头空间来理解。

### 噪波类型（Noise Type）
噪波类型（Noise Type）决定当前噪波图层使用哪一种噪波算法。不同算法会带来不同的纹理感、卷曲感或块状变化。

### 时序（Timing）
时序（Timing）决定噪波按帧时间变化，还是按粒子年龄变化。它会影响噪波图案是更像全局动画，还是更像每个粒子各自推进。

### 颜色通道（Color Channel）
颜色通道（Color Channel）决定噪波结果是先经过梯度映射成颜色，还是直接把噪波用于 RGB 通道。前者更适合艺术化调色，后者更适合直接生成彩色噪波。

### 种子（Seed）
种子（Seed）控制噪波分布结果。修改它可以在不改变整体参数范围的前提下，得到不同的噪波图案。

### 缩放（Scale）
缩放（Scale）控制噪波图案的尺度。数值越大，噪波图案通常越密或变化越频繁；数值越低，图案通常更舒展。

### 持续度（Persistence）
持续度（Persistence）控制多层噪波叠加时后续层保留多少影响。它会影响细节衰减速度和整体层次感。

### 间隙度（Lacunarity）
间隙度（Lacunarity）控制噪波不同频段之间的间隔关系。它通常会影响细节层次拉开的程度。

### 频率（Frequency）
频率（Frequency）控制噪波变化有多快。频率越高，颜色图案通常越细碎；频率越低，颜色图案更平缓。

### 倍频层数（Octaves）
倍频层数（Octaves）控制噪波叠加的层数。层数越多，噪波细节通常越丰富，但结果也更复杂。

### 低裁切（Low Clip）
低裁切（Low Clip）用于切掉噪波较低的一部分范围。它适合减少暗部或弱噪波区域的影响。

### 高裁切（High Clip）
高裁切（High Clip）用于切掉噪波较高的一部分范围。它适合压制过亮或过强的噪波区域。

### 亮度（Brightness）
亮度（Brightness）控制当前噪波图层整体偏亮还是偏暗。它主要改变噪波映射到颜色后的整体明暗感。

### 对比度（Contrast）
对比度（Contrast）控制噪波图层中亮暗差异是否明显。数值越高，颜色变化通常越分明；越低则更柔和。

## 通用页签

### 组（Groups Affected）
组（Groups Affected）用于限制颜色修改器（nxColor）只影响哪些粒子组。列表为空时，表示不额外按组过滤。

### 活动组索引（Active Group Index）
活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的条目。它主要服务于界面选择。

### 添加组（Add Group）
添加组（Add Group）把一个 nx 组（nxGroup）对象加入组（Groups Affected）列表。加入后，颜色修改器只会对这些组里的粒子生效。

### 组对象（Group Object）
组对象（Group Object）是组列表条目里实际引用的 nx 组（nxGroup）对象。只有属于这些组的粒子会进入当前着色流程。

### 组启用（Group Enabled）
组启用（Group Enabled）控制当前组条目是否参与过滤。关闭后，这个条目会保留在列表中，但暂时不生效。

### 映射（Mapping）
映射（Mapping）用于让粒子数据动态驱动颜色修改器（nxColor）的参数。它适合把整体强度或某些数值参数做成随粒子状态变化的效果。

### 映射层（Mapping Layers）
映射层（Mapping Layers）是映射（Mapping）页里的规则列表。每一层都表示“用某种粒子数据去驱动某个参数”的一条映射关系。

### 活动映射索引（Active Mapping Index）
活动映射索引（Active Mapping Index）记录当前正在编辑哪一层映射。通常通过点击映射层列表切换。

### 映射参数（Mapping Parameter）
映射参数（Mapping Parameter）决定当前映射层要驱动哪个目标参数。只有被映射到的参数，才会随粒子数据变化。

### 粒子数据（Particle Data）
粒子数据（Particle Data）决定当前映射层读取哪种粒子属性作为输入。你可以用年龄、速度、半径、颜色等数据来驱动颜色层参数。

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
衰减（Falloff）用于按空间范围限制颜色修改器（nxColor）的影响。它适合让颜色效果只出现在特定位置附近。

### 衰减对象（Falloff Objects）
衰减对象（Falloff Objects）是当前修改器使用的衰减对象列表。只有这些衰减对象定义的范围会参与当前颜色效果。

### 活动衰减索引（Active Falloff Index）
活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。它主要用于界面选择。

### 添加衰减（Add Falloff）
添加衰减（Add Falloff）把一个 NeXus nx 衰减（nxFalloff）加入当前列表。加入后，这个衰减对象就可以参与限制颜色影响范围。

### 衰减对象（Falloff Object）
衰减对象（Falloff Object）是衰减列表条目里实际引用的对象。当前修改器会根据它的空间范围调节颜色效果。

### 衰减启用（Falloff Enabled）
衰减启用（Falloff Enabled）控制当前衰减条目是否参与计算。关闭后，它会留在列表里，但不参与当前影响范围的计算。

### 衰减混合（Falloff Blend）
衰减混合（Falloff Blend）定义多个衰减结果如何与当前颜色修改器效果混合。它决定不同衰减对象叠加时的合成方式。

### 衰减混合强度（Falloff Blend Strength）
衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。数值越高，这个衰减对象对颜色结果的调制越明显。

## 列表操作按钮

这些按钮通常出现在图层、组、映射或衰减列表旁边，用于管理列表内容，不直接参与粒子计算。

### 添加项（Add Item）
添加项（Add Item）在当前列表里新增一个条目。对于颜色修改器（nxColor），具体新建哪种颜色层通常还要结合添加菜单（Add Menu）里的选择。

### 添加菜单（Add Menu）
添加菜单（Add Menu）打开一个类型菜单，用于选择要加入哪一种颜色层。它适合在同一个图层列表里混合多种着色方式。

### 创建并添加（Create and Add）
创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。颜色修改器（nxColor）的图层列表通常不会直接用到这个按钮，但通用列表系统可能会显示它。

### 连续拾取（Continuous Pick）
连续拾取（Continuous Pick）用于在视口中连续选择多个对象并加入当前列表。颜色修改器（nxColor）的图层列表通常不会直接使用它，但组或衰减类列表可能会用到。

### 移除项（Remove Item）
移除项（Remove Item）从当前列表中删除选中的条目。删除图层后，这一层的颜色规则将不再参与最终结果。

### 上移项（Move Item Up）
上移项（Move Item Up）把当前选中的列表项向上移动一位。对颜色图层来说，这会改变图层叠加顺序。

### 下移项（Move Item Down）
下移项（Move Item Down）把当前选中的列表项向下移动一位。它同样会影响颜色图层的叠加先后顺序。

### 切换启用（Toggle Enabled）
切换启用（Toggle Enabled）切换当前列表条目是否参与作用。它只影响这一条目，不等于关闭整个颜色修改器。

### 增加缩进（Indent Item）
增加缩进（Indent Item）用于层级列表，把当前条目向更深一层移动。颜色修改器（nxColor）的图层列表通常是平级结构，一般不会使用这个按钮。

### 减少缩进（Outdent Item）
减少缩进（Outdent Item）用于层级列表，把当前条目向外提升一层。颜色修改器（nxColor）的图层列表通常是平级结构，一般不会使用这个按钮。
