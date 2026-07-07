# NeXus 感染修改器使用说明

这份文档只说明感染修改器（nxInfectio）。它用于让粒子在搜索半径内传播感染，并按潜伏、感染、免疫和颜色规则改变粒子状态。

## 感染修改器（nxInfectio）

感染修改器（nxInfectio）不产生粒子。用户通常先创建能产生粒子的发射器（nxEmitter），再创建感染修改器（nxInfectio）。

创建感染修改器（nxInfectio）时，插件会自动新建一个种子（Seeds）条目，并创建一个跟随该修改器的种子对象（Seed Object）空物体。感染传播从这些种子位置开始，再按搜索半径（Search Radius）、最大感染数（Max Infected）和潜伏模式（Incubation Mode）推进。

### 设置页（Section）

设置页（Section）切换感染修改器（nxInfectio）当前显示的主页签。

普通 NeXus 修改器通用页签还包含物体属性（Object Properties）、组（Groups Affected）、映射（Mapping）和衰减（Falloff）。感染修改器（nxInfectio）的主要参数显示在自身主面板里，不额外拆成独立子页签。

### 启用（Enabled）

启用（Enabled）控制当前条目是否参与作用。

这个同名开关会出现在感染修改器（nxInfectio）本体、种子（Seeds）列表项、组（Groups Affected）列表项、映射（Mapping）列表项和衰减（Falloff）列表项上。它只影响所在层级，不会连带关闭其他条目。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制感染修改器（nxInfectio）在编辑器里的辅助显示是否可见。

感染修改器（nxInfectio）当前的辅助显示主要是种子球体。关闭后不会停止感染计算，只是不再显示这些辅助球体。

### 物体属性（Object Properties）

物体属性（Object Properties）是感染修改器（nxInfectio）的通用页签，包含修改器本体的基础控制，例如启用（Enabled）和视口可见（Visible in Editor）。

### 种子（Seeds）

种子（Seeds）是感染起点列表。每个条目都绑定一个种子对象（Seed Object），并用自己的半径（Radius）、阈值（Threshold）和颜色（Color）控制这一处感染源。

如果条目禁用、没有种子对象（Seed Object），或种子对象被删除，这个种子不会参与感染同步。

### 活动种子索引（Active Seed Index）

活动种子索引（Active Seed Index）记录种子（Seeds）列表当前选中的条目。

它决定下方显示和编辑的是哪一个种子条目的半径（Radius）、阈值（Threshold）和颜色（Color）。

### 种子类型（Seed Type）

种子类型（Seed Type）表示当前列表项的种子类别。

当前代码里只有一种类型，就是种子对象（Seed Object）。这个字段更多是给列表系统保留的类型入口。

### 种子对象（Seed Object）

种子对象（Seed Object）指定感染起点在场景里的位置。

插件在创建条目时会自动生成一个空物体并把它绑定到当前感染修改器（nxInfectio）。移动这个空物体，就等于移动感染源的位置。

### 半径（Radius）

半径（Radius）控制当前种子的球体范围。

这个值会参与同步到感染种子数据里，也会直接影响视口里种子球体的显示大小。

### 阈值（Threshold）

阈值（Threshold）控制当前种子触发感染时使用的潜伏阈值。

它是每个种子单独保存的因子值。调高后，这个种子更适合配合较高的潜伏判断门槛使用；调低后，更容易触发感染推进。

### 颜色（Color）

颜色（Color）控制当前种子在视口辅助球体里的显示颜色。

它只影响编辑器辅助显示，不直接改变感染后粒子的颜色。粒子颜色由颜色模式（Color Mode）和后续颜色设置控制。

### 颜色模式（Color Mode）

颜色模式（Color Mode）决定感染状态如何改写粒子颜色。

可选值：

- 固定值（Fixed Value）：分别使用潜伏中（Incubating）和已感染（Infected）的固定颜色。
- 梯度（Gradient）：按潜伏进度使用梯度颜色。
- 使用组（Use Groups）：按潜伏组（Incubating Group）和感染组（Infected Group）切换粒子组颜色。
- 无颜色变化（No Color Change）：不修改粒子颜色。

### 潜伏中（Incubating）

潜伏中（Incubating）设置粒子处于潜伏阶段时使用的颜色。

它只在颜色模式（Color Mode）为固定值（Fixed Value）时显示。

### 已感染（Infected）

已感染（Infected）设置粒子进入感染阶段后使用的颜色。

它只在颜色模式（Color Mode）为固定值（Fixed Value）时显示。

### 潜伏组（Incubating Group）

潜伏组（Incubating Group）指定潜伏粒子要使用的 nx 组（nxGroup）。

它只在颜色模式（Color Mode）为使用组（Use Groups）时显示。

### 感染组（Infected Group）

感染组（Infected Group）指定感染粒子要使用的 nx 组（nxGroup）。

它只在颜色模式（Color Mode）为使用组（Use Groups）时显示。

### 组颜色更改（Group Color Change）

组颜色更改（Group Color Change）控制粒子在哪个阶段切换组颜色。

它只在颜色模式（Color Mode）为使用组（Use Groups）时显示。可选范围包括两个阶段（Both Stages）、未感染到潜伏阶段（Uninfected to Incubated Stage）、从潜伏阶段到感染阶段（Incubated to Infected Stage）和无颜色变化（No Color Changes）。

### 搜索半径（Search Radius）

搜索半径（Search Radius）控制每次感染搜索时使用的空间范围。

范围越大，感染粒子越容易在更远距离找到可传播目标；范围越小，传播更局部。

### 最大感染数（Max Infected）

最大感染数（Max Infected）限制每一步最多能新增多少感染粒子。

这个值越大，传播扩散会更快；越小，传播更缓慢。

### 感染寿命（Infected Lifespan）

感染寿命（Infected Lifespan）控制粒子处于感染状态能持续多久。

代码说明 `0` 表示无限持续。只要感染寿命（Infected Lifespan）结束，粒子就不再保持当前感染状态。

### 仅搜索一次最近项（Search for Nearest Once）

仅搜索一次最近项（Search for Nearest Once）控制每个粒子是否只进行一次新的感染搜索。

开启后，粒子不会反复重复寻找新目标；关闭后，粒子可以继续参与后续搜索流程。

### 约束搜索（Constrain Search）

约束搜索（Constrain Search）决定是否对感染搜索范围再加一层轴向限制。

关闭时，感染主要按搜索半径（Search Radius）决定范围。开启后，还要同时满足限制（Limit）的轴向条件。

### 限制（Limit）

限制（Limit）控制约束搜索（Constrain Search）开启后的轴向限制范围。

它是一个三轴向量，用来分别限制搜索区域在 X、Y、Z 方向上的扩展范围。只有约束搜索（Constrain Search）开启时这个值才真正参与作用。

### 潜伏模式（Incubation Mode）

潜伏模式（Incubation Mode）决定感染进度怎样从粒子属性里读出来。

可选值：

- 从潜伏率设置（Set From Incubation Rate）：直接按潜伏率（Incubation Rate）随时间推进。
- 使用粒子颜色（Use Particle Color）：按粒子颜色值读取潜伏进度。
- 粒子半径（Particle Radius）：按粒子半径读取潜伏进度。
- 粒子质量（Particle Mass）：按粒子质量读取潜伏进度。

不同模式会决定下方显示的是潜伏率（Incubation Rate）/变化（Variation），还是最小值（Min Value）/最大值（Max Value）。

### 最小值（Min Value）

最小值（Min Value）定义当前潜伏模式（Incubation Mode）的下界。

它只在潜伏模式（Incubation Mode）为粒子半径（Particle Radius）或粒子质量（Particle Mass）时显示。

### 最大值（Max Value）

最大值（Max Value）定义当前潜伏模式（Incubation Mode）的上界。

它只在潜伏模式（Incubation Mode）为粒子半径（Particle Radius）或粒子质量（Particle Mass）时显示。

### 潜伏率（Incubation Rate）

潜伏率（Incubation Rate）控制感染进度随时间推进的基础速度。

它只在潜伏模式（Incubation Mode）为从潜伏率设置（Set From Incubation Rate）时显示。

### 变化（Variation）

变化（Variation）控制潜伏率（Incubation Rate）的随机变化。

它只在潜伏模式（Incubation Mode）为从潜伏率设置（Set From Incubation Rate）时显示。

### 潜伏倍增（Incubation Multiplier）

潜伏倍增（Incubation Multiplier）控制额外感染邻居对潜伏推进的放大倍率。

数值越高，粒子附近同时存在多个感染来源时，潜伏进度推进越快。

### 反转（Invert）

反转（Invert）反转当前潜伏模式（Incubation Mode）的判断方向。

它不在从潜伏率设置（Set From Incubation Rate）模式下显示，只在读取粒子颜色、半径或质量时可用。

### 使用免疫（Use Immunity）

使用免疫（Use Immunity）控制是否启用粒子的免疫判断。

关闭时，免疫水平（Immunity Level）不参与计算。开启后，感染传播会受免疫水平影响。

### 免疫水平（Immunity Level）

免疫水平（Immunity Level）设置粒子的基础免疫强度。

它只在使用免疫（Use Immunity）开启时可调。数值越高，粒子越不容易被感染。

### 组（Groups Affected）

组（Groups Affected）限制感染修改器（nxInfectio）影响哪些粒子组。留空时，通常表示不额外按组过滤。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表当前选中的条目。

### 添加组（Add Group）

添加组（Add Group）把一个 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）指定当前组条目引用的 nx 组（nxGroup）对象。

### 映射（Mapping）

映射（Mapping）用于用粒子数据（Particle Data）动态驱动感染修改器（nxInfectio）的参数。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是感染修改器（nxInfectio）的参数驱动列表。每一层都定义一条独立映射规则。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录映射层（Mapping Layers）列表当前选中的条目。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）指定当前映射层要驱动的感染参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）指定当前映射层读取哪一种粒子属性作为驱动源。

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

衰减（Falloff）用于用空间对象限制感染修改器（nxInfectio）的影响范围。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是感染修改器（nxInfectio）的衰减对象列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录衰减对象（Falloff Objects）列表当前选中的条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）把一个衰减对象加入感染修改器（nxInfectio）的衰减列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）指定当前衰减条目使用的对象。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象怎样合成最终影响结果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减混合在最终结果中的权重。
