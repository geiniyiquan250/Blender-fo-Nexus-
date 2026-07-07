# NeXus 约束修改器使用说明

这份文档只说明约束修改器（nxConstraints）。重点说明每个参数实际在约束解算里控制什么、什么时候需要调、调大或调小后通常会出现什么变化。

## 约束修改器（nxConstraints）

约束修改器（nxConstraints）用于给粒子之间加入约束关系。它不会负责产生粒子，粒子通常来自发射器（nxEmitter）；它的作用是让已有粒子按照某种规则互相连接、保持距离、碰撞、吸引、排斥、产生粘度、摩擦或表面张力。

这个修改器的界面分成两层理解最清楚：

- 全局设置：迭代次数（Iterations）和阻尼（Damping），影响整个约束解算。
- 层（Layers）列表：真正决定使用哪一种约束。每一层都有自己的约束类型（Constraint Type），不同类型显示不同参数。

使用时通常先做三步：

- 在层（Layers）列表里添加一层。
- 选择约束类型（Constraint Type），例如出生连接（Connection Birth）或碰撞（Collisions）。
- 再调这一层下面的半径、强度、断开、衰减等细节参数。

需要注意：约束修改器（nxConstraints）只生成和求解约束。约束线在视口中的颜色显示由发射器（nxEmitter）里的显示约束（Display Constraints）和对应颜色参数控制，不在这里调颜色。

### 迭代次数（Iterations）

迭代次数（Iterations）控制每一帧里约束求解器重复修正约束的次数。

简单理解：约束不是一次就能完全满足的，插件会反复修正粒子位置或关系。迭代次数越高，约束越容易接近目标状态；迭代次数越低，计算更轻，但约束可能更软、更容易被拉开或穿透。

常见用法：

- 粒子连接看起来松散、弹性太大，可以提高迭代次数（Iterations）。
- 碰撞或表面张力不够稳定，可以提高迭代次数（Iterations）。
- 粒子很多、播放很慢，可以先降低迭代次数（Iterations），等效果确定后再提高。

它影响整个约束修改器（nxConstraints），不是只影响某一种约束层。

### 阻尼（Damping）

阻尼（Damping）是整个约束系统的全局衰减参数，用来减少约束求解后的抖动、弹跳和过度运动。

阻尼（Damping）越高，粒子之间的约束反应越稳、更不容易来回震荡；但太高会让整体运动显得迟钝，失去活力。阻尼（Damping）越低，系统更灵敏，但也更容易出现振动或弹性过强。

常见用法：

- 粒子连接像橡皮筋一样抖动，可以提高阻尼（Damping）。
- 想保留更多弹性和活跃运动，可以降低阻尼（Damping）。
- 如果只是某一种约束太强或太弱，优先调该约束层自己的权重或刚性，不要只靠全局阻尼（Damping）解决。

### 层（Layers）

层（Layers）是约束修改器（nxConstraints）的核心，由多层约束组成。每一层都可以选择一种约束类型（Constraint Type），并且按顺序同步到约束解算流程。

插件提供这些主要约束层：

- 出生连接（Connection Birth）：按粒子出生关系建立连接。
- 距离连接（Connection Distance）：按粒子之间的距离建立连接。
- 自定义连接（Connection Custom）：提供压缩和扩展两套变形控制。
- 碰撞（Collisions）：处理粒子碰撞约束。
- 力（Forces）：提供吸引和排斥效果。
- 粘度（Viscosity）：让粒子群表现出粘滞阻尼。
- 摩擦力（Friction）：控制粒子之间或接触时的摩擦行为。
- 表面张力（Surface Tension）：让粒子趋向聚合成更紧致的表面。

如果一个参数属于某个约束层类型，它只在该层约束类型（Constraint Type）选中对应类型时才有实际意义。例如出生连接半径（Birth Radius）只属于出生连接（Connection Birth），不会影响碰撞（Collisions）层。

### 活动层索引（Active Layer Index）

活动层索引（Active Layer Index）记录当前选中的约束层。它主要服务于界面选择和内部同步，普通使用时通常不需要手动理解它。

如果右键打开到这个参数的帮助，可以把它理解成：它决定当前界面正在编辑层（Layers）列表里的哪一层。

### 层名称（Layer Name）

层名称（Layer Name）用于区分层（Layers）列表里的不同层。它不会直接改变约束强度，但在复杂场景里很重要。

建议把名称写成用途，而不是保留默认名称。例如：

- 出生连接（Connection Birth）
- 碰撞（Collisions）
- 表面张力（Surface Tension）

名称清楚后，后续调试会快很多。

### 层启用（Layer Enabled）

层启用（Layer Enabled）控制当前这一层约束是否参与解算。

关闭后，这一层不会继续把自己的权重传入求解流程。它适合用来临时对比效果：你可以关闭某一层，看当前运动变化是否由这层造成。

常见用法：

- 排查问题时，逐个关闭约束层。
- 做多个版本时，先保留参数但暂时关闭。
- 如果某层导致粒子爆开或过度收缩，先关闭层启用（Layer Enabled），再检查半径、权重、断开和连接限制。

### 约束类型（Constraint Type）

约束类型（Constraint Type）决定当前约束层使用哪一类约束。它是约束层里最重要的选择。

选择不同约束类型（Constraint Type）后，下面显示的参数会完全不同：

- 出生连接（Connection Birth）显示出生连接权重、仅新生粒子、半径、刚性、断开等参数。
- 距离连接（Connection Distance）显示距离连接权重、连接限制、半径、刚性、断开等参数。
- 自定义连接（Connection Custom）显示压缩和扩展两套参数。
- 碰撞（Collisions）显示碰撞权重和碰撞刚性。
- 力（Forces）显示吸引和排斥参数。
- 粘度（Viscosity）显示粘度权重、半径和刚性。
- 摩擦力（Friction）显示静态摩擦、动态摩擦和衰减。
- 表面张力（Surface Tension）显示表面张力半径、内半径、张力和衰减。

右键参数帮助也是按当前参数本身映射，不会把所有类型混在一起。遇到同名参数时，文档会使用更明确的名称，例如出生连接权重（Birth Weight）和距离连接权重（Distance Weight）。

---

## 出生连接（Connection Birth）

出生连接（Connection Birth）会根据粒子出生时的邻近关系建立连接。它适合做出生后希望保持局部结构的粒子群，例如软体颗粒、黏连碎片、刚产生时需要保持形状的发射结果。

这一层的默认约束类型就是出生连接（Connection Birth）。如果你刚添加约束修改器（nxConstraints）并看到一层默认约束，通常就是它。

### 出生连接权重（Birth Weight）

出生连接权重（Birth Weight）控制出生连接（Connection Birth）这一层整体有多强。

值越高，出生时建立的连接越有影响力；值越低，连接对粒子运动的限制越弱。它适合当作这一层的总强度旋钮。

常见用法：

- 想让粒子更像一个连在一起的整体，提高出生连接权重（Birth Weight）。
- 想让粒子只是轻微保持关系，降低出生连接权重（Birth Weight）。
- 如果只是连接太硬，优先看出生连接刚性（Birth Stiffness）；如果整层都太强，再调出生连接权重（Birth Weight）。

### 仅新生粒子（Only Born）

仅新生粒子（Only Born）控制出生连接是否只针对新出生的粒子。

开启后，这层更偏向处理刚出生那一批粒子的连接关系。关闭后，连接逻辑会更广泛地参与当前粒子集合。

常见用法：

- 发射过程中不断产生新粒子，并且只想让新粒子在出生附近建立关系，可以开启仅新生粒子（Only Born）。
- 如果希望已有粒子也继续按这层规则参与连接，可以关闭仅新生粒子（Only Born）。

这个参数只属于出生连接（Connection Birth）层，不影响距离连接（Connection Distance）或其他约束类型。

### 出生连接数量限制（Birth Connection Limit）

出生连接数量限制（Birth Connection Limit）控制每个粒子最多建立多少条出生连接。

值越高，每个粒子可连接的邻居更多，结构更容易保持，但计算更重，也可能让粒子群显得过度黏在一起。值越低，连接更少，结构更松散，计算也更轻。

常见用法：

- 需要更稳定的团块结构，可以提高出生连接数量限制（Birth Connection Limit）。
- 只想要轻微黏连，或者粒子很多导致很慢，可以降低出生连接数量限制（Birth Connection Limit）。

它会和出生连接半径（Birth Radius）一起决定能连到多少粒子：半径决定搜索范围，连接数量限制决定最多保留多少条连接。

### 出生连接半径（Birth Radius）

出生连接半径（Birth Radius）控制出生连接寻找邻近粒子的范围。

半径越大，一个粒子能找到的候选邻居越多；半径越小，只有更近的粒子才可能被连接。

实用理解：

- 出生连接半径（Birth Radius）太小，连接可能很少，结构不容易保持。
- 出生连接半径（Birth Radius）太大，远处粒子也可能被连上，容易出现不自然拉扯。
- 它通常要和粒子半径、发射密度一起看，不是越大越好。

### 出生连接刚性（Birth Stiffness）

出生连接刚性（Birth Stiffness）控制出生连接抵抗变形的程度。

刚性越高，连接越努力保持原始关系，粒子群更硬；刚性越低，连接更容易被拉伸或压缩，整体更软。

常见用法：

- 想要团块或软体更结实，提高出生连接刚性（Birth Stiffness）。
- 想让粒子连接有更多弹性和变形，降低出生连接刚性（Birth Stiffness）。

如果提高刚性后出现抖动，可以配合提高迭代次数（Iterations）或阻尼（Damping）。

### 最小距离（Minimum Distance）

最小距离（Minimum Distance）用于出生连接（Connection Birth）里限制连接的最小距离。

它可以避免过近的粒子建立不必要或不稳定的连接。值越高，太靠近的粒子越容易被排除在出生连接之外；值越低，近距离粒子也更容易建立连接。

常见用法：

- 粒子出生时过度堆在一起并产生细碎拉扯，可以适当提高最小距离（Minimum Distance）。
- 如果连接太少，除了检查出生连接半径（Birth Radius），也要确认最小距离（Minimum Distance）没有排除太多近邻。

### 出生断开类型（Birth Break Type）

出生断开类型（Birth Break Type）决定出生连接在什么规则下断开。

插件提供这些模式：

- 无（None）：连接不会按断开阈值主动断开。
- 相对连接（Relative Connected）：按连接建立时的相对距离判断。
- 相对半径（Relative Radius）：按粒子半径相关尺度判断。
- 绝对（Absolute）：按明确的世界距离阈值判断。

它会直接影响下面两个参数哪个真正生效：

- 当出生断开类型（Birth Break Type）是相对连接（Relative Connected）或相对半径（Relative Radius）时，使用出生相对断开阈值（Birth Break）。
- 当出生断开类型（Birth Break Type）是绝对（Absolute）时，使用出生绝对断开距离（Birth Break Above）。
- 当出生断开类型（Birth Break Type）是无（None）时，断开阈值没有实际意义。

### 出生相对断开阈值（Birth Break）

出生相对断开阈值（Birth Break）控制出生连接在相对规则下被拉到什么程度后断开。

它只在出生断开类型（Birth Break Type）为相对连接（Relative Connected）或相对半径（Relative Radius）时生效。界面上即使能看到这个参数，也要先看出生断开类型（Birth Break Type）当前选项。

值越高，连接更不容易断；值越低，连接更容易断。它适合做会被拉断的黏连、纤维或软连接效果。

### 出生绝对断开距离（Birth Break Above）

出生绝对断开距离（Birth Break Above）控制出生连接在绝对距离规则下超过多远后断开。

它只在出生断开类型（Birth Break Type）为绝对（Absolute）时生效。这个参数的好处是直观：你可以把它理解成连接允许被拉开的最大距离。

如果你需要和场景真实尺寸对应的断开行为，优先使用出生断开类型（Birth Break Type）的绝对（Absolute），再调出生绝对断开距离（Birth Break Above）。

---

## 距离连接（Connection Distance）

距离连接（Connection Distance）按粒子之间的距离建立连接。它不强调出生时关系，而是更关注当前或邻近粒子之间的空间距离，适合让粒子群形成局部网状连接。

### 距离连接权重（Distance Weight）

距离连接权重（Distance Weight）控制距离连接（Connection Distance）这一层整体强度。

值越高，距离连接对粒子运动影响越明显；值越低，这一层更像轻微辅助约束。

如果你同时使用出生连接（Connection Birth）和距离连接（Connection Distance），可以用两个权重决定谁是主约束、谁是辅助约束。

### 距离连接数量限制（Distance Connection Limit）

距离连接数量限制（Distance Connection Limit）控制每个粒子最多保留多少条距离连接。

值越高，局部网络更密，形状保持更强；值越低，网络更稀疏，粒子更自由。

它和距离连接半径（Distance Radius）一起工作：距离连接半径（Distance Radius）决定能搜索多远，距离连接数量限制（Distance Connection Limit）决定最多连接几个。

### 距离连接半径（Distance Radius）

距离连接半径（Distance Radius）控制距离连接搜索邻居的范围。

半径越大，粒子可能连接到更远的邻居；半径越小，只连接很近的粒子。

常见问题：

- 半径太小：连接数量不足，约束效果不明显。
- 半径太大：连接跨得太远，粒子群可能被不自然地拉成网。

### 距离连接刚性（Distance Stiffness）

距离连接刚性（Distance Stiffness）控制距离连接抵抗拉伸和压缩的程度。

刚性越高，粒子越努力保持连接距离；刚性越低，连接更柔软。

如果距离连接刚性（Distance Stiffness）很高但迭代次数（Iterations）很低，可能会出现看起来不够硬或轻微抖动的情况。这时优先提高迭代次数（Iterations），再微调阻尼（Damping）。

### 距离连接断开（Distance Break）

距离连接断开（Distance Break）控制距离连接在拉开到一定程度后是否断开以及断开的敏感程度。

值越高，连接更不容易断；值越低，连接更容易断。值为很低时，距离连接更适合做临时接触或容易撕裂的结构；值较高时，更适合稳定网络。

---

## 自定义连接（Connection Custom）

自定义连接（Connection Custom）提供更细的变形控制。它把变形分成压缩（Compression）和扩展（Expansion）两部分：一部分处理粒子靠得过近时的压缩反应，另一部分处理粒子被拉开时的扩展反应。

这个约束层适合需要更可控的软体、凝胶、弹性材料或特殊连接效果。

### 自定义连接权重（Custom Weight）

自定义连接权重（Custom Weight）控制自定义连接（Connection Custom）这一层整体强度。

它是压缩（Compression）和扩展（Expansion）参数之上的总强度控制。值越高，这一层整体越明显；值越低，压缩和扩展的具体设置都会被削弱。

### 自定义连接数量限制（Custom Connection Limit）

自定义连接数量限制（Custom Connection Limit）控制每个粒子最多建立多少条自定义连接。

值越高，自定义连接网络越密，材料更容易保持整体性；值越低，网络更稀疏，粒子运动更自由。

### 自定义半径（Custom Radius）

自定义半径（Custom Radius）控制自定义连接寻找邻近粒子的范围。

半径越大，能参与自定义连接的邻居越多；半径越小，只处理更近的邻居。

如果压缩（Compression）或扩展（Expansion）参数怎么调都不明显，先检查自定义半径（Custom Radius）和自定义连接数量限制（Custom Connection Limit）是否让粒子真正建立了足够连接。

### 自定义压缩强度（Custom Compression）

自定义压缩强度（Custom Compression）控制粒子靠得过近时，压缩方向的修正强度。

值越高，粒子越不容易被压得太近；值越低，粒子更容易挤在一起。

这个参数只属于自定义连接（Connection Custom）层，并且只影响压缩（Compression）部分，不影响扩展（Expansion）部分。

### 自定义压缩断开（Custom Compression Break）

自定义压缩断开（Custom Compression Break）控制压缩关系在达到某个距离条件后如何中止或断开。

它只属于自定义连接（Connection Custom）的压缩（Compression）部分。值越小，压缩关系更敏感；值越大，压缩关系允许更大的变化。

如果粒子被挤压时突然失去约束，优先检查自定义压缩断开（Custom Compression Break）是否太低。

### 自定义压缩速率（Custom Compression Rate）

自定义压缩速率（Custom Compression Rate）控制压缩修正发生的速度。

值越高，压缩修正越快，粒子更快被推回目标状态；值越低，压缩修正更慢，运动会显得更柔和。

它只影响自定义连接（Connection Custom）的压缩（Compression）部分。

### 自定义压缩衰减（Custom Compression Falloff）

自定义压缩衰减（Custom Compression Falloff）控制压缩效果随距离变化的曲线。

插件提供这些衰减：

- 平直（Flat）：范围内强度更接近一致。
- 线性（Linear）：按距离线性变化。
- 二次（Quadratic）：靠近边缘时变化更明显。
- 立方（Cubic）：变化更平滑，过渡更柔。

它只影响自定义连接（Connection Custom）的压缩（Compression）部分。想让压缩边界更自然时，通常选择立方（Cubic）。

### 自定义压缩塑性（Custom Compression Plastic）

自定义压缩塑性（Custom Compression Plastic）控制压缩后的形变保留倾向。

值越高，压缩后的形态更容易留下变化；值越低，系统更倾向恢复到原来的连接关系。

它适合用在不完全弹回的材料，例如被挤压后有一定变形残留的粒子团。

### 自定义扩展强度（Custom Expansion）

自定义扩展强度（Custom Expansion）控制粒子被拉开时的扩展方向修正强度。

值越高，粒子越不容易被拉远；值越低，连接更容易被拉伸。

它只属于自定义连接（Connection Custom）的扩展（Expansion）部分，不影响压缩（Compression）部分。

### 自定义扩展断开（Custom Expansion Break）

自定义扩展断开（Custom Expansion Break）控制扩展关系被拉到一定程度后如何中止或断开。

值越低，连接更容易在拉伸时失效；值越高，连接更能承受拉伸。

如果你要做容易撕裂的软连接，可以降低自定义扩展断开（Custom Expansion Break）。如果要保持连续性，可以提高它。

### 自定义扩展速率（Custom Expansion Rate）

自定义扩展速率（Custom Expansion Rate）控制拉伸修正发生的速度。

值越高，粒子被拉开后更快被拉回；值越低，恢复更慢、更柔。

它只影响自定义连接（Connection Custom）的扩展（Expansion）部分。

### 自定义扩展衰减（Custom Expansion Falloff）

自定义扩展衰减（Custom Expansion Falloff）控制扩展效果随距离变化的曲线。

可选衰减和自定义压缩衰减（Custom Compression Falloff）一样：

- 平直（Flat）
- 线性（Linear）
- 二次（Quadratic）
- 立方（Cubic）

如果拉伸边界过硬，可以尝试立方（Cubic）；如果需要范围内更平均的拉回效果，可以尝试平直（Flat）。

### 自定义扩展塑性（Custom Expansion Plastic）

自定义扩展塑性（Custom Expansion Plastic）控制拉伸后的形变保留倾向。

值越高，拉伸后的结构更容易留下形变；值越低，系统更倾向恢复到原始连接距离。

它只属于自定义连接（Connection Custom）的扩展（Expansion）部分。

---

## 碰撞（Collisions）

碰撞（Collisions）用于处理粒子之间的碰撞约束，让粒子不要随意穿过彼此。它通常和粒子半径、发射密度、迭代次数（Iterations）一起看。

### 碰撞权重（Collisions Weight）

碰撞权重（Collisions Weight）控制碰撞（Collisions）这一层整体强度。

值越高，碰撞约束越明显；值越低，粒子更容易相互穿插或压入。

如果碰撞完全不明显，先确认这一层已启用，再检查碰撞权重（Collisions Weight）和碰撞刚性（Collisions Stiffness）。

### 碰撞刚性（Collisions Stiffness）

碰撞刚性（Collisions Stiffness）控制碰撞修正的硬度。

刚性越高，粒子越强烈地避免重叠；刚性越低，粒子之间允许更多柔性挤压。

如果刚性很高但仍穿透，通常需要提高迭代次数（Iterations）。如果刚性很高并且抖动明显，可以增加阻尼（Damping）或降低碰撞刚性（Collisions Stiffness）。

---

## 力（Forces）

力（Forces）层提供粒子之间的吸引力（Attraction）和排斥力（Repulsion）。它适合做聚集、分散、局部吸附、避免过近等效果。

吸引力（Attraction）和排斥力（Repulsion）是同一层里的两组参数，可以同时使用。

### 力权重（Forces Weight）

力权重（Forces Weight）控制力（Forces）这一层整体强度。

值越高，吸引力（Attraction）和排斥力（Repulsion）整体更明显；值越低，整层影响减弱。

如果只想调吸引或排斥其中一个方向，优先调吸引力（Attraction）或排斥力（Repulsion），不要先动总权重。

### 力连接数量限制（Forces Connection Limit）

力连接数量限制（Forces Connection Limit）控制每个粒子最多参考多少个邻近粒子来计算力。

值越高，受影响邻居越多，效果更平滑但更重；值越低，影响更局部，计算更轻。

它会同时影响吸引力（Attraction）和排斥力（Repulsion）的邻居数量。

### 吸引力（Attraction）

吸引力（Attraction）控制粒子相互靠近的程度。

值越高，粒子更倾向聚集；值越低，聚集效果更弱。

它只属于力（Forces）层的吸引力（Attraction）部分。若排斥力（Repulsion）也很高，两者会共同决定最终距离关系。

### 吸引半径（Attraction Radius）

吸引半径（Attraction Radius）控制吸引效果的作用范围。

半径越大，较远粒子也会互相吸引；半径越小，只有近距离粒子会被吸引。

如果粒子整体都往一起塌，可能是吸引半径（Attraction Radius）过大或吸引力（Attraction）过高。

### 吸引内半径（Attraction Inner）

吸引内半径（Attraction Inner）定义吸引范围里的内侧区域。

可以把它理解成吸引计算的内部边界，用来控制靠近中心区域时的变化。它通常和吸引半径（Attraction Radius）以及吸引衰减（Attraction Falloff）一起决定吸引曲线。

如果吸引在中心附近太突兀，可以调吸引内半径（Attraction Inner）和吸引衰减（Attraction Falloff）。

### 吸引衰减（Attraction Falloff）

吸引衰减（Attraction Falloff）控制吸引力随距离变化的曲线。

可选衰减：

- 平直（Flat）
- 线性（Linear）
- 二次（Quadratic）
- 立方（Cubic）

想要吸引范围内强度更平均，可以用平直（Flat）。想要更自然的距离过渡，可以用立方（Cubic）。

### 排斥力（Repulsion）

排斥力（Repulsion）控制粒子互相推开的程度。

值越高，粒子越不容易靠得太近；值越低，排斥效果更弱。

它只属于力（Forces）层的排斥力（Repulsion）部分。常见做法是用吸引力（Attraction）让粒子聚集，用排斥力（Repulsion）避免它们压成一个点。

### 排斥半径（Repulsion Radius）

排斥半径（Repulsion Radius）控制排斥效果的作用范围。

半径越大，粒子更早开始互相推开；半径越小，只有非常接近时才推开。

如果粒子始终聚不到一起，可能是排斥半径（Repulsion Radius）过大或排斥力（Repulsion）过高。

### 排斥衰减（Repulsion Falloff）

排斥衰减（Repulsion Falloff）控制排斥力随距离变化的曲线。

可选衰减：

- 平直（Flat）
- 线性（Linear）
- 二次（Quadratic）
- 立方（Cubic）

如果排斥边界太生硬，可以尝试立方（Cubic）。如果需要范围内更均匀地推开，可以尝试平直（Flat）。

---

## 粘度（Viscosity）

粘度（Viscosity）让粒子群的相对运动更粘、更迟缓，常用于液体、凝胶、泥浆或高粘性颗粒效果。

### 粘度权重（Viscosity Weight）

粘度权重（Viscosity Weight）控制粘度（Viscosity）这一层整体强度。

值越高，粒子之间越倾向保持相对运动一致，整体更黏；值越低，粒子更自由。

如果粒子像水一样太散，可以提高粘度权重（Viscosity Weight）。如果运动太闷、太拖，可以降低它。

### 粘度连接数量限制（Viscosity Connection Limit）

粘度连接数量限制（Viscosity Connection Limit）控制每个粒子最多参考多少个邻近粒子来计算粘度。

值越高，粘度效果更平滑、更整体；值越低，粘度影响更局部。

### 粘度半径（Viscosity Radius）

粘度半径（Viscosity Radius）控制粘度作用的邻域范围。

半径越大，更多邻近粒子参与粘度计算；半径越小，只在很近的粒子之间产生粘性影响。

它通常要和粒子间距一起调。半径太小会看不出粘度，半径太大可能让大范围粒子运动被拖在一起。

### 粘度刚性（Viscosity Stiffness）

粘度刚性（Viscosity Stiffness）控制粘度约束的修正强度。

值越高，粘性约束更强，粒子相对运动更快被抹平；值越低，粘性更柔和。

如果提高粘度刚性（Viscosity Stiffness）后出现抖动或过度僵硬，可以增加阻尼（Damping）或降低刚性。

---

## 摩擦力（Friction）

摩擦力（Friction）用于控制粒子之间的摩擦阻力。它和粘度（Viscosity）不同：粘度更像整体流动阻尼，摩擦力更关注接触或邻近关系中的相对滑动。

### 摩擦力（Friction）

摩擦力（Friction）控制摩擦效果本身的强弱。

值越高，粒子更不容易相对滑动；值越低，粒子之间更容易滑开。

如果粒子接触后像冰一样滑，可以提高摩擦力（Friction）。如果粒子被锁得太死，可以降低它。

### 摩擦权重（Friction Weight）

摩擦权重（Friction Weight）控制摩擦力（Friction）这一层整体影响。

它是这一层的总权重，和摩擦力（Friction）不同。摩擦力（Friction）更像摩擦本身的效果强度，摩擦权重（Friction Weight）更像整层是否强烈参与约束解算。

### 摩擦连接数量限制（Friction Connection Limit）

摩擦连接数量限制（Friction Connection Limit）控制每个粒子最多参考多少个邻近粒子来计算摩擦。

值越高，摩擦影响更大范围、更平滑；值越低，摩擦更局部。

### 摩擦半径（Friction Radius）

摩擦半径（Friction Radius）控制摩擦作用范围。

半径越大，更远的邻近粒子也会参与摩擦；半径越小，只有接近粒子之间才明显。

如果摩擦范围不对，先调摩擦半径（Friction Radius），再调静态（Static）和动摩擦（Kinetic）。

### 静态（Static）

静态（Static）控制粒子相对静止或刚要开始滑动时的摩擦强度。

值越高，粒子越不容易从静止接触状态开始滑动；值越低，更容易被推开或滑动。

常见用法：

- 想让堆积物更稳，提高静态（Static）。
- 想让粒子更容易被扰动，降低静态（Static）。

### 动摩擦（Kinetic）

动摩擦（Kinetic）控制粒子已经发生相对滑动后的摩擦强度。

值越高，滑动会更快被减速；值越低，粒子滑动更顺。

静态（Static）和动摩擦（Kinetic）通常一起看：静态摩擦决定“是否容易开始滑”，动态摩擦决定“滑起来后减速快不快”。

### 摩擦衰减（Friction Falloff）

摩擦衰减（Friction Falloff）控制摩擦力随距离变化的曲线。

可选衰减：

- 平直（Flat）
- 线性（Linear）
- 二次（Quadratic）
- 立方（Cubic）

如果希望摩擦在范围内更平均，用平直（Flat）。如果希望边缘更柔和，用立方（Cubic）。

---

## 表面张力（Surface Tension）

表面张力（Surface Tension）让粒子趋向聚合成更紧致的团块或表面。它常用于液滴、流体边界收缩、黏性团聚效果。

### 表面张力权重（Surface Tension Weight）

表面张力权重（Surface Tension Weight）控制表面张力（Surface Tension）这一层整体强度。

值越高，粒子越倾向收缩聚合；值越低，表面张力效果更弱。

如果液滴不够抱团，可以提高表面张力权重（Surface Tension Weight）。如果粒子过度缩成团，可以降低它。

### 表面张力连接数量限制（Surface Tension Connection Limit）

表面张力连接数量限制（Surface Tension Connection Limit）控制每个粒子最多参考多少个邻近粒子来计算表面张力。

值越高，表面张力更整体、更平滑；值越低，效果更局部。

### 表面张力半径（Surface Tension Radius）

表面张力半径（Surface Tension Radius）控制表面张力作用范围。

半径越大，更多粒子参与收缩和聚合；半径越小，只有近邻粒子互相影响。

如果粒子群整体被拉成一团，可能是表面张力半径（Surface Tension Radius）过大或张力（Tension）过高。

### 表面张力内半径（Surface Tension Inner）

表面张力内半径（Surface Tension Inner）定义表面张力作用范围中的内侧边界。

它和表面张力半径（Surface Tension Radius）、表面张力衰减（Surface Tension Falloff）一起决定从内部到外部的强度变化。

如果表面张力在中心附近变化太突兀，可以调表面张力内半径（Surface Tension Inner）。

### 张力（Tension）

张力（Tension）控制粒子收缩成表面的力度。

值越高，粒子更明显地抱团、收缩；值越低，表面张力更弱。

它和表面张力权重（Surface Tension Weight）的区别是：表面张力权重（Surface Tension Weight）控制整层参与程度，张力（Tension）控制张力效果本身。

### 表面张力衰减（Surface Tension Falloff）

表面张力衰减（Surface Tension Falloff）控制表面张力随距离变化的曲线。

可选衰减：

- 平直（Flat）
- 线性（Linear）
- 二次（Quadratic）
- 立方（Cubic）

表面张力（Surface Tension）默认更适合用线性（Linear）这类可预测过渡。如果想要更柔的边缘，可以尝试立方（Cubic）。

---

## 通用页签

### 物体属性（Object Properties）

物体属性（Object Properties）是约束修改器（nxConstraints）的主设置页。这里主要编辑全局求解参数和层（Layers）列表，包括迭代次数（Iterations）、阻尼（Damping）以及每个约束层自己的类型和参数。

如果你要调整粒子之间如何保持距离、连接、碰撞、粘度、摩擦或表面张力，通常先回到物体属性（Object Properties）页。组（Groups Affected）、映射（Mapping）和衰减（Falloff）是通用控制页，用来限制影响对象、用粒子数据驱动参数或按空间范围控制效果。

### 设置页（Section）

设置页（Section）是约束修改器（nxConstraints）面板顶部的页签切换。它不直接改变约束结果，而是切换当前正在编辑哪一类设置。

约束修改器（nxConstraints）除了自身的层（Layers）列表外，也会带有普通 NeXus 修改器通用页签，例如组（Groups Affected）、映射（Mapping）和衰减（Falloff）。这些页签是通用框架提供的，不是某一种约束层专属参数。

### 启用（Enabled）

启用（Enabled）控制当前项目是否参与流程。它在不同位置代表不同层级：

- 在约束修改器（nxConstraints）本体上，启用（Enabled）控制整个约束修改器是否参与粒子流程。
- 在组（Groups Affected）列表里，启用（Enabled）控制当前这个组限制是否生效。
- 在映射（Mapping）列表里，启用（Enabled）控制当前这一条映射层是否生效。
- 在衰减（Falloff）列表里，启用（Enabled）控制当前这个衰减对象是否参与影响范围计算。

注意它和层启用（Layer Enabled）不同。层启用（Layer Enabled）只控制层（Layers）列表里的某一层约束；启用（Enabled）可以是整个修改器或通用列表项的启用状态。

### 组（Groups Affected）

组（Groups Affected）用于限制约束修改器（nxConstraints）影响哪些 nx 组（nxGroup）。

如果这里不添加任何组，通常表示不额外按组过滤。添加组后，约束只会按组过滤后的粒子范围工作。

如果某些粒子没有受到约束影响，除了检查约束层本身，还要检查组（Groups Affected）里是否添加了组过滤。

### 活动组索引（Active Group Index）

活动组索引（Active Group Index）记录组（Groups Affected）列表中当前选中的项目。

普通用户通常不需要手动调它。它只决定界面正在编辑列表里的哪一项。

### 添加组（Add Group）

添加组（Add Group）用于把 nx 组（nxGroup）加入组（Groups Affected）列表。

它只接受 nx 组（nxGroup）对象。普通网格、发射器、碰撞体或其他修改器对象不会作为有效组过滤使用。

### 组对象（Group Object）

组对象（Group Object）是组（Groups Affected）列表项里引用的 nx 组（nxGroup）。

只有当场景里真的存在对应 nx 组（nxGroup），并且粒子已经被分配到这个组时，组过滤才有实际意义。

### 映射（Mapping）

映射（Mapping）用于让粒子数据动态驱动约束参数。具体驱动规则在映射层（Mapping Layers）里逐条设置。

基本逻辑是：选择粒子数据（Particle Data）作为输入，选择要控制的目标参数（Mapping Parameter），再用范围（Range Min / Range Max）、映射权重（Mapping Weight）、钳制（Clamp）和曲线决定输入如何转换成参数变化。

如果映射（Mapping）里没有任何层，约束参数就按物体属性（Object Properties）里的固定值工作。

### 映射层（Mapping Layers）

映射层（Mapping Layers）是映射（Mapping）页里的列表。每一层代表一条“用某种粒子数据控制某个约束参数”的规则。

如果某一层没有选择目标参数（Mapping Parameter），这层不会真正参与映射。

### 活动映射索引（Active Mapping Index）

活动映射索引（Active Mapping Index）记录当前正在编辑哪一条映射层。

普通用户通常不需要直接修改它。你在映射层（Mapping Layers）列表中选中哪一层，下面显示的范围、权重、钳制和曲线就对应哪一层。

### 映射目标参数（Mapping Parameter）

映射目标参数（Mapping Parameter）决定这条映射要控制约束修改器（nxConstraints）的哪个参数。

可选项由当前插件运行时提供，不是每个界面参数都一定能被映射。如果目标参数没有选择，映射层不会产生实际效果。

### 粒子数据（Particle Data）

粒子数据（Particle Data）决定用哪种粒子属性作为映射输入。

常见输入包括年龄（Age）、生命（Life）、速度（Speed）、半径（Radius）、质量（Mass）、颜色（Color）、距离（Distance）、文档时间（Document Time）和组（Group）。

选择不同粒子数据（Particle Data）后，范围（Range Min / Range Max）的含义也会跟着变化。

### 映射图层（Mapping Layer）

映射图层（Mapping Layer）用于分层修改器里指定要映射哪一个运行层。

约束修改器（nxConstraints）本身有层（Layers）列表，但当前通用映射图层（Mapping Layer）主要服务于映射系统识别分层目标。具体是否可选到某一层，取决于运行时提供的可映射目标。

### 范围最小值（Range Min）

范围最小值（Range Min）定义粒子数据输入范围的下限。

如果粒子数据低于这个值，会按钳制（Clamp）设置处理。它和范围最大值（Range Max）一起决定输入数据如何映射到目标参数。

### 范围最大值（Range Max）

范围最大值（Range Max）定义粒子数据输入范围的上限。

范围太窄时，变化可能过于突然；范围太宽时，变化可能不明显。如果映射没有效果，先检查粒子数据实际值是否落在这个范围内。

### 映射权重（Mapping Weight）

映射权重（Mapping Weight）控制当前映射层对目标参数的影响强度。

值越高，这条映射越明显；值越低，这条映射越弱。它不会改变粒子数据本身，只改变映射结果混入目标参数的比例。

### 钳制（Clamp）

钳制（Clamp）决定粒子数据超出范围最小值（Range Min）和范围最大值（Range Max）后如何处理。

插件提供三种模式：

- 钳制（Clamp）：超出范围后停在边界值。
- 循环（Cycle）：超出范围后按区间循环。
- 继续（Continue）：超出范围后继续按趋势外推。

### 衰减（Falloff）

衰减（Falloff）用于用衰减对象控制约束修改器（nxConstraints）的影响范围。

如果你想控制“哪里受约束影响”，用衰减（Falloff）；如果想控制“哪些组受约束影响”，用组（Groups Affected）；如果想控制“按粒子数据如何变化”，用映射（Mapping）。

### 衰减对象（Falloff Objects）

衰减对象（Falloff Objects）是衰减（Falloff）页里的列表。列表里的每一项都应该指向一个nx 衰减（nxFalloff）。

### 活动衰减索引（Active Falloff Index）

活动衰减索引（Active Falloff Index）记录当前正在编辑衰减对象（Falloff Objects）列表里的哪一项。

普通用户通常不需要手动调它。

### 添加衰减（Add Falloff）

添加衰减（Add Falloff）用于把nx 衰减（nxFalloff）加入衰减（Falloff）列表。

它只接受nx 衰减（nxFalloff）。如果场景里没有合适的衰减对象，可以用衰减页右侧的创建按钮新建一个。

### 衰减对象（Falloff Object）

衰减对象（Falloff Object）是衰减（Falloff）列表项里真正引用的 nx nx 衰减（nxFalloff）。

它决定空间范围、形状和衰减曲线。列表项只是把这个衰减对象接入当前约束修改器（nxConstraints）。

### 衰减混合（Falloff Blend）

衰减混合（Falloff Blend）决定多个衰减对象或衰减结果如何叠加。

常见模式包括法线方向（Normal）、添加（Add）、减去（Subtract）、相乘（Multiply）、差值（Difference）、屏幕（Screen）、叠加（Overlay）、最小（Min）和最大（Max）。

如果只使用一个衰减对象，通常保持法线方向（Normal）即可。

### 衰减混合强度（Falloff Blend Strength）

衰减混合强度（Falloff Blend Strength）控制当前衰减对象混入最终衰减结果的比例。

值越高，这个衰减对象的影响越明显；值越低，它的影响越弱。

---

## 和发射器显示的联动

约束修改器（nxConstraints）负责生成和求解约束，发射器（nxEmitter）负责显示粒子以及部分约束线颜色。

如果你想在视口里看到约束连线，需要同时满足：

- 粒子来自发射器（nxEmitter）。
- 当前粒子流程包含约束修改器（nxConstraints）；如果使用发射器（nxEmitter）的修改器（Modifiers）列表组织流程，需要确认列表里包含它。
- 约束修改器（nxConstraints）里启用了对应约束层。
- 发射器（nxEmitter）里开启显示约束（Display Constraints）。

当前发射器（nxEmitter）里直接提供颜色设置的约束类型主要是：

- 出生连接（Connection Birth）
- 距离连接（Connection Distance）
- 自定义连接（Connection Custom）
- 粘度（Viscosity）

也就是说，碰撞（Collisions）、力（Forces）、摩擦力（Friction）和表面张力（Surface Tension）可以参与约束解算，但不一定都有独立的约束线颜色入口。

---

## 列表操作按钮

这些小按钮通常出现在对象列表、组列表、修改器列表、衰减列表或类似的树状列表旁边，用于管理列表内容，不参与粒子物理计算。

### 添加项（Add Item）

添加项（Add Item）会在当前列表中新增一个空项目。新增后，通常还需要继续选择对象、类型或填写该项目自己的参数。

### 添加菜单（Add Menu）

添加菜单（Add Menu）会打开当前列表可添加类型的菜单。它通常出现在有多种项目类型的列表里，例如层（Layers）列表。

### 创建并添加（Create and Add）

创建并添加（Create and Add）会先创建一个新的 NeXus 对象，再把它加入当前列表。例如创建新的 nx 组（nxGroup）或nx 衰减（nxFalloff）。

### 连续拾取（Continuous Pick）

连续拾取（Continuous Pick）用于在视口里连续选择多个对象并加入当前列表。按 Esc 结束连续拾取。

如果列表只接受特定类型，例如 nx 组（nxGroup）、nx 衰减（nxFalloff）或网格（Mesh）物体，不符合类型的对象不会被加入。

### 移除项（Remove Item）

移除项（Remove Item）会从当前列表中删除选中的项目。它通常只移除列表引用，不等于删除场景里的对象本体。

### 上移项（Move Item Up）

上移项（Move Item Up）会把当前选中的列表项目向上移动一位。

### 下移项（Move Item Down）

下移项（Move Item Down）会把当前选中的列表项目向下移动一位。

### 启用切换（Toggle Enabled）

启用切换（Toggle Enabled）会开关当前列表项是否参与当前列表的作用。它只影响这一项，不等于关闭整个修改器。

### 增加缩进（Indent Item）

增加缩进（Indent Item）用于层级列表，把当前项目向更深一层移动。普通平铺列表不会使用这个按钮。

### 减少缩进（Outdent Item）

减少缩进（Outdent Item）用于层级列表，把当前项目向外提升一层。
