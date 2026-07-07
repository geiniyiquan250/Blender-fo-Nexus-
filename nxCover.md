# NeXus 覆盖修改器使用说明

这份文档只说明覆盖修改器（nxCover）。重点说明目标对象怎样分配给粒子，粒子怎样移动到对象表面、顶点、边、体积或射线交点，以及到达后怎样保持、释放、对齐和变色。

## 覆盖修改器（nxCover）

覆盖修改器（nxCover）用于让已有粒子覆盖指定对象。它通过对象（Objects）列表接收网格（Mesh）或曲线（Curve）对象，并为每个对象设置覆盖方式、移动方式、保持方式、制动、法线对齐和颜色变化。

覆盖修改器（nxCover）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建覆盖修改器（nxCover）。如果场景使用发射器（nxEmitter）的修改器（Modifiers）列表组织后续修改器，需要确认覆盖修改器（nxCover）已包含在该列表里。

常见使用流程：

- 创建发射器（nxEmitter），让场景里先有粒子来源。
- 创建覆盖修改器（nxCover）。
- 在对象（Objects）列表里添加一个网格或曲线对象。
- 用对象模式（Object Mode）决定多个目标对象怎样分配给粒子。
- 在列表项里设置操作（Operation）、强度（Strength）、容差（Tolerance）、运动（Movement）和保持（Holding）。

### 启用（Enabled）

启用（Enabled）控制整个覆盖修改器（nxCover）是否参与粒子流程。

关闭后，覆盖修改器（nxCover）不会继续把粒子引导到目标对象上。调试多个运动修改器时，可以临时关闭它，判断当前粒子覆盖行为是否来自覆盖修改器（nxCover）。

### 对象模式（Object Mode）

对象模式（Object Mode）决定对象（Objects）列表里有多个目标对象时，每个粒子使用哪个目标。

插件提供这些模式：

- 序列（Sequence）：按顺序把目标对象分配给粒子。
- 最近对象（Nearest Object）：粒子使用距离自己最近的对象。
- 最远对象（Furthest Object）：粒子使用距离自己最远的对象。
- 对象索引（Object Index）：使用指定索引的对象。选择这个模式时，界面会显示对象索引（Object Index）。
- 随机对象（Random Object）：随机选择目标对象。选择这个模式时，界面会显示随机种子（Random Seed）。

当模式为序列（Sequence）或随机对象（Random Object）时，界面会显示循环（Cycle）。

### 对象索引（Object Index）

对象索引（Object Index）只在对象模式（Object Mode）为对象索引（Object Index）时显示。

它指定对象（Objects）列表里的目标对象序号。列表顺序改变后，同一个索引指向的对象也会改变。

### 随机种子（Random Seed）

随机种子（Random Seed）只在对象模式（Object Mode）为随机对象（Random Object）时显示。

它用于改变随机对象分配结果。粒子分配目标正确但随机分布不满意时，可以调整这个值。

### 循环（Cycle）

循环（Cycle）只在对象模式（Object Mode）为序列（Sequence）或随机对象（Random Object）时显示。

它用于控制对象分配在目标被覆盖后是否继续循环使用。具体效果取决于当前对象列表和粒子数量。

### 对象（Objects）

对象（Objects）列表用于添加需要被粒子覆盖的目标对象。

这个列表接受网格（Mesh）和曲线（Curve）对象。每个列表项都有独立的操作（Operation）、运动（Movement）、保持（Holding）、制动（Braking）和对齐/颜色（Alignment / Color）设置。

如果对象（Objects）列表为空，覆盖修改器（nxCover）没有可用的覆盖目标。

### 活动索引（Active Index）

活动索引（Active Index）记录当前正在编辑对象（Objects）列表里的哪一项。

普通用户通常不需要直接修改它。你在对象（Objects）列表中选中哪一项，活动索引（Active Index）就对应哪一项。

### 添加对象（Add Object）

添加对象（Add Object）用于把一个场景对象加入对象（Objects）列表。

它接受网格（Mesh）和曲线（Curve）对象。添加后，需要继续设置该列表项的覆盖方式和运动参数。

### 添加集合（Add Collection）

添加集合（Add Collection）用于把一个集合里的对象批量加入对象（Objects）列表。

只有集合里的网格（Mesh）和曲线（Curve）对象会作为有效覆盖对象。这个入口适合一次添加多个目标模型或目标曲线。

### 覆盖对象（Cover Object）

覆盖对象（Cover Object）是列表项里真正被粒子覆盖的目标对象。

它可以是网格（Mesh）或曲线（Curve）。网格对象可以用于表面、顶点、边、体积和射线交点等覆盖方式；曲线对象也可以作为覆盖目标参与同步。

### 覆盖项启用（Cover Object Enabled）

覆盖项启用（Cover Object Enabled）控制当前列表项是否参与覆盖。

关闭某一项后，该对象不会作为覆盖目标使用。它适合临时比较不同目标对象对粒子覆盖结果的影响。

### 操作（Operation）

操作（Operation）决定粒子覆盖目标对象时使用哪类目标位置。

插件提供这些模式：

- 多边形面积（Polygon Area）：按多边形面积权重放置粒子。
- 多边形中心（Polygon Center）：把粒子放到多边形中心。
- 点（Points）：把粒子放到网格顶点。
- 边（Edges）：把粒子放到网格边上。
- 体积（Volume）：把粒子放到网格体积内。
- 射线相交（Ray Intersection）：把粒子放到射线与网格相交的位置。

当操作（Operation）为纹理相关模式时，界面会显示纹理分辨率、纹理容差、纹理阈值、纹理模式和最大尝试次数。当前菜单构建代码里保留了纹理参数，但可见枚举项以运行时菜单为准。

### 纹理分辨率（Texture Resolution）

纹理分辨率（Texture Resolution）用于设置纹理采样分辨率。

它只在操作（Operation）为纹理模式时显示。分辨率越高，纹理筛选越细，但计算量也可能更高。

### 纹理容差（Texture Tolerance）

纹理容差（Texture Tolerance）用于设置纹理阈值比较的容差。

它只在操作（Operation）为纹理模式时显示。数值越高，符合条件的纹理区域越宽松。

### 纹理阈值（Texture Threshold）

纹理阈值（Texture Threshold）用于设置纹理比较的颜色阈值。

它只在操作（Operation）为纹理模式时显示。插件会结合纹理模式（Texture Mode）判断哪些位置符合覆盖条件。

### 纹理模式（Texture Mode）

纹理模式（Texture Mode）决定纹理值怎样和纹理阈值（Texture Threshold）比较。

插件提供更高（Higher）和下限（Lower）两种比较方向。

### 最大尝试次数（Max Attempts）

最大尝试次数（Max Attempts）控制插件寻找有效纹理位置时最多尝试多少次。

它只在操作（Operation）为纹理模式时显示。数值越高，寻找有效位置的机会越多，但计算量也可能更高。

### 强度（Strength）

强度（Strength）控制当前列表项覆盖效果的总体强度。

数值越高，粒子越明显地受覆盖目标影响；数值越低，覆盖影响越弱。它按百分比同步。

### 容差（Tolerance）

容差（Tolerance）定义粒子距离目标多近时可以视为已经覆盖。

数值越小，粒子需要更接近目标位置；数值越大，到达判定更宽松。它使用场景长度单位，并会按插件单位缩放同步。

### 继承父级（Inherit Parent）

继承父级（Inherit Parent）让当前列表项继承列表中第一个对象的设置。

开启后，当前项后面的对齐/颜色、运动、保持和制动设置不会继续显示。适合多个对象使用同一套覆盖参数时减少重复设置。

### 对齐/颜色（Alignment / Color）

对齐/颜色（Alignment / Color）是列表项里的折叠设置区，用于控制粒子到达目标后的旋转跟随、法线对齐和颜色变化。

关闭折叠只影响面板显示，不改变已经设置的参数。

### 随对象旋转（Rotate With Object）

跟随对象旋转（Rotate With Object）控制粒子是否随目标对象旋转。

当法线对齐（Align to Normals）开启时，这个选项在界面中会被禁用。两者用于不同的朝向控制方式。

### 法线对齐（Align to Normals）

法线对齐（Align to Normals）控制粒子是否对齐到目标表面法线。

当跟随对象旋转（Rotate With Object）开启时，这个选项在界面中会被禁用。需要粒子朝向贴合目标表面时，使用法线对齐（Align to Normals）。

### 对齐强度（Alignment Strength）

对齐强度（Alignment Strength）控制法线对齐（Align to Normals）的强度。

它只在法线对齐（Align to Normals）开启时可调。数值越高，粒子朝向越明显地靠近目标法线方向。

### 改变颜色（Change Color）

改变颜色（Change Color）控制粒子覆盖目标时是否改变颜色。

开启后，可以设置覆盖颜色（Cover Color）和颜色时序（Color Timing）。如果操作（Operation）为纹理模式，还可以使用设置为纹理（Set to Texture）。

### 设置为纹理（Set to Texture）

设置为纹理（Set to Texture）只在操作（Operation）为纹理模式且改变颜色（Change Color）开启时显示。

开启后，粒子颜色使用纹理颜色。关闭后，粒子使用覆盖颜色（Cover Color）。

### 覆盖颜色（Cover Color）

覆盖颜色（Cover Color）设置粒子覆盖目标时使用的颜色。

当改变颜色（Change Color）开启，并且没有使用设置为纹理（Set to Texture）时，这个颜色才会作为覆盖颜色使用。

### 颜色时序（Color Timing）

颜色时序（Color Timing）控制覆盖颜色变化的时间倍率。

它只在改变颜色（Change Color）开启时生效。数值越高，颜色变化越按较大的时间倍率同步。

### 改变释放颜色（Change Release Color）

改变释放颜色（Change Release Color）控制粒子从目标释放时是否改变颜色。

开启后，可以设置释放颜色（Release Color）。

### 释放颜色（Release Color）

释放颜色（Release Color）设置粒子释放时使用的颜色。

它只在改变释放颜色（Change Release Color）开启时生效。

### 运动（Movement）

运动（Movement）是列表项里的折叠设置区，用于控制粒子怎样移动到覆盖目标。

当操作（Operation）为纹理模式时，运动设置区在界面中会被禁用。

### 速度模式（Speed Mode）

速度模式（Speed Mode）决定粒子移动到目标时使用粒子速度还是指定时间。

插件提供两种模式：

- 使用速度（Use Speed）：根据粒子速度移动到目标。
- 到达目标时间（Time to Target）：使用指定时间到达目标。

### 粒子速度模式（Particle Speed Mode）

粒子速度模式（Particle Speed Mode）只在速度模式（Speed Mode）为使用速度（Use Speed）时可调。

插件提供三种模式：

- 粒子（Particle）：使用粒子自身速度。
- 固定（Fixed）：使用固定速度（Fixed Speed）。
- 力（Force）：以力的方式朝目标推动。

### 固定速度（Fixed Speed）

固定速度（Fixed Speed）只在速度模式（Speed Mode）为使用速度（Use Speed），且粒子速度模式（Particle Speed Mode）为固定（Fixed）时可调。

它设置粒子移向目标时使用的固定速度。

### 覆盖时间（Time to Cover）

覆盖时间（Time to Cover）只在速度模式（Speed Mode）为到达目标时间（Time to Target）时可调。

它设置粒子到达覆盖目标所需的时间。

### 时间变化量（Time Variation）

时间变化量（Time Variation）只在速度模式（Speed Mode）为到达目标时间（Time to Target）时可调。

它给覆盖时间（Time to Cover）增加随机变化，让粒子不是在完全相同的时间到达目标。

### 释放时间（Release Time）

释放时间（Release Time）设置粒子到达目标后经过多久释放。

它位于运动（Movement）设置区中。数值越大，粒子保持覆盖状态的时间越长。

### 释放变化量（Release Variation）

释放变化量（Release Variation）给释放时间（Release Time）增加随机变化。

用它可以避免所有粒子在同一时刻释放。

### 保持（Holding）

保持（Holding）是列表项里的折叠设置区，用于控制粒子到达覆盖目标后怎样停留或继续受力。

当操作（Operation）为纹理模式时，保持设置区在界面中会被禁用。

### 保持模式（Holding Mode）

保持模式（Holding Mode）决定粒子到达目标后怎样保持。

插件提供这些模式：

- 吸引（Attract）：持续吸引粒子到目标位置。
- 自由（Free）：粒子到达后恢复自由。
- 弹簧（Spring）：用弹簧力保持粒子。
- 粘附（Stick）：让粒子粘在目标位置。

### 模式（Mode）

吸引模式（Mode）只在保持模式（Holding Mode）为吸引（Attract）时可调。

它决定保持阶段使用速度（Velocity）还是加速度（Acceleration）方式影响粒子。

### 到达模式（Arrive Mode）

到达模式（Arrive Mode）只在保持模式（Holding Mode）为吸引（Attract）时可调。

插件提供减速（Slowdown）和吸引（Attract）两种到达方式。减速（Slowdown）会配合距离（Distance）控制靠近目标时的速度处理。

### 距离（Distance）

距离（Distance）只在保持模式（Holding Mode）为吸引（Attract），且到达模式（Arrive Mode）为减速（Slowdown）时可调。

它控制粒子距离目标多近时开始进入减速处理。

### 最小速度（Min Speed）

最小速度（Min Speed）在保持模式（Holding Mode）为吸引（Attract）时可调。

它限制粒子靠近目标或保持时使用的最低速度。

### 最大速度（Max Speed）

最大速度（Max Speed）在保持模式（Holding Mode）为吸引（Attract）时可调。

它限制粒子靠近目标或保持时使用的最高速度。

### 弹簧长度（Spring Length）

弹簧长度（Spring Length）只在保持模式（Holding Mode）为弹簧（Spring）时可调。

它设置弹簧保持的静止长度。

### 刚度（Stiffness）

刚度（Stiffness）只在保持模式（Holding Mode）为弹簧（Spring）时可调。

数值越高，弹簧约束越强。

### 阻尼（Damping）

阻尼（Damping）只在保持模式（Holding Mode）为弹簧（Spring）时可调。

它按百分比设置弹簧运动中的阻尼强度。

### 制动（Braking）

制动（Braking）是列表项里的折叠设置区，用于控制粒子接近目标时是否减速。

它只在速度模式（Speed Mode）为使用速度（Use Speed），且操作（Operation）不是纹理模式时可用。

### 使用制动（Use Braking）

使用制动（Use Braking）控制粒子接近目标时是否应用制动。

开启后，制动距离（Braking Distance）、制动最小速度（Braking Min Speed）、制动最大速度（Braking Max Speed）和制动曲线会参与控制。

### 制动距离（Braking Distance）

制动距离（Braking Distance）只在使用制动（Use Braking）开启时可调。

它设置粒子距离目标多近时开始制动。

### 制动最小速度（Braking Min Speed）

制动最小速度（Braking Min Speed）只在使用制动（Use Braking）开启时可调。

它设置制动过程中的最低速度。

### 制动最大速度（Braking Max Speed）

制动最大速度（Braking Max Speed）只在使用制动（Use Braking）开启时可调。

它设置制动过程中的最高速度。

### 制动曲线（Braking Curve）

制动（Braking）只在使用制动（Use Braking）开启时可调。

它用于调整制动距离范围内速度变化的曲线形状。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是覆盖修改器（nxCover）的主设置页。这里主要编辑对象模式（Object Mode）、对象索引（Object Index）、随机种子（Random Seed）、循环（Cycle）和对象（Objects）列表。

如果你要调整粒子覆盖哪些对象、多个目标怎样分配、每个目标怎样覆盖，通常先回到物体属性（Object Properties）页。

### 设置页（Section）

设置页（Section）是覆盖修改器（nxCover）面板顶部的页签切换。它只切换当前正在编辑的设置页。

覆盖修改器（nxCover）常见页签包括物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。

### 组（Groups Affected）

组（Groups Affected）用于限制覆盖修改器（nxCover）影响哪些粒子组。

如果这里不添加任何组，覆盖通常会按当前粒子流程正常作用，不额外按组过滤。添加 nx 组（nxGroup）后，覆盖效果会根据组列表来限制影响对象。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要直接修改它。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动覆盖参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

常见用法：

- 用年龄（Age）驱动强度（Strength），让粒子出生后逐渐覆盖目标。
- 用速度（Speed）驱动容差（Tolerance）或固定速度（Fixed Speed）。
- 用 ID（ID）驱动释放时间（Release Time）或时间变化量（Time Variation），制造逐粒子差异。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个覆盖参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会产生实际效果。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制覆盖修改器（nxCover）的哪个参数。

对于覆盖修改器（nxCover），常见目标包括强度（Strength）、容差（Tolerance）、速度、时间、保持和制动相关参数。可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）、距离（Distance）、文档时间（Document Time）、组（Group）和 ID（ID）。选择粒子数据（Particle Data）后，要配合范围最小值（Range Min）和范围最大值（Range Max）设定输入区间。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

覆盖修改器（nxCover）本身不是内部多层修改器，所以这个字段通常没有实际意义。它主要服务于湍流、缩放、速度、旋转、方向、限制、颜色这类带内部层列表的修改器。

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

衰减（Falloff）用于用空间衰减对象控制覆盖修改器（nxCover）的影响范围。

如果你想控制“哪里会覆盖”，用衰减（Falloff）；如果想控制“哪些组受覆盖影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前覆盖修改器（nxCover）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

---

## 列表操作按钮

这些小按钮通常出现在对象列表、组列表、映射列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择对象或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表可添加类型的菜单。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。例如创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff）。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。它通常只移除列表引用，不等于删除场景里的对象本体。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

对象（Objects）列表的顺序会影响序列（Sequence）和对象索引（Object Index）这类对象分配模式。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）用于快速打开或关闭当前列表项。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于树状列表里的层级调整。普通对象列表通常不需要使用它。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于树状列表里的层级调整。普通对象列表通常不需要使用它。
