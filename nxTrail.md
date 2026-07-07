# NeXus 拖尾修改器使用说明

这份文档说明拖尾修改器（nxTrail）。它为发射器（nxEmitter）的粒子记录轨迹，并把轨迹显示为视口线条或生成可渲染的 Blender 曲线（Curves）对象。

## 拖尾修改器（nxTrail）

拖尾修改器（nxTrail）用于根据粒子历史位置生成拖尾。每个拖尾源来自一个发射器（nxEmitter），并在发射器（Emitters）列表中单独设置颜色、长度、连接方式、厚度和样条生成方式。

显示（Display）为线条（Lines）时，拖尾以视口覆盖线条显示；显示（Display）为样条（Splines）时，插件会为每个有效拖尾源生成子曲线（Curves）对象，并配置曲线、材质、颜色和厚度数据。禁用拖尾修改器或切回线条（Lines）时，已生成的曲线对象会被清理或清空。

### 设置页（Section）

设置页（Section）切换当前显示的设置页。拖尾修改器（nxTrail）本体包含显示（Display）和发射器（Emitters）；每个发射器源条目内部还有常规（General）、厚度（Thickness）和样条线（Spline）三个子页签。

普通 NeXus 修改器通用页签还包含物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。右键页签时，帮助会打开对应的小节。

### 启用（Enabled）

启用（Enabled）控制拖尾修改器（nxTrail）是否参与当前 NeXus 计算。

关闭后，该拖尾修改器不会继续向管线登记拖尾源。用于样条（Splines）显示时，相关曲线输出会被清理。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制拖尾修改器（nxTrail）在编辑器中的辅助显示是否可见。

对于线条（Lines）显示模式，视口可见性会影响拖尾覆盖线条能否显示。对于样条（Splines）显示模式，还需要检查生成的曲线（Curves）子对象自身是否被隐藏。

### 物体属性（Object Properties）

物体属性（Object Properties）是通用页签，包含拖尾修改器自身的基础控制，例如启用（Enabled）和视口可见（Visible in Editor）。

这些设置作用于整个拖尾修改器，不是单个发射器源条目的设置。

### 显示（Display）

显示（Display）选择拖尾输出方式。

可选值：

- 线条（Lines）：在视口中以线条覆盖方式显示拖尾，直接使用 GPU 中的拖尾缓冲数据。
- 样条（Splines）：生成 Blender 曲线（Curves）子对象，可用于场景对象、材质和渲染流程。

线条（Lines）适合快速预览和调试。样条（Splines）会生成实际曲线对象，适合需要渲染或进一步处理曲线的场景。

### 发射器（Emitters）

发射器（Emitters）是拖尾源列表。每个条目引用一个发射器（nxEmitter），并为该发射器的粒子定义拖尾规则。

同一个拖尾修改器可以包含多个发射器源。每个源可以独立设置颜色、长度、连接算法、厚度和样条生成方式。

### 活动发射器索引（Active Emitter Index）

活动发射器索引（Active Emitter Index）是发射器（Emitters）列表中当前选中条目的索引。

它决定下方显示哪一个发射器源的常规（General）、厚度（Thickness）和样条线（Spline）设置。通常通过点击列表条目切换，不需要手动输入索引。

### 添加发射器（Add Emitter）

添加发射器（Add Emitter）把发射器（nxEmitter）加入拖尾源列表。

添加后，该条目会创建独立的内部资源，用于保存颜色渐变和厚度曲线等源级设置。移除项时，这些资源会随条目清理。

### 发射器对象（Emitter Object）

发射器对象（Emitter Object）指定当前拖尾源引用的发射器（nxEmitter）。

只有发射器类型对象可以作为拖尾源。没有有效发射器对象的条目不会生成拖尾源设置，也不会参与拖尾计算。

### 发射器启用（Emitter Enabled）

发射器启用（Emitter Enabled）控制当前发射器源是否参与拖尾计算。

关闭后，该条目保留在列表中，便于之后重新启用或对比某个发射器对拖尾结果的影响。

### 常规（General）

常规（General）是单个发射器源的主要设置页，包含颜色、长度、采样、连接算法和冻结行为。

先在这个页签确认拖尾长度和连接方式，再根据输出需要调整厚度（Thickness）和样条线（Spline）页签。

### 厚度（Thickness）

厚度（Thickness）控制拖尾是否写入厚度和颜色数据，以及厚度来源。

如果启用无厚度/颜色数据（No Thickness/Color Data），厚度模式和拖尾颜色模式会灰显，拖尾源不会输出这些额外数据。

### 样条线（Spline）

样条线（Spline）控制样条（Splines）显示模式下生成曲线对象的类型和插值方式。

这些设置主要影响生成的 Blender 曲线（Curves）对象。显示（Display）为线条（Lines）时，视口线条仍使用拖尾缓冲数据，不依赖曲线对象。

### 颜色模式（Color Mode）

颜色模式（Color Mode）选择拖尾源的整体颜色来源。

可选值：

- 标准（Standard）：使用颜色（Color）字段中的单一颜色。
- 梯度（Gradient）：沿拖尾长度采样梯度颜色。

梯度（Gradient）会使用该源条目的颜色梯度资源。无厚度/颜色数据（No Thickness/Color Data）开启时，颜色和厚度数据不会输出。

### 颜色（Color）

颜色（Color）设置标准（Standard）颜色模式下的拖尾颜色。

它用于线条（Lines）视口绘制，也会用于样条（Splines）生成曲线对象时的基础材质颜色。梯度（Gradient）模式下，颜色由梯度资源决定。

### 长度模式（Length Mode）

长度模式（Length Mode）选择拖尾长度的计量方式。

可选值：

- 时间（Time）：按时间长度记录拖尾。
- 距离（Distance）：按距离长度记录拖尾。

时间（Time）模式会显示整个场景（Full Scene）和时间长度（Time Length）。距离（Distance）模式会显示距离长度（Distance Length）。

### 时间长度（Time Length）

时间长度（Time Length）设置时间（Time）模式下的拖尾持续时间。

只有长度模式（Length Mode）为时间（Time），并且整个场景（Full Scene）关闭时显示。它使用 NeXus 时间属性，可以按当前时间单位解释拖尾长度。

### 距离长度（Distance Length）

距离长度（Distance Length）设置距离（Distance）模式下的拖尾长度。

只有长度模式（Length Mode）为距离（Distance）时显示。它按空间距离限制拖尾记录范围。

### 整个场景（Full Scene）

整个场景（Full Scene）控制时间（Time）模式下拖尾是否覆盖整个场景时间范围。

开启后，时间长度（Time Length）不显示，拖尾使用完整场景持续时间。关闭后，可以用时间长度（Time Length）指定单独的拖尾时间长度。

### 帧采样（Frame Sampling）

帧采样（Frame Sampling）设置每隔多少帧记录一个拖尾点。

数值为 1 时每帧记录。提高数值会减少记录点数量，让拖尾更稀疏，也会影响样条（Splines）输出中的点分布。

### 变化（Variation）

变化（Variation）为拖尾长度添加随机变化。

它用于让同一发射器源中的粒子拖尾长度产生差异，避免所有拖尾长度完全一致。

### 连接（Connections）

连接（Connections）选择粒子之间如何组成拖尾线段或曲线段。

可选值：

- 无连接（No Connections）：按每个粒子的历史记录形成拖尾。
- 直线序列（Straight Sequence）：按发射顺序连接连续粒子。
- 分段序列（Segmented Sequence）：按段连接粒子，中间插入间隔。
- 多序列（Multiple Sequence）：从粒子源中生成多条序列。
- 所有点（All Points）：连接源中的所有点对。
- 最近索引（Nearest Index）：按粒子 ID 顺序连接邻近索引。
- 最近距离（Nearest Distance）：按距离窗口连接粒子。
- 簇（Cluster）：按距离把粒子聚类，再在簇内连接。

不同算法会显示不同的附加参数。先选算法，再检查下方出现的限制项。

### 分段长度（Segment Length）

分段长度（Segment Length）只在连接（Connections）为分段序列（Segmented Sequence）时显示。

它设置每一段包含的连接长度。数值越大，每段连续连接的粒子越多。

### 间隙长度（Gap Length）

间隙长度（Gap Length）只在连接（Connections）为分段序列（Segmented Sequence）时显示。

它设置相邻分段之间跳过的间隔长度，用于在连续序列中形成断开的拖尾段。

### 多序列模式（Multiple Mode）

多序列模式（Multiple Mode）只在连接（Connections）为多序列（Multiple Sequence）时显示。

可选值：

- 交替（Alternating）：按轮替方式把粒子分配到多条序列。
- 连续（Sequential）：按连续块把粒子分配到多条序列。

交替（Alternating）会显示序列（Sequences）；连续（Sequential）会显示序列长度（Sequence Length）。

### 序列（Sequences）

序列（Sequences）只在连接（Connections）为多序列（Multiple Sequence），且多序列模式（Multiple Mode）为交替（Alternating）时显示。

它设置轮替生成的序列数量。数量越多，同一发射器源会被拆分为更多条拖尾序列。

### 序列长度（Sequence Length）

序列长度（Sequence Length）只在连接（Connections）为多序列（Multiple Sequence），且多序列模式（Multiple Mode）为连续（Sequential）时显示。

它设置每条连续序列使用的粒子数量。达到该长度后，后续粒子进入下一条序列。

### 最大连接数（Max Connections）

最大连接数（Max Connections）只在连接（Connections）为最近索引（Nearest Index）时显示。

它限制每个粒子可向外建立的连接数量。数值越高，按索引连接时每个粒子可连接的目标越多。

### 跳过粒子（Skip Particles）

跳过粒子（Skip Particles）只在连接（Connections）为最近索引（Nearest Index）时显示。

它用于跳过部分粒子的外向连接。数值为 0 时不额外跳过；提高数值会让连接更稀疏。

### 目标组（Destination Groups）

目标组（Destination Groups）只在连接（Connections）为最近索引（Nearest Index）、最近距离（Nearest Distance）或簇（Cluster）时显示。

它限制连接目标粒子所属的组。可选择使用全部组、仅同组、仅不同组、指定组或排除指定组。选择特定组（Specific Group）或除特定组外的全部（All Except Specific Group）时，会显示组（Group）。

### 组（Group）

组（Group）指定目标组（Destination Groups）使用的目标nx 组（nxGroup）。

它只在目标组（Destination Groups）为特定组（Specific Group）或除特定组外的全部（All Except Specific Group）时显示。该字段只能选择 nxGroup 对象。

### 最小距离（Min Distance）

最小距离（Min Distance）只在连接（Connections）为最近距离（Nearest Distance）时显示。

距离小于该值的粒子不会被连接。它和最大距离（Max Distance）一起定义按距离连接的有效窗口。

### 最大距离（Max Distance）

最大距离（Max Distance）只在连接（Connections）为最近距离（Nearest Distance）时显示。

距离大于该值的粒子不会被连接。最大距离（Max Distance）会按不小于最小距离（Min Distance）的方式传入计算。

### 最大数量（Max Number）

最大数量（Max Number）只在连接（Connections）为最近距离（Nearest Distance）时显示。

它限制每个粒子按距离可建立的连接数量。0 表示不通过这个字段设置上限；代码侧会把最大值限制在 64 以内。

### 群聚距离（Cluster Distance）

群聚距离（Cluster Distance）只在连接（Connections）为簇（Cluster）时显示。

粒子之间距离在这个范围内时会被归入相邻簇关系。该值越大，粒子更容易被归为同一簇。

### 簇中最小粒子数（Min Particles in Cluster）

簇中最小粒子数（Min Particles in Cluster）只在连接（Connections）为簇（Cluster）时显示。

它设置一个簇至少需要包含多少粒子才会输出连接。数值越高，小簇越容易被过滤。

### 冻结模式（Freeze Mode）

冻结模式（Freeze Mode）控制拖尾达到长度限制时如何处理。

可选值：

- 不冻结（Do Not Freeze）：粒子继续运动，拖尾按长度限制更新。
- 冻结粒子（Freeze Particle）：拖尾达到限制时冻结粒子运动。
- 冻结拖尾（Freeze Trail）：停止继续记录拖尾，但粒子继续移动。

选择非不冻结（Do Not Freeze）时，会显示冻结运动（Freeze Movement）和冻结缩放（Freeze Scale）。

### 冻结运动（Freeze Movement）

冻结运动（Freeze Movement）只在冻结模式（Freeze Mode）不是不冻结（Do Not Freeze）时显示。

开启后，冻结状态会影响粒子运动。它和冻结模式（Freeze Mode）一起决定拖尾到达限制后粒子是否继续移动。

### 冻结缩放（Freeze Scale）

冻结缩放（Freeze Scale）只在冻结模式（Freeze Mode）不是不冻结（Do Not Freeze）时显示。

开启后，冻结状态会影响粒子缩放。需要拖尾结束后保持粒子尺度状态时使用它。

### 无厚度/颜色数据（No Thickness/Color Data）

无厚度/颜色数据（No Thickness/Color Data）控制当前拖尾源是否省略厚度和颜色数据。

开启后，厚度模式（Thickness Mode）和拖尾颜色模式（Trail Color Mode）会灰显，颜色渐变和厚度曲线资源也不会同步到拖尾源。需要最轻量的线条数据时可以开启。

### 厚度模式（Thickness Mode）

厚度模式（Thickness Mode）选择拖尾厚度来源。

可选值：

- 不设置厚度（Do Not Set Thickness）：不创建厚度数据。
- 从值设置（Set From Value）：使用固定厚度值。
- 使用样条（Use Spline）：沿拖尾使用厚度曲线采样。
- 使用半径（当前）（Use Radius (Current)）：使用当前粒子半径。
- 使用半径（变量）（Use Radius (Variable)）：记录每个拖尾点的粒子半径。

无厚度/颜色数据（No Thickness/Color Data）开启时，该参数灰显。

### 厚度值（Thickness Value）

厚度值（Thickness Value）只在厚度模式（Thickness Mode）为从值设置（Set From Value）时显示。

它设置统一拖尾厚度。该值会用于线条（Lines）渲染参数，也会影响样条（Splines）生成曲线时的半径数据。

### 厚度变化量（Thickness Variation）

厚度变化量（Thickness Variation）只在厚度模式（Thickness Mode）为从值设置（Set From Value）时显示。

它为统一厚度增加随机变化，适合让同一发射器源中的拖尾粗细产生差异。

### 样条最大值（Spline Max）

样条最大值（Spline Max）只在厚度模式（Thickness Mode）为使用样条（Use Spline）时显示。

厚度曲线输出会按这个最大厚度值解释。需要整体放大或缩小曲线厚度时调整它。

### 样条时间（Spline Time）

样条时间（Spline Time）只在厚度模式（Thickness Mode）为使用样条（Use Spline）时显示。

它设置厚度曲线沿拖尾采样所对应的时间范围。拖尾长度和样条时间不同步时，厚度变化会按该时间范围重新解释。

### 拖尾颜色模式（Trail Color Mode）

拖尾颜色模式（Trail Color Mode）选择每个拖尾点的颜色来源。

可选值：

- 粒子颜色（Particle Color）：使用粒子当前颜色。
- 顶点颜色（Per-Vertex Color）：为每个拖尾顶点存储颜色。

无厚度/颜色数据（No Thickness/Color Data）开启时，该参数灰显。

### 样条类型（Spline Type）

样条类型（Spline Type）选择样条（Splines）显示模式下生成的曲线类型。

可选值：

- 线性（Linear）：生成精确折线。
- 贝塞尔（Bezier）：生成平滑贝塞尔曲线。
- B-Spline（B-Spline）：生成平滑样条曲线。

这个参数主要影响生成的曲线（Curves）子对象。线条（Lines）显示模式不会生成这些曲线对象。

### 闭合样条（Close Spline）

闭合样条（Close Spline）控制生成的样条是否闭合。

开启后，生成曲线会形成闭合路径。适合需要环形或封闭拖尾形状的连接算法。

### 中间点（Intermediate Points）

中间点（Intermediate Points）控制是否在生成曲线时插入额外点。

可选值：

- 无（None）：直接使用解析出的拖尾点。
- 均匀（Uniform）：每段插入固定数量的中间点。
- 自适应（Adaptive）：根据角度阈值在拐角附近插入中间点。

线性（Linear）样条会把自适应（Adaptive）当作无（None）处理。

### 数字（Number）

数字（Number）只在中间点（Intermediate Points）为均匀（Uniform）时显示。

它设置每段插入的中间点数量。数值越高，生成曲线点越多。

### 角度（Angle）

角度（Angle）只在中间点（Intermediate Points）为自适应（Adaptive）时显示。

它设置自适应插点的角度阈值。拐角变化达到阈值时，会插入中间点以改善曲线形状。

### 使用最大长度（Use Max Length）

使用最大长度（Use Max Length）控制是否限制生成样条的最大长度。

开启后，会显示最大长度（Max Length）。这个限制作用在生成曲线阶段，用于避免输出过长的曲线段。

### 最大长度（Max Length）

最大长度（Max Length）只在使用最大长度（Use Max Length）开启时显示。

它设置生成样条允许的最大长度。超过该长度的生成结果会按限制处理。

### 添加项（Add Item）

添加项（Add Item）是通用列表添加操作。拖尾发射器列表主要通过添加发射器（Add Emitter）拖放或选择发射器对象加入列表。

如果界面中出现通用加号按钮，它会在当前列表新增条目。这个操作只管理列表引用，不创建新的发射器对象。

### 移除项（Remove Item）

移除项（Remove Item）从当前列表移除选中的条目。

在拖尾发射器列表中，它会移除当前拖尾源，并清理该源关联的颜色渐变和厚度曲线资源。它不会删除场景中的发射器对象本体。

### 上移项（Move Item Up）

上移项（Move Item Up）把当前选中的发射器源在列表中上移一位。

列表顺序用于组织多个拖尾源。需要把常用源放在前面时，可以使用这个按钮。

### 下移项（Move Item Down）

下移项（Move Item Down）把当前选中的发射器源在列表中下移一位。

它只改变列表顺序，不改变发射器对象自身。

### 切换启用（Toggle Enabled）

切换启用（Toggle Enabled）切换当前列表条目的启用状态。

关闭某个发射器源后，该源不会参与拖尾输出，但保留在列表中，便于之后重新启用。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于连续从场景中拾取多个发射器并加入拖尾发射器列表。

它按列表允许的对象类型工作；拖尾发射器列表只接受 nxEmitter。

### 组（Groups Affected）

组（Groups Affected）是粒子组列表，用于限定哪些粒子组受当前拖尾修改器（nxTrail）影响。

空列表表示不按组过滤。添加组对象后，当前修改器只影响匹配这些组的粒子。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）是组（Groups Affected）列表中当前选中条目的索引。

它用于决定正在编辑哪一个组条目。通常通过点击列表条目选择。

### 添加组（Add Group）

添加组（Add Group）向组（Groups Affected）列表添加新的组条目。

添加后，需要把目标nx 组（nxGroup）指定到组对象（Group Object）字段中。

### 组对象（Group Object）

组对象（Group Object）指定组列表条目的目标nx 组（nxGroup）。

它决定该条目引用哪个粒子组。留空条目不会提供有效组目标。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动拖尾修改器（nxTrail）的参数。

具体驱动关系在映射层（Mapping Layers）里逐条设置。使用映射前，需要确认目标参数在当前显示模式和源条目模式下可用。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射规则列表，每一层定义一条输入到输出的驱动关系。

多条映射层同时存在时，需要检查每条的目标参数、粒子数据来源、输入范围和权重。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）是映射层（Mapping Layers）列表中当前选中条目的索引。

它决定下方显示和编辑哪一条映射规则。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）选择要被粒子数据驱动的拖尾参数。

选择目标参数后，映射层会把粒子数据（Particle Data）读取到的输入值转换为该参数的驱动值。

### 粒子数据（Particle Data）

粒子数据（Particle Data）选择用于驱动目标参数的输入属性。

选择时应确认该数据在当前粒子来源中存在，并且数值范围适合范围最小值（Range Min）/ 范围最大值（Range Max）。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于组织和筛选不同映射层。

它帮助管理多条映射规则。只有指定图层参与当前映射时，对应规则才会影响目标参数。

### 范围最小值（Range Min）

范围最小值（Range Min）设置映射输入范围的下限。

粒子数据低于这个下限时，映射会按下限端理解输入。

### 范围最大值（Range Max）

范围最大值（Range Max）设置映射输入范围的上限。

粒子数据高于这个上限时，映射会按上限端理解输入。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的驱动强度。

权重越高，该映射层对目标参数的影响越强。

### 钳制（Clamp）

钳制（Clamp）控制映射输出是否限制在目标参数的有效范围内。

开启后，映射结果不会超过目标参数允许的最小值和最大值。

### 衰减（Falloff）

衰减（Falloff）用于在空间范围内减弱拖尾修改器（nxTrail）对粒子的影响。

衰减对象（Falloff Objects）列表定义用于计算空间衰减的物体。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减对象列表，每个条目指定一个影响范围对象。

列表中可以添加多个衰减对象，并通过衰减混合（Falloff Blend）和衰减混合强度（Falloff Blend Strength）控制组合方式。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）是衰减对象（Falloff Objects）列表中当前选中条目的索引。

它用于决定正在编辑哪一个衰减条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）向衰减对象（Falloff Objects）列表添加新的衰减条目。

添加后，需要在衰减对象（Falloff Object）字段里指定目标对象。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）指定衰减列表条目的目标对象。

目标对象决定该条目用于计算衰减的空间位置和范围。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）控制多个衰减对象之间的混合模式。

当多个衰减对象同时存在时，它决定这些空间影响如何组合。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制衰减混合的整体强度。

提高强度会增强衰减对象对修改器影响范围的控制。
