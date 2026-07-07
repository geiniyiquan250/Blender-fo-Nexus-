# NeXus 湍流修改器使用说明

这份文档只说明湍流修改器（nxTurbulence）。它的重点是说明湍流层（Turbulence Layers）怎样叠加、每种噪波类型适合什么效果、哪些参数只在特定噪波类型下生效。

## 湍流修改器（nxTurbulence）

湍流修改器（nxTurbulence）用于给已有粒子添加基于噪波的运动变化，让粒子方向或加速度产生不规则变化。它不产生粒子，通常需要和发射器（nxEmitter）或其他粒子来源一起使用。

湍流修改器（nxTurbulence）的核心是湍流层（Turbulence Layers）。每一层都是一套独立噪波，可以选择噪波类型（Noise Type）、强度、缩放、频率、叠代层数等参数，再通过图层混合（Layer Blend）和图层混合强度（Layer Blend Strength）与前面的层叠加。

常见使用流程：

- 创建能产生粒子的发射器（nxEmitter）或确认场景里已有粒子来源。
- 创建湍流修改器（nxTurbulence）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认列表里包含湍流修改器（nxTurbulence）。
- 在湍流层（Turbulence Layers）里添加或选择一个层。
- 选择噪波类型（Noise Type），例如Voronoise（Voronoise）、卷曲（Curl）或fBm（fBm）。
- 设置作用模式（Direction Mode），决定湍流是改粒子方向还是改粒子加速度。
- 调整湍流强度（Turbulence Strength）、缩放（Scale）、频率（Frequency）和倍频层数（Octaves），控制运动幅度和细节。

默认新建时会创建一个Voronoise（Voronoise）层。它适合快速产生有块状变化和不规则区域感的扰动。

### 启用（Enabled）

启用（Enabled）控制整个湍流修改器（nxTurbulence）是否参与粒子流程。

关闭后，湍流修改器（nxTurbulence）不会继续给粒子添加噪波运动。它适合用来对比效果：关闭后如果粒子运动变得稳定，说明当前不规则运动主要来自这个湍流修改器。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制湍流修改器（nxTurbulence）的编辑器辅助显示是否可见。

它只影响编辑器里的辅助显示，不直接改变湍流计算结果。

### 湍流层（Turbulence Layers）

湍流层（Turbulence Layers）是湍流修改器（nxTurbulence）的主列表。列表里的每一项都是一个独立湍流层。

多层湍流会按列表顺序同步到运行流程。上面的层通常先参与，下面的层再通过图层混合（Layer Blend）叠加到已有结果上。也就是说，层的顺序会影响最终运动。

常见用法：

- 一层大尺度低频湍流负责整体飘动。
- 一层小尺度高频湍流负责细节抖动。
- 一层卷曲（Curl）负责旋涡感。

如果湍流完全没有效果，先检查湍流层（Turbulence Layers）里是否至少有一个启用的层，再检查该层的湍流强度（Turbulence Strength）是否大于 0。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）记录当前正在编辑湍流层（Turbulence Layers）列表里的哪一项。

普通用户通常不需要直接修改它。你在列表中选中哪一层，右侧或下方显示的参数就对应哪一层。

### 层名称（Layer Name）

层名称（Layer Name）用于标识当前湍流层。

新增层时，插件会根据噪波类型（Noise Type）自动给出名称。手动改名后，它只影响界面识别，不直接改变湍流计算。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制当前这个湍流层是否参与计算。

关闭某一层后，只会停用这一层，不会关闭整个湍流修改器（nxTurbulence）。如果你想比较不同噪波层的贡献，建议逐个关闭层启用（Layer Enabled）来观察。

### 噪波类型（Noise Type）

噪波类型（Noise Type）决定当前层使用哪种噪波算法。

插件提供这些类型：

- 单纯形（Simplex）：适合平滑、均匀的基础噪波扰动。
- 卷曲（Curl）：适合旋涡、卷动、绕流感。选择它时会额外显示卷曲混合（Curl Blend）和卷曲添加（Curl Add）。
- 湍流（Turbulence）：适合更传统的湍流扰动。
- 波浪湍流（Wavy Turbulence）：适合带波浪节奏的扰动。
- Voronoise（Voronoise）：适合块状、细胞状、不规则区域变化。默认层使用这个类型。
- fBm（fBm）：适合多层叠加的自然噪波细节。
- 立方（Cubic）：适合较硬、更规整的噪波变化。

噪波类型（Noise Type）会影响同一组参数的实际观感。例如相同的缩放（Scale）和频率（Frequency），在卷曲（Curl）和Voronoise（Voronoise）里表现会明显不同。

### 图层混合（Layer Blend）

图层混合（Layer Blend）决定当前层如何与前面已经计算出的湍流结果合成。

常见模式可以这样理解：

- 法线方向（Normal）：当前层按正常方式覆盖或加入流程，最常用。
- 最小（Min）：更偏向保留较小影响。
- 减去（Subtract）：从已有结果中减去当前层影响。
- 相乘（Multiply）：把当前层和已有结果相乘，容易让效果更强或更暗。
- 叠加（Overlay）：用叠加方式混合，适合增强层次。
- 最大（Max）：更偏向保留较大影响。
- 添加（Add）：把当前层加到已有结果上，容易增强整体扰动。
- 屏幕（Screen）：以类似滤色方式混合。
- 差值（Difference）：保留差异部分，适合制造更不规则的变化。

如果你只用一个湍流层，通常保持法线方向（Normal）即可。多层叠加时，再根据需要调整图层混合（Layer Blend）。

### 图层混合强度（Layer Blend Strength）

图层混合强度（Layer Blend Strength）控制当前层混入最终湍流结果的比例。

值越高，这一层对最终运动的影响越明显；值越低，这一层越弱。它和湍流强度（Turbulence Strength）不同：湍流强度（Turbulence Strength）控制这一层本身产生多强的扰动，图层混合强度（Layer Blend Strength）控制这一层混到总结果里有多少。

### 作用模式（Direction Mode）

作用模式（Direction Mode）决定湍流怎样影响粒子。

插件提供两种模式：

- 方向（Direction）：更偏向改变粒子的运动方向。
- 加速度（Acceleration）：更偏向给粒子添加加速度，让粒子持续被噪波力推动。

如果你想让粒子轨迹被扰乱但整体速度不被明显拉大，可以先尝试方向（Direction）。如果你想让粒子像被力场推动一样持续变化，可以使用加速度（Acceleration）。

默认方向模式是加速度（Acceleration）。

### 种子（Seed）

种子（Seed）控制当前湍流层的随机噪波序列。

同样的参数下，换一个种子（Seed）会得到不同的噪波分布。它适合用来“换一版随机形态”，而不是用来增加强度。

### 湍流强度（Turbulence Strength）

湍流强度（Turbulence Strength）控制当前层产生多强的运动扰动。

值越高，粒子受到的湍流影响越明显；值越低，效果越弱。它是判断“湍流有没有力”的主要参数之一。

如果粒子运动太乱，先降低湍流强度（Turbulence Strength）。如果几乎看不到变化，先提高湍流强度（Turbulence Strength），再检查缩放（Scale）和频率（Frequency）。

### 噪波偏移（Noise Offset）

噪波偏移（Noise Offset）用于移动当前噪波场在 X、Y、Z 方向上的采样位置。

它不会改变粒子本身的位置，而是改变粒子读取噪波的位置。可以理解为把噪波图案整体平移。调整噪波偏移（Noise Offset）可以让同一套噪波产生不同空间分布。

### 缩放（Scale）

缩放（Scale）控制当前层整体噪波尺度。

数值越大，噪波变化通常会被拉到更大的空间范围里；数值越小，变化更密集。它会被同步时按百分比换算，所以界面上的 100 通常可以理解为基础比例。

如果粒子变化太碎，可以增大缩放（Scale）。如果变化太大块、缺少细节，可以减小缩放（Scale）或提高频率（Frequency）。

### 轴方向缩放（Axis Direction Scale）

轴方向缩放（Axis Direction Scale）用于分别控制 X、Y、Z 三个方向上的噪波比例。

它适合做方向性湍流。例如只想让噪波在水平面变化明显、垂直方向变化较少，可以降低某个轴向的比例。

这个参数用于改变噪波在各轴上的采样比例，不控制最终力的方向。

### 持续度（Persistence）

持续度（Persistence）控制多层噪波叠代时，每一层细节的强度衰减。

值越高，后续细节层保留得越明显，湍流会更丰富、更粗糙。值越低，高频细节会更快减弱，效果更平滑。

它通常要和倍频层数（Octaves）一起看。倍频层数（Octaves）越高，持续度（Persistence）的影响越明显。

### 间隙度（Lacunarity）

间隙度（Lacunarity）控制多层噪波叠代时，频率如何逐层增加。

值越高，不同叠代层之间的频率差异越大，细节跨度会更明显。值越低，不同层之间更接近。

需要注意：当噪波类型（Noise Type）是单纯形（Simplex）时，界面会禁用间隙度（Lacunarity）。也就是说，在单纯形（Simplex）层里调这个参数没有实际意义。

### 频率（Frequency）

频率（Frequency）控制噪波变化的基础频率。

频率越高，空间里的变化越密；频率越低，变化越宽。它和缩放（Scale）都影响噪波尺度，但缩放（Scale）更像整体尺寸，频率（Frequency）更像基础重复密度。

### 倍频层数（Octaves）

倍频层数（Octaves）控制噪波叠加多少层细节。

值越高，细节越丰富，但计算也可能更重。值太低时，湍流会更简单、更平滑。想要自然随机感，通常需要配合持续度（Persistence）、间隙度（Lacunarity）和频率（Frequency）一起调。

### 卷曲混合（Curl Blend）

卷曲混合（Curl Blend）只在噪波类型（Noise Type）为卷曲（Curl）时显示并有意义。

它控制卷曲噪波内部的混合比例。值越高，卷曲特征通常越明显；值越低，卷曲感会减弱。

如果当前层不是卷曲（Curl），这个参数不会出现在该层设置里。

### 卷曲添加（Curl Add）

卷曲添加（Curl Add）只在噪波类型（Noise Type）为卷曲（Curl）时显示并有意义。

它控制卷曲噪波额外添加量。提高它可以增强卷动和绕流感，但过高时粒子运动可能变得很乱。

如果你想做烟雾、能量流、旋涡或绕障碍物感，通常可以从卷曲（Curl）开始，再调卷曲混合（Curl Blend）和卷曲添加（Curl Add）。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是湍流修改器（nxTurbulence）的主设置页。这里主要编辑湍流层（Turbulence Layers）以及每个层自己的噪波参数。

如果你要调整湍流本身，通常先回到物体属性（Object Properties）页。组（Groups Affected）、映射（Mapping）和衰减（Falloff）分别用于限制作用对象、用粒子数据驱动参数、按空间范围控制影响。

### 设置页（Section）

设置页（Section）是湍流修改器（nxTurbulence）面板顶部的页签切换。它不直接改变湍流结果，而是切换当前正在编辑哪一类设置。

湍流修改器（nxTurbulence）常见页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 组（Groups Affected）

组（Groups Affected）用于限制湍流修改器（nxTurbulence）影响哪些 nx 组（nxGroup）。

如果这里不添加任何组，通常表示不额外按组过滤。添加组后，湍流只会按组过滤后的粒子范围工作。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要直接修改它。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。普通网格、发射器或其他修改器对象不会作为有效组过滤使用。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动湍流参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

对湍流修改器（nxTurbulence）来说，映射图层（Mapping Layer）很重要：因为湍流是分层修改器，映射需要知道要控制哪一个湍流层。树索引 0 表示第一层。

如果映射没有效果，先检查映射目标参数（Mapping Parameter）是否选择正确，再检查映射图层（Mapping Layer）是否指向了正确的湍流层。

一条映射层通常要同时确认这些内容：

- 粒子数据（Particle Data）：选择用哪种粒子属性作为输入。
- 映射目标参数（Mapping Parameter）：选择要驱动哪个湍流参数。
- 映射图层（Mapping Layer）：选择要控制第几个湍流层。
- 范围最小值（Range Min）和范围最大值（Range Max）：定义输入数据的有效范围。
- 映射权重（Mapping Weight）：控制这条映射混入目标参数的强度。
- 钳制（Clamp）：控制输入超出范围后怎么处理。

例如，你可以用速度（Speed）驱动第一层湍流强度（Turbulence Strength），让高速粒子受到更强湍流；也可以用年龄（Age）驱动第二层缩放（Scale），让粒子越老，噪波尺度越大。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个湍流参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会真正参与映射。

湍流修改器（nxTurbulence）允许同时添加多条映射层。多条映射可以控制同一个湍流层的不同参数，也可以分别控制不同湍流层。

常见搭配：

- 年龄（Age）控制湍流强度（Turbulence Strength）：让粒子出生后逐渐被湍流影响。
- 速度（Speed）控制频率（Frequency）：让快粒子产生更细碎的扰动。
- 半径（Radius）或质量（Mass）控制图层混合强度（Layer Blend Strength）：让不同大小或质量的粒子受到不同程度的湍流。
- 组（Group）控制强度或缩放：让不同粒子组得到不同湍流效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制湍流修改器（nxTurbulence）的哪个参数。

可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。如果目标参数没有选择，映射层不会产生实际效果。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

当前映射菜单提供这些基础输入源：

- 年龄（Age）：粒子出生后经过的时间。适合做“越老越强”或“出生后逐渐消失”的湍流变化。
- 颜色明度（Color Brightness）：使用粒子颜色整体亮度作为输入。适合让亮粒子和暗粒子受到不同湍流。
- 颜色 R（Color R）：使用粒子颜色的红色通道作为输入。适合把颜色通道当作控制遮罩。
- 颜色 G（Color G）：使用粒子颜色的绿色通道作为输入。
- 颜色 B（Color B）：使用粒子颜色的蓝色通道作为输入。
- 距离（Distance）：使用粒子记录的距离数据作为输入。适合按移动距离或相关距离数据逐渐改变湍流。
- 文档时间（Document Time）：使用当前场景时间作为输入。适合让湍流参数随时间统一变化，不依赖单个粒子状态。
- 流体密度（Fluid Density）：使用流体密度数据作为输入。只有粒子流程里存在相关流体数据时才有实际意义。
- 燃料（Fuel）：使用燃料通道作为输入。主要服务于带燃料数据的流体、烟火或 ExplosiaFX 相关流程。
- 颗粒（Granular）：使用颗粒相关数据作为输入。只有粒子流程产生或传递颗粒数据时才有意义。
- 组（Group）：使用粒子所属组作为输入。适合让不同 nx 组（nxGroup）的粒子得到不同湍流强度或频率。
- ID（ID）：使用粒子唯一编号作为输入。适合制造稳定的逐粒子差异，常用于让每个粒子有固定但不同的湍流偏差。
- 生命（Life）：使用粒子生命周期长度或生命周期相关数据作为输入。适合让短寿命和长寿命粒子表现不同。
- 质量（Mass）：使用粒子质量作为输入。适合让轻粒子更容易被湍流扰动，重粒子更稳定。
- 半径（Radius）：使用粒子半径作为输入。适合让大粒子和小粒子受到不同湍流。
- 缩放（Scale）：使用粒子缩放数据作为输入。适合接在缩放修改器（nxScale）或带缩放数据的流程之后。
- 烟雾（Smoke）：使用烟雾通道作为输入。主要服务于带烟雾数据的流体、烟火或 ExplosiaFX 相关流程。
- 速度（Speed）：使用粒子速度大小作为输入。适合让快粒子产生更强或更细碎的湍流。
- 温度（Temperature）：使用温度通道作为输入。主要服务于带温度数据的流体、烟火或 ExplosiaFX 相关流程。
- 顶点权重（Vertex Weight）：使用顶点权重数据作为输入。只有粒子或来源流程提供顶点权重时才有实际意义。

选择粒子数据（Particle Data）后，要配合范围最小值（Range Min）和范围最大值（Range Max）设定输入区间。例如用速度（Speed）驱动湍流强度时，范围可以设置成低速到高速的速度区间；用文档时间（Document Time）时，范围通常对应时间或帧段。

有些输入源依赖前置数据。流体密度（Fluid Density）、烟雾（Smoke）、燃料（Fuel）和温度（Temperature）通常需要流体或 ExplosiaFX 相关流程提供数据；顶点权重（Vertex Weight）需要来源或粒子流程传递顶点权重；组（Group）需要粒子已经被分配到 nx 组（nxGroup）。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于指定映射作用到湍流层（Turbulence Layers）里的哪一个运行层。

湍流修改器（nxTurbulence）是分层修改器，所以这个字段有实际意义。树索引 0 表示第一个湍流层，1 表示第二个湍流层，以此类推。

如果你想用粒子年龄只控制第二个湍流层的湍流强度（Turbulence Strength），映射图层（Mapping Layer）就应该指向第二层对应的索引。

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

衰减（Falloff）用于用空间衰减对象控制湍流修改器（nxTurbulence）的影响范围。

如果你想控制“哪里有湍流”，用衰减（Falloff）；如果想控制“哪些组受湍流影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前湍流修改器（nxTurbulence）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

---

## 列表操作按钮

这些小按钮通常出现在湍流层列表、组列表、映射列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择类型或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表支持的可添加类型。对于湍流层（Turbulence Layers），它用于选择要添加哪一种噪波层。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。例如创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff）。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

如果列表只接受特定类型，例如 nx 组（nxGroup）或nx 衰减（nxFalloff），不符合类型的对象不会被加入。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。它通常只移除列表引用，不等于删除场景里的对象本体。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

对于湍流层（Turbulence Layers），顺序会影响多层混合结果，所以移动顺序可能改变最终湍流效果。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）用于快速打开或关闭当前列表项。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于树状列表里的层级调整。普通湍流层列表通常不需要使用它。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于树状列表里的层级调整。普通湍流层列表通常不需要使用它。
