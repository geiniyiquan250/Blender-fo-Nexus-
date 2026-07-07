# NeXus 推力修改器使用说明

这份文档只说明推力修改器（nxPush）。它用于把过近的粒子彼此推开，减少重叠和挤压。

## 推力修改器（nxPush）

推力修改器（nxPush）不产生粒子。它处理的是已经存在的粒子，并在每一帧里按设定距离反复把过近粒子分开。

这个修改器的核心思路很直接：

- 先决定距离模式（Distance Mode），也就是“多近算太近”。
- 再用距离（Distance）或粒子半径（Particle Radius）确定分离范围。
- 然后用强度（Strength）和迭代次数（Iterations）决定推开的力度与稳定程度。

它更像一个粒子间距修正器，不是碰撞体那种“粒子和几何体发生碰撞”的处理。

### 设置页（Section）

设置页（Section）用于切换当前显示的主设置页。

推力修改器（nxPush）除了自己的物体属性（Object Properties）页外，还会带有组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）

启用（Enabled）控制推力修改器（nxPush）是否参与当前粒子流程。

关闭后，粒子之间不会再执行这一步相互推开。它适合在排查“重叠来自发射本身，还是来自后续推开不足”时临时对比。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制推力修改器（nxPush）的编辑器辅助显示是否可见。

当前代码没有专门的推力视口图形，这个开关主要属于通用显示控制，不改变实际推开结果。

### 物体属性（Object Properties）

物体属性（Object Properties）是推力修改器（nxPush）的主设置页。这里集中设置距离模式（Distance Mode）、距离（Distance）、强度（Strength）、迭代次数（Iterations）、缓入（Ease In）和仅同组（Only Same Group）。

### 距离模式（Distance Mode）

距离模式（Distance Mode）决定推力修改器（nxPush）怎样理解“粒子之间至少要隔多远”。

当前有两种模式：

- 绝对（Absolute）：直接使用距离（Distance）作为固定分离距离。
- 粒子半径（Particle Radius）：改为按粒子自己的半径来判断分离范围。

如果你想所有粒子都维持同样的最小间距，用绝对（Absolute）。如果粒子大小本来就不同，希望大粒子需要更大间距，小粒子允许更近，就用粒子半径（Particle Radius）。

### 距离（Distance）

距离（Distance）定义推力修改器（nxPush）要把粒子彼此拉开的目标距离。

它只在距离模式（Distance Mode）为绝对（Absolute）时可编辑。切到粒子半径（Particle Radius）后，这个值会灰显，因为间距改由粒子半径数据决定。

### 强度（Strength）

强度（Strength）控制每次推开运算的力度。

数值越高，同一帧里粒子被分开的趋势越明显；数值越低，分离更柔和，但可能需要更多迭代次数（Iterations）才能把密集重叠完全解开。

### 迭代次数（Iterations）

迭代次数（Iterations）控制每一帧里重复执行多少次推开修正。

它影响的是稳定程度，而不是单次力度。粒子非常密集时，提高强度（Strength）可能还不够，通常还要增加迭代次数（Iterations），让粒子有更多轮次逐步分开。

### 缓入（Ease In）

缓入（Ease In）控制推力修改器（nxPush）从开始生效到达到完整强度需要多长时间。

它适合避免推力在一开始就立刻满强度介入。粒子刚出生时如果本来就很密，适当增加缓入（Ease In）可以让推开过程更渐进。

### 仅同组（Only Same Group）

仅同组（Only Same Group）控制推力修改器（nxPush）是否只处理同一个组里的粒子之间的推开。

开启后，不同粒子组之间不会互相推开；关闭时，进入当前修改器作用范围的粒子都会一起参与分离计算。

如果场景里把不同组当作不同材质、不同层次或不同效果来源，开启仅同组（Only Same Group）通常更容易保持组与组之间的独立性。

## 通用页签

### 组（Groups Affected）

组（Groups Affected）用于限制推力修改器（nxPush）影响哪些粒子组。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表当前选中的条目。

### 添加组（Add Group）

添加组（Add Group）把一个 nx 组（nxGroup）加入组（Groups Affected）列表。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

### 组启用（Group Enabled）

组启用（Group Enabled）控制这一条组（Groups Affected）列表项是否参与过滤。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动推力修改器（nxPush）的参数。

对于推力修改器（nxPush），更适合被映射的通常是距离（Distance）和强度（Strength）这类连续数值参数。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的规则列表。每一层代表一条“用某种粒子数据驱动某个目标参数”的规则。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射具体控制推力修改器（nxPush）的哪个参数。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定这条映射使用哪种粒子属性作为输入。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定当前映射要作用到哪一层。

推力修改器（nxPush）本身不是分层修改器，所以这个字段通常没有实际作用。

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

衰减（Falloff）用于按空间范围限制推力修改器（nxPush）的影响。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的对象列表。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑哪一个衰减对象条目。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）把一个 nx 衰减（nxFalloff）加入衰减（Falloff）列表。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减列表项里实际引用的 nx 衰减（nxFalloff）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）定义多个衰减对象怎样一起调制当前推力效果。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终结果的力度。

### 衰减启用（Falloff Enabled）

衰减启用（Falloff Enabled）控制这一条衰减对象是否参与影响范围计算。
