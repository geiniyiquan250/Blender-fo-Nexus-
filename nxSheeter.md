# 薄膜补粒修改器使用说明（NeXus）

这份文档只说明薄膜补粒修改器（nxSheeter）。它用于在稀薄液膜、拉伸水片和片状流体区域里补充粒子，让液膜更连续、更容易维持片状结构。

## 薄膜补粒修改器（nxSheeter）

薄膜补粒修改器（nxSheeter）会检测流体粒子之间的稀疏区域，并在合适的位置插入新粒子，帮助液体表面形成更完整的薄片和连桥。

常见用途：

- 喷溅拉出的水片
- 片状飞溅
- 液膜边缘容易断开的场景
- 需要保住连续表面的高速流体

### 启用（Enabled）

启用（Enabled）控制薄膜补粒修改器（nxSheeter）是否参与当前系统（NeXus）计算。

关闭后，修改器不会继续插入补粒。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制该修改器在编辑器里的辅助显示状态。

### 片层检测（Sheet Detection）

片层检测（Sheet Detection）这一组参数决定哪些区域会被判断为需要补粒的薄膜。

### 最小密度（Min Density）

最小密度（Min Density）定义薄膜可被识别的最低密度。

提高后，较稀的液膜更容易被视为已经破碎，从而减少补粒。

### 最大密度（Max Density）

最大密度（Max Density）定义保持原状的上限密度。

高于这个值的区域通常会被当作主体液体体积，修改器重点处理表层和薄膜区域。

### 搜索半径（Search Radius）

搜索半径（Search Radius）控制检测邻域的范围。

半径越大，修改器会参考更宽的周边粒子分布来判断液膜形态。

### 生成前粒子年龄（Spawn After Age）

生成前粒子年龄（Spawn After Age）控制源粒子至少存在多久之后，周围区域才允许开始补粒。

提高后，可以让流体先运动一段时间，再开始补齐薄膜。

### 检查年龄（Check Age）

检查年龄（Check Age）决定是否限制过老粒子继续参与薄膜补粒。

开启后，下面的最大年龄（Max Age）和变化（Variation）会生效。

### 最大年龄（Max Age）

最大年龄（Max Age）定义还能继续参与补粒的粒子年龄上限。

### 年龄变化（Variation）

年龄变化（Variation）给最大年龄加入随机波动，让截止边界更自然。

### 粒子创建（Particle Creation）

粒子创建（Particle Creation）这一组参数控制何时补、补多少、补在什么位置。

### 最小孔洞尺寸（Min Hole Size）

最小孔洞尺寸（Min Hole Size）控制多大的空缺才值得补。

较小的数值会补更多细碎空隙，较大的数值更专注于明显裂缝。

### 最大孔洞尺寸（Max Hole Size）

最大孔洞尺寸（Max Hole Size）控制允许跨越的最大空缺。

超出这个范围的断裂会保留下来，形成真实的撕裂感。

### 仅分离中（Separating Only）

仅分离中（Separating Only）控制补粒是否只发生在粒子彼此拉开的区域。

它适合做被拉伸开的水膜和飞溅片层。

### 速度对齐（Velocity Alignment）

速度对齐（Velocity Alignment）控制补粒方向是否参考粒子的运动方向。

开启后，补粒更集中在当前流动方向附近。

### 对齐角度（Alignment Angle）

对齐角度（Alignment Angle）控制速度对齐允许的夹角范围。

角度越大，允许补粒的方向范围越宽。

### 插入间距（Insert Spacing）

插入间距（Insert Spacing）控制新增粒子之间希望维持的间距。

减小这个值会让薄膜更密，增大则会保留更疏的填充。

### 最小间距（Min Spacing）

最小间距（Min Spacing）控制新粒子与邻近粒子的最近允许距离。

它影响补粒的紧密程度，也会影响局部压力感和推挤感。

### 抖动（Jitter）

抖动（Jitter）给每个插入粒子增加随机偏移。

适当提高后，补出来的片层会少一些规则格点感。

### 最大速度（Max Speed）

最大速度（Max Speed）控制会被补粒的源粒子速度上限。

数值较低时，高速飞散的喷粒更容易被排除，修改器更专注于液膜本体。

### 相对速度（Relative Speed）

相对速度（Relative Speed）控制是否按粒子对之间的相对速度范围进行筛选。

开启后，最小速度（Min Speed）和最大速度（Max Speed）这两个相对速度阈值会参与判断。

### 输出（Output）

输出（Output）这一组参数控制新增粒子被创建到哪里，以及它们的显示方式。

### 输出发射器（Output Emitter）

输出发射器（Output Emitter）指定新粒子写入哪个发射器。

留空时，新粒子会加入源流体自身。

### 组（Group）

组（Group）指定新粒子加入哪个粒子组（nxGroup）。

留空时，新粒子会继承源粒子的组信息。

### 粒子半径（Particle Radius）

粒子半径（Particle Radius）控制新粒子的半径。

设为 0 时会继承源粒子的半径。

### 速度缩放（Velocity Scale）

速度缩放（Velocity Scale）控制新粒子继承多少源粒子速度。

### 自定义显示（Custom Display）

自定义显示（Custom Display）控制是否给新粒子使用固定颜色和固定显示形状。

开启后，颜色（Color）和显示（Display）参数可用。

### 颜色（Color）

颜色（Color）控制新粒子的显示颜色。

### 显示（Display）

显示（Display）控制新粒子在视口中的显示形状。

### 自适应收缩（Adaptive Collapse）

自适应收缩（Adaptive Collapse）控制当补粒区域重新变厚时，是否把当前修改器添加的粒子移除。

它只处理这个修改器自己插入的粒子。

### 移除稀疏（Remove Sparse）

移除稀疏（Remove Sparse）控制当补出来的粒子变得过于孤立时，是否自动清理。

开启后，最小距离（Min Distance）和最大密度（Max Density）会作为清理条件。

### 限制（Limits）

限制（Limits）这一组参数用于控制补粒总量。

### 最大粒子数（Max Particles）

最大粒子数（Max Particles）控制允许新增的总粒子上限。

数值设为 0 时表示不设上限。大场景里建议结合内存和播放速度做限制。
