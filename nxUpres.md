# NeXus 提升分辨率修改器使用说明

这份文档只说明提升分辨率修改器（nxUpres）。它用于根据源发射器（Source）和目标发射器（Destination）之间的关系，为已有粒子生成更高密度的上采样粒子分布。

## 提升分辨率修改器（nxUpres）

提升分辨率修改器（nxUpres）不直接发射普通意义上的新主粒子，而是根据源发射器（Source）和目标发射器（Destination）的关系，对粒子做上采样（Upres）扩充。

可以把它理解成：

- 先指定哪些发射器提供原始粒子分布。
- 再指定哪些发射器接收提升分辨率后的结果。
- 然后用强度、位置、速度、半径、质量和颜色这些变化参数，决定上采样粒子与源粒子有多接近。

它适合做高密度补点、细化粒子外观、从低成本模拟结果扩展出更丰富的显示粒子。

### 启用（Enabled）

启用（Enabled）控制整个提升分辨率修改器（nxUpres）是否参与粒子流程。

关闭后，不会继续生成上采样结果，但源发射器（Source）和目标发射器（Destination）列表会保留。

### 源（Source）

源（Source）是提供原始粒子分布的发射器列表。

这些发射器里的粒子会被当作“参考粒子”，上采样（Upres）结果基于它们生成。

### 活动源索引（Active Source Index）

活动源索引（Active Source Index）记录源（Source）列表当前选中的条目。

它主要服务于列表编辑，本身不直接改变上采样结果。

### 添加源（Add Source）

添加源（Add Source）用于把一个 nx 发射器（nxEmitter）加入源（Source）列表。

只有 nx 发射器（nxEmitter）对象能作为有效源。

### 发射器对象（Emitter Object）

发射器对象（Emitter Object）是源（Source）或目标（Destination）列表项里引用的具体 nx 发射器（nxEmitter）。

没有有效发射器对象的条目不会参与同步。

### 发射器启用（Emitter Enabled）

发射器启用（Emitter Enabled）控制当前这一条源（Source）或目标（Destination）列表项是否参与作用。

关闭某条目后，不会删除它，只是暂时不参与当前上采样流程。

### 目标（Destination）

目标（Destination）是接收上采样结果的发射器列表。

上采样生成的粒子结果会写向这些目标发射器（Destination）对应的系统。

### 活动目标索引（Active Destination Index）

活动目标索引（Active Destination Index）记录目标（Destination）列表当前选中的条目。

它主要用于列表编辑，不直接改变上采样结果。

### 添加目标（Add Destination）

添加目标（Add Destination）用于把一个 nx 发射器（nxEmitter）加入目标（Destination）列表。

### 强度（Strength）

强度（Strength）控制整体上采样力度。

它相当于总开关的强弱系数。数值越高，提升分辨率结果越完整、越明显；数值越低，整体影响越弱。

### 位置（Position）

位置（Position）控制上采样粒子在位置上的变化量。

数值越高，新生成的上采样粒子相对于源粒子位置偏移越明显；数值越低，位置更贴近原始粒子分布。

### 速度（Velocity）

速度（Velocity）控制上采样粒子在速度上的变化量。

数值越高，生成结果的速度差异越大；数值越低，更多沿用源粒子的原始速度特征。

### 半径（Radius）

半径（Radius）控制上采样粒子半径上的变化量。

如果你想让上采样结果不只是位置更密，还要在大小上带一点差异，就可以提高这个值。

### 质量（Mass）

质量（Mass）控制上采样粒子质量上的变化量。

它适合在后续修改器还会用到质量（Mass）时，给上采样结果增加更多层次。

### 颜色（Color）

颜色（Color）控制上采样粒子颜色上的变化量。

如果目标是视觉细化，这个参数尤其有用，因为它能让补出来的粒子在颜色上不至于完全一致。

### 组（Group）

组（Group）控制是否把上采样粒子作为组结果处理。

开启后，更适合需要后续按组筛选或区分这批上采样粒子的场景。

### 最大数量（Max Count）

最大数量（Max Count）控制每个源粒子最多可生成多少个上采样粒子。

数值越高，结果越密，但计算和显示成本也会更高。它是最直接影响“密度提升程度”的参数之一。

### 限制距离（Limit Distance）

限制距离（Limit Distance）控制是否限制上采样粒子与源粒子的最大距离。

开启后，下面的最大距离（Max Distance）才会生效。

### 最大距离（Max Distance）

最大距离（Max Distance）只在限制距离（Limit Distance）开启时生效。

它控制上采样粒子允许偏离源粒子多远。数值越小，补出来的粒子云越紧；数值越大，结果分布越松。

### 推力（Push）

推力（Push）控制是否在上采样粒子之间加入额外的分离推开。

开启后，可以减少新生成粒子彼此过度堆叠的问题。

### 推力距离（Push Distance）

推力距离（Push Distance）只在推力（Push）开启时生效。

它控制上采样粒子彼此推开的目标距离。数值越高，补出来的粒子更容易被拉开；数值越低，结果更容易维持紧密团聚。

---

## 使用建议

### 做高密度补点

先提高最大数量（Max Count）和强度（Strength），再小幅调整位置（Position）与速度（Velocity），这样最容易得到既更密又不完全重叠的结果。

### 保持贴近原始模拟

把位置（Position）、速度（Velocity）、半径（Radius）、质量（Mass）和颜色（Color）都保持较低，让上采样粒子尽量接近源粒子，只做密度提升。

### 避免补出来的粒子过度挤在一起

开启推力（Push），再逐步提高推力距离（Push Distance）。如果仍然太散，可以同时开启限制距离（Limit Distance）并收紧最大距离（Max Distance）。
