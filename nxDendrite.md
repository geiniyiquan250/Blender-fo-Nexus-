# 树枝生长修改器使用说明（NeXus）

这份文档只说明树枝生长修改器（nxDendrite）。它用于按图层生成分枝、生长网络、规则晶格和晶体状枝条。

## 树枝生长修改器（nxDendrite）

树枝生长修改器（nxDendrite）是一个图层式生成器。它会围绕发射器粒子生长主枝和子枝，或者把粒子沿网络规则持续转向。不同模式下，同一套图层系统会表现为不同的生长逻辑。

创建流程：创建树枝生长修改器（nxDendrite）后，插件会自动添加一个默认图层。之后可以继续添加子图层，形成有层级关系的枝条结构。

### 启用（Enabled）

启用（Enabled）控制树枝生长修改器（nxDendrite）是否参与当前系统（NeXus）计算。

### 视口可见（Visible in Editor）

视口可见（Visible in Editor）控制该修改器在编辑器里的辅助显示状态。

## 模式（Mode）

模式（Mode）决定整个修改器采用哪种生长模型。

当前包括：

- 分枝（Branches）：经典枝条生长，适合树枝、神经、根系、分叉触手
- 网络（Network）：按固定角度规则连续转向，适合网格状路径和导线式生长
- 贝特晶格（Bethe Lattice）：规则递归晶格，适合对称结构和数学树
- 枝晶（Dendrite）：带游走和偏置的晶体状分枝，适合雪花、电结晶、矿物枝晶

## 图层（Layers）

图层（Layers）是树枝生长修改器（nxDendrite）的核心。每一层都可以是一个根层，或依附在上一层下面的子层。

常见层类型会随模式变化：

- 主枝 / 子枝（Branch / SubBranch）
- 主网络 / 子网络（Network / SubNetwork）
- 主晶格 / 子晶格（Lattice / Sub-Lattice）
- 主枝晶 / 子枝晶（Dendrite / Sub-Dendrite）

### 图层头部通用参数

每个图层顶部都有一组通用参数：

- 类型（Type）
- 颜色（Color）
- 拖尾对象（Trail）

颜色（Color）会同时影响这一代粒子的显示颜色，以及关联拖尾对象（Trail）的颜色。

拖尾对象（Trail）用来指定一个拖尾修改器（nxTrail）对象，把这一层生成的枝条路径画出来。

## 页签（Tab）

每个图层有两个主要页签：

- 常规（General）
- 相交（Intersection）

常规页签（General）负责当前模式下的生长参数，相交页签（Intersection）负责碰撞、转向和体积约束。

## 常规页签（General）

常规页签（General）会根据当前模式显示不同参数组。

### 分枝模式（Branches）

分枝模式（Branches）里最常见的是生成（Spawn）、枝干（Stem）和随机种子（Seed）。

#### 生成（Spawn）

生成（Spawn）控制什么时候产生子枝，以及每次产生多少。

常见参数包括：

- 分枝间隔（Branch Every）
- 分枝数量（Branches）
- 最大分枝数（Max Branches）
- 最小角度（Angle Min）
- 最大角度（Angle Max）
- 旋转方式（Rotation）
- 对称方式（Symmetry）
- 旋转角度（Rotation Angle）
- 分枝缩放（Branch Scale）
- 速度模式（Speed Mode）
- 分枝速度（Branch Speed）

这些参数决定分叉密度、分叉角度、旋转节奏和子枝长度比例。

#### 枝干（Stem）

枝干（Stem）控制枝条本体怎样向前生长。

常见参数包括：

- 长度模式（Length Mode）
- 最大长度（Max Length）
- 长度变化（Variation）
- 弯折间隔（Bend Every）
- 最小弯折（Bend Min）
- 最大弯折（Bend Max）
- 弯折模式（Bend Mode）

当长度模式（Length Mode）设为按样条线（By Spline）时，还会出现一条长度曲线，用来控制沿父级位置分配的长度变化。

当弯折模式（Bend Mode）设为卷曲（Curl）时，还会出现：

- 卷曲角度（Curl Angle）
- 收紧（Tighten）
- 卷曲强度（Curl Strength）

它们用来做卷曲状和螺旋状的生长。

#### 随机种子（Seed）

随机种子（Seed）控制当前图层的随机种子。

切换数值后，分叉分布、弯折和局部随机性会改变。

### 网络模式（Network）

网络模式（Network）把粒子转向限制在一组角度规则里，更适合做网状蔓延和折线路径。

常规页签（General）里重点参数包括：

- 变化方式（Change）
- 间隔（Every）
- 变化量（Variation）
- 水平转角（Heading）
- 水平变化（Heading Var）
- 俯仰转角（Pitch）
- 俯仰变化（Pitch Var）
- 平面（Plane）
- 轴向（Axis）
- 空间（Space）
- 水平概率（Heading Chance）
- 俯仰概率（Pitch Chance）

这些参数共同决定多久转一次、朝哪个方向转、是否限制在某个平面内、转向是否带随机概率。

### 贝特晶格模式（Bethe Lattice）

贝特晶格模式（Bethe Lattice）用规则递归方式持续分裂。

常规页签（General）的重点参数包括：

- 分枝因子（Branching Factor）
- 分枝角度（Branch Angle）
- 层级（Levels）
- 段长度（Segment Length）
- 缩放（Scale）
- 间距（Spacing）

它适合做高度对称、层层扩展的树状结构。

### 枝晶模式（Dendrite）

枝晶模式（Dendrite）偏向晶体状和有机枝晶生长。

常规页签（General）的重点参数包括：

- 晶体角度（Crystal Angle）
- 角度变化（Angle Variation）
- 分枝数量（Branches）
- 分枝间距（Branch Spacing）
- 层级（Levels）
- 段长度（Segment Length）
- 长度变化（Length Variation）
- 缩放（Scale）
- 种子间距（Seed Spacing）
- 游走（Wander）
- 偏置强度（Bias Strength）
- 偏置方向（Bias Direction）

游走（Wander）控制生长方向的随机漂移，偏置强度（Bias Strength）和偏置方向（Bias Direction）控制整体更倾向朝哪个方向发展。

## 相交页签（Intersection）

相交页签（Intersection）控制枝条遇到别的路径或体积边界时怎样响应。

### 路径碰撞（Intersection）

这一组参数控制图层是否检测枝条命中情况。

### 启用（Enable）

启用（Enable）控制是否开启碰撞检测。

### 检测拖尾（Detect Trails）

检测拖尾（Detect Trails）控制是否把其他枝条的拖尾对象（Trail）也纳入检测对象。

### 检测半径（Radius）

检测半径（Radius）控制命中判定的距离范围。

### 命中处理（On Hit）

命中处理（On Hit）决定碰到目标后的结果。

可选值包括：

- 改变方向（Change Direction）
- 停止（Stop）
- 消亡（Die）

### 偏转角（Deflect Angle）

偏转角（Deflect Angle）只在命中处理（On Hit）为改变方向（Change Direction）时出现。

它控制命中后新方向与原方向的偏转幅度。

## 网格体积约束（Mesh）

相交页签（Intersection）里的网格区块（Mesh）用于把枝条尖端限制在某个网格体积内部，或排除到体积外侧。

### 启用（Enable）

启用（Enable）控制是否使用体积网格约束。

### 网格（Mesh）

网格（Mesh）指定参与约束的目标网格对象。

### 区域（Region）

区域（Region）决定枝条尖端应该保持在网格内部，还是保持在网格外部。

### 命中处理（On Hit）

体积命中处理（On Hit）控制枝条接触边界后的反应。

可选值包括：

- 反射（Reflect）
- 停止（Stop）
- 消亡（Die）

### 检测距离（Detection Distance）

检测距离（Detection Distance）控制距离边界多近时开始触发响应。

### 边界偏移（Boundary Offset）

边界偏移（Boundary Offset）控制有效边界相对表面的偏移量。

它可以用来把生长范围往内缩一点，或者为边界留出缓冲。

## 使用建议

### 做树枝、根系、触手

优先使用分枝模式（Branches），从一个根层开始，再按需要叠加多个子枝层（SubBranch）。

### 做网格状路径或电路式扩展

优先使用网络模式（Network），重点调水平转角（Heading）、俯仰转角（Pitch）、平面（Plane）和变化方式（Change）。

### 做规则递归结构

优先使用贝特晶格模式（Bethe Lattice），重点调层级（Levels）、分枝因子（Branching Factor）和段长度（Segment Length）。

### 做雪花、电结晶、枝晶矿物

优先使用枝晶模式（Dendrite），重点调晶体角度（Crystal Angle）、游走（Wander）、偏置强度（Bias Strength）和偏置方向（Bias Direction）。
