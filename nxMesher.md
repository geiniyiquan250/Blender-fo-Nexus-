# NeXus 网格化修改器使用说明

这份文档说明网格化修改器（nxMesher）。它从粒子发射器（nxEmitter）或 ExplosiaFX 体积源生成 Blender 网格，并可把颜色、速度和发射器顶点映射写入生成网格的属性数据。

## 网格化修改器（nxMesher）

网格化修改器（nxMesher）用于把 NeXus 粒子或体积数据转换成多边形网格。创建修改器后，插件会在网格化对象下创建一个子网格对象，后续 NeXus 计算会把顶点、面、法线和可选导出属性写入这个子网格。

网格化修改器默认没有固定输入对象。需要在层（Layers）列表里添加 Emitter、Smoothing 或 ExplosiaFX 层来定义数据来源和处理步骤。Emitter 层引用发射器（nxEmitter），ExplosiaFX 层引用 ExplosiaFX 对象，Smoothing 层对列表前面产生的网格化结果继续平滑。

生成网格会跟随当前计算结果更新。重置修改器或清除状态时，子网格几何会被清空。当前实现只在 Blender 4.3 及以上版本写入子网格数据。

### 设置页（Section）

设置页（Section）切换当前显示的设置页。网格化修改器（nxMesher）自己的页签包含 General、Export Tags 和 Domain；普通 NeXus 修改器通用页签还包含 Object Properties、Groups Affected、Mapping 和 Falloff。

右键页签时，帮助会打开对应页签的小节。查看参数说明时，先确认当前页签，因为有些参数只在特定页签或特定模式下显示。

### 启用（Enabled）

启用（Enabled）控制网格化修改器（nxMesher）是否参与当前 NeXus 计算。关闭后，该修改器保留在场景和管线中，但不会继续把当前计算结果写入网格化输出。

调试时可以临时关闭它，用来确认场景中的网格结果是否来自当前网格化修改器。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制网格化修改器（nxMesher）在编辑器中的辅助显示是否可见。

它影响编辑器辅助显示，不等同于删除生成的子网格对象。需要隐藏或显示实际网格对象时，请检查子网格对象自身的可见性。

### 物体属性（Object Properties）

物体属性（Object Properties）是通用页签，包含网格化修改器自身的基础控制，例如启用（Enabled）和视口可见（Visible in Editor）。

这些设置作用在当前网格化修改器对象上，不是层（Layers）列表里某个单独条目的设置。

### 常规（General）

常规（General）包含生成网格的主要设置：多边形尺寸、表面尺寸来源、表面重建类型、多边形模式，以及层（Layers）列表。

创建网格化修改器后，通常先在这个页签添加输入层，再根据粒子大小和目标细节调整 Polygon Size、Surface Size 和 Surface Type。

### 导出标签（Export Tags）

导出标签（Export Tags）控制是否把粒子数据写入生成网格的属性。

当前可导出的数据包括颜色和速度。发射器顶点映射不是在这个页签里控制，而是在层（Layers）列表中每个 Emitter 层右侧的图标按钮控制。

### 域（Domain）

域（Domain）控制网格化计算范围和视口域显示。

自适应域（Adaptive Domain）开启时，域范围根据粒子范围自动适配；关闭时使用域大小（Domain Size）作为固定范围。绘制域（Draw Domain）只控制视口辅助线显示，方便检查当前计算范围。

### 多边形尺寸（Polygon Size）

多边形尺寸（Polygon Size）设置生成网格的基础面片大小。它使用长度单位，并会同步为网格化计算的体素/采样尺度。

数值越小，生成网格可表达的细节越细，计算量和输出网格规模通常也会更高。数值越大，网格更粗，适合先快速预览整体形状。

### 表面尺寸（Surface Size）

表面尺寸（Surface Size）选择粒子表面半径的来源。

可选值：

- Custom：使用半径（Radius）中的固定半径。
- Source：读取源粒子的半径，并用缩放（Scale）按百分比调整。

当不同发射器的粒子半径需要保留差异时，使用 Source 更直观；当希望所有输入粒子使用统一半径时，使用 Custom。

### 半径（Radius）

半径（Radius）设置用于网格化的固定粒子半径。表面尺寸（Surface Size）为 Custom 时显示并生效。

它决定每个粒子参与表面重建时的基础影响范围。半径和多边形尺寸（Polygon Size）需要配合观察：半径定义表面厚度趋势，多边形尺寸定义最终网格细分尺度。

### 缩放（Scale）

缩放（Scale）按百分比调整源粒子半径。表面尺寸（Surface Size）为 Source 时显示并生效。

100% 表示使用源粒子半径本身。提高该值会放大源半径对表面重建的影响，降低该值会减小源半径参与网格化时的影响。

### 表面类型（Surface Type）

表面类型（Surface Type）选择表面重建算法。

可选值：

- Zhu-Bridson：使用 Zhu-Bridson 表面重建。
- Spheres：使用球形表面重建。
- 基础（Basic）：使用各向异性表面重建。

选择 基础（Basic） 后，会显示速度各向异性（Speed Anisotropy）相关参数。其他表面类型不会显示这些各向异性控制。

### 速度各向异性（Speed Anisotropy）

速度各向异性（Speed Anisotropy）只在表面类型（Surface Type）为 基础（Basic） 时显示。开启后，各向异性拉伸会使用粒子速度作为控制来源。

开启时使用最大速度（Max Speed）来定义速度拉伸的上限。关闭时使用离心率（Eccentricity）控制各向异性粒子的形状偏移程度。

### 离心率（Eccentricity）

离心率（Eccentricity）只在表面类型为 基础（Basic），并且速度各向异性（Speed Anisotropy）关闭时显示。

它控制各向异性粒子的形状偏移程度，用百分比表示。需要固定的各向异性形状时调整它；需要根据粒子速度变化时，改用速度各向异性。

### 最大速度（Max Speed）

最大速度（Max Speed）只在表面类型为 基础（Basic），并且速度各向异性（Speed Anisotropy）开启时显示。

它设置用于速度各向异性拉伸的速度上限。速度达到或超过这个值时会按上限理解；速度低于这个值时按比例影响拉伸。

### 多边形模式（Polygon Mode）

多边形模式（Polygon Mode）选择生成网格使用三角面还是四边面。

可选值：

- Tris：生成三角面。
- Quads：生成四边面。

这个选择会影响写入子网格时每个面的顶点数量。需要稳定的三角拓扑时使用 Tris；需要四边面输出时使用 Quads。

### 传递颜色（Transfer Color）

传递颜色（Transfer Color）控制是否把粒子颜色写入生成网格的颜色属性。

开启后，网格化输出会尝试生成名为 `color` 的顶点颜色属性。关闭时，颜色导出相关的颜色平滑（Color Smoothing）不会显示。

### 颜色平滑（Color Smoothing）

颜色平滑（Color Smoothing）设置颜色传递后的平滑迭代次数。传递颜色（Transfer Color）开启时显示。

它用于减少颜色属性在生成网格上的局部突变。数值越高，颜色数据会经过更多平滑处理。

### 传递速度（Transfer Velocity）

传递速度（Transfer Velocity）控制是否把粒子速度写入生成网格的速度属性。

开启后，网格化输出会尝试生成名为 `velocity` 的点属性，属性类型为向量。关闭时，最大速度 X / Y / Z 和速度平滑（Velocity Smoothing）不会显示。

### 最大速度 X / Y / Z（Max Velocity X / Y / Z）

最大速度 X / Y / Z（Max Velocity X / Y / Z）分别设置 X、Y、Z 方向速度归一化的最大值。传递速度（Transfer Velocity）开启时显示。

这些值用于解释不同方向的速度范围。需要保留某个方向更大的速度变化时，可以单独提高对应轴的最大速度。

### 速度平滑（Velocity Smoothing）

速度平滑（Velocity Smoothing）设置速度传递后的平滑迭代次数。传递速度（Transfer Velocity）开启时显示。

它作用在导出的速度属性上，用于减少相邻区域之间速度数据的突变。数值越高，速度属性越平滑。

### 域大小（Domain Size）

域大小（Domain Size）设置固定网格化域的 X、Y、Z 尺寸。自适应域（Adaptive Domain）关闭时可编辑。

固定域以当前网格化对象为参考绘制。使用固定域时，需要让粒子或体积输入落在域范围内，方便网格化计算覆盖目标区域。

### 自适应域（Adaptive Domain）

自适应域（Adaptive Domain）开启后，网格化域会根据粒子范围自动适配。关闭后，网格化修改器使用域大小（Domain Size）中的固定范围。

开启自适应域适合输入范围持续变化的模拟；关闭自适应域适合需要固定计算范围、固定视口参考框的场景。

### 自适应颜色（Adaptive Color）

自适应颜色（Adaptive Color）设置自适应域在视口中绘制时使用的颜色。自适应域（Adaptive Domain）开启时可编辑。

它只影响视口辅助显示颜色，不改变生成网格的顶点颜色属性。要导出粒子颜色，请使用导出标签（Export Tags）里的传递颜色（Transfer Color）。

### 绘制域（Draw Domain）

绘制域（Draw Domain）控制是否在视口中显示网格化域范围。

自适应域开启时，视口会绘制自适应域线框；自适应域关闭时，会绘制固定域大小对应的盒状范围。这个开关用于检查域范围，不会单独改变网格化结果。

### 层（Layers）

层（Layers）是网格化处理列表。每个条目定义一个输入或处理步骤，列表顺序会影响最终结果。

层类型包括：

- Emitter：引用发射器（nxEmitter）作为粒子输入。
- Smoothing：对前面已经生成的网格化结果进行平滑。
- ExplosiaFX：引用 ExplosiaFX 体积源作为输入。

Emitter 和 ExplosiaFX 层需要设置目标（Target）。Smoothing 层不需要目标对象，只使用自身的平滑参数。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）是层（Layers）列表中当前选中条目的索引。

它用于决定下方显示哪一个层条目的详细设置。一般不需要手动理解数值本身，只需要在列表中选择要编辑的层。

### 添加菜单（Add Menu）

添加菜单（Add Menu）打开层类型菜单，用于选择要添加的网格化层类型。

网格化层列表使用菜单添加，因为新条目需要先确定类型。选择 Emitter、Smoothing 或 ExplosiaFX 后，会创建对应类型的层条目。

### 创建并添加（Create and Add）

创建并添加（Create and Add）从添加菜单中创建指定类型的层，并加入当前层（Layers）列表。

新层会根据类型自动命名。添加后，在列表中选中该层即可编辑目标对象、平滑参数或体积阈值。

### 添加项（Add Item）

添加项（Add Item）是通用列表添加操作。网格化层列表带有类型菜单，因此通常通过添加菜单（Add Menu）选择具体层类型。

如果某个列表直接显示加号按钮，这个操作会在当前列表新增一个条目。它只管理列表内容，不创建新的 Blender 场景对象。

### 移除项（Remove Item）

移除项（Remove Item）从当前列表移除选中的条目。

它只移除列表引用，不删除场景中的发射器、ExplosiaFX 或其他目标对象。移除输入层后，该层不再参与网格化计算。

### 上移项（Move Item Up）

上移项（Move Item Up）把当前选中的层在列表中上移一位。

层顺序会影响输入和处理步骤的先后关系。需要先输入、再平滑时，把 Emitter 或 ExplosiaFX 层放在 Smoothing 层之前。

### 下移项（Move Item Down）

下移项（Move Item Down）把当前选中的层在列表中下移一位。

当某个处理层应该在更多输入层之后执行时，可以把它下移到对应输入层后面。

### 切换启用（Toggle Enabled）

切换启用（Toggle Enabled）切换当前列表条目的启用状态。

关闭后，该条目保留在列表中，便于之后重新启用或对比效果。需要临时排查某个输入层或平滑层的影响时，可以使用这个按钮。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于连续从场景中拾取多个对象并加入支持快速添加的列表。

网格化层列表本身通过类型菜单添加层；如果其它通用列表显示连续拾取按钮，它会按列表允许的对象类型连续添加目标对象。

### 切换图标标记（Toggle Icon Flag）

切换图标标记（Toggle Icon Flag）切换层条目上的图标状态。在网格化发射器层中，它用于启用或关闭发射器顶点映射输出。

开启后，生成网格会尝试为对应 Emitter 层写入一个点属性，属性名使用该发射器对象名。该属性记录发射器对生成顶点的权重贡献。关闭后，发射器平滑（Emitter Smoothing）在界面中灰显。

### 层名称（Layer Name）

层名称（Layer Name）显示和编辑当前层条目的名称。

新层会根据类型自动命名，例如 Emitter、Smoothing 或 ExplosiaFX。手动改名后，列表会保留自定义名称，方便区分多个输入或处理步骤。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制当前层是否参与网格化计算。

关闭某一层适合做对比：例如暂时关闭某个 Emitter 层，观察它对生成网格的贡献；或关闭 Smoothing 层，检查未平滑前的表面状态。

### 类型（Type）

类型（Type）选择当前层的作用。

可选值：

- Emitter：使用粒子发射器作为网格化输入。
- Smoothing：对前面层产生的网格化结果进行平滑。
- ExplosiaFX：使用 ExplosiaFX 体积源作为网格化输入。

切换类型时，目标对象会按新类型重新校验。当前目标对象不符合新类型要求时，界面会清空目标。

### 目标（Target）

目标（Target）指定当前层引用的对象。

Emitter 层只能选择发射器（nxEmitter）。ExplosiaFX 层只能选择 ExplosiaFX 对象。Smoothing 层不显示目标对象，因为它只处理列表中已有的网格化结果。

### 发射器平滑（Emitter Smoothing）

发射器平滑（Emitter Smoothing）设置 Emitter 层的发射器贡献平滑迭代次数。

它在发射器顶点映射图标开启时可编辑。这个值会随 Emitter 层同步到计算端，用于发射器贡献数据的平滑处理。

### 平滑模式（Smoothing Mode）

平滑模式（Smoothing Mode）选择 Smoothing 层使用的平滑算法。

可选值：

- Gaussian：高斯平滑。
- Laplacian：拉普拉斯平滑。
- Mean Curvature：平均曲率流平滑。

只有 Smoothing 层显示这个参数。选择 Gaussian 时，会额外显示影响范围（Influence Range）。

### 平滑强度（Smoothing Strength）

平滑强度（Smoothing Strength）控制 Smoothing 层的整体平滑力度，用百分比表示。

它和迭代次数（Smoothing Iterations）一起决定平滑处理的强弱。强度控制单次处理的幅度，迭代次数控制处理重复次数。

### 影响范围（Influence Range）

影响范围（Influence Range）设置 Gaussian 平滑的作用范围。平滑模式（Smoothing Mode）为 Gaussian 时可编辑。

当平滑模式不是 Gaussian 时，界面会灰显这个参数。灰显表示当前算法不使用该范围值。

### 平滑迭代（Smoothing Iterations）

平滑迭代（Smoothing Iterations）设置 Smoothing 层执行的平滑次数。

数值越高，平滑处理重复次数越多。需要先确认 Smoothing 层在列表中的顺序，因为它会处理列表前面产生的结果。

### 烟雾（Smoke）

烟雾（Smoke）控制 ExplosiaFX 层是否使用烟雾密度生成表面。

它只在 ExplosiaFX 层显示。开启后，烟雾等值（Smoke Iso-value）可编辑，用来设置烟雾密度的表面阈值。

### 烟雾等值（Smoke Iso-value）

烟雾等值（Smoke Iso-value）设置烟雾密度生成表面的阈值。烟雾（Smoke）开启时可编辑。

提高或降低这个值会改变哪些烟雾密度值参与表面生成。它只作用于 ExplosiaFX 层的烟雾通道。

### 温度（Temperature）

温度（Temperature）控制 ExplosiaFX 层是否使用温度生成表面。

它只在 ExplosiaFX 层显示。开启后，温度等值（Temperature Iso-value）可编辑，用来设置温度通道的表面阈值。

### 温度等值（Temperature Iso-value）

温度等值（Temperature Iso-value）设置温度生成表面的阈值。温度（Temperature）开启时可编辑。

它只作用于 ExplosiaFX 层的温度通道。烟雾和温度可以分别开启，用于选择 ExplosiaFX 中哪些体积数据参与网格化。

### 组（Groups Affected）

组（Groups Affected）是粒子组列表，用于限定哪些粒子组受当前网格化修改器（nxMesher）影响。

空列表表示不按组过滤，当前修改器可影响输入中的所有粒子。添加组对象后，只有匹配这些组的粒子会进入该修改器的影响范围。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）是组（Groups Affected）列表中当前选中条目的索引。

它用于决定正在编辑哪一个组条目。一般通过点击列表条目选择，不需要手动输入索引。

### 添加组（Add Group）

添加组（Add Group）向组（Groups Affected）列表添加新的组条目。

添加后，需要把目标nx 组（nxGroup）指定到组对象（Group Object）字段中。这个列表只限制影响范围，不创建新的粒子组对象。

### 组对象（Group Object）

组对象（Group Object）指定组列表条目的目标nx 组（nxGroup）。

当列表中有多个组对象时，当前网格化修改器按这些组限定受影响粒子。留空条目不会提供有效组目标。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动网格化修改器（nxMesher）的参数。

具体驱动关系在映射层（Mapping Layers）里逐条设置。映射适合让粒子属性影响参数值，例如用粒子数据改变某个可映射参数的强度或范围。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射规则列表，每一层定义一条输入到输出的驱动关系。

列表里的条目可以单独启用或关闭。多条映射层同时存在时，需要检查每条的目标参数、粒子数据来源、范围和权重。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）是映射层（Mapping Layers）列表中当前选中条目的索引。

它决定下方显示和编辑哪一条映射规则。通过列表选择条目即可切换当前编辑对象。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）选择要被粒子数据驱动的网格化参数。

选择目标参数后，映射层会把粒子数据（Particle Data）读取到的输入值转换为该参数的驱动值。需要确认目标参数本身在当前模式下可用。

### 粒子数据（Particle Data）

粒子数据（Particle Data）选择用于驱动目标参数的输入属性。

常见输入来自粒子模拟数据。选择时应考虑该数据是否在当前粒子来源中存在，以及数值范围是否适合后面的 Range Min / Range Max。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于组织和筛选不同映射层。

它帮助把多条映射规则分组管理。只有指定图层参与当前映射时，对应规则才会影响目标参数。

### 范围最小值（Range Min）

范围最小值（Range Min）设置映射输入范围的下限。

粒子数据低于这个下限时，映射会按下限端理解输入。调整它可以改变粒子数据从哪个值开始影响目标参数。

### 范围最大值（Range Max）

范围最大值（Range Max）设置映射输入范围的上限。

粒子数据高于这个上限时，映射会按上限端理解输入。范围最大值和范围最小值一起定义输入数据如何转换到目标参数。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的驱动强度。

权重越高，该映射层对目标参数的影响越强。需要混合多条映射规则时，可以通过权重控制每条规则的贡献。

### 钳制（Clamp）

钳制（Clamp）控制映射输出是否限制在目标参数的有效范围内。

开启后，映射结果不会超过目标参数允许的最小值和最大值。关闭后，映射输出按规则计算，是否被后续系统接受取决于目标参数自身限制。

### 衰减（Falloff）

衰减（Falloff）用于在空间范围内减弱网格化修改器（nxMesher）对粒子的影响。

衰减对象（Falloff Objects）列表定义用于计算空间衰减的物体。它适合让修改器影响只集中在某些区域，而不是作用于全部输入粒子。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减对象列表，每个条目指定一个影响范围对象。

列表中可以添加多个衰减对象，并通过衰减混合（Falloff Blend）和衰减混合强度（Falloff Blend Strength）控制它们的组合方式。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）是衰减对象（Falloff Objects）列表中当前选中条目的索引。

它用于决定正在编辑哪一个衰减条目。通常通过点击列表选择条目，不需要手动调整索引。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）向衰减对象（Falloff Objects）列表添加新的衰减条目。

添加后，需要在衰减对象（Falloff Object）字段里指定目标对象。这个列表只保存引用，不创建新的场景对象。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）指定衰减列表条目的目标对象。

目标对象决定该条目用于计算衰减的空间位置和范围。留空条目不会提供有效衰减目标。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）控制多个衰减对象之间的混合模式。

当列表中只有一个衰减对象时，混合模式影响较小；当多个衰减对象同时存在时，它决定这些空间影响如何组合。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制衰减混合的整体强度。

提高强度会增强衰减对象对修改器影响范围的控制。需要更柔和或更弱的空间影响时，可以降低这个值。
