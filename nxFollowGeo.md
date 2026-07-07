# NeXus 跟随几何体修改器使用说明

这份文档只说明跟随几何体修改器（nxFollowGeo）。它用于让粒子贴着几何表面或沿曲线/边线移动，并按连接、释放、扩展层和起始规则控制跟随过程。

## 跟随几何体修改器（nxFollowGeo）

跟随几何体修改器（nxFollowGeo）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建跟随几何体修改器（nxFollowGeo）。

这个修改器的核心输入是对象（Objects）列表。每个条目都引用一个网格（Mesh）、曲线（Curve）或曲线集合（Curves）对象，然后按该对象类型显示不同设置：

- 网格（Mesh）或曲线集合（Curves）对象：主要使用模式（Mode）、连接（Connection）和释放（Release）页签。
- 曲线（Curve）对象：主要使用连接（Connection）、扩展数据（Extended Data）、释放（Release）和样条数据（Spline Data）页签。

当条目引用曲线（Curve）对象，且当前还没有扩展层时，插件会自动添加一个偏移（Offset）扩展层，方便直接开始调整偏移曲线。

### 设置页（Section）

设置页（Section）用于切换当前显示的设置区域。

这个同名字段会出现在两个层级：

- 修改器本体：切换物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）等通用页签。
- 对象条目内部：切换连接（Connection）、释放（Release）、扩展数据（Extended Data）和样条数据（Spline Data）等条目设置页。

### 启用（Enabled）

启用（Enabled）控制当前层级是否参与作用。

这个同名开关会出现在跟随几何体修改器（nxFollowGeo）本体、对象（Objects）条目、扩展层（Layers）条目，以及通用的组（Groups Affected）、映射（Mapping）和衰减（Falloff）列表项上。它只影响当前层级。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制跟随几何体修改器（nxFollowGeo）的编辑器辅助显示是否可见。

它不会关闭实际跟随计算，只影响编辑器里的辅助可见性。

### 物体属性（Object Properties）

物体属性（Object Properties）是跟随几何体修改器（nxFollowGeo）的通用页签，包含修改器本体的基础控制，例如启用（Enabled）和视口可见（Visible in Editor）。

### 对象（Objects）

对象（Objects）是跟随几何体修改器（nxFollowGeo）的输入列表。

每个条目都指定一个几何对象，并把后续参数都绑定到这个对象上。没有有效对象的条目不会显示具体设置，也不会参与跟随计算。

### 活动对象索引（Active Object Index）

活动对象索引（Active Object Index）记录对象（Objects）列表当前选中的条目。

它决定当前编辑的是哪一个对象条目的连接、释放或扩展层设置。

### 添加对象（Add Object）

添加对象（Add Object）把一个可用对象加入对象（Objects）列表。

当前允许的类型是网格（Mesh）、曲线（Curve）和曲线集合（Curves）。

### 物体（Object）

物体（Object）指定当前条目引用的目标对象。

条目绑定到网格（Mesh）或曲线集合（Curves）时，会进入表面/边线跟随分支；绑定到曲线（Curve）时，会进入样条跟随分支。

### 模式（Mode）

模式（Mode）决定当前条目用哪一种跟随方式解释目标对象。

这个同名字段也分两种上下文：

- 网格（Mesh）或曲线集合（Curves）对象时：模式（Mode）在表面（Surface）和边缘（Edge）之间切换。
- 曲线（Curve）对象时：模式（Mode）在引导（Guide）和力（Force）之间切换。

表面（Surface）/边缘（Edge）决定粒子贴着表面还是沿边界特征移动；引导（Guide）/力（Force）决定曲线对粒子更像路径引导还是像距离力场。

### 连接（Connection）

连接（Connection）是当前对象条目的主要连接设置页。

网格（Mesh）和曲线集合（Curves）对象时，这里主要调表面吸附相关参数；曲线（Curve）对象时，这里主要调沿曲线运动的吸引、跟随和对齐参数。

### 释放（Release）

释放（Release）是当前对象条目的释放设置页。

它控制粒子什么时候脱离当前表面或曲线，以及脱离后执行什么动作。

### 扩展数据（Extended Data）

扩展数据（Extended Data）只在曲线（Curve）对象条目里出现。

它用于给当前曲线条目叠加额外的偏移（Offset）或扭曲（Twist）层，并可分别配合曲线资源沿长度做变化。

### 样条数据（Spline Data）

样条数据（Spline Data）只在曲线（Curve）对象条目里出现。

它控制多段曲线怎样选段，以及粒子从曲线的哪个位置开始进入跟随。

### 拉力（Pull）

拉力（Pull）控制粒子朝当前表面或边线被拉回去的强度。

它只在网格（Mesh）或曲线集合（Curves）对象的连接（Connection）页里出现。

### 变化（Variation）

变化（Variation）给当前区域里紧邻的主参数增加随机变化。

在跟随几何体修改器（nxFollowGeo）里，这个同名字段会出现在拉力（Pull）、推力（Push）、偏移（Offset）、吸引强度（Attract Strength）、跟随强度（Follow Strength）、释放时间（Release Time）和位置（Position）旁边。读取时应按它所在那一行的主参数理解。

### 推力（Push）

推力（Push）控制粒子离开当前表面法线方向的推开强度。

它只在网格（Mesh）或曲线集合（Curves）对象的连接（Connection）页里出现。

### 偏移（Offset）

偏移（Offset）控制粒子与表面之间保持的基础距离。

它只在网格（Mesh）或曲线集合（Curves）对象的连接（Connection）页里出现。数值越大，粒子会更远离当前表面。

### 距离（Distance）

距离（Distance）表示当前上下文里的有效距离控制。

这个同名字段有两种用法：

- 在网格（Mesh）或曲线集合（Curves）对象的连接（Connection）页里，它是最大影响距离。
- 在曲线（Curve）对象的释放（Release）页里，它表示沿样条百分比的释放距离。

### 摩擦力（Friction）

摩擦力（Friction）控制粒子沿表面移动时的摩擦阻力。

它只在网格（Mesh）或曲线集合（Curves）对象的连接（Connection）页里出现。

### 视场（FOV）

视场（FOV）控制表面检测时使用的角度范围。

它只在网格（Mesh）或曲线集合（Curves）对象的连接（Connection）页里出现。角度越大，粒子越容易在更宽的方向范围内检测到目标表面。

### 边缘（Edge）

边缘（Edge）控制粒子沿边线特征移动的强度。

它只在对象模式（Mode）为边缘（Edge）时真正有意义；模式（Mode）为表面（Surface）时，这一组参数会灰显。

### 平滑（Smoothing）

平滑（Smoothing）控制边线跟随结果的平滑程度。

它和边缘（Edge）一起只在对象模式（Mode）为边缘（Edge）时真正参与作用。

### 方向（Direction）

方向（Direction）控制粒子沿曲线（Curve）前进的方向。

可选值包括向前（Forwards）和向后（Backwards）。

### 激活范围（Activate Range）

激活范围（Activate Range）控制粒子距离曲线多近时，曲线才开始接管其运动。

它只在曲线（Curve）对象的连接（Connection）页里出现。

### 强度（Strength）

强度（Strength）控制当前曲线条目整体的影响强度。

它是曲线（Curve）对象连接（Connection）页里的总混合量，不等于单独的吸引强度（Attract Strength）或跟随强度（Follow Strength）。

### 吸引强度（Attract Strength）

吸引强度（Attract Strength）控制粒子朝曲线靠拢的强度。

曲线模式（Mode）为引导（Guide）时，它按百分比理解；模式（Mode）为力（Force）时，它按距离强度理解。

### 吸引衰减（Attract Falloff）

吸引衰减（Attract Falloff）控制吸引强度（Attract Strength）随距离衰减的程度。

### 吸引衰减类型（Attract Falloff Type）

吸引衰减类型（Attract Falloff Type）决定吸引衰减（Attract Falloff）使用哪种衰减曲线。

可选值包括平直（Flat）、线性（Linear）、二次（Quadratic）和立方（Cubic）。

### 跟随强度（Follow Strength）

跟随强度（Follow Strength）控制粒子顺着曲线前进的强度。

曲线模式（Mode）为引导（Guide）时，它按百分比理解；模式（Mode）为力（Force）时，它按距离强度理解。

### 跟随衰减（Follow Falloff）

跟随衰减（Follow Falloff）控制跟随强度（Follow Strength）随距离衰减的程度。

### 跟随衰减类型（Follow Falloff Type）

跟随衰减类型（Follow Falloff Type）决定跟随衰减（Follow Falloff）使用哪种衰减曲线。

可选值包括平直（Flat）、线性（Linear）、二次（Quadratic）和立方（Cubic）。

### 对齐（Align）

对齐（Align）控制粒子自身运动方向朝曲线切线对齐的程度。

数值越高，粒子朝曲线前进方向的朝向越稳定。

### 层（Layers）

层（Layers）是曲线（Curve）对象条目内部的扩展层列表。

当前每一层可以是偏移（Offset）或扭曲（Twist）。这些层按列表顺序写入内部扩展树。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）记录层（Layers）列表当前选中的扩展层。

### 类型（Type）

类型（Type）指定当前扩展层是偏移（Offset）还是扭曲（Twist）。

当前代码只处理这两种类型，并且同一类型的曲线资源会按层的唯一标识绑定。

### 偏移值（Offset Value）

偏移值（Offset Value）控制偏移（Offset）层把粒子向曲线外侧推开的基础距离。

### 偏移混合（Offset Blend）

偏移混合（Offset Blend）控制偏移在不同轴向分量之间的混合比例。

### 扭曲方向（Twist Direction）

扭曲方向（Twist Direction）控制粒子围绕曲线旋绕时使用顺时针（Clockwise）还是逆时针（Anti-clockwise）。

### 扭曲数（Twists）

扭曲数（Twists）控制粒子沿曲线前进过程中绕曲线旋绕多少圈。

### 扭曲半径（Twist Radius）

扭曲半径（Twist Radius）控制扭曲轨迹离曲线中心有多远。

### 释放模式（Release Mode）

释放模式（Release Mode）决定粒子在当前对象条目里怎样脱离跟随状态。

这个同名字段有两组上下文：

- 表面分支：当前代码实际提供无（None）和时间（Time）两种释放方式。
- 曲线分支：可选样条末端（Spline End）、衰减（Falloff）、时间（Time）和选集（Selection）。

### 时间模式（Time Mode）

时间模式（Time Mode）决定释放时间（Release Time）按哪种时间来源计算。

可选值包括粒子寿命（Particle Age）和帧时间（Frame Time）。

### 释放时间（Release Time）

释放时间（Release Time）控制粒子在当前条目里停留多久后脱离跟随状态。

这个同名字段会分别出现在表面释放和曲线释放里，读取时要按当前页签理解。

### 释放时（On Release）

释放时（On Release）控制粒子从曲线分支释放后立刻执行什么动作。

可选值包括无操作（Do Nothing）、循环（Loop）、反转（Reverse）、销毁（Kill）和更改组（Change Group）。

### 多段（Multi Segment）

多段（Multi Segment）控制曲线包含多段时，粒子选择哪一种分段策略。

可选值包括任意分段（Any Segment）、特定段（Specific Segment）、序列中的段数（Segments In Sequence）和最近线段（Nearest Segment）。

### 段（Segment）

段（Segment）指定多段（Multi Segment）为特定段（Specific Segment）时使用哪一段。

### 起始模式（Starting Mode）

起始模式（Starting Mode）决定粒子初次接入曲线时从哪里开始。

可选值包括最近点（Nearest Point）、最近顶点（Nearest Vertex）、特定顶点（Specific Vertex）和沿样条位置（Position Along Spline）。

### 位置（Position）

位置（Position）指定沿样条位置（Position Along Spline）模式下的起始百分比位置。

它只在起始模式（Starting Mode）为沿样条位置（Position Along Spline）时显示。

### 索引（Index）

索引（Index）指定特定顶点（Specific Vertex）模式下要使用的顶点编号。

它只在起始模式（Starting Mode）为特定顶点（Specific Vertex）时显示。

### 组（Groups Affected）

组（Groups Affected）限制跟随几何体修改器（nxFollowGeo）影响哪些粒子组。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表当前选中的条目。

### 添加组（Add Group）

添加组（Add Group）把一个 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）指定当前组条目引用的 nx 组（nxGroup）对象。

### 映射（Mapping）

映射（Mapping）用于用粒子数据（Particle Data）动态驱动跟随几何体修改器（nxFollowGeo）的参数。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是跟随几何体修改器（nxFollowGeo）的参数驱动列表。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录映射层（Mapping Layers）列表当前选中的条目。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）指定当前映射层要驱动的目标参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）指定当前映射层读取哪一种粒子属性作为输入。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）是当前映射条目的内部标识。

### 范围最小值（Range Min）

范围最小值（Range Min）定义映射输入范围的下界。

### 范围最大值（Range Max）

范围最大值（Range Max）定义映射输入范围的上界。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层混入最终结果的强度。

### 钳制（Clamp）

钳制（Clamp）决定映射结果是否限制在当前范围内。

### 衰减（Falloff）

衰减（Falloff）用于用空间对象限制跟随几何体修改器（nxFollowGeo）的作用范围。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是跟随几何体修改器（nxFollowGeo）的衰减对象列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录衰减对象（Falloff Objects）列表当前选中的条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）把一个衰减对象加入跟随几何体修改器（nxFollowGeo）的衰减列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）指定当前衰减条目使用的对象。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象怎样合成最终影响结果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减混合在最终结果中的权重。
